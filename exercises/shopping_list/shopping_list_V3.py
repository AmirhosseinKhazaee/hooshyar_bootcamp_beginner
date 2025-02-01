import json
import csv
from shopping_list_V2 import ShoppingList

class ShoppingListV3(ShoppingList):
    def __init__(self):
        super().__init__()
        self.helps["add"] = "1. Add item: add <item> [optional: <category>]"
        self.helps["search"] = "8. Search Item in List: search <item>"
        self.commands["search"] = self.search
        self.items = {}

    def add(self, item):
        categories = ["Fruits" , "Vegetables" , "Supermarket"]
        args = item.split(" ")
        if len(args) < 2 :
            category = "Supermarket"
            item_name = args[0].capitalize()
        else:
            item_name, category = args[0].capitalize() , args[1].capitalize()
        if category not in categories:
            print("Invalid Category!")
            print("Valid Categories :")
            for ctg in categories:
                print(f"    {ctg}")
        else:
        # Ensure the category exists in the dictionary
            if category not in self.items:
                self.items[category] = {}

            # Add or increase the quantity of the item
            if item_name in self.items[category]:
                self.items[category][item_name] += 1
                message = f"Item {item_name} (Category: {category}) amount increased to {self.items[category][item_name]}."
            else:
                self.items[category][item_name] = 1
                message = f"Item {item_name} added to the shopping list under {category} category."

            print(message)

    def search(self, item_name):
        item_name = item_name.capitalize().strip()
        results = []

        # Search in all categories
        for category, items in self.items.items():
            for item in items:
                if item_name in item:
                    results.append(f"{item} (Category: {category})")

        if results:
            print("Similar items found:")
            for result in results:
                print(f"{result}")
        else:
            print("No matching items found.")

    def show(self):
        """Display the shopping list."""
        if not self.items:
            print("The shopping list is empty.")
        else:
            print("\nShopping List:")
            for category, items in self.items.items():
                print(f"Category: {category}")
                for item, quantity in items.items():
                    print(f"  - {item} - Amount: {quantity}")
                print()

if __name__ == "__main__":
    shopping_list = ShoppingListV3()
    shopping_list.run()
