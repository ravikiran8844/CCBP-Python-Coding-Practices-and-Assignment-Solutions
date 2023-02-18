# All Possible Subsets


# Given a sentence as input, print all the unique combinations of the words of the sentence, considering different possible number of words each time (from one word to N unique words in lexicographical order).

def all_unique_combinations(words):
    words = sorted(words)
    items = list(range(len(words)))
    old_combinations = [[]]
    new_combinations = []
    new_combinations_set = []
    for i in range(len(words)):
        new_combinations = []
        for combination in old_combinations:
            for item in items:
                if (combination and item > combination[-1]) or len(combination) == 0:
                    new_combinations.append(combination + [item])
            old_combinations = new_combinations
            word_combinations = []
        for combination in new_combinations:
            word_combination = []
            for index in combination:
                word_combination.append(words[index])
            word_combinations.append(tuple(word_combination))
        new_combinations_set.append((sorted(tuple(word_combinations))))

    new_combinations_set.sort()
    for i in new_combinations_set:
        for j in sorted(set(i)):
            print(*j)


words = input().split()
all_unique_combinations(words)


# Coding Solutions Youtube Channel
