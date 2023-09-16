##############################################################################
#
# Computer Project #6
# ALGORTIHM
#
# This project uses a total of 10 functions and then a main() function
# The functions are as follows:
# open_file() used for opening the csv file
# raed_file() used for outputting a list of tuples form the file such that each
# tuple contains only those attributes that are mentioned in the source pdf 
# get_books_by_criterion() used for filtering out those tuples that the specified
# criterion and value demand for.
# get_books_by_criteria() used for filtering books effectively through category,
# rating and number of pages
# get_books_by_keywords() used for filtering books whose description contains the 
# inputted keywords by the user
# sort_authors() used for arranging the list of books in ascending or descending
# order based on Author's name
# recommend_books() used for recommending books based on the inputted values of
# keywords, category, number of pages, rating and based on whether the user wants 
# the recommendations in the ascending or descending order
# display_books() used for displaying the list of books desired by the user  
# main() function prompts the user to choose from a group of options. dependding 
# on what option was chosen, the code outputs the desired result. 
# #############################################################################


import csv
from operator import itemgetter
import copy

TITLE = 1
CATEGORY = 3
YEAR = 5
RATING = 6
PAGES = 7

MENU = "\nWelcome to the Book Recommendation Engine\n\
        Choose one of below options:\n\
        1. Find a book with a title\n\
        2. Filter books by a certain criteria\n\
        3. Recommend a book \n\
        4. Quit the program\n\
        Enter option: "

CRITERIA_INPUT = "\nChoose the following criteria\n\
                 (3) Category\n\
                 (5) Year Published\n\
                 (6) Average Rating (or higher) \n\
                 (7) Page Number (within 50 pages) \n\
                 Enter criteria number: "
TITLE_FORMAT = "{:15s} {:35s} {:35s} {:6s} {:8s} {:15s} {:15s}"
TABLE_FORMAT = "{:15s} {:35s} {:35s} {:6s} {:<8.2f} {:<15d} {:<15d}"

def open_file():
    """This function prompts the user to input a file name. Then it 
    tries to open the file. If file cannot be opened, it displays an
    error message. If file opens, it returns the file pointer (fp)"""
   
    #while loop to keep asking for filename until file found
    while True:
        try:
            filename = input("Enter file name: ")
            fp = open(filename, "r", encoding ="utf-8")
            return fp
        #if file not found, disply error message
        except FileNotFoundError:
            print("\nError opening file. Please try again.")

def read_file(fp):
    """This function has 1 arguement: the fp. This function reads the 
    comma-separated value (csv) file using file pointer fp and returns the 
    list of tuples"""
    books_list = []
    reader = csv.reader(fp)  
    next(reader) # for skipping the header line

    #iteration loop to read csv file 
    for row in reader:
        try:
        #assigning each attribute the desired value from csv file
            isbn13 = row[0]
            title = row[2]
            authors = row[4]
            categories = row[5].lower().split(",")
            description = row[7]
            published_year = row[8]
            average_rating = float(row[9])
            num_pages = int(row[10])
            rating_count = int(row[11])
            book_tuple = (isbn13, title, authors, categories, description, published_year, average_rating, num_pages, rating_count)
            books_list.append(book_tuple)
        #if any conversion error found, restart the loop
        except:
            continue
    return books_list

def get_books_by_criterion(list_of_tuples, criterion, value):
    """This function has 3 arguements: A list, criterion and value which is associated 
    with the criterion entered. This function retrieves the books that match a certain criterion and 
    returns them in the form of a list. If there is a problem with a value or
    criterion parameter,it doesn't add the book to the return list and returns
    an empty list. If criterion is title it will return just the tuple
    containing the desired title(value) """
    result = []   #defining empty list to append is ahead

    for book_tuple in list_of_tuples:
        #If criterion is titel, only return that particular tuple
        if criterion == 1 and value.lower() == (book_tuple[criterion]).lower():
            return book_tuple

        #if criterion is categore, find if the entered category is in list of categories
        elif criterion == 3:
            for element in book_tuple[criterion]:      #element refers to each element of category list
                if element == value.lower():
                    result.append(book_tuple)

        elif criterion == 5 and value == book_tuple[criterion]:
            result.append(book_tuple)
        
        #if criterion is rating, retrive all books with rating higher or equal to specified rating
        elif criterion == 6 and float(value) <= float(book_tuple[criterion]):
            result.append(book_tuple)
        
        #if criterion is page_number, return books with page numbers ranging 50 less or 50 more
        elif criterion == 7 and ((int(value) - 50) <= int(book_tuple[PAGES]) <= (int(value) + 50)):
            result.append(book_tuple)
        
    return result

