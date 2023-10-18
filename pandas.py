import pandas as pd

MENU = '''
Welcome to the Book Recommendation Engine
Choose one of the below options:
1. Find a book with a title
2. Filter books by a certain criteria
3. Recommend a book 
4. Quit the program
Enter option: '''

CRITERIA_INPUT = '''
Choose the following criteria
(3) Category
(5) Year Published
(6) Average Rating (or higher) 
(7) Page Number (within 50 pages) 
Enter criteria number: '''

def open_file():
    while True:
        try:
            filename = input("Enter file name: ")
            return pd.read_csv(filename)
        except FileNotFoundError:
            print("\nError opening file. Please try again.")

def get_books_by_criterion(df, criterion, value):
    if criterion == 1:
        return df[df['title'].str.lower() == value.lower()]
    elif criterion == 3:
        return df[df['categories'].str.contains(value, case=False)]
    elif criterion == 5:
        return df[df['published_year'] == value]
    elif criterion == 6:
        return df[df['average_rating'] >= float(value)]
    elif criterion == 7:
        return df[(df['num_pages'] >= int(value)-50) & (df['num_pages'] <= int(value)+50)]
    return pd.DataFrame()

def recommend_books(df, keywords, category, rating, page_number, a_z):
    filtered_df = df.copy()

    if category:
        filtered_df = get_books_by_criterion(filtered_df, 3, category)
    if rating:
        filtered_df = get_books_by_criterion(filtered_df, 6, rating)
    if page_number:
        filtered_df = get_books_by_criterion(filtered_df, 7, page_number)
    
    keyword_filtered_df = filtered_df[filtered_df['description'].str.contains('|'.join(keywords), case=False)]
    
    return keyword_filtered_df.sort_values(by='authors', ascending=a_z)

def display_books(df):
    if df.empty:
        print("\nBook Details:\nNothing to print.")
        return
    print("\nBook Details:")
    print(df[['isbn13', 'title', 'authors', 'published_year', 'average_rating', 'num_pages', 'rating_count']].to_string(index=False))

def main():
    df = open_file()
    
    while True:
        choice = input(MENU)
        if choice == '4':
            break
        if choice == '1':
            title = input("\nInput a book title: ").lower()
            result_df = get_books_by_criterion(df, 1, title)
            display_books(result_df)
        elif choice == '2':
            criterion = int(input(CRITERIA_INPUT))
            value = input("\nEnter value: ")
            result_df = get_books_by_criterion(df, criterion, value)
            display_books(result_df.head(30))
        elif choice == '3':
            category = input("\nEnter the desired category: ")
            rating = input("\nEnter the desired rating: ")
            page_number = input("\nEnter the desired page number: ")
            sorting_order = input("\nEnter 1 for A-Z sorting, and 2 for Z-A sorting: ")
            keywords = input("\nEnter keywords separated by space: ").split()
            result_df = recommend_books(df, keywords, category, rating, page_number, sorting_order == '1')
            display_books(result_df)

if __name__ == '__main__':
    main()

"C:\Book_Recommendation_Engine\mian.py"
