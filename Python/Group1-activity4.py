# Activity 4 (OOP) | Group 1

"""
# Names:-

- Michael
- Faizah
- Yaseen Gaber

# Contribution:-

- Michael ---> 'main()' function ~ (33.3%)
- Faizah ---> 'Article()' class ~ (33.3%)
- Yaseen Gaber ---> 'Cart()' class ~ (33.3%)

# Manifesto:-

Article() class: This class represents an article or product in the shopping cart. It has methods for getting and setting the name, price, and quantity of the article.
It also has a method to convert the article information to a string format for display.

Cart() class: This class represents the shopping cart itself.
It allows users to add, remove, and display items in the cart. It also has functionality for listing all available items, displaying the cart's contents, and performing checkout operations.

main() function: This function serves as the entry point of the shopping cart CLI program.
It initializes the program, reads product data from a CSV file, and enters a loop where users can interact with the shopping cart by selecting various options from a menu. The menu options include listing available items, displaying the cart, adding items to the cart, removing items from the cart, and checking out. The program continues to execute until the user chooses to exit.

Overall, the program provides a command-line interface for managing a shopping cart, allowing users to add, remove, and purchase items interactively.

# Github:-

- Michael: https://github.com/GCIS-123-603/githubpractice-micheal-haddad
- Faizah: https://github.com/54izah/group1_activity1.git
- Yaseen Gaber: https://github.com/Yaseen-Gaber/Group_5.git
"""

# Comma Separated Values
import csv

# 'Inventory' stores the following: item, quantity and the price
INVENTORY = {}
# Store the data of the file in lists ~ Prevents hard-coding
NAME = []
QUANTITY = []
PRICE = []

class Article:
    '''
This class, Article, represents an item that can be added to a shopping cart.
It has attributes like name, price, and quantity. The __init__ method initializes these attributes.
The getName method prompts the user to add an item to the shopping cart and validates the input against a predefined list of item names.
The getPrice method retrieves the price of the item based on its name. The getQunatity method returns the quantity of the item.
The setQuanitity method allows the user to set the quantity of the item, handling cases where the specified quantity exceeds the available quantity in the inventory.
The __str__ method returns a string representation of the item with its name, quantity, and price.
    '''
    def __init__(self, name=None, price=float, quantity=None):
        # Initialize the Article object with the following parameters: name, price, and quantity
        self.name = name
        self.price = price
        self.quantity = quantity

    def getName(self):
        # Prompt the user to input the name of an item from the catalogue
        while True:
            user_input = input("\nAdd an item from the catalogue to the shopping cart: ").strip()
            # Check if the user input matches any of the predefined item names
            if user_input == NAME[0]:
                self.name = user_input
                break
            elif user_input == NAME[1]:
                self.name = user_input
                break
            elif user_input == NAME[2]:
                self.name = user_input
                break
            else:
                print("\nInvalid item, please try again...")
                continue
        return self.name

    def getPrice(self):
        # Check if the price is a float
        if self.price is float:
            # Set the price based on the item name
            if self.name == NAME[0]:
                self.price = PRICE[0]
            elif self.name == NAME[1]:
                self.price = PRICE[1]
            elif self.name == NAME[2]:
                self.price = PRICE[2]
        return float(self.price)

    def getQunatity(self):
        # Return the quantity of the item
        return self.quantity
    
    def setQuanitity(self, quantity=None):
        # Define a method (function) to handle user input for quantity
        def user_input():
            while True:
                try:
                    return int(input(f"\nAdd the quantity of {self.name}: ").strip())
                except ValueError:
                    print(f"\nERROR: invalid input detected, please try again...")
                    continue

        # Define functions to reset the quantity of specific items
        def reset_iphone_15():
            reset_to_default = QUANTITY[0]
            stock_reset = (reset_to_default, INVENTORY["iphone 15"][1])
            INVENTORY["iphone 15"] = stock_reset
            new_quantity = int(INVENTORY["iphone 15"][0]) - quantity
            updated_inventory = (new_quantity, INVENTORY["iphone 15"][1])
            INVENTORY["iphone 15"] = updated_inventory
        
        def reset_galaxy():
            reset_to_default = QUANTITY[1]
            stock_reset = (reset_to_default, INVENTORY["galaxy"][1])
            INVENTORY["galaxy"] = stock_reset
            new_quantity = int(INVENTORY["galaxy"][0]) - quantity
            updated_inventory = (new_quantity, INVENTORY["galaxy"][1])
            INVENTORY["galaxy"] = updated_inventory
        
        def reset_ipad_9th():
            reset_to_default = QUANTITY[2]
            stock_reset = (reset_to_default, INVENTORY["ipad 9th"][1])
            INVENTORY["ipad 9th"] = stock_reset
            new_quantity = int(INVENTORY["ipad 9th"][0]) - quantity
            updated_inventory = (new_quantity, INVENTORY["ipad 9th"][1])
            INVENTORY["ipad 9th"] = updated_inventory

        # If quantity is not specified, prompt the user to input it
        if quantity is None:
            while True:                
                quantity = user_input()
                # Check if the item name matches any of the predefined names
                if self.name == NAME[0]:
