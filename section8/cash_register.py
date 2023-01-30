class CashRegister:
    def __init__(self, name):
        self.name = name
        self.products = {}

    def add_product(self, product, price, quantity=1):
        new_product = {product: price * quantity}
        self.products.update(new_product)

    def remove_product(self, product):
        if product in self.products:
            self.products.pop(product)
        else:
            print("This product is not in the cart.")

    def show_current_purchase(self):
        print(self.products)

    def update_price(self, product, new_price, quantity=1):
        if product in self.products:
            self.products.pop(product)
            updated_product = {product: new_price * quantity}
            self.products.update(updated_product)
        else:
            print("This product is not in the cart.")

    def calculate_subtotal(self):
        self.subtotal = 0
        for value in self.products.values():
            self.subtotal += value
        return self.subtotal

    def calculate_taxes(self, tax=0.05):
        self.taxes = self.subtotal * tax
        return self.taxes

    def calculate_total(self):
        self.total = self.subtotal + self.taxes
        return self.total

    def clear_cart(self):
        self.products.clear()


cash_register_instance = CashRegister("Jonas")

cash_register_instance.add_product("Uvas", 5)
cash_register_instance.add_product("Azeite", 35)
cash_register_instance.add_product("Picanha", 65)
cash_register_instance.add_product("Sal", 2)
cash_register_instance.show_current_purchase()

cash_register_instance.update_price("Uvas", 3)
cash_register_instance.show_current_purchase()

cash_register_instance.remove_product("Vinho")
cash_register_instance.show_current_purchase()

cash_register_instance.remove_product("Sal")
cash_register_instance.show_current_purchase()

print("Subtotal:", cash_register_instance.calculate_subtotal())
print("Taxes:", cash_register_instance.calculate_taxes())
print("Total:", cash_register_instance.calculate_total())

cash_register_instance.clear_cart()
cash_register_instance.show_current_purchase()