def get_books_by_criteria(list_of_tuples, category, rating, page_number):
    """This function has 4 arguements: A list, category, rating and page number.
    category, rating and number of pages are the criterions used in this function
    This function calls the get_books_by_criterion function three times. 
    These three calls effectively filter for each criterion by passing the 
    returned list of one function as an argument to the next call"""
    filtered_book_list =copy.deepcopy(list_of_tuples)

    #this passess list of each criterion as an arguement to the next call
    #this ensures a list that has been effectivelt filtered
    if category:
        filtered_book_list = get_books_by_criterion(filtered_book_list, 3, category)
    if rating:
        filtered_book_list = get_books_by_criterion(filtered_book_list, 6, rating)
    if page_number:
        filtered_book_list = get_books_by_criterion(filtered_book_list, 7, page_number)
    return filtered_book_list


def get_books_by_keyword(list_of_tuples, keywords):
    """This function has 2 arguements: A list and keywords. This function 
    retrieves all books whose description contains any of the keywords value"""
    result = [] 

    #this loop finds books whose description conatin the entered keywords
    for book_tuple in list_of_tuples:
        description = book_tuple[4].lower()
        for word in keywords:
            if word.lower() in description.lower():
                result.append(book_tuple)
                break
    return result

def sort_authors(list_of_tuples, a_z = True):
    """This function has 2 arguements: a list and a_Z which is set to true by default.
    If user wants books to be displayed in the ascending order of author name,
    a_z will be set to true, if user wants the books to be displayed in the
    descending order of author name, a_z will be set to false. Here, the itemgetter
    function was used in order to sort the list of tuples"""
#copy.deep.copy() used for copying creating a duplicate list without compromise
    new_list = copy.deepcopy(list_of_tuples)  
    new_list.sort(key=itemgetter(2))
    if not a_z:
        new_list.reverse() #returns reversed list (descending order)
    return new_list

def recommend_books(list_of_tuples, keywords, category, rating, page_number, a_z):
    """This function has 6 arguements: a list, a list of keywords, category, rating, 
    number of pages and a_z. It calls the get_books_by_criteria function to obtain
    a filtered list of books based on category, rating and nuber of pages. Furthe,
    is calls the get_books_by_keyword function to retrieve a list of books whose 
    description contains the keywords specified by the user. It then sorts the 
    list in ascending or descending order of author name. Finally, outputs this list"""
   
    #calling three functions to recommend the desired book 
    criteria_book_list = get_books_by_criteria(list_of_tuples, category, rating, page_number)
    keyword_book_list = get_books_by_keyword(criteria_book_list, keywords)
    result = sort_authors(keyword_book_list, a_z)
    return result

def display_books(list_of_tuples):
    """This function displays the books along with their information, using the 
    provided formats. It ignores a book if its title or its authors are longer
    than 35 characters."""
    #if loop that prints nothing to print if list is empty
    if len(list_of_tuples) == 0:
        print("\nBook Details:")
        print("Nothing to print.")

    #else it prints the header line and book info in the required format
    else:
        print("\nBook Details:")
        print("{:15s} {:35s} {:35s} {:6s} {:8s} {:15s} {:15s}".format("ISBN-13","Title","Authors","Year","Rating","Number Pages","Number Ratings"))
        for book_tuple in list_of_tuples: 
            if type(book_tuple) == tuple:
                book_tuple=list(book_tuple)  
                #this condition skips any book with a title or author name exceeding 35 characters
                if len(book_tuple[1]) <= 35 and len(book_tuple[2]) <= 35:
                    print("{:15s} {:35s} {:35s} {:6s} {:<8.2f} {:<15d} {:<15d}".format(book_tuple[0],book_tuple[1],book_tuple[2],book_tuple[5],book_tuple[6],book_tuple[7],book_tuple[8]))
                else:
                    continue

