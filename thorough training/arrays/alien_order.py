def isAlienSorted(words, order):
    rank = {char: i for i, char in enumerate(order)}

    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i + 1]
        min_len = min(len(word1), len(word2))

        j = 0
        while j < min_len:
            c1 = word1[j]
            c2 = word2[j]
            if rank[c1] < rank[c2]:
                break   
            elif rank[c1] > rank[c2]:
                return False
            j += 1

        if j == min_len and len(word1) > len(word2):
            return False

    return True
