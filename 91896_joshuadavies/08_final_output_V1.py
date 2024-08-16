def final_output(shift, text, changed_text, method):
    message = f"The text '{text}' was encrypted successfully using a shift of {shift}. \nThe result is '{changed_text}'."

    # Print the message
    print(message)


# Example usage
shift = 2
text = "hello"
changed_text = "jgnnq"
method = "encrypt"

final_output(shift, text, changed_text, method)
