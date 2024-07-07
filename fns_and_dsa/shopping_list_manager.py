shopping_list = []
def add_Item(item_name):
    """Adds items to an empty shoppping list"""
    shopping_list.append(item_name)
    print(f"{item_name} added successfully")

def view_list(shopping_list):
    for i in shopping_list: 
        print(i) 
    if not shopping_list:
            print('no items in shopping list')

def remove_item(shopping_list, item):
    shopping_list[:] =[i for i in shopping_list if i != item] 
    for n in shopping_list:
       if n != item:
           print(f'{item} not found in list')
          

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item_name = input('Enter the item to add:')
            add_Item(item_name)
            # Prompt for and add an item
            pass
        elif choice == '2':
            # Prompt for and remove an item
            item_to_remove = input('Enter the item to remove:')
            remove_item(shopping_list, item_to_remove)
            pass
        elif choice == '3':
            view_list(shopping_list)
            # Display the shopping list
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
