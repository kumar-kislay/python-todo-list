import sys
import json

#Function to display the options during the interactive session
def showMenu():
    print("Menu:")
    print("1. Add ToDo item(s): ")
    print("2. Mark item(s) Complete: ")
    print("3. List ToDo item(s): ")
    print("4. Update Item Description: ")
    print("5. Delete item(s): ")
    print("6. Delete all items: ")
    print("7. Exit: ")

#Main Function with all the business logic   
def main():
    
    #variable assignment with default values
    user_input = '99'
    item_list = list()
    create_item_list = list()
    delete_item_list = list()
    complete_item_list = list()
    not_complete_item_list = list()
    
    #dictionary variable to hold all the todo items
    todo_dict = {}
    
    #read the items from data.json file at the start and load in todo dictionary
    with open('data.json') as json_file:
        todo_dict=json.load(json_file)
    
    #read the command line arguments
    item_list = sys.argv
    action = item_list[1]
    
    #create action to add one or more todo item
    if action == "create":
        create_item_list = item_list
        create_item_list.pop(0)
        create_item_list.pop(0)
        for item in create_item_list:
            todo_dict[item]="ToDo"
        print("ToDo items created successfully")
    
    #List action to list items in the todo list
    elif action == "list-all":
        #list all items
        if len(item_list) == 2:
            for items in todo_dict:
                print("[Item]: " + items + " [Status]: " + todo_dict.get(items))
        else:
            #list items containing a keyword / substring
            if item_list[2] == "--substring":
                for item in todo_dict:
                    if item.find(item_list[3]) >= 0:
                        print("[Item]: " + item + " [Status]: " + todo_dict.get(item))
                #print("Print all with substring " + item_list[3])
                
            #list all items which are complete
            elif item_list[2] == "--complete":
                for item in todo_dict:
                    if todo_dict[item] == "Complete":
                        print("[Item]: " + item + " [Status]: " + todo_dict.get(item))
                        
            #list all items which are not complete
            elif item_list[2] == "--no-complete":
                for item in todo_dict:
                    if todo_dict[item] == "ToDo":
                        print("[Item]: " + item + " [Status]: " + todo_dict.get(item))
                        
            else:
                print("Incorrect list argument - Please check")
            
    #Update item description with a new description
    elif action == "toggle":
        new_key = item_list[3]
        old_key = item_list[2]
        todo_dict[new_key] = todo_dict.pop(old_key)
        print("ToDo item description successfully updated")
        
    #Mark one or more item Complete
    elif action == "update":
        complete_item_list=item_list
        complete_item_list.pop(0)
        complete_item_list.pop(0)
        for item in complete_item_list:
            if todo_dict.get(item,"ItemNotPresent") == "ToDo":
                todo_dict[item]="Complete"
                print("Item " + item + " marked complete successfully")
            elif todo_dict.get(item,"ItemNotPresent") == "Complete":
                print("Item "+ item + " already marked complete ")
            else:
                print("Item " + item + " does not exist in the list ")
                
    #Delete one or more item
    elif action == "delete":
        delete_item_list = item_list
        delete_item_list.pop(0)
        delete_item_list.pop(0)
        for item in delete_item_list:
            element = todo_dict.pop(item, "defaultvalue")
            if element == "defaultvalue":
                print("Item " + item + " is not present in the list")
            else:
                print("Item " + item + " deleted successfully")
        print("Item deletion complete successfully")
        
    #Delete all the items from the list
    elif action == "delete-all":
        todo_dict.clear()
        print("All items deleted successfully")
        
    #Interactive session - ToDo List
    elif action == "interactive":
        print("Welcome to the Interactive Mode")
        
        #Continue with the interactive session until the user keys in option 7
        while user_input != '7':
            
            #continuously show the interactive session menu
            showMenu()
            user_input = input("Enter Your Choice: ")
            
            #User to select option 1 to add one or more to items
            if user_input == '1':
                item_list = input("Enter the ToDo items ").split()
                for item in item_list:
                    todo_dict[item]="ToDo"
                    print("Added item: ", item)
                print("Added item(s) successfully ")
            
            #User to select option 2 to mark one or more items complete
            elif user_input == '2':
                item_list = input("Enter the item(s) to be marked complete ").split()
                for item in item_list:
                    if todo_dict.get(item,"ItemNotPresent") == "ToDo":
                        todo_dict[item]="Complete"
                        print("Item "+ item + " successfully marked complete ")
                    elif todo_dict.get(item,"ItemNotPresent") == "Complete":
                        print("Item " + item + " already marked complete ")
                    else:
                        print("Item " + item + " does not exist in the list ")
                    
            #Option 3 to list all the items in the list
            elif user_input == '3':
                print("List of TO-DO Items: ")
                for items in todo_dict:
                    print("[Item]: " + items + " [Status]: " + todo_dict.get(items))
                    
            #Option 4 to Update an item's description
            elif user_input == '4':
                old_item = input("Enter the item to update: ")
                new_item = input("Enter the new item description: ")
                todo_dict[new_item] = todo_dict.pop(old_item)
                print("ToDo item description successfully updated")
                
            #Option 5 to delete one or more items from the list
            elif user_input == '5':
                item_list = input("Enter the items to delete: ").split()
                for item in item_list:
                    element = todo_dict.pop(item, "defaultvalue")
                    if element == "defaultvalue":
                        print("Item " + item + " is not present in the list")
                    else:
                        print("Item " + item + " deleted successfully")
                print("Item deletion complete successfully")   
            
            #Option 6 to delete all the items from the list
            elif user_input == '6':
                todo_dict.clear()
                print("All items deleted successfully")
                    
            #Option 7 to jump out of the interactive session and end the program
            elif user_input == '7':
                #y = json.dumps(todo_dict)
                #print(y)
                #with open('data.json', 'w') as outfile:
                    #json.dump(todo_dict, outfile, indent=4)
                print("Good Bye ")
            
        
    else:
        print("Incorrect action argument - Please check and try again")

    
    #save the current state of the todo dictionary in the file data.json
    with open('data.json', 'w') as outfile:
        json.dump(todo_dict, outfile, indent=4)


if __name__ == '__main__':
    main()