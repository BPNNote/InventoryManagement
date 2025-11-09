from pathlib import Path




class Inventory:

    def __init__(self, inventory):
        self.inventory = inventory

    def read_inventory(self):
        with open(self.inventory, "r") as file:
            return file.read()

class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

def main():
    current_dir = Path(__file__).resolve().parent
    inventory = current_dir / "inventory.txt"

    print("Inventory Management System")
    data = Inventory(inventory)
    line = data.read_inventory()

    print(f"The text is {line}")



if __name__ == "__main__":
    main()
