FROM bentoml/model-server:0.11.0-py37
LABEL author="ersilia"

WORKDIR /repo
COPY . /
RUN pip install rdkit-pypi==2022.9.5
RUN pip install torch==1.13.1+cpu torchvision==0.14.1+cpu -f https://download.pytorch.org/whl/torch_stable.html
RUN conda install -c conda-forge xorg-libxrender
