
# Password Manager

This is a simple and beginner-friendly Python-based password manager script that allows users to securely store and retrieve their passwords using encryption. 

## Features
- **Encryption with a Master Password**: All passwords are securely encrypted using the `cryptography.fernet` library.
- **Add and View Passwords**: Users can add new account credentials or view existing ones.
- **Master Password Protection**: The encryption key is derived from a combination of a stored key and a user-provided master password.

## Requirements
- Python 3.6 or later
- `cryptography` library

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/derinnnn/password_manager.git
   cd password_manager
   ```

2. Install the required library:
   ```bash
   pip install cryptography
   ```

3. Generate the encryption key:
   Run the script once to generate a key file:
   ```bash
   python3 password_manager.py
   ```
   You will be prompted to create a master password during the first run. This password is required for all subsequent operations.

## How to Use
### Adding a New Password
1. Select the `add` mode.
2. Enter the account name.
3. Enter the password you want to store.
4. The password will be securely encrypted and saved to a `passwords.txt` file.

### Viewing Saved Passwords
1. Select the `view` mode.
2. The script will decrypt and display saved passwords in the format:
   ```
   User: <account-name> | Password: <password>
   ```

### Quitting the Program
- Enter `q` to quit the program.

## File Structure
- **`password_manager.py`**: The main script.
- **`key.key`**: The encryption key file generated during the first run.
- **`passwords.txt`**: The file where encrypted passwords are stored.

## Security Notes
- **Master Password**: Choose a strong master password to secure your data.
- **Key File**: The `key.key` file is critical for decryption. If lost, the saved passwords cannot be recovered.
- **Local Storage**: Passwords are stored locally in encrypted form. Ensure the script and files are stored securely.

## Example Output
```
Would you like to add a new password or view existing ones (view, add), press q to quit: view
What is the master password? ********
User: example_account | Password: securepassword123
```

