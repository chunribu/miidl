## MIIDL

**MIIDL** */ˈmaɪdəl/* is the abbreviation of "Markers Identification with Interpretable Deep Learning". MIIDL is a biomarker screening tool based on interpretable deep learning and applied to datasets with a large number of features.

***NOTE: Not available yet***

---
### Installation

```bash
pip install miidl
```

---
### Features

+ One-stop profiling
+ Multiple strategies for biological data
+ Better performance than traditional machine learning
+ More robust than ordinary artificial neural networks

---
### Get Started

MIIDL is designed to be a user friendly tool. Parameters are listed below, and you can use this graphic interface to generate a ready-to-run command if MIIDL is installed. (NOTE: Not yet fully functional)

<iframe src="cmd_generater.html" width="100%" height="700" style="border: none"></iframe>

---
### Workflow

#### Quality Control

This is the very first procedure to perform filtering according to the missing rate.

#### Normalization

MIIDL offers plenty of normalization methods to transform data and make samples more comparable. 

#### Imputation

By default, this step is unactivated, as MIIDL is designed to solve problems including sparseness. But imputation can be useful in some cases, there are various methods to choose if needed. 

#### Reshape

In order to apply a 2d-CNN for modeling, data after pre-processing need to be reshaped to a 2d-array which can be visualized like a photograph.

#### Modeling

Notably, we build a 2d-CNN classifier to perform discrimination. You can also write annother model manually in PyTorch.

#### Interpretation

Shapley values have become one of the most popular feature attribution explanation methods for its sufficient theoretical support. Here, Shapley method is recommanded. Meanwhile, many other methods are also available.

#### Networking

Finally, MIIDL builds a network with key genes to reveal potential regulatory relationships, providing reference for further analysis.

---
### *Citation*


<script>
    document.head.innerHTML+='<link rel="shortcut icon" type="image/x-icon" href="favicon.ico">'
</script>