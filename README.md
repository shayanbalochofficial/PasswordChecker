# Password Checker

This `Password Checker` is a web-based tool built with Python and Streamlit, designed to evaluate the strength of your passwords in real-time. Simply type a password, and it checks for length, uppercase and lowercase letters, numbers, and special characters, giving you a strength rating and personalized tips to make it stronger. Perfect for boosting your online security with ease!

## Features

- **Strength Evaluation**: Rates your password as "Weak," "Okay," or "Strong" based on five criteria:
  - At least 8 characters long.
  - Contains an uppercase letter (e.g., A, B).
  - Contains a lowercase letter (e.g., a, b).
  - Includes a number (e.g., 1, 2).
  - Has a special character (e.g., !, @, #, $, %).
- **Scoring System**: Assigns a score out of 5, reflecting how many criteria your password meets.
- **Personalized Tips**: Provides actionable suggestions to improve your password if it’s not strong enough.
- **Interactive Web App**: Powered by Streamlit, offers a clean, browser-based interface with a secure password input field.
- **Instant Feedback**: Displays strength, score, and tips as soon as you enter a password.

## How to Use

1. **Prerequisites**:

   - Ensure you have Python installed (version 3.7 or higher recommended).
   - Install Streamlit using `pip` or `uv` (a faster package manager):

     ```bash
     pip install streamlit
     # OR with uv
     uv pip install streamlit
     ```

2. **Clone the Repository**:

   ```bash
   git clone https://github.com/shayanbalochofficial/PasswordChecker.git
   cd PasswordChecker
   ```

3. **Run the App**:

   - Execute the following command in your terminal:

     ```bash
     streamlit run password_checker.py
     ```
   - Your default web browser will open to `http://localhost:8501`, where you can start checking passwords.

4. **Usage**:

   - Enter a password in the secure text input field (hidden for privacy).
   - Instantly see the password’s strength ("Weak," "Okay," or "Strong"), score (out of 5), and tips to improve it.
   - Use the tips to tweak your password and recheck until you get a "Strong" rating!

## Requirements

- Python 3.7+
- Streamlit (`pip install streamlit` or `uv pip install streamlit`)

## File Structure

- `password_checker.py`: The main script containing the password checking logic and Streamlit UI.

## Contributors

- **Shayan Baloch** - Creator and developer of this Password Checker.

## License

This project is open-source and available under the MIT License.

## Acknowledgments

- Built as part of my Python learning journey—helping me explore practical ways to enhance digital security!
- Thanks to the Streamlit community for an amazing framework that makes web apps so approachable.

---

Stay secure and happy coding! 🚀
