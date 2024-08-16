# asks user whether they want to encrypt or decrypt
def method_checker(methods):
    print("Please choose an option:")
    for key, value in methods.items():
        print(f"{key} ({value.capitalize()})")

    while True:
        response = input(f"Select an option ({', '.join(methods.keys())}): ").upper()
        if response in methods:
            return methods[response]
        else:
            print("Please select a valid option: A or B.")

methods = {
        "A": "encrypt",
        "B": "decrypt",
}

while True:
    print(method_checker(methods))