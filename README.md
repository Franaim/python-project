# ARTWORK TITLE GENERATOR
---

The "Artwork Title Generator" is a Python terminal program designed to enhance the creative process for contemporary artists and creators by leveraging the power of programming.
It enables users to generate, manage, and consult titles for contemporary works of art. It uses Google Sheets as a data storage solution and integrates external functionality for title generation.

[Here is the live version of my project](https://artwork-title-generator-b1c0129c3591.herokuapp.com/)

![Artwork Title Generator Responsiveness](https://iili.io/JJkCoEx.jpg)

## How to use it

At the start of the program the user is given a brief description of what the program can do and must choose (by entering 1 or 2) whether they want to:

1. Perform query tasks on a database.
2. Generate data which can then be included in the database.

### Query tasks on database

In case of entering 1, the user will again have to choose between some options:

1. View the list of data generated with the program and saved in the database.
This option will use an API connected to the Pyhton program to get and print on the terminal an indexed list of all the artwork titles that other users have generated and saved in the external worksheet.

2. Query the frequency of a particular word within this database.
This option will allow the user to type in a particular word and receive a corresponding response, either if that word is not found in the database or, if it is, how many times in total.

3. Back to previous menu.
This option will take the user to the previous menu, enabling other options.

### Generating data and storing it

If, from the main menu, the user selected option 2, then they will enter the section for generating titles for works of art.
There the user will be asked for a number of words to form the title and, if the answer is a number between 1 and 3, then the programme will generate a title, always including a noun and one or two adjectives.

Once the title has been generated, the user can choose whether to save it in the database or not, and can choose whether to continue generating new titles or return to the main menu.

## Features

1. Title Generation:

- Users can generate artwork titles of varying lengths (between 1 and 3 words) using a custom algorithm that combines nouns and adjectives from predefined lists.
- Generated titles are displayed to the user along with the word count.

![Artwork Title Generating](https://iili.io/JJUAZQ4.jpg)

2. Database Management:

- Users can save generated artwork titles to the Google Sheets-based database.
- The program appends new titles as rows in the "artwork" worksheet.

![Artwork Title Saving](https://iili.io/JJUAQjf.jpg)

3. Consult Artwork Database:

- Users can access and view the list of artwork titles stored in the database.
- Titles are presented with an index number for reference.

![Artwork Title Database](https://iili.io/JJUADCl.jpg)

4. Search in Database:

- Users can search for specific words in the artwork titles database.
- The program counts and displays the frequency of the searched word's occurrence.

![Artwork Title Search](https://iili.io/JJUALTG.jpg)

5. Data Validation:

- The program validates user inputs to ensure that they are within the specified range and format. For example, it checks that the user's choice is either '1' or '2' and that the word count for title generation is between 1 and 3.

![Invalid Input](https://iili.io/JJUAbG2.jpg)

6. Menu System:

- The program utilizes a menu-driven system to guide users through different functionalities.
- It offers a main menu and a database menu for easy navigation.

![Menu System](https://iili.io/JJUAm4S.jpg)

7. Error Handling:

- The program incorporates error handling to address potential exceptions that may occur during operations, such as database updates.

![Error Handling](https://iili.io/JJUR9a9.jpg)

8. Integration with External Libraries:

- The program integrates external libraries, including gspread for Google Sheets interaction and the generate_string function from an external file for title generation.

9. User-Friendly Interface and Interaction via Terminal

- The program provides clear and informative messages to guide users through various operations.
- It continuously prompts for user input until valid choices are made.

10. Persistence:

- The program ensures data persistence by saving generated titles to the Google Sheets database, allowing users to access their titles even after closing the program.

### Future Features

1. Unique Title Generation:

- The program could implement a "no-repeat" system to ensure that generated artwork titles are unique and do not repeat. This would enhance the program's utility and creativity, providing users with a constantly expanding pool of distinct titles for their works of art.

2. Extended Title Generation: 

- Explore the possibility of expanding the program's capabilities to generate longer and more intricate artwork titles. This could involve incorporating additional words, phrases, or thematic elements to create titles that are not only unique but also richer in artistic context.

## Data Model

The most critical aspect of the data model in the "Artwork Title Generator" project is its utilization of Google Sheets as the central repository for storing and managing generated artwork titles. This choice of data storage not only offers structured organization but also ensures data persistence. Titles are stored as rows within a dedicated worksheet, making it easy for users to access, search, and maintain their collection of titles over time.

## Testing

I have manually tested this project in the following ways:

- Utilizing PEP8 Linter: I ran the PEP8 linter on the codebase to ensure adherence to Python's style guidelines. No major issues were found.

- Testing Invalid Inputs: I conducted extensive testing by intentionally providing invalid inputs in various scenarios and evaluated the program's responses to ensure robust error handling and user-friendly feedback.

- Local Terminal Testing: I executed the program multiple times in the local development environment to verify its functionality and user experience. This helped identify and address any potential issues during development.

- Heroku Terminal Testing: I ensured the program's compatibility and functionality by testing it in the Code Institute Heroku terminal. This step ensured that the application performs as expected in a real-world, cloud-hosted environment.

### Bugs

#### Solved Bugs

- I encountered a bug where the string (the title artwork) was not being properly formatted as a list before attempting to save it to the connected worksheet. I fixed this issue by ensuring that the data to be saved is formatted correctly as a list before updating the worksheet.

- I identified a bug where the database was successfully updated with new data in the connected worksheet, but the program was not reflecting these updates when consulting the list of data. I solved this issue by updating the data variable with the latest values from the artwork_worksheet using 'data = artwork_worksheet.get_all_values()'.

#### Remaining Bugs

- No bugs remaining

## Deployment

The project was deployed using Code Institute's mock terminal for Heroku.

Steps for deployment:

- Clone the repository from GitHub
- Create a new Heroku app
- Set the buildpacks to Python and NodeJS
- Link the Heroku app to the repository
- Click on Deploy

## Credits

- Code Institute for the deployment terminal and for the API wiring up code
- ChatGPT for the nouns and adjectives used to build the artwork titles




