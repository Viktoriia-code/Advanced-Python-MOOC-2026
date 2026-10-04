
def balanced_brackets(my_string: str):
    # Remove characters that are not brackets
    my_string = "".join(char for char in my_string if char in "()[]")

    if len(my_string) == 0:
        return True
    if my_string[0] == '(' and my_string[-1] != ')':
        return False
    if my_string[0] == '[' and my_string[-1] != ']':
        return False
    if my_string[0] == ')' or my_string[0] == ']':
        return False

    # remove first and last character
    return balanced_brackets(my_string[1:-1])