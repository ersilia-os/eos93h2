# imagemol-gpcr

ImageMol is a Representation Learning Framework that utilizes molecule images for encoding molecular inputs as machine readable vectors for downstream tasks such as bio-activity prediction, drug metabolism analysis, or drug toxicity prediction. The approach utilizes transfer learning, that is, pre-training the model on massive unlabeled datasets to help it in generalizing feature extraction and then fine tuning on specific tasks. This model is fine tuned on 10 GPCR assays with the largest number of reported ligands from ChEMBL datasets.

This model was incorporated on 2023-01-25.

## Information
### Identifiers
- **Ersilia Identifier:** `eos93h2`
- **Slug:** `image-mol-gpcr`

### Domain
- **Task:** `Representation`
- **Subtask:** `Featurization`
- **Biomedical Area:** `Any`
- **Target Organism:** `Homo sapiens`
- **Tags:** `Target identification`, `GPCR`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `10`
- **Output Consistency:** `Fixed`
- **Interpretation:** Binding activity prediction (as a regression task) for the following GPCR assays: 5HT1A, 5HT2A, AA1R, AA2AR, AA3R, CNR2, DRD2, DRD3, HRH3, OPRM

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| 5ht1a | float | high | Ligand binding prediction to 5HT1A |
| 5ht2a | float | high | Ligand binding prediction to 5HT2A |
| aa1r | float | high | Ligand binding prediction to AA1R |
| aa2ar | float | high | Ligand binding prediction to AA2AR |
| aa3r | float | high | Ligand binding prediction to AAR3 |
| cnr2 | float | high | Ligand binding prediction to CNR2 |
| drd2 | float | high | Ligand binding prediction to DRD2 |
| drd3 | float | high | Ligand binding prediction to DRD3 |
| hrh3 | float | high | Ligand binding prediction to HRH3 |
| oprm | float | high | Ligand binding prediction to OPRM |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos93h2](https://hub.docker.com/r/ersiliaos/eos93h2)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos93h2.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos93h2.zip)

### Resource Consumption
- **Model Size (Mb):** `428`
- **Environment Size (Mb):** `1203`
- **Image Size (Mb):** `2424.83`

**Computational Performance (seconds):**
- 10 inputs: `36.88`
- 100 inputs: `106.33`
- 10000 inputs: `-1`

### References
- **Source Code**: [https://github.com/HongxinXiang/ImageMol](https://github.com/HongxinXiang/ImageMol)
- **Publication**: [https://www.nature.com/articles/s42256-022-00557-6](https://www.nature.com/articles/s42256-022-00557-6)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2022`
- **Ersilia Contributor:** [DhanshreeA](https://github.com/DhanshreeA)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [MIT](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos93h2
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos93h2
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
