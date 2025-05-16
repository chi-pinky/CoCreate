

usernames = ["Temitopefx", "SamsonDrums", "DaniellaNoise"]
passwords = ["Password@1$", "Gateway22", "Qwerty.6"]

while True:
    try:
        username = input("Enter Username: ")
        password = input("Enter Password: ")

        if not username or not password:
            raise ValueError("Username and password cannot be empty.")

        if username in usernames and password in passwords:
            print(f"Welcome {username}")
            break
        else:
                print("Incorrect username and password! Please try again.\n")

    except Exception as e:
        print(f"Error: {e}\nPlease try again.\n")
