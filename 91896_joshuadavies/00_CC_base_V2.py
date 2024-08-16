# function to print the title and tell them a bit about the program
def title():
    print("Caesar Cipher")
    print("--------------")
    print("Welcome to the Caesar Cipher program!")
    print("This tool allows you to easily encrypt and decrypt messages using the classical Caesar Cipher.")
    print("Originally used by Julius Caesar, this cipher is a simple yet effective method of encryption.")


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



# asks a question and then checks if a number is within a certain range
def int_check(question, low_num, high_num):
    error = f"Please enter a whole number between {low_num} and {high_num}"
    while True:
        try:
            response = int(input(question))
            if low_num <= response <= high_num:
                return response
            else:
                print(error)
        except ValueError:
            print(error)

# checks that a string is within a certain range
def string_checker(question, max_len, min_len):
    while True:
        answer = input(question).strip()
        if min_len <= len(answer) <= max_len:
            return answer
        elif len(answer) < min_len:
            print(f"Invalid input. Answer needs to be longer than {min_len} characters.")
        elif len(answer) > max_len:
            print(f"Invalid input. Answer needs to be shorter than {max_len} characters.")


# encrypts the text
def encrypt(alphabet, text, shift):
    result = ""
    alphabet_length = len(alphabet)
    text = text.lower()
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

# decrypts the text
def decrypt(alphabet, text, shift):
    shift = shift - shift * 2
    result = ""
    alphabet_length = len(alphabet)
    text = text.lower()

    for char in text:
        if char in alphabet:
            old_index = alphabet.index(char)
            new_index = (old_index + shift) % alphabet_length
            result += alphabet[new_index]
        else:
            result += char

    return result

def final_output(shift, text, changed_text, method):
    message = f"The text '{text}' was encrypted successfully using a shift of {shift}. \nThe result is '{changed_text}'."

    # Print the message
    print(message)


methods = {
        "A": "encrypt",
        "B": "decrypt",
}
alphabet = "abcdefghijklmnopqrxtuvwxyz"

while True:
    title()
    print("")
    instructions()
    print("")
    method = method_checker(methods)
    print("")
    shift = int_check("Please enter the shift / key: ", 0, 26)
    print("")
    text = string_checker("What do you want to encrypt? ", 100, 1)
    print("")
    if method == "encrypt":
        changed_text = encrypt(alphabet, text, shift)
    elif method == "decrypt":
        changed_text = decrypt(alphabet, text, shift)
    final_output(shift, text, changed_text, method)
    print("")
    restart = yes_no("Do you want to restart? ")
    print("")
    if restart == "yes":
        pass
    elif restart == "no":
        break

