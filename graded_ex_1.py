# Products available in the store by category
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
    if sort_order.lower() == "1" or sort_order == "asc":
        sorted_products = sorted(products_list, key=lambda x: x['price'], reverse=False)
    elif sort_order.lower() == "2" or sort_order == "desc":
        sorted_products = sorted(products_list, key=lambda x: x['price'], reverse=True)
    else:
        print("invailid value")
    return sorted_products

def display_products(products_list):
    for i, (product, price) in enumerate(products_list, start=1):
        print(f"{i}. {product} - ${price}")


def display_categories():
    print("Available Categories:")   
    for i, category in enumerate(products.keys(), start=1):
        print(f"{i}. {category}")


def add_to_cart(cart, product, quantity):
    cart.append((product[
0], product[1], quantity))

def display_cart(cart):
    total_cost = 0
    for item, price, quantity in cart:
            cost = price * quantity
            total_cost += cost
            print(f"{item} - ${price} x {quantity} = ${cost}")
    
   
            print(f"Total cost: ${total_cost}")
            return total_cost


def generate_receipt(name, email, cart, total_cost, address):
    print("\n--- Receipt ---")
    print(f"Customer: {name}")
    print(f"Email: {email}")
    print("\nItems Purchased:")
for item, price, quantity in cart:    
     print(f"{quantity} x {item} - ${price} = ${price * quantity}")
     print(f"\nTotal: ${total_cost}")
     print(f"Delivery Address: {address}")
     print("\nYour items will be delivered in 3 days.")
     print("Payment will be accepted upon delivery.")
     print("-----------------------------\n")
   



def validate_name(name):
     parts = name.split()
     return len(parts) == 2 and all(part.isalpha() for part in parts)

def validate_email(email):
     return "@" in email


def main():
    cart = []
    print("Welcome to the online shopping store!")
    

""" The following block makes sure that the main() function is called when the program is run. 
It also checks that this is the module that's being run directly, and not being used as a module in some other program. 
In that case, only the part that's needed will be executed and not the entire program """
if __name__ == "__main__":
    main()
