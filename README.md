# [MIIDL](https://chunribu.github.io/miidl)

**MIIDL** */ˈmaɪdəl/*, the abbreviation of "Markers Identification with Interpretable Deep Learning", is a biomarker screening tool based on interpretable deep learning.

---
### Installation

```bash
pip install miidl
# or
conda install miidl -c bioconda
```

***NOTE: Not available yet***

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

A 1d-CNN classifier is trained for discrimination. 

#### 6) Interpretation

[Captum](https://captum.ai/) is designed for model interpretability for PyTorch. This step relies heavily on captum.


<!-- ---
### Citation

doi: -->