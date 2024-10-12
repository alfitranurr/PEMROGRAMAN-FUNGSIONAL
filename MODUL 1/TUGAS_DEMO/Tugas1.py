# Data storage using dictionaries and lists
accounts = {}  # Stores account information in the format: {NIM: password}
profiles = {}  # Stores profile information in the format: {NIM: {Name, Role, Email}}
friends = {}   # Stores friends list in the format: {NIM: [friend1, friend2]}

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
    
    # Ask the user if they want to fill their profile now or later
    choice = input("Would you like to complete your profile now? (yes/skip): ").lower()
    if choice == 'yes':
        create_profile(nim)
    else:
        profiles[nim] = {'Name': None, 'Role': None, 'Email': None}
    
    # Initialize an empty friends list for the user
    friends[nim] = []

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
    name = capitalize_first_letter(input("Enter your name: "))  # Capitalize first letter
    role = capitalize_first_letter(input("Enter your role: "))  # Capitalize first letter
    
    while True:
        email = input("Enter your email: ")
        if email.count('@') == 1:  # Check if there is exactly one '@'
            email = email.lower()  # Make the email lowercase for consistency
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
        return nim  # Return the old NIM without changes
    
    while True:
        new_nim = input("Enter your new NIM (must be numeric): ")
        if new_nim.isdigit():
            if new_nim in accounts and new_nim != nim:
                print("This NIM is already taken. Please choose another one.")
            else:
                new_password = input("Enter your new password: ")
                
                # Update NIM and password in the accounts dictionary
                accounts[new_nim] = new_password
                
                # Copy profile and friends to new NIM
                profiles[new_nim] = profiles.pop(nim)
                friends[new_nim] = friends.pop(nim)
                
                # Remove old NIM from accounts
                del accounts[nim]
                print("NIM and password updated successfully!")
                return new_nim  # Return the new NIM
        else:
            print("Invalid NIM. Please enter a numeric value.")

# Function to manage friends list
def manage_friends(nim):
    while True:
        print("\n1. View Friends List\n2. Add Friend\n3. Remove Friend\n4. Exit")
        choice = input("Select an option: ")
        
        if choice == '1':
            if friends[nim]:
                print(f"Your friends: {{{nim}: {friends[nim]}}}")
            else:
                print(f"Your friends list is empty! Please add some friends.")
        elif choice == '2':
            friend = capitalize_first_letter(input("Enter friend's name to add: "))  # Capitalize first letter
            if friend in friends[nim]:
                print(f"{friend} is already in your friends list.")
            else:
                friends[nim].append(friend)
                print(f"{friend} added to your friends list.")
        elif choice == '3':
            if friends[nim]:  # Check if the friends list is not empty
                print(f"Your current friends: {friends[nim]}")
                friend = capitalize_first_letter(input("Enter friend's name to remove: "))  # Capitalize first letter
                if friend in friends[nim]:
                    friends[nim].remove(friend)
                    print(f"{friend} removed from your friends list.")
                else:
                    print(f"{friend} is not in your friends list.")
            else:
                print("Your friends list is empty! You can't remove friends.")
        elif choice == '4':
            break
        else:
            print("Invalid option. Try again.")

# Function for the user menu
def user_menu(nim):
    while True:
        print("\n1. View Profile\n2. Edit Profile\n3. Edit NIM and Password\n4. Manage Friends List\n5. Delete Profile\n6. Logout")
        choice = input("Select an option: ")
        
        if choice == '1':
            print(f"Profile: {{{nim}: {profiles[nim]}}}")
        elif choice == '2':
            create_profile(nim)
        elif choice == '3':
            nim = edit_nim_password(nim)  # Update NIM after editing
        elif choice == '4':
            manage_friends(nim)
        elif choice == '5':
            confirm = input("Are you sure you want to delete your profile? (yes/no): ").lower()
            if confirm == 'yes':
                del profiles[nim]
                del friends[nim]
                del accounts[nim]
                print("Profile and account deleted successfully.")
                break
        elif choice == '6':
            print("Logged out successfully.")
            break
        else:
            print("Invalid option. Try again.")

# Main function to control the flow of the program
def main():
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Select an option: ")
        
        if choice == '1':
            register()
        elif choice == '2':
            nim = login()
            if nim:
                user_menu(nim)
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

# Run the main function
if __name__ == "__main__":
    main()
