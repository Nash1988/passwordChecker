Password Checker using Have I Been Pwned API
This script checks the security status of passwords by querying the "Have I Been Pwned" API, which checks if a password has been exposed in known data breaches.

Prerequisites
Python 3.x
requests library
Installation
Clone or download the repository.
Install the required Python libraries using pip:
bash
Copy code
pip install -r requirements.txt
Usage
Run the script from the command line and pass the passwords you want to check:

bash
Copy code
python password_checker.py password1 password2 password3
Replace password1, password2, etc., with the passwords you want to check.

The script will output whether each password has been found in any data breaches or not. If found, it's advisable to change the password immediately for enhanced security.

How it works
The script hashes the password using SHA-1 and sends the first five characters of the hash to the Have I Been Pwned API.
The API returns a list of password hashes that match the same prefix.
The script then checks if the remaining hash characters match any of the received hashes, indicating a breached password.
The count of occurrences indicates how many times the password has been found in breaches.
Warning
Do not use real passwords when testing this script.
This script does not send the actual password to the API. It only sends the hashed prefix of the password.
Always handle passwords securely and avoid exposing them unnecessarily.
Credits
This script utilizes the Have I Been Pwned API (https://haveibeenpwned.com/API/v3) for checking compromised passwords.

