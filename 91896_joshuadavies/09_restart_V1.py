def yes_no(question):
    while True:
        response = input(question).lower()
        if response in ["yes", "y"]:
            return "yes"
        elif response in ["no", "n"]:
            return "no"
        else:
            print("Please answer either yes or no")

#asks user if they want to restart
while True:
    while True:
        print("Program Restarts...")
        print("Program Runs...")
        restart = yes_no("Do you want to restart? ")
        if restart == "yes":
            pass

        elif restart == "no":
            print("Program Ends...")
            break