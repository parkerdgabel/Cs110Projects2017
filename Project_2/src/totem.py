
# const for the width of the totem.
SIZE = 6


def nose(left_char, right_char, spaces=" "):
    """Generic function to print totem noses."""

    s = "|" + (spaces * (SIZE - 2)) + left_char
    s = s + right_char + (spaces * (SIZE - 2)) + "|"
    return s


def leading_whitespaces(num):
    """Prints leading whitespaces."""
    return " " * num


def backslash_line():
    """Returns the hair for the first totem."""
    return (("\\" * (SIZE + 1)) + ("/" * (SIZE + 1)))


def hairline(char):
    """Generic function for the top line of the totem."""
    return char * (SIZE * 2)


def eyes(edges_left, inner, edges_right="|"):
    """Generic Function to print the eyes for the totems."""
    return edges_left + ((SIZE - 3) * " ") + inner + ((SIZE - 3) * " ") + edges_right

def owl_hair():
    """Returns the owl's hair."""
    return eyes("|", "-..-")

def owl_eyes():
    """Returns the owls eyes."""
    return eyes("|", "0\\/0")

def left_wing_top():
    """Returns the owls top part of the left wing."""
    return ".----\\"

def left_wing_top_folded():
    """Returns the owls top part of the left wing that is folded."""
    return "(\\"

def right_wing_top():
    """Returns the owls top part of the right wing."""
    return "/----."

def right_wing_top_folded():
    """Returns the owls top part of the right wing that is folded."""
    return "/)"

def owl_top_part_of_wings():
    """Returns the const scaled top portion to the wings."""
    return leading_whitespaces(3) + left_wing_top() + ((SIZE - 1) * " ") + ((SIZE - 1) * " ") + right_wing_top()

def owl_top_part_of_wings_folded():
    """Returns the const scaled top portion to the wings that is folded."""
    return leading_whitespaces(7) + left_wing_top_folded() + ((SIZE - 1) * " ") + ((SIZE - 1) * " ") + right_wing_top_folded()

def owl_wings_middle_part_left_1():
    """Returns the first left-middle part of the wing."""
    return "/ / / "

def owl_wings_middle_part_left_1_folded():
    """Returns the first left-middle part of the wing that is folded."""
    return "( "

def owl_wings_middle_part_right_1():
    """Returns the first right-middle part of the wing."""
    return " \\ \\ \\"

def owl_wings_middle_part_right_1_folded():
    """Returns the first right-middle part of the wing that is folded."""
    return " )"

def owl_body_middle(char):
    """Returns the first part of the midle of the owl's body."""
    return "|" + ((SIZE - 1) * char) + ((SIZE - 1) * char) + "|"

def owl_middle_part_1(char):
    """Returns the entire first middle portion of the owl."""
    return owl_wings_middle_part_left_1() + owl_body_middle(char) + owl_wings_middle_part_right_1()

def owl_middle_part_1_folded(char):
    """Returns the entire first middle portion of the owl that is folded."""
    return owl_wings_middle_part_left_1_folded() + owl_body_middle(char) + owl_wings_middle_part_right_1_folded()

def owl_wings_middle_part_left_2():
    """Returns the second left-middle part of the wing."""
    return "/ / / /"

def owl_wings_middle_part_right_2():
    """Returns the second right-middle part of the wing."""
    return "\\ \\ \\ \\"

def owl_middle_part_2(char):
    return owl_wings_middle_part_left_2() + owl_body_middle(char) + owl_wings_middle_part_right_2()

def owl_wings_bottom_left():
    return "'-'-'-'-"

def owl_wings_bottom_right():
    return "-'-'-'-'"

def owl_wings_bottom(char):
    return owl_wings_bottom_left() + owl_body_middle(char) + owl_wings_bottom_right()

def owl_tail():
    return (SIZE * "(") + "^^" + (SIZE * ")")

def owl_feet():
    return "T" + ((SIZE - 2) * " ") + ((SIZE - 2) * " ") + "T"

def cat_ears():
    return "/\\" + ((SIZE - 2) * "-") + ((SIZE - 2) * "-") + "/\\"

def cat_eyes():
    return "(" + ((SIZE - 2) * " ") + ".  ." + ((SIZE - 2) * " ") + ")"

def print_cat():
    print(leading_whitespaces(8) + cat_ears())
    print(leading_whitespaces(7) + cat_eyes())
    
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

def print_owl():
    print(leading_whitespaces(8) + owl_hair())
    print(leading_whitespaces(8) + owl_eyes())
    print(owl_top_part_of_wings())
    print(leading_whitespaces(2) + owl_middle_part_1("~"))
    print(leading_whitespaces(1) + owl_middle_part_2(":"))
    print(owl_wings_bottom(":"))
    print(leading_whitespaces(7) + owl_tail())

def print_forward_slash_hair_guy():
    print(leading_whitespaces(8) + hairline("/"))
    print(leading_whitespaces(8) + eyes("|", ".)(."))
    print(leading_whitespaces(8) + nose("|", "|"))
    print(leading_whitespaces(8) + mouth_1())

def print_owl_with_folded_wings():
    print(leading_whitespaces(8) + owl_hair())
    print(leading_whitespaces(8) + owl_eyes())
    print(owl_top_part_of_wings_folded())
    print(leading_whitespaces(6) + owl_middle_part_1_folded("v"))
    print(leading_whitespaces(6) + owl_middle_part_1_folded("v"))
    print(leading_whitespaces(9) + owl_feet())
# def numbers():
   # for i in range():
print_face_1()
print_oh_guy()
print_owl()
print_forward_slash_hair_guy()
print_cat()
print_owl_with_folded_wings()
