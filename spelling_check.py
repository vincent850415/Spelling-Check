with open('dictionary.txt', 'r') as file:
    dictionary = file.readlines()


def LevenshteinDistance(s, t):
    LD = {}

    for i in range(len(s)+1):
        LD[i,0] = i

    for j in range(len(t)+1):
        LD[0,j] = j

    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):

            cost = 0 \
                if s[i-1] == t[j-1] \
                else 1

            LD[i,j] = min(LD[i, j-1] + 1, LD[i-1, j] + 1, LD[i-1, j-1] + cost)

    return LD[i,j]


input_word = input("Please enter a word : ")
string = input_word.strip()
decide = 1


for line in dictionary:
     if LevenshteinDistance(string,line.strip()) == 0:
            print("Input match Dictionary : ",string)
            decide=0


if decide == 1:
    print("Input not match Dictionary")
    for line in dictionary:
        if LevenshteinDistance(string,line.strip()) == 1:
            print("Similar word : ", line.strip(), " Distance : ", LevenshteinDistance(string, line.strip()))
    for line in dictionary:
        if LevenshteinDistance(string,line.strip()) == 2:
            print("Similar word : ", line.strip(), " Distance : ", LevenshteinDistance(string, line.strip()))
    for line in dictionary:
        if LevenshteinDistance(string,line.strip()) == 3:
            print("Similar word : ", line.strip(), " Distance : ", LevenshteinDistance(string, line.strip()))