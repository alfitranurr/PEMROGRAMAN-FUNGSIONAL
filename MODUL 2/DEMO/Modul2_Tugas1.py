# Program berdasarkan paradigma fungsional

# Data Storage (immutable by default in functional programming)
initial_accounts = {}  # {NIM: password}
initial_profiles = {}  # {NIM: {Name, Role, Email}}
initial_books = {
    "B001": {"title": "Data Science", "author": "John Doe"}, 
    "B002": {"title": "Machine Learning", "author": "Jane Smith"}, 
    "B003": {"title": "Python Programming", "author": "Alice Johnson"}, 
    "B004": {"title": "Artificial Intelligence", "author": "Bob Brown"}, 
    "B005": {"title": "Deep Learning", "author": "Chris Green"}
}  
initial_rented_books = {}  # {NIM: [(book_id, book_title, author)]}

# Helper function to capitalize the first letter of each word
def capitalize_first_letter(string):
    return string.title()

# Pure function to register a new user
def register(accounts, profiles):
    nim = input("Enter your NIM (must be numeric): ")
    
    if not nim.isdigit():
        print("Invalid NIM. Please enter a numeric value.")
        return accounts, profiles
    
    if nim in accounts:
        print("NIM already registered. Try logging in.")
        return accounts, profiles

    password = input("Enter your password: ")
    accounts = {**accounts, nim: password}
    print("Registration successful! You can now login.")
    
    choice = input("Would you like to complete your profile now? (yes/skip): ").lower()
    if choice == 'yes':
        profiles = create_profile(nim, profiles)
    else:
        profiles = {**profiles, nim: {'Name': None, 'Role': None, 'Email': None}}

    return accounts, profiles

# Pure function for user login
def login(accounts):
    nim = input("Enter your NIM (must be numeric): ")
    
    if not nim.isdigit():
        print("Invalid NIM. Please enter a numeric value.")
        return None
    
    if nim not in accounts:
        print("NIM not registered. Please register first.")
        return None
    
    password = input("Enter your password: ")
    if accounts[nim] == password:
        print("Login successful!")
        return nim
    else:
        print("Incorrect password.")
        return None

# Pure function to create or edit profile
def create_profile(nim, profiles):
    name = capitalize_first_letter(input("Enter your name: "))  
    role = capitalize_first_letter(input("Enter your role: "))  
    
    while True:
        email = input("Enter your email: ")
        if email.count('@') == 1:
            email = email.lower()
            break
        else:
            print("Invalid email. Please make sure it contains exactly one '@'.")
    
    profiles = {**profiles, nim: {'Name': name, 'Role': role, 'Email': email}}
    print("Profile updated successfully!")
    return profiles

# Pure function to edit NIM and password
def edit_nim_password(nim, accounts, profiles, rented_books):
    current_password = input("Enter your current password: ")
    if accounts[nim] != current_password:
        print("Incorrect current password. Unable to change NIM or password.")
        return nim, accounts, profiles, rented_books

    new_nim = input("Enter your new NIM (must be numeric): ")
    
    if not new_nim.isdigit():
        print("Invalid NIM. Please enter a numeric value.")
        return nim, accounts, profiles, rented_books
    
    if new_nim in accounts:
        print("This NIM is already taken. Please choose another one.")
        return nim, accounts, profiles, rented_books

    new_password = input("Enter your new password: ")
    
    # Update accounts and profiles with the new NIM
    accounts = {**accounts, new_nim: new_password}
    profiles = {**profiles, new_nim: profiles.pop(nim)}
    
    # Pindahkan daftar buku yang dipinjam dari NIM lama ke NIM baru
    if nim in rented_books:
        rented_books[new_nim] = rented_books.pop(nim, [])
    
    # Hapus NIM lama dari accounts dan profiles
    del accounts[nim]
    print("NIM and password updated successfully!")
    return new_nim, accounts, profiles, rented_books

# Pure function to view available books
def view_books(books):
    if books:
        print("Available Books:")
        for book_id, details in books.items():
            print(f"{book_id}: {details['title']} by {details['author']}")
    else:
        print("No books available.")
    return books

# Pure function for the user to view rented books
def view_rented_books(nim, rented_books):
    if nim in rented_books and rented_books[nim]:
        print("Rented Books:")
        for book_id, book_title, author in rented_books[nim]:
            print(f"- {book_id}: {book_title} by {author}")
    else:
        print("You have not rented any books.")
    return rented_books

# Pure function for admin to view rented books and their renters
def view_rented_books_admin(profiles, rented_books):
    if rented_books:
        seen_nims = set()  # Untuk menyimpan NIM yang sudah ditampilkan
        print("Rented Books and Renters:")
        for nim, rented_list in rented_books.items():
            if nim in seen_nims:
                continue  # Lewati jika NIM sudah ditampilkan
            seen_nims.add(nim)  # Tambahkan NIM ke set yang sudah ditampilkan
            
            print(f"NIM: {nim}, Name: {profiles[nim]['Name']}")
            for book_id, book_title, author in rented_list:
                print(f"    - {book_id}: {book_title} by {author}")
    else:
        print("No books are currently rented.")
    return rented_books

