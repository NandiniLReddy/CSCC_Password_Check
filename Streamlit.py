import streamlit as st
from PIL import Image
import re


def password_strength_category(password, disallowed_names):

    length_regex = r'^.{8,}$'
    uppercase_regex = r'[A-Z]'
    lowercase_regex = r'[a-z]'
    digit_regex = r'[0-9]'
    special_char_regex = r'[!@#$%^&*()]'

    has_length = re.search(length_regex, password)
    has_uppercase = re.search(uppercase_regex, password)
    has_lowercase = re.search(lowercase_regex, password)
    has_digit = re.search(digit_regex, password)
    has_special_char = re.search(special_char_regex, password)

    password_contains_names = any(
        str(name).lower() in password.lower() for name in disallowed_names
    )

    if password_contains_names:
        return "Weak", "A weak password should not contain any part of the provided names."

    if (
        has_length and
        has_uppercase and
        has_lowercase and
        has_digit and
        has_special_char
    ):
        return "Very Strong", "A very strong password contains a mix of uppercase and lowercase letters, digits, and special characters."

    if (
        has_length and
        has_uppercase and
        has_lowercase and
        has_digit
    ):
        return "Strong", "A strong password contains a mix of uppercase and lowercase letters and digits."

    if (
        has_length and
        has_lowercase and
        has_digit
    ):
        return "Intermediate", "An intermediate password contains lowercase letters and digits."

    return "Weak", "A weak password is shorter and may not contain a mix of characters."


def main():

    st.markdown(
        f"""
        <style>
        .reportview-container {{
            background: url('/Users/nandinilreddy/Desktop/CSCC_Club/cscc.jpeg');
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("Password Strength Checker")

    st.title("Password Strength Checker")

    username = st.text_input("Enter your username:")
    address = st.text_input("Enter your address:")
    country = st.text_input("Enter your country:")
    date_of_birth = st.date_input("Enter your date of birth:")
    father_name = st.text_input("Enter your father's name:")
    mother_name = st.text_input("Enter your mother's name:")

    password = st.text_input("Enter your password:", type="password")


    disallowed_names = [username, address, country,
                        date_of_birth, father_name, mother_name]

    if st.button("Check Password Strength"):
        category, description = password_strength_category(
            password, disallowed_names)
        st.write(f"Password Strength: **{category}**")
        st.write(f"Description: {description}")


if __name__ == "__main__":
    main()

