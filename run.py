import gspread
from google.oauth2.service_account import Credentials
import random

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


# Lists of nouns and adjectives to generate the artwork title
nouns = ["aurora", "object", "panorama", "elixir", "chair", "mirror", "facade", "phenomenon", "resonance", "memento", "artifact"]
adjectives1 = ["enigmatic", "expressive", "dynamic", "political", "honest", "provocative", "real", "cruel", "truthful", "world's"]
adjectives2 = ["ivory", "cerulean", "golden", "indigo", "unique", "Japanese", "Maltese", "Eastern", "Western", "southern", "blood-red", "dystopian"]


# Function to get user input as an integer
def get_integer_input():
    """
    Gets the number entered by the user.
    The while loop keeps requesting a number until a valid input is entered.
    It checks if the input is a valid number between 1 and 3 and prints an error if it's not.
    """
    print("Please enter the number of words you'd like your artwork title to have.")
    print("It should be a number between 1 and 3.\n")
    while True:
        user_input = input("Enter a number here:\n")
        try:
            user_input = int(user_input)
            if 1 <= user_input <= 3:
                return user_input
            else:
                print("It must be a number between 1 and 3.")
        except ValueError:
            print("Please enter a valid number")

def generate_string(num_words):
    """
    Based on the number entered by the user, it generates random strings from the lists of nouns and adjetives. 
    """
    title_words = []
    adjectives_lists = [adjectives1, adjectives2]
    number_of_adjectives = num_words - 1
    for n in range(number_of_adjectives):
        title_words.append(random.choice(adjectives_lists.pop()))
    title_words.append(random.choice(nouns))
    return ' '.join(title_words).capitalize()



def generate_title(artwork_title):
    """
    Once the user has entered a number and, based on it, a string has been made randomly, it prints a message
    including the artwork title that has been generated. In this case, it checks if the number entered is 1
    or if it's 2 or 3 so that the word 'word' isn't plural when referring to 1. 
    """
    num_words = len(artwork_title.split(" "))
    if num_words == 1:
        message = f"\nYour artwork has {num_words} word: '{artwork_title}'\n"
        return(message)
    else:
        message =  f"\nYour artwork has {num_words} words: '{artwork_title}'\n"
        return(message)

def ask_to_save_artwork(artwork_data):
    """
    Asks the user if they want to save the artwork title and updates the worksheet if they choose to do so.
    """
    while True:
        save_artwork = input("Do you want to save this artwork title? (y/n):\n").lower()
        if save_artwork == 'y':
            update_artwork_worksheet(artwork_data)
            break
        elif save_artwork == 'n':
            print("Artwork title not saved.")
            print("Exiting program now")
            break
        else:
            print("Invalid input. Please enter 'y' to save or 'n' to not save the artwork title.")


def update_artwork_worksheet(data):
    """
    Updates artwork worksheet, adds new row with the data generated.
    """
    print("Updating artwork worksheet...\n")
    
    artwork_worksheet = SHEET.worksheet("artwork")
    artwork_worksheet.append_row(data)

    print("Artwork title saved successfully.\n")

def consult_artwork_titles():
    """
    Gets and prints the list of artwork titles from the worksheet.
    If there's no data found, it prints a message accordingly. If there is, it prints the title with its index.
    """
    print("Consulting the database for artwork titles...\n")
    
    artwork_worksheet = SHEET.worksheet("artwork")
    database = artwork_worksheet.get_all_values()

    if not database:
        print("No artwork titles found in the database.")
    else:
        print("Artwork titles in the database:\n")
        for i, row in enumerate(data[1:], start=1):
            print(f"{i}. {row[0]}")
        print()


# Calls the generate_title function
def main():
    """
    Run main program functions.
    """
    num_words = get_integer_input()
    artwork_title = generate_string(num_words)
    generate_title_result = generate_title(artwork_title)


    # Prints the result for the user
    print(generate_title_result)
    print()
    print(artwork_title)

    # Turns the data into a list so it can be added to the worksheet
    artwork_data = [artwork_title]


    ask_to_save_artwork(artwork_data)


print("Welcome to the artwork title generator\n")
consult_artwork_titles()
main()





