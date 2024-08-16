#asks the user if they want to encrypt or decrypt
def method_checker():
    while True:
        response = input("Do you want to encrypt or decrypt? ").lower()

        if response == "decrypt" or response == "d":
            method = "decrypt"
            return method
        elif response == "encrypt" or response == "e":
            method = "encrypt"
            return method
        else:
            print("please awnser decrypt or encrypt.")
            pass
while True:
    method_checker()