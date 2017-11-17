# This is the code that you will need to debug, test and
# fix the style of for Project 9 Part B.

# This program reads in data about the Scottish Independence
# referendum and outputs data about each shire's votes
# It then outputs the result of the referendum and
# What percentage voted for independence in each shire


def main():
    file = open("voting.txt")
    Lines = file.readlines()
    Lines = lines.split()

    votes = 0
    count = 0
    countAll = 0
    for m in range(16):
        line = lines[m].split()
        for v in line:
            if v == 'a':
                countAll += 1
            elif v == 'y':
                countAll += 1
                count += 1
            else:
                countAll += 1

        print("percentage:" + (str(count / countAl))

    print("Overall there were ", (count / countAll), "  yes votes")

main()
