# Dataset Overview

## Introduction

The dataset used in this project is the **Ames Housing Dataset**, originally compiled by **Dean De Cock**, Professor of Statistics at Iowa State University. It is one of the most widely used datasets for regression and house price prediction tasks.

The dataset contains detailed information about residential properties sold in Ames, Iowa, USA. Various property-related features such as location, plot size, construction quality, living area, garage details, basement characteristics, and sale information are included.

---

# Dataset Statistics

| Attribute                 | Value     |
| ------------------------- | --------- |
| Total Rows (Observations) | 1460      |
| Total Columns (Features)  | 81        |
| Input Features            | 80        |
| Target Variable           | SalePrice |
| Numerical Features        | 36        |
| Categorical Features      | 43        |

---

# Target Variable

The objective of this dataset is to predict the **SalePrice**, which represents the final selling price of a house.

| Target Variable | Description                      |
| --------------- | -------------------------------- |
| SalePrice       | Final selling price of the house |

---

# Feature Categories

# Dataset Overview

## Basic Information

- Total Records: **1460**
- Total Features: **81**
- Target Variable: **SalePrice**
- Problem Type: **Regression**
- Goal: Predict house selling price based on house characteristics.

---

# Feature Categories

## 1. Property / Land Information

These features describe the land and plot characteristics.

| Column | Description |
|----------|----------|
| LotArea | Total plot area |
| LotFrontage | Linear feet connected to street |
| LotShape | Shape of the property |
| Street | Type of road access |
| Alley | Alley access |
| LandContour | Flatness of the property |

---

## 2. Location Features

These features describe the location of the property.

| Column | Description |
|----------|----------|
| Neighborhood | Physical location within Ames city |
| Condition1 | Proximity to various conditions |
| Condition2 | Secondary proximity condition |

### Importance
Location significantly affects house prices.

---

## 3. Building Structure Features

These features describe the overall construction and structure.

| Column | Description |
|----------|----------|
| BldgType | Type of dwelling |
| HouseStyle | Style of dwelling |
| OverallQual | Overall material and finish quality |
| OverallCond | Overall condition rating |

### Importance
Higher quality homes generally have higher selling prices.

---

## 4. Construction Year Features

| Column | Description |
|----------|----------|
| YearBuilt | Original construction year |
| YearRemodAdd | Remodel year |

### Importance
Newer and recently renovated homes usually have higher market value.

---

## 5. Exterior Features

| Column | Description |
|----------|----------|
| Exterior1st | Exterior covering on house |
| Exterior2nd | Secondary exterior covering |
| ExterQual | Exterior material quality |
| ExterCond | Exterior condition |

---

## 6. Basement Features

These features describe basement quality and size.

| Column | Description |
|----------|----------|
| BsmtQual | Basement quality |
| BsmtCond | Basement condition |
| BsmtExposure | Walkout or garden level walls |
| BsmtFinType1 | Finished basement rating |
| BsmtFinSF1 | Finished basement area |
| TotalBsmtSF | Total basement area |

### Importance
Basement area and quality can significantly impact house value.

---

## 7. Heating and Utility Features

| Column | Description |
|----------|----------|
| Heating | Heating type |
| HeatingQC | Heating quality and condition |
| CentralAir | Central air conditioning |
| Electrical | Electrical system |

---

## 8. Room Features

These features describe the living space inside the house.

| Column | Description |
|----------|----------|
| BedroomAbvGr | Number of bedrooms |
| KitchenAbvGr | Number of kitchens |
| FullBath | Number of full bathrooms |
| HalfBath | Number of half bathrooms |
| TotRmsAbvGrd | Total rooms above ground |
| GrLivArea | Above-ground living area |

### Importance
Living area and room count are major factors affecting sale price.

---

## 9. Fireplace Features

| Column | Description |
|----------|----------|
| Fireplaces | Number of fireplaces |
| FireplaceQu | Fireplace quality |

---

## 10. Garage Features

| Column | Description |
|----------|----------|
| GarageType | Garage location/type |
| GarageCars | Garage capacity |
| GarageArea | Garage area |
| GarageQual | Garage quality |
| GarageCond | Garage condition |

### Importance
Garage size and condition often influence house prices.

---

## 11. Outdoor Features

| Column | Description |
|----------|----------|
| WoodDeckSF | Deck area |
| OpenPorchSF | Open porch area |
| EnclosedPorch | Enclosed porch area |
| ScreenPorch | Screen porch area |

---

## 12. Luxury Features

| Column | Description |
|----------|----------|
| PoolArea | Pool area |
| PoolQC | Pool quality |
| Fence | Fence quality |
| MiscFeature | Miscellaneous features |

### Importance
Luxury amenities can increase property value.

---

## 13. Sale Information

| Column | Description |
|----------|----------|
| MoSold | Month sold |
| YrSold | Year sold |
| SaleType | Type of sale |
| SaleCondition | Condition of sale |

---

## 14. Target Variable

| Column | Description |
|----------|----------|
| SalePrice | Final selling price of the house |

### Objective

The machine learning model uses all property-related features to predict the final house selling price (**SalePrice**).

---

# Data Type Distribution

| Feature Type         | Count |
| -------------------- | ----- |
| Numerical Features   | 36    |
| Categorical Features | 43    |
| Total Features       | 81    |

### Visualization

```text
Total Features : 81
├── Numerical Features : 38
└── Categorical Features : 43
```

---

# Key Characteristics of the Dataset

* Contains detailed information about residential properties.
* Suitable for regression and predictive analytics tasks.
* Includes both numerical and categorical variables.
* Contains missing values that require preprocessing.
* Widely used for machine learning, feature engineering, and exploratory data analysis (EDA).
* The primary goal is to predict house prices accurately using property attributes.

---

# Dataset Source

**Dean De Cock**
Professor of Statistics
Iowa State University

**Citation:**

De Cock, D. (2011). *Ames, Iowa: Alternative to the Boston Housing Data as an End of Semester Regression Project*. Journal of Statistics Education, Volume 19, Number 3.
