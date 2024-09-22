products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}

def display_sorted_products(products_list, sort_order):
    if sort_order.lower() == "1" or sort_order.lower() == "asc":
        sorted_products = sorted(products_list, key=lambda x: x[1], reverse=False)
    elif sort_order.lower() == "2" or sort_order.lower() == "desc":
        sorted_products = sorted(products_list, key=lambda x: x[1], reverse=True)
    else:
        print("Invalid value")
        return []
    return sorted_products

def display_products(products_list):
    for i, (product, price) in enumerate(products_list, start=1):
        print(f"{i}. {product} - ${price:.2f}")

def display_categories():
    print("Available Categories:")   
    for i, category in enumerate(products.keys(), start=1):
        print(f"{i}. {category}")

def add_to_cart(cart, product, quantity):
    cart.append((product[0], product[1], quantity))

def display_cart(cart):
    total_cost = 0
    print("\nYour Cart:")
    for item, price, quantity in cart:
        cost = price * quantity
        total_cost += cost
        print(f"{item} - ${price:.2f} x {quantity} = ${cost:.2f}")
    print(f"\nTotal cost: ${total_cost:.2f}")
    return total_cost

def generate_receipt(name, email, cart, total_cost, address):
    print(f"\nReceipt\n{'-'*40}")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print("\nProducts purchased:")
    for item, price, quantity in cart:
        print(f"- {item} - ${price:.2f} x {quantity}")
    print(f"\nTotal cost: ${total_cost:.2f}")
    print(f"\nDelivery address: {address}")
    print("Your items will be delivered in 3 days. Payment will be accepted after successful delivery.\n")

def validate_name(name):
    parts = name.split()
    if len(parts) != 2 or not all(part.isalpha() for part in parts):
        return False
    return True

def validate_email(email):
    return "@" in email

def main():
    cart = []
    print("Welcome to the online shopping store!")
    
    # Ask for user details and validate
    name = input("Enter your name (First Last): ")
    while not validate_name(name):
        print("Invalid name format. Please provide your first and last name.")
        name = input("Enter your name (First Last): ")

    email = input("Enter your email: ")
    while not validate_email(email):
        print("Invalid email format. Please provide a valid email.")
        email = input("Enter your email: ")

    # Show categories
    display_categories()
    category_choice = int(input("Select a category by number: "))
    category_name = list(products.keys())[category_choice - 1]
    selected_category = products[category_name]
    
    # Sort products if needed
    sort_order = input("Sort products by price? (1 for ascending, 2 for descending, or press Enter to skip): ")
    if sort_order:
        sorted_products = display_sorted_products(selected_category, sort_order)
    else:
        sorted_products = selected_category

   
if __name__ == "__main__":
    main()
