# Three Words Combination

# Given a sentence as input, print all the unique combinations of three words in lexicographical order.

words = input().split()
words.sort()
combinations = []
for i in range(len(words)):
    for j in range(i+1, len(words)):
        for k in range(j+1, len(words)):
            threeWords = words[i]+" "+words[j]+" "+words[k]
            combinations.append(threeWords)
uniques = set(combinations)
uniques = list(uniques)
uniques.sort()
for i in uniques:
    print(i)


# Coding Solutions Youtube Channel
