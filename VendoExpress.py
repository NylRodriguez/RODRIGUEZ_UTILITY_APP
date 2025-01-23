class VendoExpress:
    # This method displays the food menu to the user
    def display_food_menu(self):
        print("\nFOOD MENU:")
        print("1. Chips     - $1.50")
        print("2. Chocolates- $2.00")
        print("3. Candy     - $1.00")
        print("4. Cookies   - $1.75")

    # This method displays the drinks menu to the user
    def display_drinks_menu(self):
        print("\nDRINKS MENU:")
        print("1. Soda         - $1.50")
        print("2. Juice        - $2.00")
        print("3. Milk         - $1.75")
        print("4. Energy Drink - $2.50")
        print("5. Coffee       - $2.00")
        print("6. Tea          - $1.50")

    # This method calculates the price of the selected item based on its type and choice
    def calculate_price(self, item_type, choice):
        prices = {
            'food': {1: 1.50, 2: 2.00, 3: 1.00, 4: 1.75},  # Prices for food items
            'drink': {1: 1.50, 2: 2.00, 3: 1.75, 4: 2.50, 5: 2.00, 6: 1.50}  # Prices for drinks
        }
        # Return the price for the selected item
        return prices[item_type][choice]

    # This method returns the name of the selected item based on its type and choice
    def get_item_name(self, item_type, choice):
        items = {
            'food': {1: 'Chips', 2: 'Chocolates', 3: 'Candy', 4: 'Cookies'},  # Food items
            'drink': {1: 'Soda', 2: 'Juice', 3: 'Milk', 4: 'Energy Drink', 5: 'Coffee', 6: 'Tea'}  # Drink items
        }
        # Return the name of the selected item
        return items[item_type][choice]

    # This is the main method where the vending machine runs
    def run(self):
        cart = []  # A list to store the items the user selects
        total_amount = 0  # Variable to keep track of the total amount the user needs to pay

        # Infinite loop to keep the vending machine running until the user decides to stop
        while True:
            print("\n=== VENDING MACHINE ===")
            choice = input("What would you like to purchase? (1-Food, 2-Drinks): ")

            # If the user chooses food
            if choice == '1':
                self.display_food_menu()  # Display the food menu
                try:
                    food_choice = int(input("Enter your choice (1-4): "))  # Get user input for food choice
                    if 1 <= food_choice <= 4:  # Check if the choice is valid (1 to 4)
                        price = self.calculate_price('food', food_choice)  # Get the price for the chosen food item
                        item_name = self.get_item_name('food', food_choice)  # Get the name for the chosen food item
                        cart.append(item_name)  # Add the item to the cart
                        total_amount += price  # Add the price to the total amount
                    else:
                        print("Invalid choice!")  # If the user enters an invalid number
                        continue
                except ValueError:
                    print("Please enter a valid number!")  # If the user doesn't enter a number
                    continue

            # If the user chooses drinks
            elif choice == '2':
                self.display_drinks_menu()  # Display the drinks menu
                try:
                    drink_choice = int(input("Enter your choice (1-6): "))  # Get user input for drink choice
                    if 1 <= drink_choice <= 6:  # Check if the choice is valid (1 to 6)
                        price = self.calculate_price('drink', drink_choice)  # Get the price for the chosen drink item
                        item_name = self.get_item_name('drink', drink_choice)  # Get the name for the chosen drink item
                        cart.append(item_name)  # Add the item to the cart
                        total_amount += price  # Add the price to the total amount
                    else:
                        print("Invalid choice!")  # If the user enters an invalid number
                        continue
                except ValueError:
                    print("Please enter a valid number!")  # If the user doesn't enter a number
                    continue

            else:
                print("Invalid choice!")  # If the user enters something other than 1 or 2
                continue

            # Ask if the user wants to purchase more items
            more = input("\nWould you like to purchase more items? (yes/no): ").lower()
            if more != 'yes':  # If the user does not want to purchase more items
                break  # Exit the loop and proceed to checkout

        # Display the final order summary
        print("\n=== YOUR ORDER ===")
        print("Items purchased:")
        for item in cart:
            print(f"- {item}")  # Print each item in the cart
        print(f"\nTotal amount: ${total_amount:.2f}")  # Display the total amount to be paid

        # Ask the user to choose a payment method
        payment_method = input("\nSelect payment method (1-Cash/2-Card): ").upper()
        if payment_method == '1':
            # If the user chooses cash, ask them to enter the cash amount
            while True:
                try:
                    cash = float(input(f"Please enter cash amount (${total_amount:.2f}): "))
                    if cash >= total_amount:  # Check if the user entered enough cash
                        change = cash - total_amount  # Calculate the change to give back
                        print(f"Change: ${change:.2f}")  # Print the change
                        break  # Exit the loop
                    else:
                        print("Insufficient amount!")  # If the user doesn't have enough money
                except ValueError:
                    print("Please enter a valid amount!")  # If the user doesn't enter a valid number
        elif payment_method == '2':
            print("Card payment processed successfully!")  # If the user chooses to pay by card
        else:
            print("Invalid payment method!")  # If the user enters an invalid payment option

        print("\nThank you for your purchase!")  # Thank the user for their purchase

# To run the vending machine program, create an object and call the 'run' method
machine = VendoExpress()  
machine.run()



