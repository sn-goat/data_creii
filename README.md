# Data CREII

## Introduction

Data Creii is a Python project developed for the Centre de Référence des élèves Issus de l'immigration (CREII). The purpose of this project is to collect data from Facebook, Instagram, and LinkedIn and store it in separate CSV files for further analysis and reference.

## About CREII

The Centre de Référence des élèves Issus de l'immigration (CREII) is an organization dedicated to supporting students from immigrant backgrounds. Data Creii aims to aid CREII in their mission by providing valuable insights through data collection and analysis.

## Getting Started

To get started with data_creii, follow these steps:

1. **Install the necessary libraries**: Ex: Execute `pip install playwright` to install Playwright.
2. **Run the script**: Execute `python3 data_collector_main.py` to start collecting data or `python3 data_predictions_main.py` to see trends and predict data.
2. **Run the script**: Execute `python3 main.py` to start collecting data or execute `python3 data_predictions_main.py` to see trends and predict data.

## Features

* **Data collection from Facebook, Instagram, and LinkedIn**
* **Data storage in CSV files**
* **Customizable data collection parameters**
* **Data prediction from Facebook, Instagram, and LinkedIn**
* **Model storage in pickle files**
* **Data visualisation with graphs**

## CSV Files

The following CSV files will be generated or updated in the data directory:

* `data_facebook.csv`
* `data_instagram.csv`
* `data_linkedin.csv`

## Data Prediction

The `data_prediction.py` script is used to predict data trends using linear regression. It utilizes the `sklearn` for building the predictive models. The script also uses `plotly.express` to visualize data and the different slopes of the regression lines.

The models generated for each platform are saved in the following files:

* `facebookmodel.pickle`
* `instagrammodel.pickle`
* `linkedinmodel.pickle`

## Acknowledgments

I would like to thank the CREII organization for their support on this project.
