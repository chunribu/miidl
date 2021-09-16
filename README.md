# [MIIDL](https://chunribu.github.io/miidl)

**MIIDL** `/ˈmaɪdəl/` is a Python package for biomarker identification based on interpretable deep learning.

---
### Installation

```bash
pip install miidl
```
or
```bash
conda install miidl -c bioconda
```

---
### Features

+ One-stop profiling
+ Multiple strategies for biological data
+ More interpretable, not a "black box"

---
### Workflow

#### 1) Quality Control

This is the very first procedure to perform filtering according to the non-missing (observation) rate.

#### 2) Normalization

MIIDL offers plenty of normalization methods to transform data and make samples more comparable. 

#### 3) Imputation

By default, this step is unactivated, as MIIDL is designed to solve problems including sparseness. But imputation can be useful in some cases. If needed, there are several methods to choose from. 

#### 4) Reshape

In order to apply a CNN model, pre-processed data needs to be zero-completed to a certain length.

#### 5) Modeling

A CNN classifier is trained for discrimination. [PyTorch](https://pytorch.org) is needed.

#### 6) Interpretation

[Captum](https://captum.ai/) is designed for model interpretability for PyTorch. This step relies heavily on captum.

---
### [Getting Started](https://github.com/chunribu/miidl/blob/main/Tutorials.ipynb)

Welcome! 👋 [This guide](https://github.com/chunribu/miidl/blob/main/Tutorials.ipynb) will provide you with a specific example that using miidl to detect microbial biomarkers for the diagnosis of colorectal cancer. After that, you will konw how to use this tool properly.

---
<!-- ---
### Citation

doi: -->