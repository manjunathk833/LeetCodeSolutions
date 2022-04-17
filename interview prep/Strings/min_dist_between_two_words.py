# function to calculate the minimum
# distance between w1 and w2 in s

def distance(s, w1, w2):
    if w1 == w2:
        return 0

    # get individual words in a list
    words = s.split(" ")

    # assume total length of the string as
    # minimum distance
    min_dist = len(words) + 1

    # traverse through the entire string
    for index in range(len(words)):

        if words[index] == w1:
            for search in range(len(words)):

                if words[search] == w2:

                    # the distance between the words is
                    # the index of the first word - the
                    # current word index
                    curr = abs(index - search) - 1;

                    # comparing current distance with
                    # the previously assumed distance
                    if curr < min_dist:
                        min_dist = curr

    # w1 and w2 are same and adjacent
    return min_dist


# Driver code
s = "geeks for geeks contribute practice"
w1 = "geeks"
w2 = "practice"
print(distance(s, w1, w2))
