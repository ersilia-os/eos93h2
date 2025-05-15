FROM bentoml/model-server:0.11.0-py38
LABEL author="ersilia"

RUN pip install rdkit-pypi==2022.9.5
RUN pip install torch==1.13.1 --extra-index-url https://download.pytorch.org/whl/cpu
RUN pip install torchvision==0.14.1 --extra-index-url https://download.pytorch.org/whl/cpu

WORKDIR /repo
COPY . /