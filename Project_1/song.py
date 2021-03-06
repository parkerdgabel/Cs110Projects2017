# Parker Gabel, CSc 110, Autumn 2017, Section 1B
# Programming Assignment #1, 06/07/49
#
# This program's behavior is to add verses to a song by using functions.


def very_first_line():
    "First line ends in a period."
    return "There was an old woman who swallowed a fly.\n"


def print_very_first_line():
    print(very_first_line())


def first_line(animal):
    """Returns a string that is the first line of the song.
       Parameter: animal string
                  animal is the string that is formatted
                  and added to the line."""
    return "There was an old woman who swallowed a {},\n".format(animal)


def verse_ending():
    """Returns a string that is the last couplet of the song."""
    return "I don't know why she swallowed that fly,\nPerhaps she'll die.\n"


def swallow_line(larger, smaller):
    """Returns a string of the repeated swallow line.
       Parameters: larger string
                   smaller string"""
    return "She swallowed the {0} to catch the {1},\n".format(larger, smaller)


def verse_1():
    """Returns the first verse in a string."""
    return very_first_line() + verse_ending()


def print_verse_1():
    """Prints the first verse"""
    print(verse_1())


def verse_2():
    """Returns the second verse in a string."""
    return first_line("spider") + "That wriggled and iggled and jiggled inside her.\n" + swallow_line("spider", "fly") + verse_ending()


def print_verse_2():
    """Prints the second verse"""
    print(verse_2())


def verse_3():
    """Returns the third verse in a string."""
    return first_line("bird") + "How absurd to swallow a bird.\n" + swallow_line("bird", "spider") + swallow_line("spider", "fly") + verse_ending()


def print_verse_3():
    """Prints the third verse"""
    print(verse_3())


def verse_4():
    """Returns the fourth verse in a string."""
    return first_line("cat") + "Imagine that to swallow a cat.\n" + swallow_line("cat", "bird") + swallow_line("bird", "spider") + swallow_line("spider", "fly") + verse_ending()


def print_verse_4():
    """Prints the fourth verse"""
    print(verse_4())


def verse_5():
    """Returns the fifth verse in a string."""
    return first_line("dog") + "What a hog to swallow a dog.\n" + swallow_line("dog", "cat") + swallow_line("cat", "bird") + swallow_line("bird", "spider") + swallow_line("spider", "fly") + verse_ending()


def print_verse_5():
    """Prints the fifth verse"""
    print(verse_5())


def verse_6():
    """Returns the sixth verse."""
    return first_line("boar") + "She ate it but still wanted more.\n" + swallow_line("boar", "dog") + swallow_line("dog", "cat") + swallow_line("cat", "bird") + swallow_line("bird", "spider") + swallow_line("spider", "fly") + verse_ending()


def print_verse_6():
    """Prints the sixth verse."""
    print(verse_6())


def final_lines():
    """Returns the last lines of the song."""
    return "There was an old woman who swallowed a horse,\nShe died of course."


def print_final_lines():
    """Prints the last lines of the song."""
    print(final_lines())


def print_song():
    """Prints the entire song"""
    print_verse_1()
    print_verse_2()
    print_verse_3()
    print_verse_4()
    print_verse_5()
    print_verse_6()
    print_final_lines()


def main():
    print_song()


main()
