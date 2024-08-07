from mod import *
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
            item_name = input('Enter an item to be added:')
            add_Item(item_name)
            # Prompt for and add an item
            pass
        elif choice == '2':
            # Prompt for and remove an item
            item_to_remove = input('Enter item to be removed:')
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
