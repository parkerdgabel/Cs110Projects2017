# const for the width of the totem.
SIZE = 3


def nose(char, spaces=" "):
    print("|" + (spaces * (SIZE - 2)) + char +
          " " + char + (spaces * (SIZE - 2)) + "|")


def leading_whitespaces(num):
    return " " * num


def slash_line():
    return (("\\" * 4) + ("/" * 4))


def eyes(edges, inner):
    return edges + ((SIZE - 3) * " ") + inner + ((SIZE - 3) * " ") + edges


def mouth_1():
    return "\\(__)/"


def arrow_line():
    return (">" * SIZE) + ("<" * SIZE)


def print_face_1():
    print(slash_line())
    print(eyes_1())
    print()


def dec(num):
    num = int(num) - 1
    return num


def numbers():
    s = [7, 8, 9, 9, 8, 7]

    def numbers_closure():
        nonlocal s
        s = list(map(dec, s))
        s = list(map(str, s))
        s = "".join(s)
        return s
    return numbers_closure
