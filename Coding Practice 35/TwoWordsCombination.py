# Two Words Combination

# Given a sentence as input, print all the unique combinations of two words in lexicographical order.

words = input().split()
words.sort()
comibinationList = []
for i in range(len(words)):
    for j in range(i+1, len(words)):
        twoWords = words[i]+" "+words[j]
        comibinationList.append(twoWords)
uniques = set(comibinationList)
uniques = list(uniques)
uniques.sort()
for i in uniques:
    print(i)


# Coding Solutions Youtube Channel
