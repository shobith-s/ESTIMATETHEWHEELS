# ESTIMATETHEWHEELS

## A Machine Learning App to Estimate Car Resale Prices Based on Market Trends and Car Features

## Overview
The Car Resale Value Prediction app uses machine learning to estimate the resale value of cars based on various parameters such as car specifications, color demand preferences, and accident history. This interactive web application provides users with a data-driven price estimation for better decision-making when buying or selling cars.

# Features
1. Car Specifications Input:
Car brand, model year, mileage, engine capacity, max power, fuel type, and other attributes are collected.

3. Color Demand Preference:
Incorporates the market demand for car colors to adjust resale predictions.
Popular colors (e.g., black, white, grey) positively influence the resale value.

3. Accident History:
Users can input the number of past accidents or select accident history to account for price depreciation.

4. Image Uploads:
Allows users to upload images (e.g., front view, back view, side views) to support the resale evaluation process.

5. Machine Learning Model:
Predicts car prices using a trained regression model based on historical car sales data.

6. Responsive UI:
Built with Streamlit, providing an intuitive user interface for inputs and results.

# Requirements
1. Python (>= 3.7)
2. Pandas
3. NumPy
4. xgboost
5. Scikit-Learn
6. Streamlit
7. Pickle

# Prediction Logic

Base Price Prediction:
The trained regression model estimates a base price based on car attributes (engine size, mileage, fuel type, etc.).

Color Demand Adjustment:
Colors in high demand (e.g., white, black) will receive a positive adjustment to the predicted value.
Less popular colors are slightly depreciated.

Accident Penalty:
Cars with accident history receive a depreciation factor proportional to the number of accidents reported.
