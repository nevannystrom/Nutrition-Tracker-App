import streamlit as st

st.title("Nutrition Tracker App")

st.write("Enter your information to get recommended calorie and protein goals.")

# Inputs
gender = st.selectbox("Select your gender:", ["Male", "Female"])
weight = st.number_input("Enter your weight (lbs):", min_value=1)
height = st.number_input("Enter your height (inches):", min_value=1)
age = st.number_input("Enter your age:", min_value=1)

# Convert units (needed for BMR)
weight_kg = weight * 0.453592
height_cm = height * 2.54

# BMR calculation
if gender == "Male":
    bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
else:
    bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161

# Assume moderately active
calories = bmr * 1.55

# Protein estimate (still simple)
protein = weight * 0.8

# Output
st.subheader("Your Daily Goals")
st.write(f"Recommended Calories: {calories:.0f}")
st.write(f"Recommended Protein: {protein:.0f} grams")

st.write("These are estimates based on a moderately active lifestyle.")
