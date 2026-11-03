## Shopping Bill Generator
## Project Description
The Shopping Bill Generator is a Python-based program that accepts product names, quantities, and prices from the user and generates a formatted shopping bill.
It calculates the subtotal, discount, tax, and final payable amount automatically.
## Objective
To practice Python concepts such as:
Lists
Dictionaries
Loops
Functions
Conditional statements
Mathematical calculations
String formatting
## Technologies Used
Programming Language: Python 
## Features
Accepts multiple product details.
Stores product information using dictionaries.
Uses a list to manage multiple products.
Calculates individual product totals.
Calculates subtotal.
Applies a 10% discount.
Calculates 5% tax on the discounted amount.
Displays a formatted shopping bill.
## How to Run the Project
Step 1: Install Python 3 on your computer.
Step 2: Download or clone this project.
Step 3: Open the project folder in VS Code.
Step 4: Open the terminal and execute:bash
python shopping_bill.py
Step 5: Enter the number of products and provide their details.
## Sample Input
text
Enter number of products: 3
Product name: Rice
Quantity: 2
Price per item: 60
Product name: Soap
Quantity: 3
Price per item: 30
Product name: Oil
Quantity: 1
Price per item: 150
## Sample Output
text
========== SHOPPING BILL ==========

Product        Qty    Price     Total
Rice           2      60.00     120.00
Soap           3      30.00     90.00
Oil            1      150.00    150.00

-----------------------------------
Subtotal:       Rs. 360.00
Discount:       Rs. 36.00
Tax:            Rs. 16.20
-----------------------------------
Final Amount:   Rs. 340.20
===================================

## Calculation Logic
Subtotal = Sum of all product totals.
Discount = Subtotal × 10 / 100.
Tax = (Subtotal − Discount) × 5 / 100.
Final Amount = Subtotal − Discount + Tax.
## Concepts Learned
Creating and using Python functions.
Working with lists and dictionaries.
Using for loops.
Performing mathematical calculations.
Formatting output using f-strings.
Organizing code into reusable functions.
## Conclusion
The Shopping Bill Generator project was completed successfully. It demonstrates the practical use of Python lists, dictionaries, loops, functions, and mathematical operations to generate an itemized shopping bill with discount and tax calculations.
