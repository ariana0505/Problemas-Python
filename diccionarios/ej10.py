
clients = {}

def _add_client():
    nif = input("Enter your NIF: ")
    name = input("Enter your name: ")
    phoneNumber = input("Enter your phone number: ")
    email = input("Enter your email: ")
    preference = input("Are you the preferred one?(y/n): ").lower().strip()
    address = input("Enter your address: ")
    if preference == "y":
        preference= True
    elif preference == "n":
        preference = False
    else:
        print("you are not entering a valid value")
        preference = False
    clients[nif] = {"name":name, "address":address, "phoneNmber":phoneNumber, "email":email, "preference":preference}

def _delete_client_by_nif():
    nif = input("Enter the user's NIF you want to delete.: ")
    if nif in clients:
        del clients[nif]
        print("¡Removed successfully!")
    else:
        print("The NIF does not exist")

def _get_client_by_nif():
    nif = input("Enter the user's NIF you want to retrieve: ")
    if nif in clients:
        client = clients[nif]
        print("User information:")
        for field, value in client.items():  
            print(f"{field}: {value}")
    else:
        print("The NIF does not exist.")

def _show_all_clients():
    print("Displaying users' information...")
    for nif, information in clients.items():
        print(f"{nif}: {information}")

def _show_all_preference_clients():
    clientsWithPreference = {}
    for nif, information in clients.items():
        if information.get("preference") == True:
            clientsWithPreference[nif] = information.get("name","unnamed")
    for nif, name in clientsWithPreference.items():
        print(f"{nif}: {name}")

def main():
    while True:
        print("""
        1. Add client
        2. Delete client
        3. Search client by NIF
        4. Show all clients
        5. Show preferred clients
        6. Exit
        """)
        choice = input("Choose an option: ")
        if choice == "1":
            _add_client()
        elif choice == "2":
            _delete_client_by_nif()
        elif choice == "3":
            _get_client_by_nif()
        elif choice == "4":
            _show_all_clients()
        elif choice == "5":
            _show_all_preference_clients()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")

main()