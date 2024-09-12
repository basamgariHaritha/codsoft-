import random
import string

def generate_password(length):
    if length < 4:
        raise ValueError("Password length should be at least 4")
    
    # Define the characters to be used in the password
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure the password has at least one lowercase, one uppercase, one digit, and one special character
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    # Fill the rest of the password length with random choices from all characters
    password += random.choices(all_characters, k=length - 4)
     # Shuffle the list to avoid predictable patterns
    random.shuffle(password)

    # Convert the list to a string
    return ''.join(password)

# Generate a password of a specified length
password_length = 12  # You can change the length as needed
password = generate_password(password_length)
print("Generated Password:",password)

