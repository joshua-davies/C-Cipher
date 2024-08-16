def yes_no(question):
    while True:
        response = input(question).lower()
        if response in ["yes", "y"]:
            return "yes"
        elif response in ["no", "n"]:
            return "no"
        else:
            print("Please answer either yes or no")


# asks user if they want instructions and if yes print them else pass
def instructions():
    want_instructions = yes_no("Do you want to read the"
                               " instructions? ").lower()

    if want_instructions == "yes":
        print("Instructions")
        print("--------------")
        print("1. Select whether you want to encrypt or decrypt.")
        print("2. Select which alphabet you want to use.")
        print("3. Enter what you want to encrypt/decrypt.")
        print("4. Type how much shift you want.")
        print("5. Select whether you want to restart the cipher.")
    elif want_instructions == "no":
        pass

while True:
    instructions()