# Pure function for admin to add a new book (case-insensitive book ID)
def add_book(books, rented_books):
    book_id = input("Enter book ID: ").strip().upper()  # Convert to uppercase

    # Memeriksa apakah book_id sudah ada di books
    if book_id in books:
        print("Book ID already exists in the catalog.")
        return books

    # Memeriksa apakah book_id sedang dipinjam (ada di rented_books)
    for rented_nim, rented_list in rented_books.items():
        if any(book_id == book[0] for book in rented_list):
            print("Book ID is already rented out and cannot be added.")
            return books

    title = capitalize_first_letter(input("Enter book title: "))
    author = capitalize_first_letter(input("Enter book author: "))
    
    # Menambahkan buku baru ke dalam books
    books = {**books, book_id: {"title": title, "author": author}}
    print(f"Book '{title}' by '{author}' added successfully!")
    
    return books


# Pure function for admin to delete a book
def delete_book(books):
    view_books(books)
    book_id = input("Enter the ID of the book you want to delete: ").strip().lower()
    
    matching_ids = [bid for bid in books if bid.lower() == book_id]
    if matching_ids:
        book_id = matching_ids[0]
        confirm = input(f"Are you sure you want to delete '{books[book_id]['title']}' by '{books[book_id]['author']}'? (yes/no): ").lower()
        if confirm == 'yes':
            books = {k: v for k, v in books.items() if k != book_id}
            print(f"Book '{book_id}' deleted successfully!")
        else:
            print("Deletion cancelled.")
    else:
        print("Book ID not found.")
    return books

# Pure function to rent a book (can rent multiple books until 'exit' is entered)
def rent_book(nim, books, rented_books):
    while True:
        view_books(books)
        book_id = input("Enter the ID of the book you want to rent (or type 'exit' to finish): ").strip().lower()

        if book_id == 'exit':
            print("Exiting the rental process.")
            break
        
        # Cari ID buku yang cocok (insensitive case)
        matching_ids = [bid for bid in books if bid.lower() == book_id]
        if matching_ids:
            book_id = matching_ids[0]
            if nim not in rented_books:
                rented_books = {**rented_books, nim: []}
            
            # Tambah buku yang dipinjam ke daftar peminjaman user
            rented_books[nim] = rented_books[nim] + [(book_id, books[book_id]["title"], books[book_id]["author"])]
            print(f"You rented '{books[book_id]['title']}' by '{books[book_id]['author']}'.")

            # Hapus buku yang sudah dipinjam dari daftar buku yang tersedia
            books = {k: v for k, v in books.items() if k != book_id}
        else:
            print("Book ID not found.")

    return books, rented_books


# Main function to control the flow of the program (impure part)
def main():
    accounts, profiles, books, rented_books = initial_accounts, initial_profiles, initial_books, initial_rented_books

    while True:
        print("\n1. Register\n2. Login\n3. Admin Login\n4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            accounts, profiles = register(accounts, profiles)
        elif choice == '2':
            nim = login(accounts)
            if nim:
                while True:
                    print("\n1. View Profile\n2. Edit Profile\n3. Edit NIM and Password\n4. View Available Books\n5. Rent a Book\n6. View Rented Books\n7. Logout")
                    user_choice = input("Select an option: ")

                    if user_choice == '1':
                        print(f"Profile: {{{nim}: {profiles[nim]}}}")
                    elif user_choice == '2':
                        profiles = create_profile(nim, profiles)
                    elif user_choice == '3':
                        nim, accounts, profiles, rented_books = edit_nim_password(nim, accounts, profiles, rented_books)
                    elif user_choice == '4':
                        books = view_books(books)
                    elif user_choice == '5':
                        books, rented_books = rent_book(nim, books, rented_books)
                    elif user_choice == '6':
                        rented_books = view_rented_books(nim, rented_books)
                    elif user_choice == '7':
                        print("Logged out successfully.")
                        break
                    else:
                        print("Invalid option. Try again.")
        elif choice == '3':
            admin_password = input("Enter admin password: ")
            if admin_password == "admin123":
                print("Admin login successful!")
                while True:
                    print("\nAdmin Menu:\n1. View Available Books\n2. Add New Book\n3. Delete Book\n4. View Rented Books and Renters\n5. Logout")
                    admin_choice = input("Select an option: ")

                    if admin_choice == '1':
                        books = view_books(books)
                    elif admin_choice == '2':
                        books = add_book(books, rented_books)
                    elif admin_choice == '3':
                        books = delete_book(books)
                    elif admin_choice == '4':
                        rented_books = view_rented_books_admin(profiles, rented_books)
                    elif admin_choice == '5':
                        print("Logged out successfully.")
                        break
                    else:
                        print("Invalid option. Try again.")
        elif choice == '4':
            confirm_exit = input("Are you sure you want to exit? (yes/no): ").lower()
            if confirm_exit == 'yes':
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Returning to the main menu.")
        else:
            print("Invalid option. Try again.")

# Run the main function
if __name__ == "__main__":
    main()
