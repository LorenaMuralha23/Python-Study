from store import Store

def __init__():
    print("Starting the show...\n")

    print("Products >>>>>>>>>>>>>")
    for product in Store.products:
        print(product["name"])
        print("------")

    quantity_per_product= []
    total = calculate_final_total(Store.products)
    categories = set()
    sumary = tuple()
    
    for product in Store.products:
        quantity_product = {}
        quantity_product["name"] = product["name"]
        quantity_product["total"] = product["quantity"] * product["price"]
        categories.add(product["category"])

        quantity_per_product.append(quantity_product)

    sumary = (total, len(Store.products), len(categories))

    print("\nSHOPING DATA >>>>>>>>>>>>>\n")
    
    print("Total per product >>>>>>>>")
    for quantity in quantity_per_product:
        print("Product: ", quantity["name"])
        print("Total: ", quantity["total"])
        print("------")

    print("\nCategories >>>>>>>>")
    print(categories)
    print("------")

    print("\nSummary >>>>>>>>")
    print(sumary)
    print("------")

    print("\nTotal >>>>>>>>")
    print("R$ ", total)
    print("------")

def calculate_final_total(products):
    total = 0
    for product in products:
        individual_price = product["quantity"] * product["price"]

        total += individual_price
    
    return total


__init__()