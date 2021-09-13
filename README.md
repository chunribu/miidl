# [MIIDL](https://chunribu.github.io/miidl)

**MIIDL** */ˈmaɪdəl/* is the abbreviation of "Markers Identification with Interpretable Deep Learning". MIIDL is a biomarker screening tool based on interpretable deep learning and applied to datasets with a large number of features.

---
### Installation

```bash
pip install miidl
# or
conda install miidl
```

***NOTE: Not available yet***

---
### Features

+ One-stop profiling
+ Multiple strategies for biological data
+ Better performance than traditional machine learning
+ More robust than ordinary artificial neural networks

---
### Workflow

#### 1) Quality Control

This is the very first procedure to perform filtering according to the missing rate.

#### 2) Normalization

MIIDL offers plenty of normalization methods to transform data and make samples more comparable. 

#### 3) Imputation

By default, this step is unactivated, as MIIDL is designed to solve problems including sparseness. But imputation can be useful in some cases, there are various methods to choose if needed. 

#### 4) Reshape

In order to apply a 2d-CNN for modeling, data after pre-processing need to be reshaped to a 2d-array which can be visualized like a photograph.

#### 5) Modeling

Notably, we build a 2d-CNN classifier to perform discrimination. You can also write annother model manually in PyTorch.

#### 6) Interpretation

Shapley values have become one of the most popular feature attribution explanation methods for its sufficient theoretical support. Here, Shapley method is recommanded. Meanwhile, many other methods are also available.


<!-- ---
### Citation

doi: -->