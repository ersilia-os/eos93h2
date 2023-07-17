# imports
import os
import csv
import glob
import sys

import torch
import torchvision

from image_dataloader import smiles_to_image, ImageData

DEVICE = 'cpu'

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))
checkpoints_dir = os.path.abspath(os.path.join(root, "..", "..", "checkpoints"))
ckpts = glob.glob(f"{checkpoints_dir}/*.pth")
gpcr_assays = [os.path.split(pt)[-1].split(".")[0] for pt in ckpts]

# Load GPCR models
def load_models():
    models = {}

    for idx, assay in enumerate(gpcr_assays):
        mdl = torchvision.models.resnet18(weights=None)
        mdl.fc = torch.nn.Linear(mdl.fc.in_features, 1)
        checkpoint = torch.load(ckpts[idx], map_location=torch.device(DEVICE))
        mdl.load_state_dict(checkpoint)
        models.update({assay: mdl})

    return models


# Get predictions
def get_predictions(smiles):
    models = load_models()

    outputs = []

    img_processor = ImageData()
    for idx, smi in enumerate(smiles):
        per_row_preds = []
        path = f"{os.getcwd()}/{idx}.png"
        smiles_to_image(smi, savePath=path)
        img_tensor = img_processor.get_image(path).to(DEVICE)
        for assay in gpcr_assays:
            assay_mdl = models[assay]
            assay_mdl.eval()
            with torch.no_grad():
                pred = assay_mdl(img_tensor)
            per_row_preds.append(pred.item())
        outputs.append(per_row_preds)
        os.remove(path)
    return outputs

# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

# run _model
outputs = get_predictions(smiles_list)

##ensure the input and the output are the same
input_len = len(smiles_list)
output_len = len(outputs)
assert input_len == output_len

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(gpcr_assays)  # header
    for o in outputs:
        writer.writerow(o)
