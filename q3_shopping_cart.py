def add_item(item, cart=[]):
    cart.append(item)
    return cart

print(add_item("apple"))
print(add_item("banana"))
print(add_item("milk", cart=["bread"]))
print(add_item("eggs"))

# Error Fix
def add_item(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart

# Full Cart

def create_cart(owner, discount=0):
    return {
        "owner": owner,
        "items": [],
        "discount": discount  
    }

def add_to_cart(cart, name, price, qty=1):
    cart["items"].append({"name": name, "price": price, "qty": qty})

def update_price(price_tuple, new_price):
    return "Tuples cannot be modified. They are immutable."

def calculate_total(cart):
    total = 0
    for item in cart["items"]:
        total += item["price"] * item["qty"]

    # apply discount %
    final_total = total * (1 - cart["discount"] / 100)
    return final_total

# Customer 1
cart1 = create_cart("Alice", discount=10)
add_to_cart(cart1, "apple", 30, qty=2)
add_to_cart(cart1, "milk", 50)

# Customer 2
cart2 = create_cart("Bob")
add_to_cart(cart2, "bread", 25, qty=3)

# Show independent carts
print("Cart 1:", cart1)
print("Cart 2:", cart2)

# Show totals
print("Cart1 Total:", calculate_total(cart1))
print("Cart2 Total:", calculate_total(cart2))

# Demonstrate tuple immutability
price_info = (100, "MRP")
print(update_price(price_info, 120)) 


"""
1. Why is discount=0 safe but cart=[] dangerous?
   • discount=0 → int → immutable → cannot be modified
   • cart=[] → list → mutable → persists across calls → causes shared state bugs

2. Difference between rebinding and mutating?
   • Rebinding: changing a variable to point to a new object
        x = [1,2]
        x = [3,4]      # rebinding
   • Mutating: modifying the same object in place
        x.append(5)

3. Which are mutable?
   Mutable: list, dict, set
   Immutable: tuple, str, int

4. If you pass a list into a function and modify it, do changes reflect outside?
   Yes. Because lists are passed by object reference. 
   The function receives a reference to the **same list object**, not a copy.
"""