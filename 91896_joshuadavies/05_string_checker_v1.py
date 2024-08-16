#makes sure that a string is the required lenth

def string_checker(question, max, min):
    while True:
        awnser = input(question).lower()
        x = len(awnser)
        if x < min:
            print("Invalid input. Awnser needs to be longer than {} charactors.".format(min))
            pass
        elif not isinstance(awnser, str):
            print("Invalid input. Please enter a valid string.")
            pass
        elif x > max:
            print("Invalid input. Awnser needs to be shorter than {} charactors.".format(max))
            pass
        else: 
            text = awnser
            return text
        
while True:
    string_checker("What do you want to encrypt? ", 100, 1)
    print("program continues...")