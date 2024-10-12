accounts = {}  # Penyimpanan format: {NIM: password}
profiles = {}  # Penyimpanan format: {NIM: {Name, Role, Email}}
books = {
    "B001": {"title": "Data Science", "author": "John Doe"}, 
    "B002": {"title": "Machine Learning", "author": "Jane Smith"}, 
    "B003": {"title": "Python Programming", "author": "Alice Johnson"}, 
    "B004": {"title": "Artificial Intelligence", "author": "Bob Brown"}, 
    "B005": {"title": "Deep Learning", "author": "Chris Green"}
}  
rented_books = {}  # Penyimpanan format: {NIM: [(book_id, book_title, author)]}

# Function to register a new user
def register():
    while True:
        nim = input("Enter your NIM (must be numeric): ")
        if nim.isdigit():  # Check if NIM is numeric
            if nim in accounts:
                print("NIM already registered. Try logging in.")
                return
            break
        else:
            print("Invalid NIM. Please enter a numeric value.")
    
    password = input("Enter your password: ")
    accounts[nim] = password
    print("Registration successful! You can now login.")
    
    # Ask the user 
    choice = input("Would you like to complete your profile now? (yes/skip): ").lower()
    if choice == 'yes':
        create_profile(nim)
    else:
        profiles[nim] = {'Name': None, 'Role': None, 'Email': None}

# Function for user login
def login():
    while True:
        nim = input("Enter your NIM (must be numeric): ")
        if nim.isdigit():  # Check if NIM is numeric
            if nim not in accounts:
                print("NIM not registered. Please register first.")
                return None
            break   
        else:
            print("Invalid NIM. Please enter a numeric value.")
    
    password = input("Enter your password: ")
    if accounts[nim] == password:
        print("Login successful!")
        return nim
    else:
        print("Incorrect password.")
        return None

# Function to capitalize the first letter of each word
def capitalize_first_letter(string):
    return string.title()

# Function to create or edit profile
def create_profile(nim):
    name = capitalize_first_letter(input("Enter your name: "))  
    role = capitalize_first_letter(input("Enter your role: "))  
    
    while True:
        email = input("Enter your email: ")
        if email.count('@') == 1:  
            email = email.lower()  
            break
        else:
            print("Invalid email. Please make sure it contains exactly one '@'.")
    
    profiles[nim] = {'Name': name, 'Role': role, 'Email': email}  # Updated keys
    print("Profile updated successfully!")

# Function to edit NIM and password
def edit_nim_password(nim):
    current_password = input("Enter your current password: ")
    if accounts[nim] != current_password:
        print("Incorrect current password. Unable to change NIM or password.")
        return nim  # return ke nim yang lama
    
    while True:
        new_nim = input("Enter your new NIM (must be numeric): ")
        if new_nim.isdigit():
            if new_nim in accounts and new_nim != nim:
                print("This NIM is already taken. Please choose another one.")
            else:
                new_password = input("Enter your new password: ")
                
                # Update NIM and password in the accounts dictionary
                accounts[new_nim] = new_password
                
                # Copy profile to new NIM
                profiles[new_nim] = profiles.pop(nim)

                # Check if rented_books has an entry for the old NIM before popping
                if nim in rented_books:
                    rented_books[new_nim] = rented_books.pop(nim)
                else:
                    rented_books[new_nim] = []  # Create an empty list if no books were rented

                # Remove old NIM from accounts
                del accounts[nim]
                print("NIM and password updated successfully!")
                return new_nim  
        else:
            print("Invalid NIM. Please enter a numeric value.")

# Function to display available books
def view_books():
    if books:
        print("Available Books:")
        for book_id, details in books.items():
            print(f"{book_id}: {details['title']} by {details['author']}")
    else:
        print("No books available.")

# Function for the user to view rented books
def view_rented_books(nim):
    if nim in rented_books and rented_books[nim]:
        print("Rented Books:")
        for book_id, book_title, author in rented_books[nim]:
            print(f"- {book_id}: {book_title} by {author}")  
    else:
        print("You have not rented any books.")

