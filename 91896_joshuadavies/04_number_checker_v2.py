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
while True:
    print(int_check("Please enter the shift / key: ", 0, 26))