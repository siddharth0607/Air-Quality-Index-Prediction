# Delhi Air Quality Index (AQI) Prediction

A machine learning-based project to predict Delhi's Air Quality Index (AQI) using historical data and various atmospheric features. The project involves feature engineering, model training, and deployment using modern web technologies and containerization.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [AQI Formula](#aqi-formula)
- [Directory Structure](#directory-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Model Performance](#model-performance)
- [How to Contribute](#how-to-contribute)

## Overview
This project aims to predict Delhi's AQI using machine learning models. The **Random Forest Regressor** model delivered the best performance with an R<sup>2</sup> score of **0.996** and RMSE of **7.62**. The dataset, which includes atmospheric pollutant data, is processed to calculate the AQI using a predefined formula. The project includes a backend built with **Flask, a user-friendly frontend developed with **HTML**, **CSS**, and **JavaScript**, and is containerized with **Docker** for seamless deployment.

## Features
- Trained multiple machine learning models to predict AQI with high accuracy.
- Performed extensive exploratory data analysis (EDA) and feature engineering to enhance model performance.
- Developed a REST API using Flask for processing user inputs and generating predictions.
- Built a responsive frontend for user interaction.
- Containerized the application using Docker and deployed it on Docker Hub.

## Tech Stack
- **Languages**: Python, HTML, CSS, JavaScript
- **Libraries**: scikit-learn, Flask, Pandas, NumPy, Matplotlib, Seaborn
- **Tools**: Docker, Docker Hub

## AQI Formula

The AQI is calculated based on the concentration of specific pollutants. For each pollutant, a specific formula is used to calculate the AQI. The general formula for AQI calculation is:

$$
I_{P} = \frac{(I_{HI} - I_{LO})}{(BP_{HI} - BP_{LO})} \cdot (C_{P} - BP_{LO}) + I_{LO}
$$

Where:
- I<sub>P</sub>: sub-index for pollutant P
- C<sub>P</sub>: Pollutant Concentration
- BP<sub>HI</sub>: Upper breakpoint for the pollutant's concentration range
- BP<sub>LO</sub>: Lower breakpoint for the pollutant's concentration range
- I<sub>HI</sub>: Upper AQI value for the corresponding range
- I<sub>LO</sub>: Lower AQI value for the corresponding range

For each pollutant, the individual AQI is computed using this formula, and the final AQI value is the maximum of these individual AQI values.

### Pollutants Used:
- *PM2.5 (Particulate Matter < 2.5 micrometers)*
- *PM10 (Particulate Matter < 10 micrometers)*
- *CO (Carbon Monoxide)*
- *NO<sub>2</sub> (Nitrogen Dioxide)*
- *SO<sub>2</sub> (Sulfur Dioxide)*
- *O<sub>3</sub> (Ozone)*
- *NH<sub>3</sub> (Ammonia)*

Each pollutant has a set of concentration ranges that map to specific AQI levels, which are then used to calculate the overall AQI.

## Directory Structure
```plaintext
project-directory/
|
|-- data/                      
|   |-- aqi_data.csv          # Processed dataset with AQI feature
|   |-- delhi_aqi.csv         # Raw dataset containing atmospheric pollutant data
|
|-- saved_models/              
|   |-- rf_model.pkl          # Trained Random Forest model
|
|-- static/                   # Static files for the frontend
|   |-- styles.css            # Custom styles for the frontend
|   |-- script.js             # Custom JavaScript for frontend interactions
|
|-- app.py                    # Flask-based backend application
|
|-- calculate_aqi.ipynb       # Jupyter Notebook used to calculate AQI from pollutant values
|
|-- model.ipynb               # Jupyter Notebook for training the Random Forest model
|
|-- Dockerfile                # Docker Configuration file
|
|-- requirements.txt          # Python Dependencies
```
## Installation
### Prerequisites
- Python 3.10 or later
- Docker

### Steps
**Option 1:** Pull the Pre-Built Docker Image
1. Pull the Docker image from Docker Hub:
```bash
docker pull siddharth0607/delhi-aqi-prediction:latest
```
2. Run the container:
```bash
docker run -d -p 5000:5000 siddharth0607/delhi-aqi-prediction:latest
```
3. Open your browser and navigate to `http://127.0.0.1:5000` to use the app.

**Option 2:** Build the Docker Image Locally
1. Clone the repository:
```bash
git clone https://github.com/siddharth0607/Air-Quality-Index-Prediction.git
```
2. Navigate to the project directory:
```bash
cd Air-Quality-Index-Prediction
```
3. Build the Docker image:
```bash
docker build -t your-dockerhub-username/delhi-aqi-prediction .
```
4. Run the container:
```bash
docker run -d -p 5000:5000 your-dockerhub-username/delhi-aqi-prediction
```
5. Open your browser and navigate to `http://127.0.0.1:5000` to use the app.

## Usage
1. Input the required atmospheric parameters like PM2.5, PM10, CO, NO, etc., into the provided fields on the frontend.
2. Submit the form to get the predicted AQI value.
3. View the prediction and interpret the results based on the AQI scale.

## Model Performance
The **Random Forest Regressor** achieved the following metrics:
- R<sup>2</sup> Score: 0.996
- RMSE: 7.62
## How to Contribute
If you'd like to contribute to this project, please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to your branch (`git push origin feature-branch`).
5. Create a pull request to merge your changes into the main branch.
