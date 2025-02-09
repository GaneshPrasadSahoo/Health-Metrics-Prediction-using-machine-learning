# Health Metrics Prediction using Deep Learning

## Project Overview

This project leverages machine learning techniques to predict key health metrics based on user inputs. The objective is to predict **Blood Pressure (Systolic/Diastolic)**, **Stress Level**, and **Heart Rate** using input features like **Gender**, **Age**, **Sleep Duration**, **Physical Activity Level**, **Daily Steps**, and **BMI Category**.

The project includes a **Streamlit** web interface where users can input their details, and the model predicts their health metrics. Various machine learning models, including **RandomForestRegressor**, **DecisionTreeRegressor**, and **K-Nearest Neighbors (KNN)**, are trained to make accurate predictions.

Here’s a screenshot of the web application:

![Web Application Screenshot](./Screenshot%202025-02-09%20232104.png)

## Key Features
- **User Input:**
  - Gender
  - Age
  - Sleep Duration
  - Physical Activity Level
  - Daily Steps
  - BMI Category

- **Output:**
  - Predicted Blood Pressure (Systolic/Diastolic)
  - Blood Pressure Status (Hypertension Stage 1 or Normal)
  - Stress Level (Moderate Stress or Low Stress)
  - Heart Rate

## Models Used
- **RandomForestRegressor**: High accuracy with a Mean Squared Error of 0.495 and an R-squared value of 0.9835.
- **DecisionTreeRegressor**: Moderate performance with a Mean Squared Error of 1.243 and an R-squared value of 0.9519.
- **K-Nearest Neighbors (KNN)**: Training accuracy of 100% and testing accuracy of 81.43%.

## Evaluation Metrics
- **RandomForestRegressor**:
  - Mean Squared Error: 0.495
  - Mean Absolute Error: 0.177
  - R-squared: 0.9835

- **DecisionTreeRegressor**:
  - Mean Squared Error: 1.243
  - Mean Absolute Error: 0.17
  - R-squared: 0.9519

- **K-Nearest Neighbors (KNN)**:
  - Mean Squared Error: 5.14
  - Mean Absolute Error: 0.383
  - R-squared: 0.814

## Streamlit Web Interface
The project includes a **Streamlit**-based web interface, allowing users to input their health data and receive predictions. The web interface is easy to use, and the output consists of predicted **Blood Pressure**, **Stress Level**, and **Heart Rate**.

### Sample Output:
- **Blood Pressure**: 135/90 (Hypertension Stage 1)
- **Stress Level**: 6 (Moderate Stress)
- **Heart Rate**: 65 bpm

## Requirements
To run this project, you need the following Python libraries:
- `pandas`
- `numpy`
- `scikit-learn`
- `streamlit`
- `matplotlib` (optional for data visualization)

## Conclusion
This project showcases the power of machine learning to predict health metrics based on a variety of inputs. The RandomForestRegressor model performs the best, providing highly accurate predictions. This tool can be used for health monitoring and provides an easy-to-use interface for users to get their health metrics instantly.
