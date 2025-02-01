helps = {
    "add": "1. Add item: add <item>",
    "edit": "2. Edit item: edit <item number> <new item>",
    "delete": "3. Delete item: delete <item number>",
    "show": "4. Show list: show",
    "help": "5. Show help: help",
    "finalize": "6. Finalize list: finalize"
}

commands = {
    "help": lambda: help_command(),
    "add": lambda item: add(item),
    "edit": lambda index, new_item: edit(index, new_item),
    "delete": lambda index: delete(index),
    "show": lambda: show(),
    "finalize": lambda: finalize()
}

items = {}

def help_command():
    print("\nCommands:")
    for help_text in helps.values():
        print(help_text)
    print()

def add(item):
    item = item.capitalize()
    message = f"Item {item} added to the shopping list."
    if item in items:
        items[item] += 1
        message =f"Item {item} Amount increased to {items[item]}."
    else:
        items[item] = 1
    print(message)

def edit(index, new_item):
    try:
        index = int(index) - 1
        if index < 0 or index >= len(items):
            print("Invalid item number!")
            return
        old_item = list(items.keys())[index]
        items[new_item.capitalize()] = items.pop(old_item)
        print(f"Item {index+1} has been updated to {new_item.capitalize()}.")
    except (ValueError, IndexError):
        print("Invalid input! Use: edit <item number> <new item>")

def delete(index):
    try:
        index = int(index) - 1
        if index < 0 or index >= len(items):
            print("Invalid item number!")
            return
        item = list(items.keys())[index]
        del items[item]
        print(f"Item {item} deleted from the shopping list.")
    except (ValueError, IndexError):
        print("Invalid input! Use: delete <item number>")

def show():
    if not items:
        print("The shopping list is empty.")
    else:
        print("\nShopping List:")
        for i, (item, quantity) in enumerate(items.items(), 1):
            print(f"{i}. {item} - Amount : {quantity}")
    print()

def finalize():
    print("Shopping list finalized. No further changes can be made.")
    print("\nFinalized Shopping List:")
    show()
    exit()

print("Welcome to the Shopping List Program!\n")
help_command()

while True:
    prompt = input("Write your commands here! : ").strip().lower()
    
    if not prompt:
        continue
    
    parts = prompt.split(" ", 2)
    command = parts[0]
    args = parts[1:] if len(parts) > 1 else []

    if command in commands:
        try:
            commands[command](*args)
        except TypeError:
            print(f"Invalid usage of '{command}'. Refer to 'help' for correct usage.")
    else:
        print("Wrong command!")
        help_command()
