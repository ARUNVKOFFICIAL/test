import streamlit as st
import bcrypt  # For password hashing

# In-memory storage for simplicity (replace with a database in a real application)
users = {'logan': bcrypt.hashpw('password999'.encode('utf-8'), bcrypt.gensalt())}

def verify_password(stored_password, input_password):
    return bcrypt.checkpw(input_password.encode('utf-8'), stored_password)

def login(username, password):
    if username in users and verify_password(users[username], password):
        return True
    else:
        return False

def welcome_page(username):
    st.title(f"Welcome, {username}!")
    st.write("congratulations logan - website hacked successfully")

def main():
    st.title("HACK MY SITE - BY ARUN VK")

    # Add input fields for username and password
    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")

    # Check if the user clicked the "Login" button
    if st.button("Login"):
        if login(username, password):
            st.success(f"Welcome, {username}!")

            # Create a placeholder for the new page content
            placeholder = st.empty()

            # Display the welcome page content
            with placeholder:
                welcome_page(username)

        else:
            st.error("invalid login")

if __name__ == "__main__":
    main()
