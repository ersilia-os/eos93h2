import os
import glob

import torch
import torchvision
from PIL import Image
from rdkit import Chem
from rdkit.Chem import Draw

from rdkit.Chem.SaltRemover import SaltRemover
from rdkit import Chem
from rdkit.Chem import Descriptors

import numpy as np
import torchvision.transforms as transforms

root = os.path.dirname(os.path.abspath(__file__))
checkpoints_dir = os.path.abspath(os.path.join(root, "..", "..", "checkpoints"))
ckpts = glob.glob(f"{checkpoints_dir}/*.pth")
gpcr_assays = [os.path.split(pt)[-1].split(".")[0] for pt in ckpts]


IMG_SIZE = 224
ORGANIC_ATOM_SET = set([5, 6, 7, 8, 9, 15, 16, 17, 35, 53])
REMOVER = SaltRemover()

DEVICE = 'cpu'


class ImageData:
    def __init__(self):
        """
        Loads an image and transforms it
        """
        self.normalize = transforms.Normalize(
            mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]
        )
        self._image_transformer = transforms.Compose(
            [transforms.CenterCrop(IMG_SIZE), transforms.ToTensor()]
        )

    def get_image(self, filename):
        img = Image.open(filename).convert("RGB")
        data = self._image_transformer(img)
        data = self.normalize(data)
        data.resize_(1, 3, IMG_SIZE, IMG_SIZE)
        return data


def smiles_to_image(smi, size=IMG_SIZE, savePath=None):
    """
    smis: e.g. COC1=C(C=CC(=C1)NS(=O)(=O)C)C2=CN=CN3C2=CC=C3
    path: E:/a/b/c.png
    """
    try:
        mol = Chem.MolFromSmiles(smi)
        img = Draw.MolsToGridImage([mol], molsPerRow=1, subImgSize=(size, size))
        if savePath is not None:
            img.save(savePath)
        return img
    except Exception as err:
        print(err)
        return None


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
    return gpcr_assays,outputs