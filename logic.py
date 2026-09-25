def set_secret(key, secrets):
    if 9 > key > -1:
        value = input("Enter value: ")
        secrets[key] = value
    return
def get_secret(key, secrets):
    if 9 > key > -1:
        return secrets[key]