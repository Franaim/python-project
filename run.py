import gspread
from google.oauth2.service_account import Credentials
import random
from title_generator import generate_string # Imported function from external file


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

def get_integer_input():
    """
    Gets the number entered by the user.
    The while loop keeps requesting a number until a valid input is entered and prints an error if it's not.
    It checks if the input is a valid number between 1 and 3 and prints a message if it's not.
    """
    print("----------------------------------------------")
    print("\nPlease enter the number of words you'd like your artwork title to have.")
    print("It should be a number between 1 and 3.\n")
    while True:
        user_input = input("Enter a number here:\n")
        try:
            user_input = int(user_input)
            if 1 <= user_input <= 3:
                print("Generating title...")
                return user_input
            else:
                print("\nIt must be a number between 1 and 3.")
        except ValueError: # If the user enters something that can't be converted to an integer it catches the error
            print("\nPlease enter a valid number")



def generate_title(artwork_title):
    """
    Prints a message including the artwork title that has been generated.
    It checks if the number entered was 1 or more so that a clear message about the amount of words is included.
    """
    num_words = len(artwork_title.split(" ")) # First it splits the title separated by spaces into a list of words and then counts the amount of words in it
    if num_words == 1:
        message = f"\nArtwork title: '{artwork_title}' (1 word)\n"
        return(message)
    else:
        message =  f"\nArtwork title: '{artwork_title}' ({num_words} words)\n" # If the title has more than one word, it includes the count of words in the formated string
        return(message)


def update_artwork_worksheet(data):
    """
    Updates artwork worksheet, adds new row with the data generated. Once done, it prints a message accordingly.
    """
    print("Updating artwork titles database...\n")
    
    artwork_worksheet = SHEET.worksheet("artwork")

    try:
        artwork_worksheet.append_row(data)
        print("Artwork title saved successfully.\n")
        print("----------------------------------------------")
    except Exception as e: # This catches any exception that inherits from the base Exception class
        print(f"An error occurred while saving the artwork title: {e}\n")
        print("----------------------------------------------")


def consult_artwork_database():
    """
    Gets and prints the list of artwork titles from the worksheet.
    If there's no data found, it prints a message accordingly. If there is, it prints the title with its index.
    """
    print("Consulting the database for artwork titles...\n")
    
    artwork_worksheet = SHEET.worksheet("artwork") # This accesses the worksheet and stores it in a variable
    data = artwork_worksheet.get_all_values() # This gets the values in the worksheet and stores them in another variable

    if not data: # In case the database is empty, a message is printed for the user
        print("No artwork titles found in the database.")
    else:
        print("----------------------------------------------")
        print("Artwork titles in database:\n")
        for i, row in enumerate(data[1:], start=1): # The loop iterates over the rows of data, starting from the second row because the first one is a header row. Then it assigns an index to each row starting from 1.
            print(f"{i}. {row[0]}") # A formated string idicating the index number and the title in the database
        print() # Spacing
        print("----------------------------------------------")

    while True: # After the list has been printed, a new set of options appear for the user
        choice = input("\n1. Go back to database options\n2. Go to Main Menu\n\nEnter your choice (1/2):\n")
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
    print("----------------------------------------------")
    while True:
        word_to_search = input("\nEnter a word to search in the database:\n").lower()
        word_count = sum(1 for row in data if word_to_search in row[0].lower()) # This counts the number of rows where the entered word is found. It applies only to the first column

        if word_count > 0:
            print("----------------------------------------------")
            print(f"\nThe word '{word_to_search}' appears {word_count} times in the database.\n")
            print("----------------------------------------------")

        else:
            print("----------------------------------------------")
            print(f"\nThe word '{word_to_search}' is not in the database.\n")
            print("----------------------------------------------")

        another_search = input("\nWould you like to search for another word? (y/n):\n").lower()

        if another_search != 'y':
            break

def main_menu():
    """
    Menu to introduce the program and its functions to the user
    """
    print("----------------------------------------------")
    print("\nWelcome to the Artwork Title Generator\n")
    print("----------------------------------------------")
    print("With it, you can:\n")
    
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
    print("----------------------------------------------")
    print("\nArtwork Database Menu\n")
    print("----------------------------------------------\n")

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


def generate():
    """
    Run functions related to artwork title generation
    """
    while True:
        num_words = get_integer_input()
        artwork_title = generate_string(num_words)
        generate_title_result = generate_title(artwork_title)


        # Prints the result for the user
        print("----------------------------------------------")
        print(generate_title_result)
        print("----------------------------------------------")
        print()

        # Turns the data into a list so it can be added to the worksheet
        artwork_data = [artwork_title]

        while True:
            ask_to_save = input("Do you want to save this artwork title? (y/n):\n").lower()
            if ask_to_save == 'y':
                update_artwork_worksheet(artwork_data)
                break # Exits after saving
            elif ask_to_save == 'n':
                print("Title not saved")
                break # Exits without saving
            else:
                print("Invalid choice. Please enter 'y' or 'n'.")
        

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






