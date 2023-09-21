import gspread
import random
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

# Lists of nouns and adjectives to generate the artwork title
nouns = ["aurora", "object", "panorama", "elixir", "chair", "mirror", "facade", "phenomenon", "resonance", "memento", "artifact"]
adjectives1 = ["enigmatic", "expressive", "dynamic", "political", "honest", "provocative", "real", "cruel", "truthful", "world's"]
adjectives2 = ["ivory", "cerulean", "golden", "indigo", "unique", "Japanese", "Maltese", "Eastern", "Western", "southern", "blood-red", "dystopian"]


# Function to get user input as an integer
def get_integer_input():
    """
    Gets the number entered by the user.
    The while loop keeps requesting a number until a valid input is entered.
    Strip and isdigit methods check that the input exists and it's a number. Then if this is correct, it turns it
    into an integer. Once that's done, it makes sure that the integer is not bigger than 3. If it is, it prints a 
    message asking for a smaller number. If it's not, it returns the input and breaks the loop. If, at the beginning 
    of the loop, the input entered isn't a number or is empty a message is printed into the console requesting a 
    valid number.
    """
    while True:
        user_input = input("Enter a number here: ")
        if user_input.strip() and user_input.isdigit():
            user_input = int(user_input)
            if 1 <= user_input <= 3:
                return user_input
            else:
                print("It must be a number between 1 and 3.")
        else:
            print("Please enter a valid number")

def generate_string(num_words):
    """
    Based on the number entered by the user, it generates random strings from the lists of nouns and adjetives
    """
    if num_words == 1:
        noun = random.choice(nouns)
        noun = noun.capitalize()
        artwork_title = f"{noun}"
        return artwork_title
    elif num_words == 2:
        adj1 = random.choice(adjectives1)
        adj1 = adj1.capitalize()
        noun = random.choice(nouns)
        artwork_title = f"{adj1} {noun}"
        return artwork_title
    elif num_words == 3:
        adj1 = random.choice(adjectives1)
        adj1 = adj1.capitalize()
        adj2 = random.choice(adjectives2)
        noun = random.choice(nouns)
        artwork_title = f"{adj1} {adj2} {noun}"
        return artwork_title
    
print("Welcome to the artwork title generator\n")
print("Please enter the number of words you'd like your artwork title to have.")
print("It should be a number between 1 and 3.\n")

def generate_title():
    """
    Once the user has entered a number and, based on it, a string has been made randomly, it prints a message
    including the artwork title that has been generated. In this case, it checks if the number entered is 1
    or if it's 2 or 3 so that the word 'word' isn't plural when referring to 1. 
    """
    num_words = get_integer_input()
    artwork_title = generate_string(num_words)

    if num_words == 1:
        message = f"\nYour artwork has {num_words} word: '{artwork_title}'\n"
        return(message)
    else:
        message =  f"\nYour artwork has {num_words} words: '{generate_string(num_words)}'\n"
        return(message)

# Calls the generate_title function
generate_title_result = generate_title()

# Prints the result for the user
print(generate_title_result)

