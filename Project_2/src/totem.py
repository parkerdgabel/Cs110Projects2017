
# const for the width of the totem.
SIZE = 3


def nose(left_char, right_char, spaces=" "):
    """Generic function to print totem noses."""

    s = "|" + (spaces * (SIZE - 2)) + left_char
    s = s + right_char + (spaces * (SIZE - 2)) + "|"
    return s


def leading_whitespaces(num):

    return " " * num


def backslash_line():
    "Generic function for the top line of the totem."
    return (("\\" * (SIZE + 1)) + ("/" * (SIZE + 1)))


def hairline(char):
    return char * (SIZE * 2)


def eyes(edges_left, inner, edges_right="|"):
    return edges_left + ((SIZE - 3) * " ") + inner + ((SIZE - 3) * " ") + edges_right


def mouth_1():
    return "\\" + ((SIZE - 3) * " ") + "(__)" + ((SIZE - 3) * " ") + "/"


def arrow_line():
    return (">" * SIZE) + ("<" * SIZE)


def print_face_1():
    print(leading_whitespaces(7) + backslash_line())
    print(leading_whitespaces(8) + eyes("|", ".)(."))
    print(leading_whitespaces(8) + nose("|", "|"))
    print(leading_whitespaces(8) + mouth_1())


def print_oh_guy():
    print(leading_whitespaces(8) + hairline("\\"))
    print(leading_whitespaces(8) + eyes())
    print(leading_whitespaces(8) + nose("/", "\\"))


# def numbers():
   # for i in range():
print_face_1()
print_oh_guy()
