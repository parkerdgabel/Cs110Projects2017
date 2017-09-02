
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

def owl_hair():
    return eyes("|", "-..-")

def owl_eyes():
    return eyes("|", "0\\/0")

def left_wing_top():
    return ".----\\"

def right_wing_top():
    return "/----."

def owl_top_part_of_wings():
    return leading_whitespaces(3) + left_wing_top() + ((SIZE - 1) * " ") + ((SIZE - 1) * " ") + right_wing_top()

def owl_wings_middle_part__left_1():
    return "/ / / "

def owl_wings_middle_part__right_1():
    return " \\ \\ \\"


def owl_body_middle(char):
    return "|" + ((SIZE - 1) * char) + ((SIZE - 1) * char) + "|"

def owl_middle_part_1(char):
    return owl_wings_middle_part__left_1() + owl_body_middle(char) + owl_wings_middle_part__right_1()

def owl_wings_middle_part__left_2():
    return "/ / / /"

def owl_wings_middle_part__right_2():
    return " \\ \\ \\ \\"

def owl_middle_part_2(char):
    return owl_wings_middle_part__left_2() + owl_body_middle(char) + owl_wings_middle_part__right_2()


def print_owl():
    print(leading_whitespaces(8) + owl_hair())
    print(leading_whitespaces(8) + owl_eyes())
    print(owl_top_part_of_wings())
    print(leading_whitespaces(2) + owl_middle_part_1("~"))
    print(leading_whitespaces(1) + owl_middle_part_2(":"))
def mouth_1():
    return "\\" + ((SIZE - 3) * " ") + "(__)" + ((SIZE - 3) * " ") + "/"

def oh_mouth():
    return "(" + ((SIZE - 2) * " ") + "()" + ((SIZE - 2) * " ") + ")"

def oh_guy_eyes():
    return "(0)" + ((SIZE - 3) * " ") + ((SIZE - 3) * " ") + "(0)"

def arrow_line():
    return (">" * SIZE) + ("<" * SIZE)


def print_face_1():
    print(leading_whitespaces(7) + backslash_line())
    print(leading_whitespaces(8) + eyes("|", ".)(."))
    print(leading_whitespaces(8) + nose("|", "|"))
    print(leading_whitespaces(8) + mouth_1())


def print_oh_guy():
    print(leading_whitespaces(8) + hairline("\\"))
    print(leading_whitespaces(8) + oh_guy_eyes())
    print(leading_whitespaces(8) + nose("/", "\\"))
    print(leading_whitespaces(8)+ oh_mouth())

# def numbers():
   # for i in range():
print_face_1()
print_oh_guy()
print_owl()
