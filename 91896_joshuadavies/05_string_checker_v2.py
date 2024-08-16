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

while True:
    string_checker("What do you want to encrypt? ", 100, 1)
    print("program continues...")