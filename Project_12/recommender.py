# Parker Gabel, CSc 110, Autumn 2017, Section 1B
# Programming Assignment #12, 11/27/17
# This program makes recommendations based on previous user ratings.
AVERAGES = "averages"
RECOMMEND = 'recommend'
QUIT = "quit"


def main():
    """Main function of the program.
    Args: 
        None
    Returns: 
        A+ grade on assignment."""
    ratings_file = open_ratings_file()
    lines = ratings_file.readlines()
    ratings_file.close()
    titles = build_text_list(lines)
    users = build_user_dict(lines, titles)
    update_ratings(lines, titles, users)
    average = averages(titles, users)
    average.sort()
    done = False
    prompt_user()
    while not done:
        response = input("next task? ")
        response = response.lower()
        if response == AVERAGES:
            print_averages(average)
        elif response == RECOMMEND:
            username = input("user? ")
            if username not in users.keys():
                print_averages(average)
            else:
                similar = build_similarity(username, users)
                similar.sort()
                most_similar = get_most_similar(similar)
                ratings = average_ratings(most_similar, users, titles)
                recommendations = build_recomendations_list(ratings, titles)
                print_recommendations(recommendations)
        elif response == QUIT:
            done = True
        print()


def open_ratings_file():
    """Opens the rating file.
    Args: None
    Returns: file"""
    return open("ratings.txt")


def build_text_list(lines):
    """Builds the text list.
    Args: lines list
    Returns: list"""
    titles = set()
    for i in range(1, len(lines), 3):
        titles.add(lines[i].strip())
    return list(titles)


def build_user_dict(lines, titles):
    """Builds the dictionary of user ratings.
    Args:
        lines list
        titles list
    Returns:
        dict"""
    users = {}
    for i in range(0, len(lines), 3):
        if lines[i].strip() not in users.keys():
            users[lines[i].strip()] = [0] * len(titles)
    return users


def update_ratings(lines, titles, users):
    """Udates the user dictionary ratings.
    Args:
        lines list
        titles list
        users dict
    Returns: None"""
    for i in range(0, len(lines), 3):
        elem = lines[i].strip()
        users[elem][titles.index(lines[i + 1].strip())] = int(lines[i + 2])


def prompt_user():
    """Presents the user with the menu options and gets the response.
    Args: None
    Returns: None"""
    print("Welcome to the CSC110 Book Recommender. Type the word in the")
    print("left column to do the action on the right.")
    print("recommend : recommend books for a particular user")
    print("averages : output the average ratings of all books in the system")
    print("quit : exit the program")
    print()


def __compute_average_for_book(book, titles, users):
    """Computes the average rating for a book.(helper function)
    Args:
        book string
        titles list
        users dict
    Returns:
        float"""
    total = 0
    count = 0
    for elem in users.keys():
        if users[elem][titles.index(book)] != 0:
            total += users[elem][titles.index(book)]
            count += 1
    return float(total / count)


def averages(titles, users):
    """Computes the averages for all titles.
    Args:
        titles list
        users dict
    Returns:
        list"""
    average = []
    for elem in titles:
        tup = (elem, __compute_average_for_book(elem, titles, users))
        average.append(tup)
    return average


def print_averages(average):
    """Prints the averages with the titles.
    Args:
        averages list
    Returns:
        None"""
    for elem in average:
        print(elem[0], elem[1])


def __dot_product(a_vec, b_vec):
    """Computes the dot product of two lists
    Args:
        a_vec list
        b_vec list
    Returns:
        int"""
    total = 0
    for i in range(len(a_vec)):
        total += a_vec[i] * b_vec[i]
    return total


def build_similarity(username, users):
    """Builds the similarity list
    Args:
        username string
        users dict
    Returns:
        list"""
    similar = []
    for elem in users.keys():
        if elem != username:
            similar.append((__dot_product(users[username], users[elem]), elem))
    return similar


def get_most_similar(similar):
    """Finds the 3 most similar users.
    Args:
        similar list
    Returns:
        list"""
    most_similar = []
    for _ in range(3):
        elem = similar.pop()
        most_similar.append(elem[1])
    return most_similar


def average_ratings(most_similar, users, titles):
    """Computes the average ratings among the most similar users.
    Args:
        most_similar list
        users dict
        titles list
    Returns:
        lists"""
    ratings = [0] * len(titles)
    for i in range(len(ratings)):
        count = 0
        total = 0
        for user in most_similar:
            if users[user][i] != 0:
                total += users[user][i]
                count += 1
        if count != 0:
            ratings[i] = total / count
    return ratings


def build_recomendations_list(ratings, titles):
    """Builds the final recommendations for a user.
    Args:
        ratings list
        titles list
    Returns:
        list"""
    recommendations = []
    for i in range(len(titles)):
        if ratings[i] > 0:
            recommendations.append((ratings[i], titles[i]))
    return recommendations


def print_recommendations(recommendations):
    """Prints the recommendations.
    Args:
        recommendations list
    Returns:
        None"""
    recommendations.sort()
    for _ in range(len(recommendations)):
        elem = recommendations.pop()
        print(elem[1], elem[0])


main()
