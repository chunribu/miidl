## MIIDL

**MIIDL** */ˈmaɪdəl/* is the abbreviation of "Markers Identification with Interpretable Deep Learning". MIIDL is a biomarker screening tool based on interpretable deep learning and applied to datasets with a large number of features.


---
### Installation

```bash
pip install miidl
# or
conda install -c bioconda miidl
```
**NOTE:** Not available yet

---
### Features

+ One-stop profiling
+ Multiple strategies for biological data
+ Better performance than traditional machine learning
+ More robust than ordinary artificial neural networks

---
### Command Generator

MIIDL is designed to be a user-friendly tool. Parameters are listed below, you can easily generate ready-to-run commands. (NOTE: Not yet fully functional)

<iframe src="cmd_generater.html" width="100%" height="600" style="border: none"></iframe>

---
### Workflow

#### Quality Control

This is the very first procedure to perform filtering according to the non-missing (observation) rate.

#### Normalization

MIIDL offers plenty of normalization methods to transform data and make samples more comparable. 

#### Imputation

By default, this step is unactivated, as MIIDL is designed to solve problems including sparseness. But imputation can be useful in some cases. If needed, there are several methods to choose from. 

#### Reshape

In order to apply a 2d-CNN for modeling, data after pre-processing need to be reshaped to a 2d-array which can be visualized like a photograph.

#### Modeling

Notably, we build a 2d-CNN classifier to perform discrimination. 

#### Interpretation

Shapley values have become one of the most popular feature attribution explanation methods for its sufficient theoretical support. Here, Shapley method is recommanded. Many other methods are also available.



<script>
    document.head.innerHTML+='<link rel="shortcut icon" type="image/x-icon" href="favicon.ico">'
</script>