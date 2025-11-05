# Lab3\_project

preprocessing, analysis, visualization


**Author:**

**Luciana Restrepo Cadavid**


**Biomedical Data Analysis Project — Labs 1, 2 \& 3**

This repository contains the development of three integrated laboratory exercises for biomedical data analysis, focused on the preprocessing, exploration, and statistical evaluation of respiratory pressure data.  

The work was developed as part of the Scientific Programming course and aims to demonstrate analytical, programming, and statistical skills for handling physiological datasets.


**Overview**


The dataset represents ventilatory cycles, including pressure, volume, and flow variables recorded over time.  

The analysis pipeline includes:

**1. Preprocessing:** Loading, cleaning, and preparing data for analysis.

**2. Exploratory Analysis:** Statistical summaries, normality assessment, detect outliers, correlation analysis, normality test (Kolmogorov) and Implementation of non-parametric tests (Kruskal–Wallis).

**3. Visualization:** Graphical representation of relationships and distributions.



**- Project Structure**


Lab3\_project/

│

├── data/

│ ├── raw/ # Original datasets

│ │ ├── train.csv

│ │ ├── test.csv

│ │ └── sample\_submission.csv

│ └── processed/ # Cleaned or transformed data

│

├── notebooks/ # Jupyter notebooks of the labs

│ ├── Laboratorio1.ipynb

│ ├── Laboratorio2.ipynb

│ └── Laboratorio3.ipynb

│

├── src/ # Source code (modularized by function)

│ ├── preprocessing/

│ │ └── clean\_data.py # Data loading and preprocessing

│ ├── analysis/

│ │ └── exploratory\_analysis.py # Descriptive and statistical analysis

│ └── visualization/

│ └── plots.py # Visualization and plotting scripts

│

└── README.md



**- Requirements**

Setup and Execution Guide

To execute the project, install the required Python packages:

```bash


git clone https://github.com/lucianarpo14/Lab3_project.git
cd Lab3_project


python -m venv venv
venv\Scripts\activate   # On Windows
# source venv/bin/activate   # On macOS or Linux


pip install -r requirements.txt

pip install pandas numpy matplotlib seaborn scipy openpyxl

python notebooks/Lab3.py

```

Finally, ensure the dataset files are located in the following directory structure:

data/raw/train.csv

data/raw/test.csv

data/raw/sample_submission.csv

