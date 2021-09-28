# [MIIDL](https://chunribu.github.io/miidl)

[![chunribu logo](https://img.shields.io/badge/chunribu-🚀-black?logo=github)](https://github.com/chunribu/) [![Anaconda-Server Badge](https://anaconda.org/bioconda/miidl/badges/version.svg)](https://anaconda.org/bioconda/miidl) [![Conda](https://img.shields.io/conda/dn/bioconda/miidl?color=green&logo=anaconda&style=flat-square)](https://anaconda.org/bioconda/miidl) [![PyPI - Downloads](https://img.shields.io/pypi/dm/miidl?logo=pypi&style=flat-square)](https://pypi.org/project/miidl/) [![Anaconda-Server Badge](https://anaconda.org/bioconda/miidl/badges/platforms.svg)](https://anaconda.org/bioconda/miidl) [![arXiv](https://img.shields.io/badge/arXiv-2109.12204-default?style=flat-square)](https://arxiv.org/abs/2109.12204) [![Anaconda-Server Badge](https://anaconda.org/bioconda/miidl/badges/license.svg)](https://anaconda.org/bioconda/miidl) 

**MIIDL** `/ˈmaɪdəl/` is a Python package for microbial biomarkers identification powered by interpretable deep learning.

![model.png](https://github.com/chunribu/miidl/raw/main/docs/model.png)

---
### [Getting Started](https://github.com/chunribu/miidl/blob/main/Tutorials.ipynb)

👋Welcome! 

[🔗This guide](https://github.com/chunribu/miidl/blob/main/Tutorials.ipynb) will provide you with a specific example that using `miidl` to detect microbial biomarkers of colorectal cancer and predict clinical outcomes. 

After that, you will learn how to use this tool properly.

---
### Installation

```bash
pip install miidl
```
or
```bash
conda install miidl captum -c pytorch -c conda-forge -c bioconda
```

---
### Features

+ One-stop profiling
+ Multiple strategies for biological data
+ More interpretable, not a "black box"

---
### Workflow

#### 1) Quality Control

The very first procedure is filtering features according to a threshold of observation (non-missing) rate (0.3 by default).

#### 2) Normalization

`miidl` offers plenty of normalization methods to transform data and make samples more comparable. 

#### 3) Imputation

By default, this step is inactivated, as `miidl` is designed to solve problems including sparseness. But imputation can be useful in some cases. Commonly used methods are available if needed. 

#### 4) Reshape

The pre-processed data also need to be zero-completed to a certain length, so that a CNN model can be applied.

#### 5) Modeling

A CNN classifier is trained for discrimination. [PyTorch](https://pytorch.org) is needed.

#### 6) Interpretation

[Captum](https://captum.ai/) is dedicated to model interpretability for PyTorch. This step depends heavily on captum.

---
### Contact

If you have further thoughts or queries, please feel free to email at chunribu@mail.sdu.edu.cn or open an issue!

---
### Citation

```
@misc{jiang2021miidl,
      title={MIIDL: a Python package for microbial biomarkers identification powered by interpretable deep learning}, 
      author={Jian Jiang},
      year={2021},
      eprint={2109.12204},
      archivePrefix={arXiv},
      primaryClass={q-bio.QM}
}
```

---
### License

MIIDL is released under the [MIT license](https://github.com/chunribu/miidl/blob/main/LICENSE).
