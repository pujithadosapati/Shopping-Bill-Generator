def calculate_subtotal(products):
    subtotal = 0

    for product in products:
        total = product["quantity"] * product["price"]
        subtotal += total

    return subtotal
def calculate_discount(subtotal):
    discount_rate = 10
    return subtotal * discount_rate / 100
def calculate_tax(subtotal, discount):
    tax_rate = 5
    taxable_amount = subtotal - discount
    return taxable_amount * tax_rate / 100
def generate_bill(products, subtotal, discount, tax):
    print("\n========== SHOPPING BILL ==========")
    print(f"{'Product':<15}{'Qty':<7}{'Price':<10}{'Total':<10}")

    for product in products:
        total = product["quantity"] * product["price"]

        print(
            f"{product['name']:<15}"
            f"{product['quantity']:<7}"
            f"{product['price']:<10.2f}"
            f"{total:<10.2f}"
        )
    final_amount = subtotal - discount + tax

    print("-----------------------------------")
    print(f"Subtotal:      Rs. {subtotal:.2f}")
    print(f"Discount:      Rs. {discount:.2f}")
    print(f"Tax:           Rs. {tax:.2f}")
    print("-----------------------------------")
    print(f"Final Amount:  Rs. {final_amount:.2f}")
    print("===================================")

# Main program
products = []
n = int(input("Enter number of products: "))
for i in range(n):
    print(f"\nEnter details for product {i + 1}")
    name = input("Product name: ")
    quantity = int(input("Quantity: "))
    price = float(input("Price per item: "))
    product = {
        "name": name,
        "quantity": quantity,
        "price": price
    }
    products.append(product)
subtotal = calculate_subtotal(products)
discount = calculate_discount(subtotal)
tax = calculate_tax(subtotal, discount)
generate_bill(products, subtotal, discount, tax)