# If the specified quantity exceeds the available quantity in the inventory (INVENTORY) (stock), only the available quantity will be added
                    if quantity > int(QUANTITY[0]):
                        self.quantity = QUANTITY[0]
                        new_quantity = 0
                        updated_inventory = (new_quantity, INVENTORY["iphone 15"][1])
                        INVENTORY["iphone 15"] = updated_inventory
                        print("\nUpdated inventory:", INVENTORY, '\n')
                        break
                    # If the quantity is within the available quantity, set the quantity accordingly
                    elif quantity > 0 and quantity <= int(QUANTITY[0]):
                        self.quantity = quantity
                        # Reset the quantity of the item in the inventory
                        if int(INVENTORY["iphone 15"][0]) < 0:
                            reset_iphone_15()
                            print("\nUpdated inventory:", INVENTORY, '\n')
                        elif int(INVENTORY["iphone 15"][0]) > 0:
                            reset_iphone_15()
                            print("\nUpdated inventory:", INVENTORY, '\n')
                        elif int(INVENTORY["iphone 15"][0]) == 0:
                            reset_iphone_15()
                            print("\nUpdated inventory:", INVENTORY, '\n')
                        break
                # Similar checks and operations for other item names
                elif self.name == NAME[1]:
                    # Similar operations for the galaxy item
                    if quantity > int(QUANTITY[1]):
                        self.quantity = QUANTITY[1]
                        new_quantity = 0
                        updated_inventory = (new_quantity, INVENTORY["galaxy"][1])
                        INVENTORY["galaxy"] = updated_inventory
                        print("\nUpdated inventory:", INVENTORY, '\n')
                        break
                    elif quantity > 0 and quantity <= int(QUANTITY[1]):
                        self.quantity = quantity
                        if int(INVENTORY["galaxy"][0]) < 0:
                            reset_galaxy()
                            print("\nUpdated inventory:", INVENTORY, '\n')
                        elif int(INVENTORY["galaxy"][0]) > 0:
                            reset_galaxy()
                            print("\nUpdated inventory:", INVENTORY, '\n')
                        elif int(INVENTORY["galaxy"][0]) == 0:
                            reset_galaxy()
                            print("\nUpdated inventory:", INVENTORY, '\n')
                        break
                # Similar operations for the ipad 9th item
                elif self.name == NAME[2]:
                    if quantity > int(QUANTITY[2]):
                        self.quantity = QUANTITY[2]
                        new_quantity = 0
                        updated_inventory = (new_quantity, INVENTORY["ipad 9th"][1])
                        INVENTORY["ipad 9th"] = updated_inventory
                        print("\nUpdated inventory:", INVENTORY, '\n')
                        break
                    elif quantity > 0 and quantity <= int(QUANTITY[2]):
                        self.quantity = quantity
                        if int(INVENTORY["ipad 9th"][0]) < 0:
                            reset_ipad_9th()
                            print("\nUpdated inventory:", INVENTORY, '\n')
                        elif int(INVENTORY["ipad 9th"][0]) > 0:
                            reset_ipad_9th()
                            print("\nUpdated inventory:", INVENTORY, '\n')
                        elif int(INVENTORY["ipad 9th"][0]) == 0:
                            reset_ipad_9th()
                            print("\nUpdated inventory:", INVENTORY, '\n')
                        break
                if quantity < 0:
                    print("\nNegative integer detected, please enter a positive integer...")
                    continue
        Article.getQunatity(self)

    def __str__(self):
        # Return a formatted string representation of the Article object
        return f"Article: {self.name}, Quantity: {self.quantity}, Price: {float(self.price)}"
    
