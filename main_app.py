import datetime
import streamlit as st

# Lunar New Year dates and Zodiac animals for each year
lunar_new_year_dates = {
    1900: "February 16", 1901: "February 5", 1902: "January 26", 1903: "February 14", 1904: "February 4", 
    1905: "January 25", 1906: "February 13", 1907: "February 2", 1908: "January 23", 1909: "February 10",
    1910: "January 31", 1911: "February 18", 1912: "February 7", 1913: "January 27", 1914: "February 14",
    1915: "February 3", 1916: "January 23", 1917: "February 11", 1918: "January 31", 1919: "February 19",
    2020: "January 25", 2021: "February 12", 2022: "February 1", 2023: "January 22", 2024: "February 10",
    2025: "January 29", 2026: "February 17", 2027: "February 6"
}

zodiac_data = {
    1900: 'Rat', 1901: 'Ox', 1902: 'Tiger', 1903: 'Rabbit', 1904: 'Dragon', 1905: 'Snake',
    1906: 'Horse', 1907: 'Goat', 1908: 'Monkey', 1909: 'Rooster', 1910: 'Dog', 1911: 'Pig',
    2020: 'Rat', 2021: 'Ox', 2022: 'Tiger', 2023: 'Rabbit', 2024: 'Dragon', 2025: 'Snake',
    2026: 'Horse', 2027: 'Goat'
}

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

# Function to calculate the zodiac animal based on full birth date
def get_zodiac(birth_date):
    birth_year = birth_date.year
    lunar_new_year_str = lunar_new_year_dates.get(birth_year)
    if lunar_new_year_str:
        lunar_new_year_date = datetime.datetime.strptime(f"{birth_year} {lunar_new_year_str}", "%Y %B %d").date()
        if birth_date < lunar_new_year_date:
            birth_year -= 1
    zodiac = zodiac_data.get(birth_year, "Unknown")
    return zodiac

# Function to get zodiac details
def get_zodiac_info(zodiac):
    traits = zodiac_traits.get(zodiac, "No traits available.")
    compatibility = zodiac_compatibility.get(zodiac, "No compatibility information available.")
    return traits, compatibility

# Streamlit app
st.title("Chinese Zodiac Animal Finder")

birth_date_input = st.date_input("Enter your birth date:")
if birth_date_input:
    zodiac = get_zodiac(birth_date_input)
    traits, compatibility = get_zodiac_info(zodiac)
    st.subheader(f"Your Chinese Zodiac Animal is: {zodiac}")
    st.markdown(f"**Personality Traits:** {traits}")
    st.markdown(f"**Compatibility:** {compatibility}")