def get_option():
    """This function asks for a valid option. It keeps prompting the user until
    a valid option is entered"""
    choice = input(MENU)

    #if condition returns choice if between 1-4 inclusive
    if choice.isdigit() and 1 <= int(choice) <= 4:
        return int(choice)
    
    #returns none is option chosen is invalid
    else:
        print("\nInvalid option")
        return None
    
def main():
    #open the file and read its contents into a list of tuples
    fp = open_file()    #opening file
    list_of_tuples = read_file(fp)
    
    #defining valid criterion options and initializing other variables
    valid_criterion = [3,5,6,7]
    criterion = 0
    valid_values = []
    value = ""
    rating = 0
    page_number = 0

    while True:  #main loop
        choice = get_option()    #asks for option choice each time after loop restarts

        #if user chooses option 4, break loop
        if choice == 4:
            break

        #if user chooses option 1, prompt them to input a book title, retrieve book info, and display it
        if choice == 1:
            book_title = input("\nInput a book title: ").lower()
            book_tuple = get_books_by_criterion(list_of_tuples, 1, book_title)   
            display_books([book_tuple])

        #if user chooses option 2, prompt them to select a criterion and input a value, retrieve book info, sort authors, and display
        if choice == 2:

            #loop to get valid input for criterion
            while criterion not in valid_criterion:
                try:
                    criterion = int(input(CRITERIA_INPUT))
                    if criterion not in valid_criterion:
                        print("\nInvalid input")
                    else:
                        break
                except ValueError:
                        print("\nInvalid input")

            #loop to get valid input for value 
            while value not in valid_values:
                try:
                    value = input("\nEnter value: ")
                    if criterion == 6:
                        value = float(value)   #converting rating to float
                        break
                    elif criterion == 7:
                        value = int(value)     #converting page_number to int
                        break
                    elif criterion == 3 or criterion == 5:
                        break
                except ValueError:
                    print("\nInvalid input")

            # Get list of books that match criterion and value, sort by author, and display top 30
            criterion_list = get_books_by_criterion(list_of_tuples, criterion, value)
            author_list = sort_authors(criterion_list)
            display_books(author_list[0:30])

            #reset criterion and value to default values
            criterion = 0
            value = ""

        #if user chooses option 3, prompt them for category, rating, number of pages, sorting format and keywords
        if choice == 3:
            #asking user to input category, rating, page number, sorting format, and keywords
            category = input("\nEnter the desired category: ")
            rating = input("\nEnter the desired rating: ")
            page_number = input("\nEnter the desired page number: ")
            sorting_order = input("\nEnter 1 for A-Z sorting, and 2 for Z-A sorting: ")
            keywords = input("\nEnter keywords (space separated): ").split()

            #converting rating and page_number to expected data types (float and int, respectively)
            while not rating.replace('.', '', 1).isdigit():
                rating = input("\nEnter the desired rating (must be a number): ")
            rating = float(rating)

            while not page_number.isdigit():
                page_number = input("\nEnter the desired page number (must be a whole number): ")
            page_number = int(page_number)

            #determine sorting order based on user's input
            if sorting_order == '1':
                ascending_order = True
            else:
                ascending_order = False

            #calling the recommend_books function with user inputs and displaying the result
            recommended_books = recommend_books(list_of_tuples, keywords, category, rating, page_number, ascending_order)
            display_books(recommended_books)


# DO NOT CHANGE THESE TWO LINES
# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.
if __name__ == "__main__":
    main()

