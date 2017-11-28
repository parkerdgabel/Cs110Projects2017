# Parker Gabel, CSc 110, Autumn 2017, Section 1B
# Programming Assignment #11, 11/21/17
# This program learns to asses the sentiment of a body of text
POSITIVE = "positive"
NEGATIVE = "negative"
NEUTRAL = "neutral"


def main():
    name = query_training_file_name()
    infile = open(name)
    data = infile.read()
    counts = build_counts(data)
    scores = build_keys_for_score(counts)
    scores = build_scores(data, scores)
    learned = build_learned_dict(scores, counts)
    infile.close()
    done = False
    while not done:
        print("What would you like to do?")
        present_options()
        response = query_user_response()
        if len(response) > 1:
            pass
        elif not(ord("0") <= ord(response) <= ord("5")):
            pass
        elif ord("1") == ord(response):
            word = query_word()
            query_score(word, learned)
        elif ord("2") == ord(response):
            input_data = query_file_and_get_words()
            average = compute_average(input_data, learned)
            print(input_data, "is", positive_or_negative(average))
            yes_or_no = input("Am I right (yes/no)? ")
            if yes_or_no.lower()[0] == "n":
                print("What score should this sentence have ", end="")
                ans = int(input("(0 - 4 where 4 is the most positive)? "))
                update_counts(input_data, counts)
                update_scores(ans, input_data, scores)
                update_learned(learned, counts, scores, input_data)
                infile.close()
        elif ord("3") == ord(response):
            input_data = query_file_and_get_words()
            max_word = find_max(input_data, learned)
            min_word = find_min(input_data, learned)
            print_max_and_min(max_word, min_word, learned)
        elif ord("4") == ord(response):
            positive = open("positive.txt", 'w')
            negative = open("negative.txt", 'w')
            pos_words = get_positive_words(learned)
            neg_words = get_negative_words(learned)
            write_to_positive(positive, pos_words)
            write_to_negative(negative, neg_words)
            positive.close()
            negative.close()
        elif ord("5") == ord(response):
            done = True
        print()
    # print(counts)
    # print(scores)
    # print(learned)


def query_training_file_name():
    """Gets the input file name from user.
    Args: None
    Returns: string"""
    return input("Learning data file name: ")


def present_options():
    """Presents user with their options for the program.
    Args:   None
    Returns: None"""
    print("1: Get the score of a word")
    print("2: Get the average score of words in a file")
    print("3: Find the highest / lowest scoring words in a file")
    print("4: Sort the words in a file into positive.txt and negative.txt")
    print("5: Exit the program")


def query_user_response():
    """Gets the response from user.
    Args: None
    Returns: string"""
    return input("Enter a number 1-5: ")


def query_word():
    """Gets the input word from user.
    Args: None
    Returns: string"""
    return input("which word? ")


def build_counts(data):
    """Builds the counts dictionary.
    Args:    data string
    Returns: dict"""
    counts = {}
    words = get_words(data)
    for elem in words.split():
        if ord('a') <= ord(elem[0]) <= ord('z'):
            if elem not in counts.keys():
                counts[elem] = 1
            else:
                counts[elem] += 1
    return counts


def update_counts(data, counts):
    """Increments the counts in the counts dictionary
    Args:   data string
            counts dict
    Returns: None"""
    for elem in data.split():
        counts[elem] += 1


def update_scores(update_score, data, scores):
    """Updates the scores dictionary.
    Args:   update_score int
            data         string
            scores       dict
    Returns:None"""
    for elem in data.split():
        scores[elem] += update_score


def update_learned(learned, counts, scores, data):
    """Updates the learned library.
    Args: learned dict
          counts dict
          scores dict
          data string
    Returns: None"""
    for elem in data.split():
        learned[data] = scores[elem] / counts[elem]


def build_scores(data, scores):
    """Builds the total score for the scores dict.
    Args:    data string
             scores dict
    Returns: dict"""
    for elem in data.split('\n'):
        if len(elem) > 1:
            num = int(elem[0])
            line = get_words(elem)
            line = line[1:]
            for word in line.strip().split():
                if word in scores.keys():
                    scores[word] += num
    return scores


def build_keys_for_score(counts):
    """Copies the keys from counts to the keys of scores.
    Args:    counts dict
    Returns: dict"""
    scores = {}
    for elem in counts.keys():
        scores[elem] = 0
    return scores


def build_learned_dict(scores, counts):
    """builds a dictionary containg a words learned scores.
    Args: scores dict
          counts dict
    Returns: dict"""
    learned = {}
    for elem in scores.keys():
        learned[elem] = scores[elem] / counts[elem]
    return learned


def get_words(data):
    """Removes unnecessary characters from string.
    Args: data string
    Returns: string"""
    words = data.replace("?", "")
    words = words.replace("!", "")
    words = words.replace(".", "")
    words = words.replace(",", "")
    words = words.replace("--", " ")
    words = words.replace("\\", " ")
    words = words.replace("\\", "")
    words = words.replace("/", " ")
    words = words.replace("-", " ")
    words = words.lower()
    return words


def query_file_and_get_words():
    """Gets an input file and formats the data.
    Args: None
    Returns: string"""
    name = input("file name? ")
    infile = open(name)
    input_data = infile.read()
    return get_words(input_data).strip()


def query_score(word, learned):
    """Gets the word to be scored from user.
    Args: None
    Returns: string"""
    if word not in learned.keys():
        pass
    else:
        print("score =", learned[word])


def compute_average(input_data, learned):
    """Computes the average score of a string
    Args:  input_data string
           learned dict
    Returns: float"""
    total = 0
    for elem in input_data.split():
        total += learned[elem]
    return total / len(input_data)


def positive_or_negative(score):
    """Determines wheather a score is positive, negative, or neutral.
    Args: score float
    Returns: string"""
    if score >= 2.01:
        return POSITIVE
    elif score <= 1.99:
        return NEGATIVE
    else:
        return NEUTRAL


def find_max(data, learned):
    """Finds the max score for the input data.
    Args: data string
          learned dict
    Returns"""
    max_score = -1
    word = ""
    for elem in data.split():
        max_score = max(max_score, learned[elem])
        if max_score == learned[elem]:
            word = elem
    return word


def find_min(data, learned):
    """Finds the min score for the input data.
    Args: data string
          learned dict
    Returns"""
    min_score = 5
    word = ""
    for elem in data.split():
        if elem in learned.keys():
            min_score = min(min_score, learned[elem])
            if min_score == learned[elem]:
                word = elem
    return word


def print_max_and_min(max_word, min_word, learned):
    """Prints the max word and min word.
    Args: max_word string
          min_word string
          learned dict
    Returns: None"""
    print("Maximum score is", learned[max_word], "for", max_word)
    print("Minimum score is", learned[min_word], "for", min_word)


def get_positive_words(learned):
    """Finds all words in learned that are positive
    Args: learned dict
    Returns: list"""
    return [x for x in learned if learned[x] > 2.0]


def get_negative_words(learned):
    """Finds all words in learned that are negative
    Args: learned dict
    Returns: list"""
    return [x for x in learned if learned[x] < 2.0]


def write_to_positive(pos_file, pos_words):
    """Writes all the positive words to the positve file.
    Args: pos_file file
          pos_words list
    Returns: None"""
    for pos in pos_words:
        pos_file.write(pos + "\n")


def write_to_negative(neg_file, neg_words):
    """Writes all the negative words to the negative file.
    Args: neg_file file
          neg_words list
    Returns: None"""
    for neg in neg_words:
        neg_file.write(neg + "\n")


main()
