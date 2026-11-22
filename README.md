
# 🏠 Bengaluru House Price Prediction

A Machine Learning-based House Price Prediction System that estimates residential property prices in Bengaluru based on property features such as location, area type, total square feet, number of bedrooms, bathrooms, and balconies.

The project uses multiple regression algorithms to predict house prices, compares their performance, performs hyperparameter tuning, and deploys the trained model using **Streamlit**.

## 📌 Project Overview

Real estate prices depend on several factors, including property size, location, and available facilities. This project aims to build a predictive system that helps estimate house prices in Bengaluru using historical housing data.

The project follows a complete Machine Learning workflow, starting from data preprocessing and exploratory data analysis to model training, evaluation, optimization, and deployment.

## 🎯 Objectives

- Analyze Bengaluru housing data.
- Perform data cleaning and preprocessing.
- Handle missing values and duplicate records.
- Perform exploratory data analysis (EDA).
- Identify and remove outliers.
- Apply feature engineering.
- Train multiple regression algorithms.
- Compare model performance using evaluation metrics.
- Perform hyperparameter tuning using GridSearchCV.
- Deploy the trained model using Streamlit.

## 📂 Dataset Information

**Dataset:** Bengaluru House Data

**Target Variable:** `price`

**Features used:**

| Feature | Description |
|---|---|
| area_type | Type of property area |
| location | Property location in Bengaluru |
| total_sqft | Total area in square feet |
| bhk | Number of bedrooms |
| bath | Number of bathrooms |
| balcony | Number of balconies |
| price | Property price in lakhs (target) |

The `bhk` feature is extracted from the original `size` column, and `total_sqft` is converted into numerical values.

## 🛠️ Technologies & Libraries Used

**Programming Language**
- Python

**Data Analysis & Visualization**
- Pandas
- NumPy
- Matplotlib
- Seaborn

**Machine Learning**
- Scikit-learn
- Linear Regression
- Ridge Regression
- Decision Tree Regressor
- Random Forest Regressor
- Extra Trees Regressor

**Model Optimization**
- GridSearchCV
- Cross-validation
- Hyperparameter tuning

**Deployment & Model Serialization**
- Streamlit
- Joblib

## ⚙️ Machine Learning Workflow

1. **Data Collection:** Load the Bengaluru housing dataset using Pandas.
2. **Data Understanding:** Examine dataset dimensions, data types, statistical summaries, and missing values.
3. **Data Cleaning:** Remove duplicates and handle missing values.
4. **Feature Engineering:** Extract BHK values and convert square-foot ranges into numerical values.
5. **EDA:** Visualize distributions, relationships, and correlations.
6. **Outlier Removal:** Remove unrealistic property configurations.
7. **Encoding:** Apply OneHotEncoder to categorical features.
8. **Scaling:** Apply StandardScaler to numerical features.
9. **Train-Test Split:** Divide the dataset into 80% training and 20% testing data.
10. **Model Training:** Train multiple regression algorithms.
11. **Model Evaluation:** Compare models using MAE, MSE, RMSE, and R² Score.
12. **Hyperparameter Tuning:** Optimize the Random Forest model using GridSearchCV.
13. **Model Saving:** Save the trained model using Joblib.
14. **Deployment:** Build an interactive prediction interface using Streamlit.

## 🤖 Machine Learning Algorithms

The following regression algorithms are implemented:

| Algorithm | Purpose |
|---|---|
| Linear Regression | Establishes a linear relationship between features and price |
| Ridge Regression | Applies regularization to reduce overfitting |
| Decision Tree Regressor | Captures nonlinear relationships |
| Random Forest Regressor | Combines multiple decision trees |
| Extra Trees Regressor | Uses randomized decision trees for ensemble prediction |

## 📊 Model Evaluation Metrics

The models are evaluated using:

- **MAE (Mean Absolute Error):** Measures the average absolute difference between actual and predicted prices.
- **MSE (Mean Squared Error):** Measures the average squared prediction error.
- **RMSE (Root Mean Squared Error):** Represents prediction error in the original price unit.
- **R² Score:** Measures how much variation in house prices is explained by the model.

## 📁 Project Structure

```text
Bengaluru_House_Prediction/
│
├── Bengaluru_House_Data.csv
│
├── house_price_prediction.ipynb
│
├── house_price_model.pkl
│
├── app.py
│
└── README.md
```

## 🚀 Installation & Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project directory

```bash
cd Bengaluru_House_Prediction
```

### 3. Install dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn streamlit joblib
```

### 4. Train the Machine Learning Model

Open and execute `house_price_prediction.ipynb` to perform preprocessing, model training, evaluation, and hyperparameter tuning.

Generate the trained model file:

```python
joblib.dump(model_data, 'house_price_model.pkl')
```

### 5. Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open in your default web browser.

## 🖥️ Application Features

- Interactive user interface.
- Location selection.
- Area type selection.
- Input property size in square feet.
- Select number of bedrooms (BHK).
- Enter bathroom and balcony details.
- Predict estimated property prices.
- Display predicted prices in Indian Rupees.

## 🔮 Future Improvements

- Integrate additional regression algorithms such as XGBoost and CatBoost.
- Improve feature engineering and outlier detection.
- Implement advanced location-based analysis.
- Add interactive data visualizations.
- Deploy the application on Streamlit Community Cloud.
- Improve model performance through advanced optimization techniques.

## 👩‍💻 Author

**Sreyoshi Nath**

B.Tech | Computer Science and Engineering (Artificial Intelligence & Machine Learning)

**Areas of Interest:** Artificial Intelligence, Machine Learning, Data Science, and Frontend Development.

---

⭐ If you find this project interesting, consider giving the repository a star!

*This project is developed for educational and machine learning practice purposes. Predicted prices are estimates and should not be considered professional real estate valuations.*

