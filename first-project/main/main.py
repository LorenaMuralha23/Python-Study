from calculator import Calculator

def __init__():
    print("=========================")
    print("Starting project...")
    print("=========================")

    calculator = Calculator()

    print("Enter the product's name: ")
    product_name = input()
    
    print("Enter the product's price: ")
    product_price = float(input())

    print("Enter product's quantity: ")
    product_quantity = int(input())

    total = calculator.calculate_final_price(product_price, product_quantity)
    print("=========================")
    print("Result")
    print("=========================")

    print("Product: ", product_name, " :: Quantity: ", product_quantity, " :: Price: ", product_price)
    print("Total: ", total)

__init__()