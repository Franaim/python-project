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
    print("\nPlease enter the number of words you'd like your artwork title to have.")
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
        message = f"\nArtwork title: '{artwork_title}' (1 word)\n"
        return(message)
    else:
        message =  f"\nArtwork title: '{artwork_title}' ({num_words} words)\n"
        return(message)


def update_artwork_worksheet(data):
    """
    Updates artwork worksheet, adds new row with the data generated.
    """
    print("Updating artwork titles database...\n")
    
    artwork_worksheet = SHEET.worksheet("artwork")
    artwork_worksheet.append_row(data)

    print("Artwork title saved successfully.\n")

def consult_artwork_database():
    """
    Gets and prints the list of artwork titles from the worksheet.
    If there's no data found, it prints a message accordingly. If there is, it prints the title with its index.
    """
    print("Consulting the database for artwork titles...\n")
    
    artwork_worksheet = SHEET.worksheet("artwork")
    data = artwork_worksheet.get_all_values()

    if not data:
        print("No artwork titles found in the database.")
    else:
        print("Artwork titles in the database:\n")
        for i, row in enumerate(data[1:], start=1):
            print(f"{i}. {row[0]}")
        print()

    while True:
        choice = input("1. Go back to database options\n2. Go to Main Menu\n\nEnter your choice (1/2):\n")
        if choice == '1':
            return
        elif choice == '2':
            return main_menu()
        else:
            print("Invalid choice. Please enter '1' or '2'.")

def search_word_in_database(data):
    """
    Searches for a word in the artwork titles database and provides information about its frequency.
    """
    while True:
        word_to_search = input("Enter a word to search in the database:\n").lower()
        word_count = sum(1 for row in data if word_to_search in row[0].lower())

        if word_count > 0:
            print(f"\nThe word '{word_to_search}' appears {word_count} times in the database.\n")
        else:
            print(f"\nThe word '{word_to_search}' is not in the database.\n")

        another_search = input("Would you like to search for another word? (y/n):\n").lower()

        if another_search != 'y':
            break

def main_menu():
    """
    Menu to introduce the program and its functions to the user
    """
    print("\nWelcome to the Artwork Title Generator\n")
    print("With it, you can:")
    
    while True:
        choice = input("1. Consult our artwork titles database\n2. Generate artwork titles and add them to our database\n\nEnter your choice (1/2):\n")
        if choice == '1':
            database_menu()
        elif choice == '2':
            generate()
        else:
            print("Invalid choice. Please enter '1' or '2'.")

def database_menu():
    """
    Menu for functions related to consulting the database
    """
    print("\nArtwork Database Menu\n")

    while True:
        choice = input("1. See list of artwork titles in database\n2. Search for a word in the database\n3. Go back to Main Menu\n\nEnter your choice (1/2/3):\n")
        if choice == '1':
            consult_artwork_database()
        elif choice == '2':
            search_word_in_database(data)
        elif choice == '3':
            return main_menu()
        else:
            print("Invalid choice. Please enter '1' or '2'.")



# Calls the generate_title function
def generate():
    """
    Run functions related to artwork title generation
    """
    while True:
        num_words = get_integer_input()
        artwork_title = generate_string(num_words)
        generate_title_result = generate_title(artwork_title)


        # Prints the result for the user
        print(generate_title_result)
        print()

        # Turns the data into a list so it can be added to the worksheet
        artwork_data = [artwork_title]

        ask_to_save = input("Do you want to save this artwork title? (y/n):\n").lower()
        if ask_to_save == 'y':
            update_artwork_worksheet(artwork_data)
        elif ask_to_save == 'n':
            print("Title not saved")

        ask_to_generate_again = input("1. Generate another title\n2. Go to Main Menu\n\nEnter your choice (1/2):\n")
        if ask_to_generate_again == '1':
            continue
        elif ask_to_generate_again == '2':
            break
        else:
            print("Invalid choice. Please enter '1' or '2'.")


def main():
    """
    Run the program's main function
    """
    main_menu()


main()