class Cart:
    '''
This class, Cart, represents a shopping cart where users can add and remove items.
It has attributes such as list_of_purchased, which stores the items added to the cart, and article, an instance of the Article class used to manage individual items.
The __init__ method initializes the list_of_purchased attribute as an empty list and creates an instance of the Article class.
The __str__ method returns a string representation of the list of purchased items.
The list_items method lists the available items with their quantities and prices.
The displayCart method displays the contents of the cart if it's not empty.
The addProduct method allows users to add products to the cart, handling cases where the product is already in the cart and updating the quantities accordingly.
The removeProduct method allows users to remove items from the cart and updates the inventory accordingly.
The checkout method calculates the total price of the items in the cart, applying VAT and discount if applicable. It also handles cases where items are added without quantities.
    '''
    def __init__(self):
        # Initialize Cart object with an empty list for purchased items and an Article object
        self.list_of_purchased = []
        self.article = Article()

    def __str__(self):
        # Return a string representation of the list of purchased items
        return self.list_of_purchased

    def list_items(self):
        # Create a list of formatted strings representing each item with its quantity and price
        items = [f"Item: {NAME[0]}, Quantity: {QUANTITY[0]}, Price: {PRICE[0]}",
                f"Item: {NAME[1]}, Quantity: {QUANTITY[1]}, Price: {PRICE[1]}",
                f"Item: {NAME[2]}, Quantity: {QUANTITY[2]}, Price: {PRICE[2]}"
                ]
        # Print each item string in the list
        for item in items:
            print(item)

    def displayCart(self):
        # Check if the cart is empty, if so, print a message
        if not self.list_of_purchased:
            print("\nSorry, the shopping cart is empty.")
        else:
            # If the cart is not empty, iterate over the list of purchased items and print each one
            for index in range(len(self.list_of_purchased)):
                article = self.list_of_purchased[index]
                print(f"Article {index + 1}: {article}")

    def addProduct(self, name=None, quantity=None):
        # Define functions to check if specific items are already in the cart
        def iphone_15_found():
            if NAME[0] in str(self.list_of_purchased):
                return True
            else:
                return False
        
        def galaxy_found():
            if NAME[1] in str(self.list_of_purchased):
                return True
            else:
                return False
        
        def ipad_9th_found():
            if NAME[2] in str(self.list_of_purchased):
                return True
            else:
                return False
        
        # If name and quantity are not provided, get them from the Article object
        if name is None and quantity is None:
            name = self.article.getName()
            self.article.setQuanitity()

        # Get price and quantity from the Article object
        price = self.article.getPrice()
        new_quantity = self.article.getQunatity()
        Article(name=name, price=price, quantity=new_quantity)

        # Check which item is being added and adjust the cart accordingly
        if self.article.name == NAME[0]:
            iphone_found = iphone_15_found()
            if iphone_found:
                # If iPhone 15 is already in the cart, update its quantity
                # Remove the old entry and add the updated one
                print(f"The product '{self.article.name}' is already in the cart\n")

                for i in self.list_of_purchased:
                    if NAME[0] in str(i):
                        self.list_of_purchased.remove(i)
                        self.list_of_purchased.append(str(self.article))
                        break
                    if NAME[1] in str(i):
                        continue
                    if NAME[2] in str(i):
                        continue
            else:
                # If iPhone 15 is not in the cart, add it
                self.list_of_purchased.append(str(self.article))

        elif self.article.name == NAME[1]:
            # Similar operations for the Galaxy item
            samsung_galaxy_found = galaxy_found()
            if samsung_galaxy_found:
                print(f"The product '{self.article.name}' is already in the cart\n")

                for index in self.list_of_purchased:
                    if NAME[0] in str(index):
                        continue
                    if NAME[1] in str(index):
                        self.list_of_purchased.remove(index)
                        self.list_of_purchased.append(str(self.article))
                        break
                    if NAME[2] in str(index):
                        continue
            else:
                self.list_of_purchased.append(str(self.article))
        
        elif self.article.name == NAME[2]:
            # Similar operations for the iPad 9th item
            ipad_found = ipad_9th_found()
            if ipad_found:
                print(f"The product '{self.article.name}' is already in the cart\n")

                for article in self.list_of_purchased:
                    if NAME[0] in str(article):
                        continue
                    if NAME[1] in str(article):
                        continue
                    if NAME[2] in str(article):
                        self.list_of_purchased.remove(article)
                        self.list_of_purchased.append(str(self.article))
                        break
            else:
                self.list_of_purchased.append(str(self.article))

        # Print the updated list of purchased articles
        print("Updated list of purchased articles:\n")
        for article in self.list_of_purchased:
            print(article)
    
    def removeProduct(self, name=None, quantity=None):
        # Define functions to reset the quantity of specific items in the inventory
        def reset_iphone_15():
            # Reset iPhone 15 quantity to default and update the inventory
            reset_to_default = QUANTITY[0]
            stock_reset = (reset_to_default, INVENTORY["iphone 15"][1])
            INVENTORY["iphone 15"] = stock_reset
        
        def reset_galaxy():
            # Reset Galaxy quantity to default and update the inventory
            reset_to_default = QUANTITY[1]
            stock_reset = (reset_to_default, INVENTORY["galaxy"][1])
            INVENTORY["galaxy"] = stock_reset

        def reset_ipad_9th():
            # Reset iPad 9th quantity to default and update the inventory
            reset_to_default = QUANTITY[2]
            stock_reset = (reset_to_default, INVENTORY["ipad 9th"][1])
            INVENTORY["ipad 9th"] = stock_reset

        # INforms the user to select option 2 to replace an item's quantity in the cart
        print("\nThis option is intended to remove an item from the shopping cart...\n")
        print("To remove (replace) an item's quantity, please select option 2\n")

        if name is None and quantity is None:
            # If name and quantity are not provided, prompt the user to input the item to remove
            while True:
                user_input = input("Remove an item from the shopping cart: ").strip()
                # Check if the input matches any predefined item names
                if user_input == NAME[0]:
                    name = user_input
                    break
                elif user_input == NAME[1]:
                    name = user_input
                    break
                elif user_input == NAME[2]:
                    name = user_input
                    break
                else:
                    print("\nInvalid item, please try again...\n")
                    continue
        
        # Depending on the selected item, remove it from the cart and update the inventory
        if name == NAME[0]:
            # If iPhone 15 is selected, remove it from the cart and update the inventory
            for i in self.list_of_purchased:
                if NAME[0] in str(i):
                    self.list_of_purchased.remove(i)
                    reset_iphone_15()
                    print("\nUpdated inventory:", INVENTORY)
                    break
                if NAME[1] in str(i):
                    continue
                if NAME[2] in str(i):
                    continue
        elif name == NAME[1]:
            # If Galaxy is selected, remove it from the cart and update the inventory
            for index in self.list_of_purchased:
                if NAME[0] in str(index):
                    continue
                if NAME[1] in str(index):
                    self.list_of_purchased.remove(index)
                    reset_galaxy()
                    print("\nUpdated inventory:", INVENTORY)
                    break
                if NAME[2] in str(index):
                    continue
        elif name == NAME[2]:
            # If iPad 9th is selected, remove it from the cart and update the inventory
            for article in self.list_of_purchased:
                if NAME[0] in str(article):
                    continue
                if NAME[1] in str(article):
                    continue
                if NAME[2] in str(article):
                    self.list_of_purchased.remove(article)
                    reset_ipad_9th()
                    print("\nUpdated inventory:", INVENTORY)
                    break
        
        # Print the updated list of purchased articles
        print("\nUpdated list of purchased articles:\n")
        if self.list_of_purchased == []:
            print("The list is empty. No items found")
        else:
            for _ in self.list_of_purchased:
                print(_)

    # Perform Price calculations using VAT & Discount
    def checkout(self):
        # Define VAT and discount constants
        VAT = 0.07
        DISCOUNT = 0.1
        total_quantity = []
        # Define a function to extract item quantities from the list of purchased articles
        def extract_quantity():
            # Iterate over the list of purchased articles
            for index in self.list_of_purchased:
                if "Quantity: " in index:
                    # Extract item info
                    item_info = str(index).split("Quantity: ")[0].replace("Article: ", "").replace(",", "").strip()
                    # Extract quantity
                    quantity = str(index).split("Quantity: ")[1].strip() 
                    found_quantity = ''
                    for element in quantity:
                        if element != ',':
                            found_quantity += element
                        else:
                            break
                    # Combine item info and quantity
                    item_with_quantity = f"{item_info}: {found_quantity}"
                    # Append the combined string to the total_quantity list
                    total_quantity.append(item_with_quantity)
            # If no items with quantity are found, print a message
            if not total_quantity:
                print("\nNo item quantity selected")
            else:
                print("\nSelected item quantities:", total_quantity)

        # Extract item quantities
        extract_quantity()
        # Calculate total price based on item quantities
        total_iphone_price = 0
        total_galaxy_price = 0
        total_ipad_9th_price = 0
        # if total_quantity list is not empty...
        if total_quantity != []:
            # Iterate over the list of selected item quantities
            for article in total_quantity:
            # Extract and calculate prices for each item
                if NAME[0] in article:
                    iphone_quantity = str(article).split(": ")[1]
                    if int(iphone_quantity) > 3:
                        print("\nApplying Discount...\n")
                        iphone_15_discount = int(iphone_quantity) * int(PRICE[0]) * DISCOUNT
                        total_iphone_price = int(iphone_quantity) * int(PRICE[0]) - iphone_15_discount
                    else:
                        total_iphone_price = int(iphone_quantity) * int(PRICE[0])
                if NAME[1] in article:
                    galaxy_quantity = str(article).split(": ")[1]
                    if int(galaxy_quantity) > 3:
                        print("\nApplying Discount...\n")
                        galaxy_discount = int(galaxy_quantity) * int(PRICE[1]) * DISCOUNT
                        total_galaxy_price = int(galaxy_quantity) * int(PRICE[1]) - galaxy_discount
                    else:
                        total_galaxy_price = int(galaxy_quantity) * int(PRICE[1])
                if NAME[2] in article:
                    ipad_9th_quantity = str(article).split(": ")[1]
                    if int(ipad_9th_quantity) > 3:
                        print("\nApplying Discount...\n")
                        ipad_9th_discount = int(ipad_9th_quantity) * int(PRICE[2]) * DISCOUNT
                        total_ipad_9th_price = int(ipad_9th_quantity) * int(PRICE[2]) - ipad_9th_discount
                    else:                    
                        total_ipad_9th_price = int(ipad_9th_quantity) * int(PRICE[2])
            
            # Calculate total price, tax, and total price including VAT
            total_price = total_iphone_price + total_galaxy_price + total_ipad_9th_price
            tax = total_price * VAT
            total_price_with_vat = total_price + tax
            # Print the total bill with VAT
            print(f"\nYour bill is ${float(total_price_with_vat)} including VAT")
        # If no items are selected, print a message
        else:
            print("\nPlease select an item")

