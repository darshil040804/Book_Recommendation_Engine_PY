# Project Title: Book Recommendation Engine

## Project Overview:

The Book Recommendation Engine is a Python project designed to help users discover books based on various criteria, including title, category, year published, average rating, and number of pages. The project reads data from a CSV file containing information about different books and provides a user-friendly interface to search, filter, and recommend books.

## Project Functions:

The project consists of the following key functions:

### 1. `open_file()`

This function allows users to input a file name, attempts to open the specified CSV file, and returns the file pointer (fp) if successful. It handles errors and prompts users to retry if the file cannot be opened.

### 2. `read_file(fp)`

This function reads the CSV file using the provided file pointer (fp) and returns a list of tuples, where each tuple represents information about a book. It extracts attributes such as ISBN-13, title, authors, categories, description, published year, average rating, number of pages, and rating count from the file.

### 3. `get_books_by_criterion(list_of_tuples, criterion, value)`

This function filters the list of book tuples based on a specified criterion and its corresponding value. It can filter by title, category, year published, average rating, and number of pages. It returns a list of book tuples that match the given criterion and value.

### 4. `get_books_by_criteria(list_of_tuples, category, rating, page_number)`

This function filters books effectively through category, rating, and number of pages. It calls `get_books_by_criterion` for each specified criterion and value, progressively narrowing down the list of books that meet the user's criteria.

### 5. `get_books_by_keyword(list_of_tuples, keywords)`

This function filters books based on user-inputted keywords. It searches for books whose descriptions contain any of the provided keywords and returns a list of matching book tuples.

### 6. `sort_authors(list_of_tuples, a_z=True)`

This function arranges the list of books in either ascending (A-Z) or descending (Z-A) order based on the author's name. It uses the `itemgetter` function to sort the list of book tuples.

### 7. `recommend_books(list_of_tuples, keywords, category, rating, page_number, a_z)`

This function provides book recommendations based on user-defined criteria, including keywords, category, rating, page number, and sorting order. It calls the necessary filtering and sorting functions to generate the recommendations and returns a list of recommended book tuples.

### 8. `display_books(list_of_tuples)`

This function displays a list of book tuples along with their information. It formats the output using predefined column headers and ensures that book titles and authors are not longer than 35 characters.

### 9. `get_option()`

This function prompts the user to choose from a menu of options and returns the selected option. It handles invalid inputs and ensures that the chosen option is within the valid range.

### 10. `main()`

The main function serves as the entry point for the project. It orchestrates the entire user experience, from opening the CSV file to executing user-selected actions. Users can choose to find a book by title, filter books by criteria, recommend books, or quit the program.

## Project Usage:

The Book Recommendation Engine provides an interactive interface for users to explore and discover books that match their preferences. Users can search for specific titles, filter books by various criteria, receive personalized recommendations, and explore book details.

To use the program, follow these steps:

1. Run the Python script.
2. Enter the name of the CSV file containing book data when prompted.
3. Choose one of the following options from the menu:
   - Find a book by title
   - Filter books by criteria (category, year, rating, page number)
   - Recommend books based on keywords, category, rating, and page number
   - Quit the program

Depending on your selection, the program will guide you through the necessary inputs and display the relevant book information.

Enjoy exploring books and discovering new reads with the Book Recommendation Engine!
