# 🏠 House Price Prediction Web App

This is a simple Flask web application that predicts California house prices using a trained linear regression model. The model was built using features like median income, house age, population, and more.

## 🔍 Project Overview

The app allows users to input six numerical features and returns a predicted house price based on a pre-trained model (`lr.house_model.joblib`).

### 🔢 Features Used for Prediction:
- **MedInc**: Median income in the block
- **HouseAge**: Median house age in the block
- **Population**: Block population
- **AvgOccup**: Average occupancy per household
- **Latitude**: Block latitude
- **AveRooms**: Average number of rooms per household

---

## 🚀 How to Run the Project Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/house-price-prediction-flask.git
cd house-price-prediction-flask
    