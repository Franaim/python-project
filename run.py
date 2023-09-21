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

# Function to get user input as an integer
def get_integer_input():
    """
    Validate the number entered in the generate_title function
    """
    while True:
        user_input = input("Enter a number here: ")
        if user_input.strip() and user_input.isdigit():
            user_input = int(user_input) # Convert the input to an integer
            if user_input <= 3:
                return user_input
            else:
                print("It must be a number between 1 and 3.")
        else:
            print("Please enter a valid number")

# Define the generate_title function
def generate_title():
    """
    Get number of words for the artwork's title
    """
    print("Welcome to the artwork title generator\n")
    print("Please enter the number of words you'd like your artwork title to have.")
    print("It should be a number between 1 and 3.\n")

    # Get the number of words from the user
    num_words = get_integer_input()
    if num_words == 1:
        print(f"Your artwork title will have {num_words} word.\n")
    else:
        print(f"Your artwork title will have {num_words} words.\n")

# Call the generate_title function
generate_title()
