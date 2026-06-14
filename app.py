
import streamlit as st
import pandas as pd
import numpy as np
import pickle

# ==================================================
# PAGE CONFIG
# ==================================================
st.markdown("""
<style>

/* App */
.stApp{
    background:#0F172A;
}

/* Hero */
.hero{
    background:linear-gradient(
        135deg,
        #06b6d4,
        #8b5cf6
    );

    padding:40px;
    border-radius:20px;
    text-align:center;
    margin-bottom:25px;
}

.hero h1{
    color:white !important;
    font-size:48px;
    font-weight:700;
    margin-bottom:10px;
}

.hero h3{
    color:white !important;
    margin-bottom:10px;
}

.hero p{
    color:white !important;
    font-size:18px;
}

/* Metrics */
[data-testid="metric-container"]{
    background:#1E293B;
    border:1px solid #334155;
    border-radius:15px;
    padding:15px;
}

[data-testid="metric-container"] label{
    color:white !important;
}

[data-testid="metric-container"] div{
    color:white !important;
}

/* Sidebar */
[data-testid="stSidebar"]{
    background:#020617;
}

[data-testid="stSidebar"] *{
    color:white !important;
}

/* Inputs */
label{
    color:white !important;
    font-weight:600 !important;
}

/* Prediction Card */
.prediction-card{
    background:linear-gradient(
        135deg,
        #06b6d4,
        #8b5cf6
    );

    padding:30px;
    border-radius:20px;

    text-align:center;
    color:white;

    box-shadow:0 0 25px rgba(139,92,246,.4);
}

.prediction-card h1,
.prediction-card h2{
    color:white !important;
}

/* Button */
.stButton button{
    width:100%;
    height:60px;

    background:linear-gradient(
        90deg,
        #06b6d4,
        #8b5cf6
    );

    color:white;
    font-size:20px;
    font-weight:bold;

    border:none;
    border-radius:15px;
}

.stButton button:hover{
    transform:scale(1.02);
}

/* Dataframe */
[data-testid="stDataFrame"]{
    border-radius:15px;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# LOAD MODEL
# ==================================================
model = pickle.load(open("models/xgb_model.pkl", "rb"))
default_row = pickle.load(open("models/default_row.pkl", "rb"))

# ==================================================
# SIDEBAR
# ==================================================
st.sidebar.markdown("""
# 🏠 House Price AI

---

### 📊 Model Information

✅ **Model:** XGBoost Regressor

✅ **Dataset:** Ames Housing

✅ **Total Features:** 258

✅ **User Inputs:** 10

---

### 🎯 Performance

**R² Score:** 0.91

**RMSE:** 0.11

---

The model was trained using extensive feature engineering and optimization techniques.
""")

# ==================================================
# HERO SECTION
# ==================================================
st.markdown("""
<div style="
padding:35px;
border-radius:20px;
background:linear-gradient(135deg,#06b6d4,#8b5cf6);
text-align:center;
margin-bottom:25px;
">

<h1 style="color:white;">
🏠 House Price Prediction System
</h1>

<h4 style="color:white;">
AI Powered Real Estate Valuation using XGBoost
</h4>

<p style="color:white;">
Predict property prices using Machine Learning and advanced feature engineering.
</p>

</div>
""", unsafe_allow_html=True)

# ==================================================
# TOP METRICS
# ==================================================
m1, m2, m3, m4 = st.columns(4)

with m1:
    st.metric("Model", "XGBoost")

with m2:
    st.metric("Features", "258")

with m3:
    st.metric("Inputs", "10")

with m4:
    st.metric("Dataset Rows", "1460")

st.divider()

# ==================================================
# INPUTS
# ==================================================
st.subheader("🏡 Property Information")

col1, col2 = st.columns(2)

with col1:

    overall_qual = st.slider(
        "Overall Quality",
        1, 10, 5
    )

    gr_liv_area = st.number_input(
        "Living Area (sq ft)",
        500, 10000, 1500
    )

    garage_cars = st.slider(
        "Garage Capacity",
        0, 5, 2
    )

    garage_area = st.number_input(
        "Garage Area",
        0, 2000, 500
    )

    total_bsmt = st.number_input(
        "Basement Area",
        0, 5000, 1000
    )

with col2:

    year_built = st.number_input(
        "Year Built",
        1900, 2025, 2005
    )

    year_remod = st.number_input(
        "Year Remodeled",
        1900, 2025, 2005
    )

    full_bath = st.slider(
        "Full Bathrooms",
        0, 5, 2
    )

    rooms = st.slider(
        "Rooms Above Ground",
        1, 15, 6
    )

    lot_area = st.number_input(
        "Lot Area",
        1000, 50000, 8000
    )

st.divider()

# ==================================================
# PROPERTY SUMMARY
# ==================================================
st.subheader("📋 Property Summary")

summary = pd.DataFrame({
    "Feature": [
        "Overall Quality",
        "Living Area",
        "Garage Capacity",
        "Garage Area",
        "Basement Area",
        "Year Built",
        "Year Remodeled",
        "Bathrooms",
        "Rooms",
        "Lot Area"
    ],
    "Value": [
        overall_qual,
        gr_liv_area,
        garage_cars,
        garage_area,
        total_bsmt,
        year_built,
        year_remod,
        full_bath,
        rooms,
        lot_area
    ]
})

st.dataframe(
    summary,
    use_container_width=True,
    hide_index=True
)

st.divider()

# ==================================================
# PREDICTION
# ==================================================
if st.button("🔮 Predict House Price"):

    house = default_row.copy()

    house["OverallQual"] = overall_qual
    house["GrLivArea"] = gr_liv_area
    house["GarageCars"] = garage_cars
    house["GarageArea"] = garage_area
    house["TotalBsmtSF"] = total_bsmt
    house["YearBuilt"] = year_built
    house["YearRemodAdd"] = year_remod
    house["FullBath"] = full_bath
    house["TotRmsAbvGrd"] = rooms
    house["LotArea"] = lot_area

    input_df = pd.DataFrame([house])

    prediction = model.predict(input_df)

    predicted_price = np.expm1(prediction[0])

    rupees_price = predicted_price * 83

    st.markdown(f"""
    <div class="prediction-card">

    <h2>🏡 Estimated House Price</h2>

    <h1>${predicted_price:,.0f}</h1>

    <h2>₹ {rupees_price:,.0f}</h2>

    </div>
    """, unsafe_allow_html=True)

    st.balloons()

# ==================================================
# MODEL COMPARISON
# ==================================================
st.divider()

st.subheader("📈 Model Comparison")

comparison_df = pd.DataFrame({
    "Model": [
        "Linear Regression",
        "Random Forest",
        "XGBoost"
    ],
    "R² Score": [
        0.89,
        0.87,
        0.91
    ]
})

st.dataframe(
    comparison_df,
    use_container_width=True,
    hide_index=True
)

st.bar_chart(
    comparison_df.set_index("Model")
)

# ==================================================
# FOOTER
# ==================================================
st.divider()

st.markdown("""
<div class="glass">

### 🚀 Project Pipeline

1. Data Cleaning
2. Exploratory Data Analysis (EDA)
3. Feature Engineering
4. Linear Regression
5. Random Forest Regressor
6. XGBoost Regressor
7. Model Evaluation
8. Feature Importance Analysis
9. Streamlit Deployment

---

### 🏆 Final Selected Model

**XGBoost Regressor**

</div>
""", unsafe_allow_html=True)

st.caption(
    "Built with ❤️ using Streamlit, XGBoost and Ames Housing Dataset"
)

