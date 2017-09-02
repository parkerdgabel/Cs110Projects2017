import totem


def test_leading_whitespace():
    assert totem.leading_whitespaces(1) == " "
    assert totem.leading_whitespaces(2) == "  "


def test_slash_line():
    assert totem.backslash_line() == "\\\\\\\\////"


def test_hairline():
    assert totem.hairline("|") == "||||||"
    assert totem.hairline("/") == "//////"


def test_eyes():
    assert totem.eyes("|", ".)(.") == "|.)(.|"


def test_mouth_1():
    assert totem.mouth_1() == "\\(__)/"


def test_arrow_line():
    assert ">>><<<" == totem.arrow_line()