# Function for admin to view rented books and their renters
def view_rented_books_admin():
    if rented_books:
        print("Rented Books and Renters:")
        for nim, rented_list in rented_books.items():
            print(f"NIM: {nim}, Name: {profiles[nim]['Name']}")
            for book_id, book_title, author in rented_list:
                print(f"    - {book_id}: {book_title} by {author}")
    else:
        print("No books are currently rented.")

# Function for admin to add a new book
def add_book():
    book_id = input("Enter book ID: ")
    if book_id in books:
        print("Book ID already exists.")
    else:
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        books[book_id] = {
            "title": capitalize_first_letter(title),
            "author": capitalize_first_letter(author)
        }
        print(f"Book '{title}' by '{author}' added successfully!")

# Function for admin to delete a book
def delete_book():
    view_books()  # Display available books first
    book_id = input("Enter the ID of the book you want to delete : ").strip().lower()
    
    # Check if the book_id exists in the books dictionary (case insensitive)
    matching_ids = [bid for bid in books if bid.lower() == book_id]
    if matching_ids:
        book_id = matching_ids[0]  # Get the matching book ID (the first one found)
        confirm = input(f"Are you sure you want to delete '{books[book_id]['title']}' by '{books[book_id]['author']}'? (yes/no): ").lower()
        if confirm == 'yes':
            del books[book_id]  # Remove the book from the books dictionary
            print(f"Book '{book_id}' deleted successfully!")
        else:
            print("Deletion cancelled.")
    else:
        print("Book ID not found.")

# Function to rent a book
def rent_book(nim):
    while True:
        view_books()
        book_id = input("Enter the ID of the book you want to rent (or type 'exit' to finish): ").strip().lower()
        if book_id == 'exit':
            print("Exiting the rental process.")
            break  # Exit the loop if the user types 'exit'
        
        # Check if the book_id exists in the books dictionary (case insensitive)
        matching_ids = [bid for bid in books if bid.lower() == book_id]
        if matching_ids:
            book_id = matching_ids[0]  # Get the matching book ID (the first one found)
            if nim not in rented_books:
                rented_books[nim] = []
            # Store tuple of (book_id, book_title, author) for rented books
            rented_books[nim].append((book_id, books[book_id]["title"], books[book_id]["author"]))
            print(f"You rented '{books[book_id]['title']}' by '{books[book_id]['author']}'.")  # Include author in the output
            del books[book_id]  # Remove book from available books
        else:
            print("Book ID not found.")

# Function for the user menu
def user_menu(nim):
    while True:
        print("\n1. View Profile\n2. Edit Profile\n3. Edit NIM and Password\n4. View Available Books\n5. Rent a Book\n6. View Rented Books\n7. Logout")
        choice = input("Select an option: ")
        
        if choice == '1':
            print(f"Profile: {{{nim}: {profiles[nim]}}}")
        elif choice == '2':
            create_profile(nim)
        elif choice == '3':
            nim = edit_nim_password(nim)  
        elif choice == '4':
            view_books()
        elif choice == '5':
            rent_book(nim)
        elif choice == '6':
            view_rented_books(nim)  
        elif choice == '7':
            print("Logged out successfully.")
            break
        else:
            print("Invalid option. Try again.")

# Function for admin menu
def admin_menu():
    while True:
        print("\nAdmin Menu:\n1. View Available Books\n2. Add New Book\n3. Delete Book\n4. View Rented Books and Renters\n5. Logout")
        choice = input("Select an option: ")
        
        if choice == '1':
            view_books()
        elif choice == '2':
            add_book()
        elif choice == '3':
            delete_book()  
        elif choice == '4':
            view_rented_books_admin() 
        elif choice == '5':
            print("Logged out successfully.")
            break
        else:
            print("Invalid option. Try again.")

# Main function to control the flow of the program
def main():
    while True:
        print("\n1. Register\n2. Login\n3. Admin Login\n4. Exit")
        choice = input("Select an option: ")
        
        if choice == '1':
            register()
        elif choice == '2':
            nim = login()
            if nim:
                user_menu(nim)
        elif choice == '3':
            admin_password = input("Enter admin password: ")
            if admin_password == "admin123":
                print("Admin login successful!")
                admin_menu()
            else:
                print("Incorrect admin password.")
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

# Run the main function
if __name__ == "__main__":
    main()
