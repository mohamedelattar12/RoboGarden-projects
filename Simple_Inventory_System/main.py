class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Product Name: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Quantity: {self.quantity}")

    def update_quantity(self, amount):
        if self.quantity + amount < 0:
            print(f"Insufficient stock for {self.name}.")
        else:
            self.quantity += amount
            print(f"Updated quantity for {self.name}: {self.quantity}")

    def calculate_value(self):
        return self.price * self.quantity


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Added {product.name} to inventory.")

    def display_inventory(self):
        print("\nInventory Details:")
        if not self.products:
            print("No products in inventory.")
        for product in self.products:
            product.display_info()
            print("-" * 20)

    def calculate_total_value(self):
        total_value = sum(product.calculate_value() for product in self.products)
        print(f"\nTotal Inventory Value: ${total_value:.2f}")


def main():
    inventory = Inventory()
    product1 = Product("Laptop", 1200.00, 5)
    product2 = Product("Smartphone", 800.00, 10)
    product3 = Product("Headphones", 150.00, 15)
    inventory.add_product(product1)
    inventory.add_product(product2)
    inventory.add_product(product3)
    inventory.display_inventory()
    product1.update_quantity(-1)  
    product3.update_quantity(5)  
    inventory.display_inventory()
    inventory.calculate_total_value()



main()
