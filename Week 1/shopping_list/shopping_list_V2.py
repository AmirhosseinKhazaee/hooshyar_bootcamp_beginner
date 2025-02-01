import json
import csv
class ShoppingList:
    def __init__(self):
        self.items = {}
        self.helps = {
            "add": "1. Add item: add <item>",
            "edit": "2. Edit item: edit <item number> <new item>",
            "delete": "3. Delete item: delete <item number>",
            "show": "4. Show list: show",
            "help": "5. Show help: help",
            "finalize": "6. Finalize list: finalize",
            "export" : "7. Export to file : export <format>"
        }
        self.commands = {
            "help": self.help_command,
            "add": self.add,
            "edit": self.edit,
            "delete": self.delete,
            "show": self.show,
            "finalize": self.finalize,
            "export" : self.export
        }
    
    def help_command(self):
        print("\nCommands:")
        for help_text in self.helps.values():
            print(help_text)
        print()
    
    def add(self, item):
        item = item.capitalize()
        message = f"Item {item} added to the shopping list."
        if item in self.items:
            self.items[item] += 1
            message = f"Item {item} Amount increased to {self.items[item]}."
        else:
            self.items[item] = 1
        print(message)
    
    def edit(self, index, new_item):
        try:
            index = int(index) - 1
            if index < 0 or index >= len(self.items):
                print("Invalid item number!")
                return
            old_item = list(self.items.keys())[index]
            self.items[new_item.capitalize()] = self.items.pop(old_item)
            print(f"Item {index+1} has been updated to {new_item.capitalize()}.")
        except (ValueError, IndexError):
            print("Invalid input! Use: edit <item number> <new item>")
    
    def delete(self, index):
        try:
            index = int(index) - 1
            if index < 0 or index >= len(self.items):
                print("Invalid item number!")
                return
            item = list(self.items.keys())[index]
            del self.items[item]
            print(f"Item {item} deleted from the shopping list.")
        except (ValueError, IndexError):
            print("Invalid input! Use: delete <item number>")
    
    def show(self):
        if not self.items:
            print("The shopping list is empty.")
        else:
            print("\nShopping List:")
            for i, (item, quantity) in enumerate(self.items.items(), 1):
                print(f"{i}. {item} - Amount : {quantity}")
        print()
    
    def finalize(self):
        print("Shopping list finalized. No further changes can be made.")
        print("\nFinalized Shopping List:")
        self.show()
        exit()
    
    def export(self,format):
        format = format.lower()
        formats = ["csv","json"]
        if format not in formats:
            print("Available formats : csv , json")
        else:
            if format == "csv":
                with open("shopping_list/list.csv", "w", newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["Item", "Amount"])
                    for item, amount in self.items.items():
                        writer.writerow([item, amount])
            else:
                 with open("shopping_list/list.json", "w") as file:
                    json.dump(self.items, file, indent=4)
            print(f"Shopping list exported to shopping_list/list.{format}")
    def run(self):
        print("Welcome to the Shopping List Program!\n")
        self.help_command()
        while True:
            prompt = input("Write your commands here! : ").strip().lower()
            if not prompt:
                continue
            parts = prompt.split(" ", 1) 
            command = parts[0]
            if command in self.commands:
                args = parts[1:] if len(parts) > 1 else []
                hint =self.helps[command].split(".")[1].strip()
                try:
                    self.commands[command](*args)
                except TypeError:
                    print(f"Invalid usage of '{command}'. Refer to 'help' for correct usage.")
                    print(f"Hint : {hint}")        
            else:
                print("Wrong command!")
                self.help_command()

if __name__ == "__main__":
    shopping_list = ShoppingList()
    shopping_list.run()
