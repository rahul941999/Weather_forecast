import streamlit as st
import plotly.express as px
import backend

st.title("Weather Forecast")
City = st.text_input("Enter the name of city / Place", key="city")
if not City:
    City = "Delhi"
Days = st.slider(label="No. of days", min_value=1, max_value=5,
                 help="number of days to forecast the weather for")
Option = st.selectbox("Select data to show :", ("Temperature", "Sky"))
st.subheader(f"{Option} for next {Days} days in {City.capitalize()}")

data, dates = backend.get_data(City, Days, Option)
figure = px.line(x=dates, y=data,
                 labels={"x": "Date", "y": Option})
st.plotly_chart(figure)
