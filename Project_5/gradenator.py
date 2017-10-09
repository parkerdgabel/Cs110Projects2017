# Parker Gabel, CSc 110, Autumn 2017, Section 1B
# Programming Assignment #5, 09/21/17
#
# This program's behavior is to grade students score for the semester.


def main():
    introduction()
    grade = test_1_query()
    grade += test_2_query()
    grade += final_query()
    grade += homework()
    grade += quizzes()
    grade += daily_homework()
    conclusion(round(grade, 1))


def introduction():
    """introduction simply prints the intro."""
    print("This program reads exam/homework scores")
    print("and reports your overall course grade.")
    print()


def query_test_scores(num):
    """query_test_scores colletcs and computes to score for student's tests."""
    if num > 2:
        print("Final :")
    else:
        print("Midterm ", num, ":")
    weight = int(input("Weight (0-100)? "))

    score = int(input("Score earned? "))
    shifted = int(input("Were scores shifted (1=yes, 2=no)? "))
    if shifted != 2:
        shifted = int(input("Shift amount? "))
        score = min(100, score + shifted)
    print("Total points = ", score, " / ", 100)
    score = round((score / 100) * weight, 1)
    print("Weighted score = ", score, " / ", weight)
    print()
    return score


def test_1_query():
    """query first test score."""
    return query_test_scores(1)


def test_2_query():
    """query second test score."""
    return query_test_scores(2)


def final_query():
    """query final test score."""
    return query_test_scores(3)


def homework():
    """homework colletcs and computes to score for student's homework."""
    print("Homework:")
    weight = int(input("Weight (0 - 100)? "))

    assignments = int(input("Number of assignments? "))
    total = 0
    score = 0
    for i in range(1, assignments + 1):
        assignNum = "Assignment " + str(i) + " score? "
        assignMax = "Assignment " + str(i) + " max? "
        score += int(input(assignNum))
        total += int(input(assignMax))
    sections = int(input("How many sections did you attend? "))
    sections *= 3
    print("Section points = ", sections, " / ", 37)
    total += 37
    score += sections
    print("Total points = ", score, " / ", total)
    score = round((score / total) * weight, 1)
    score = round(min(score, total), 1)
    print("Weighted score = ", score, " / ", weight)
    print()
    return score


def quizzes():
    """quizzes colletcs and computes to score for student's quizzes."""
    print("Quizzes:")
    weight = int(input("Weight (0 - 100)? "))
    score = int(input("Total points earned? "))
    total = int(input("Total points possible? "))
    print("Total points = ", score, " / ", total)
    score = round((score / total) * weight, 1)
    score = min(score, total)
    print("Weighted score = ", score, " / ", weight)
    print()
    return score


def daily_homework():
    """daily_homework colletcs and computes to score for student's daily homework."""
    print("Daily homework:")
    weight = int(input("Weight (0 - 100)? "))

    score = int(input("Total points earned? "))
    total = int(input("Total points possible? "))
    print("Total points = ", score, " / ", total)
    score = round(min((score / total) * weight, total), 1)
    print("Weighted score = ", score, " / ", weight)
    print()
    return score


def letter_grade(grade):
    """letter_grade returns the proper letter grade.
       Parameter: grade float students final grade."""
    if grade > 89.99:
        return "A"
    elif grade > 79.99:
        return "B"
    elif grade > 69.99:
        return "C"
    elif grade > 59.99:
        return "D"
    return "F"


def creative_message(grade):
    """creative_message prints my unique message.
       Parameters: grade float students final grade."""
    if grade > 89.99:
        return "Don't get complacent."
    elif grade > 79.99:
        return "Great Job!"
    elif grade > 69.99:
        return "You'll pass the class but you can do better."
    elif grade > 59.99:
        return "Better luck next semester. You can do it. I believe in you."
    else:
        return "Aww shucks..."


def conclusion(grade):
    """Conclusion simply prints the conclusion Message
       Parameters: grade float students final grade"""
    print("Overall percentage = ", grade)
    print("Your grade will be at least: ", letter_grade(grade))
    print(creative_message(grade))


main()
