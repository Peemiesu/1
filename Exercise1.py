from auth import login
from logic import get_secret, set_secret

secrets = [""] * 10
for i in range(999):
    password = input("passowrd: ")
    if not login(password):
     print("wrong password")
    else:
        option = input("option(get/set): ")
        key = int(input("key (0-9): "))
    if option == "get":
        print(get_secret(key, secrets))
    elif option == "set":
        set_secret(key, secrets)