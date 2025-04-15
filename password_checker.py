import streamlit as st

# Function to check password strength
def check_password(password):
    score = 0
    tips = []

    # Check if password is 8 or more characters
    if len(password) >= 8:
        score = score + 1
    else:
        tips.append("Make it 8 or more characters.")

    # Check for uppercase letter
    has_upper = False
    for char in password:
        if char >= 'A' and char <= 'Z':
            has_upper = True
    if has_upper:
        score = score + 1
    else:
        tips.append("Add an uppercase letter (like A or B).")

    # Check for lowercase letter
    has_lower = False
    for char in password:
        if char >= 'a' and char <= 'z':
            has_lower = True
    if has_lower:
        score = score + 1
    else:
        tips.append("Add a lowercase letter (like a or b).")

    # Check for a number
    has_number = False
    for char in password:
        if char >= '0' and char <= '9':
            has_number = True
    if has_number:
        score = score + 1
    else:
        tips.append("Add a number (like 1 or 2).")

    # Check for special character
    special_chars = "!@#$%"
    has_special = False
    for char in password:
        if char in special_chars:
            has_special = True
    if has_special:
        score = score + 1
    else:
        tips.append("Add a special character (like ! or @).")

    # Decide strength
    if score == 5:
        strength = "Strong"
        tips = ["Your password is great!"]
    elif score >= 3:
        strength = "Okay"
    else:
        strength = "Weak"

    return strength, score, tips

# Streamlit app
st.title("Password Checker")
st.write("Type a password to see if it’s strong!")

# Get password from user
password = st.text_input("Your password:", type="password")

# Show results if user types something
if password:
    strength, score, tips = check_password(password)
    st.write("Strength:", strength)
    st.write("Score:", score, "out of 5")
    st.write("Tips:")
    for tip in tips:
        st.write("-", tip)