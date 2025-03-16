import streamlit as st
import pandas as pd
import datetime

# Load the Excel data
excel_file = "Chinese_Lunar_New_Year_1900_2030_Full.xlsx"
zodiac_df = pd.read_excel(excel_file)

# Convert 'Lunar New Year Date' to datetime (assuming format like "January 1")
zodiac_df['Lunar New Year Date'] = pd.to_datetime(zodiac_df['Lunar New Year Date'] + ' ' + zodiac_df['Year'].astype(str))

# Create lookup dictionaries
lunar_new_year_dates = pd.Series(zodiac_df['Lunar New Year Date'].values, index=zodiac_df['Year']).to_dict()
zodiac_data = pd.Series(zodiac_df['Zodiac Animal'].values, index=zodiac_df['Year']).to_dict()
chinese_names = pd.Series(zodiac_df['Chinese Name Animal'].values, index=zodiac_df['Year']).to_dict()

# Zodiac traits and compatibility
zodiac_traits = {
    "Rat": "Clever, quick-witted, resourceful, versatile, and sharp-minded.",
    "Ox": "Hardworking, reliable, determined, and methodical.",
    "Tiger": "Brave, confident, ambitious, and competitive.",
    "Rabbit": "Gentle, kind-hearted, compassionate, and peaceful.",
    "Dragon": "Charismatic, intelligent, and natural leaders.",
    "Snake": "Wise, intuitive, graceful, and intelligent.",
    "Horse": "Energetic, independent, and intelligent.",
    "Goat": "Gentle, creative, and compassionate.",
    "Monkey": "Clever, mischievous, and intelligent.",
    "Rooster": "Confident, honest, and punctual.",
    "Dog": "Loyal, honest, and friendly.",
    "Pig": "Generous, kind-hearted, and diligent."
}

zodiac_compatibility = {
    "Rat": "Compatible with Ox, Dragon, Monkey. Incompatible with Horse, Sheep.",
    "Ox": "Compatible with Rat, Snake, Rooster. Incompatible with Sheep, Horse.",
    "Tiger": "Compatible with Horse, Dog. Incompatible with Monkey, Snake.",
    "Rabbit": "Compatible with Sheep, Dog. Incompatible with Rooster, Dragon.",
    "Dragon": "Compatible with Rat, Monkey, Rooster. Incompatible with Dog, Rabbit.",
    "Snake": "Compatible with Rooster, Ox. Incompatible with Tiger, Pig.",
    "Horse": "Compatible with Tiger, Goat. Incompatible with Rat, Ox.",
    "Goat": "Compatible with Rabbit, Horse, Pig. Incompatible with Ox, Rat.",
    "Monkey": "Compatible with Rat, Dragon, Snake. Incompatible with Tiger, Pig.",
    "Rooster": "Compatible with Ox, Snake, Dragon. Incompatible with Rabbit, Dog.",
    "Dog": "Compatible with Tiger, Rabbit, Horse. Incompatible with Dragon, Sheep.",
    "Pig": "Compatible with Rabbit, Sheep, Tiger. Incompatible with Snake, Monkey."
}

# Function to calculate the zodiac animal based on birth date
def get_zodiac(birth_date):
    birth_year = birth_date.year

    if birth_year not in lunar_new_year_dates:
        return "Unknown", "Unknown"

    lunar_new_year_date = lunar_new_year_dates[birth_year]
    lunar_new_year_date = lunar_new_year_date.date()  # Convert datetime to date for comparison

    if birth_date < lunar_new_year_date:
        birth_year -= 1
    
    zodiac = zodiac_data.get(birth_year, "Unknown")
    chinese_name = chinese_names.get(birth_year, "Unknown")
    return zodiac, chinese_name

# Function to get zodiac details
def get_zodiac_info(zodiac):
    traits = zodiac_traits.get(zodiac, "No traits available.")
    compatibility = zodiac_compatibility.get(zodiac, "No compatibility information available.")
    return traits, compatibility

# Streamlit app
st.title("Chinese Zodiac Web App")
#birth_date_input = st.date_input("Enter your birth date:")
# Date picker with full range from 1900 to 2030
birth_date_input = st.date_input(
    "Select your birth date:",
    value=pd.Timestamp("2000-01-01"),
    min_value=pd.Timestamp("1900-01-01"),
    max_value=pd.Timestamp("2030-12-31")
)

if birth_date_input:
    zodiac, chinese_name = get_zodiac(birth_date_input)

    if zodiac == "Unknown":
        st.error("Sorry, I don't have information for that year.")
    else:
        st.subheader(f"Your Chinese Zodiac Animal is: {zodiac} ({chinese_name})")
        traits, compatibility = get_zodiac_info(zodiac)
        st.markdown(f"**Personality Traits:** {traits}")
        st.markdown(f"**Compatibility:** {compatibility}")