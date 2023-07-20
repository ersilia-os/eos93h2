# imports
import csv
import sys


from image_dataloader import get_predictions


# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]


# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

# run _model
gpcr_assays, outputs = get_predictions(smiles_list)

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
