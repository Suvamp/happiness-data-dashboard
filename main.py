import pandas as pd
import streamlit as st
import plotly.express as px

# Add a title widget
st.title("In Search for Happiness")

# Add two selectboxes
x_option = st.selectbox("Select the data for the X-axis",
                        ("GDP", "Happiness", "Generosity"))

y_option = st.selectbox("Select the data for the Y-axis",
                        ("GDP", "Happiness", "Generosity"))

# Load the dataframe
df = pd.read_csv("happy.csv")

# Match value of the first option
match x_option:
    case "GDP":
        x_array = df["gdp"]
    case "Happiness":
        x_array = df["happiness"]
    case "Generosity":
        x_array = df["generosity"]

# match value of the second option
match y_option:
    case "GDP":
        y_array = df["gdp"]
    case "Happiness":
        y_array = df["happiness"]
    case "Generosity":
        y_array = df["generosity"]

st.subheader(f"{x_option} and {y_option}")

figure = px.scatter(x=x_array, y=y_array, labels={"x": f"{x_option}", "y": f"{y_option}"})
st.plotly_chart(figure)
