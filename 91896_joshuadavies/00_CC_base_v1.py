#defines variables 

alphabet = "abcdefghijklmnopqrxtuvwxyz"

#functions

#function to print the title and tell them a bit about the program
def Title():
    print("Caesar Cipher")
    print("--------------")
    print ("welcome to the Caesar Cipher, An program that lets you encrypt / decript messages\nusing a Cipher known for being used by Julius Caesar.")

#asks a yes or no question and Gets a yes or no response
def yes_no(question):

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please answer yes / no")
            pass

#asks a question and then cheacks if a number is within a certain range
def int_check(question, low_num, high_num):

    error = "Please enter a whole number between {} " \
            "and {}".format(low_num, high_num)

    valid = False
    while not valid:

        # ask user for number and check it is valid
        try:
            response = int(input(question))

            if low_num <= response <= high_num:
                return response
            else:
                print(error)

        # if an integer is not entered, display an error message
        except ValueError:
            print(error)

#asks user wether or not they want to encrypt or decrypt 
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

#checks that a string is within a sertain range
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

            
#asks user if they want instructions and if yes print them else pass
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

#encrypts the provided text, by shifting it using the provided shift
def encrypt(alphabet, text, shift):
    result = ""
    alphabet_length = len(alphabet)
    
    for char in text:
        if char in alphabet:
            old_index = alphabet.index(char)
            new_index = (old_index + shift) % alphabet_length
            if new_index > 26:
                print("hi")
            result += alphabet[new_index]
        else:
            result += char
    
    return result
#decrypts the provided text, by shifting it using the provided shift
def decrypt(alphabet, text, shift):
    shift = shift - shift*2
    result = ""
    alphabet_length = len(alphabet)
    
    for char in text:
        if char in alphabet:
            old_index = alphabet.index(char)
            new_index = (old_index + shift) % alphabet_length
            result += alphabet[new_index]
        else:
            result += char
    
    return result

# Main code here
#calls all the functions
Title()
print("")
instructions()
print("")
shift = int_check("Shift: ", 0, 26)
print("")
method = method_checker()
print("")
text = string_checker("What do you want to encrypt / decrypt? ", 100, 0)
print("")
if method == "encrypt":
    print("Encrypted Text: " + encrypt(alphabet, text, shift))
elif method == "decrypt":
    print("Decrypted Text: " + decrypt(alphabet, text, shift))
print("")



