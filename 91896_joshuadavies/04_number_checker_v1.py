#checks if a number is within a certain range
def int_check(question, low_num, high_num):

    error = "Please enter a whole number between {} " \
            "and {}".format(low_num, high_num)

    valid = False
    while not valid:

        # ask user for number and check it is valid
        try:
            key = int(input(question))

            if low_num <= key <= high_num:
                return key
            else:
                print(error)

        # if an integer is not entered, display an error message
        except ValueError:
            print(error)

while True:
    print(int_check("Key:",0, 26))