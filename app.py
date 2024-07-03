import streamlit as st 
from PIL import Image

st.title("This is My Body Mass Index (BMI) Calculator")

img = Image.open("bmi.jpg")
st.image(img)

# Introduction

st.subheader("Introduction")
st.caption("DRAFT Example Only")

st.text("""A healthy BMI for an adult is between 20 and 25. For older Australians over the age
of 74 years, your general health may be more important than being mildly overweight. '

Some researchers have suggested that a BMI range of 22-26 is acceptable for older
Australians.""")


# Input

weight = st.number_input("Enter your Weight in KG", step = 0.1)

height = st.number_input("Enter your Height in Meters")

if weight > 0 and height > 0:
    bmi = weight/(height)**2.0
    st.success(f"Your BMI is {bmi}")
else:
    st.error("Please enter your weight and height - then press the ENTER key.")
    
    




