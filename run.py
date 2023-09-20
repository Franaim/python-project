import gspread
from google.oauth2.service_account import Credentials

# Written in capitals for it is a constant variable
SCOPE = [ 
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('python_project_database')

artwork = SHEET.worksheet('artwork')

data = artwork.get_all_values()
test_String = "This is a test message. The program is now being executed."
print(test_String)
print(data)
print()

# Define the generate_title function
def generate_title():
    """
    Get number of words for the artwork's title
    """
    print("Welcome to the artwork title generator\n")
    print("Please enter the number of words you'd like your artwork title to have.")
    print("It should be a number between 1 and 3.\n")

    # Get user input as a string
    user_input = input("Enter a number here: ")
    print(f"Your artwork title will have {user_input} words.\n")

    # Check if the input is valid and turn it into an integer
    if user_input.strip() and user_input.isdigit():
        num_words = int(user_input)
        print(num_words)
    else:
        print("Please enter a valid number")

generate_title()
