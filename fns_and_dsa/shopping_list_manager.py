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
           
