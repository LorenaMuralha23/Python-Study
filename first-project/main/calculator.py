class Calculator:
    product_name: str
    product_price: float
    product_qunatity: int

    def calculate_final_price(self, product_price: float, product_quantity: int):
        return product_price * product_quantity