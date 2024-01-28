import streamlit as st
import plotly.express as px
import backend

st.set_page_config(layout="centered")
st.title("Weather Forecast")
City = st.text_input("Enter the name of city / Place", key="city")
Days = st.slider(label="No. of days", min_value=1, max_value=5,
                 help="number of days to forecast the weather for")
Option = st.selectbox("Select data to show :", ("Temperature", "Sky"))
st.subheader(f"{Option} for next {Days} days in {City.capitalize()}")
if City:
    try:
        data, dates = backend.get_data(City, Days, Option)
        if Option == "Temperature":
            figure = px.line(x=dates, y=data, labels={"x": "Date", "y": Option})
            st.plotly_chart(figure)
        if Option == "Sky":
            images = []
            times = []
            for weather, time in zip(data, dates):
                images.append(f'image/{weather}.png')
                times.append(time)
            st.image(images, caption=times, width=85)
    except KeyError:
        st.warning('City does not exist in database', icon="⚠️")