def main():
    '''
The read_data function reads product data from a CSV file, extracting product names, quantities, and prices, then stores them in appropriate data structures.
The operations function implements the main menu of the shopping cart application.
It displays commands, takes user input, and executes corresponding actions such as listing items, adding items to the cart, removing items from the cart, and checking out.
It also handles file input for loading product data.
Overall, the main function initializes the application, reads product data, and enters a loop to execute user-selected operations until the user chooses to exit.
    '''
    # Function for reading the csv file for processing
    def read_data(csvfile):
        with open(csvfile, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                # Store the data
                NAME.append(row[0])
                QUANTITY.append(row[1])
                PRICE.append(row[2])

                # Extract product name, quantity, and price from the row
                product_name, quantity, price = row
        
                # Convert quantity and price to integers
                quantity = int(quantity)
                price = int(price)
        
                # Create a tuple of quantity and price
                product_tuple = (quantity, price)
        
                # Add the product information to the dictionary
                INVENTORY[product_name] = product_tuple
        print("File data read successfully")

    # Initialize Main Menu function
    def operations():
        # create an instance variable of 'Cart()' class to access its methods
        cart = Cart()
        # Define function that Displays the commands
        def display_commands():
            commands = ["\n1. List all items, inventory and price",
                        "2. List shopping cart items",
                        "3. Add an item to the shopping cart",
                        "4. Remove an item from the shopping cart",
                        "5. Checkout",
                        "6. Exit\n"]
            for command in commands:
                print(command)

        # Define functions that take user input for code robustness
        def input_command():
            return input("Enter your choice (1/2/3/4/5/6): ")
        
        def do_you_want_to_continue():
            return input("\nDo you want to continue (y/n): ").strip().casefold()

        def yes_or_no():
            while True:
                user_input = do_you_want_to_continue()
                if user_input in ('y', 'yes'):
                    return True
                elif user_input in ('n', 'no'):
                    print("\nExiting the program...\n")
                    return False
                else:
                    print("\nInvalid input. Please enter 'y' or 'n'.\n")

        # Loop to handle user input and execute program stages
        while True:
            # Display commands
            display_commands()
            command = input_command()
            
            # Check user input and perform tasks accordingly
            if command == "1":
                print("\nThe inventory --->", INVENTORY, '\n')
                print("is formatted as follows...\n")
                cart.list_items()
                restart = yes_or_no()
                if restart:
                    continue
                else:
                    break
            elif command == "2":
                cart.displayCart()
                restart = yes_or_no()
                if restart:
                    continue
                else:
                    break
            elif command == "3":
                cart.addProduct()
                restart = yes_or_no()
                if restart:
                    continue
                else:
                    break
            elif command == "4":
                cart.removeProduct()
                # pass
                restart = yes_or_no()
                if restart:
                    continue
                else:
                    break
            elif command == "5":
                cart.checkout()
                # pass
                restart = yes_or_no()
                if restart:
                    continue
                else:
                    break
            elif command == "6":
                print("\nExiting the program...\n")
                break
            else:
                print("\nInvalid option. Please try again.")
                continue

    # while loop that asks for the csv file
    while True:
            file_path = input("\nEnter path to the CSV file (absolute or relative path): ").strip()
            try:                
                if "products.csv" in file_path:
                    print("\nChecking if file exists...\n")
                    read_data(file_path)
                    break
                else:
                    # Any wrong input
                    print("\nInvalid file path. Please try again.")
                    continue
            except FileNotFoundError:
                # when "products.csv" is entered, prints out file not found if the file doesn't exist
                print("ERROR: File not found...")
                continue

    # Main Menu
    print("\nWelcome to the shopping cart CLI")
    print("\nPlease select one of the following options:")
    operations()

if __name__ == "__main__":
    main()