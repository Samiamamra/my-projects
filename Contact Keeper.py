import os as o

def Add_new_contact(name,phone_number,email):
    with open("C:/Users/Rami Info/Desktop/my/Python/contect management system/contact_list.txt", "a+") as file:
        file.write(f"{name}{phone_number}{email}/n")
    input("contact saved!")

def Search_for_a_contact():
    search_name = input("Enter the name of the contact: ")
    o.system("cls")
    found = False
    with open("C:/Users/amamr/OneDrive/Desktop/my_files/Python/contect management system/contact_list.txt", "r") as file:
        contacts = file.readlines()
        
        for contact in contacts:
            if search_name.lower() in contact.lower():
                input(f"Contact found: {contact.strip()}")
                found = True
    if not found:
        print("Contact not found!")

def View_all_contacts_stored():
    with open("C:/Users/Rami Info/Desktop/my/Python/contect management system/contact_list.txt" ,"r+") as file:
        contact_list = file.read()
    input(contact_list)

def Exit_screen():
    o.system("cls")
    print("""
1.Main menu
2.Exit""")
    chouse = input("enter your chouse:")
    if chouse == "1":
        Main()
    else:
        exit()

def Main ():
    o.system("cls")
    print("""
welcome to my simpol contact management system!
what did you whant?
1.add new contact.
2.Search for a contact
3.View all contacts stored""")
    Choose =input("enter your Choose 1 or 2 or 3 :")
    if Choose == "1":
        o.system("cls")
        name = input("enter the contact name:")
        o.system("cls")
        phone_number = input("enter the contact phone_number:")
        o.system("cls")
        email = input("enter the contact email:")
        o.system("cls")
        Add_new_contact(name,phone_number,email)
    elif Choose == "2":
        o.system("cls")
        Search_for_a_contact()
    elif Choose == "3":
        o.system("cls")
        View_all_contacts_stored()
    else :
        input("Invalid choice. Please select 1, 2, or 3.")
        o.system("cls")
        Main()
    Exit_screen()

Main()

def My_search_for_a_contact():


    # with open("contact_list.txt" ,"r") as file:
    #     all_contacts_stored = file.read()

    # Search_word = input("enter the name of the contact:")
    # if all_contacts_stored.find(Search_word) == -1:
    #     is_find = False
    # else :
    #     is_find = True
    # contacte_location = all_contacts_stored.find(Search_word)
    # if is_find == True:
    #     print(all_contacts_stored[contacte_location:contacte_location+60])
    # else:
    #     print("contact not found!")
    None
