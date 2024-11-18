from cryptography.fernet import Fernet
import base64
import hashlib

# Function to generate and save a key
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Function to load the saved key
def load_key():
    try:
        with open("key.key", "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        print("Error: Key file not found. Please generate the key using the write_key() function.")
        exit()

# Function to generate an encryption key using the master password
def derive_key(base_key, master_password):
    combined_key = base_key + master_password.encode()
    hashed_key = hashlib.sha256(combined_key).digest()  # Hash the combined key
    return base64.urlsafe_b64encode(hashed_key)  # Encode to a Fernet-compatible format

# Ask the user for the master password
master_pwd = input("What is the master password? ")

# Load the key from the key file
base_key = load_key()

# Derive the encryption key
encryption_key = derive_key(base_key, master_pwd)

# Create the Fernet object for encryption and decryption
fer = Fernet(encryption_key)

# Function to view saved accounts
def view():
    try:
        with open('passwords.txt', 'r') as f:
            for line in f.readlines():  # Ensure () after readlines
                # Check if the line is valid
                if ":" not in line:
                    print("Invalid entry in passwords file:", line.strip())
                    continue
                user, enc_pwd = line.strip().split(":", 1)  # Split only at the first colon
                try:
                    dec_pwd = fer.decrypt(enc_pwd.encode()).decode()
                    print("User:", user, "| Password:", dec_pwd)
                except Exception as e:
                    print("Error decrypting password for user", user, ":", e)
    except FileNotFoundError:
        print("Error: Passwords file not found.")
    except Exception as e:
        print("Error while viewing passwords:", e)

# Function to add a new account
def add():
    name = input("Account name: ")
    pwd = input("Password: ")
    try:
        with open('passwords.txt', 'a') as f:
            enc_pwd = fer.encrypt(pwd.encode()).decode()
            f.write(name + ":" + enc_pwd + "\n")
    except Exception as e:
        print("Error while adding the password:", e)

# Main loop
while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit: ")
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
