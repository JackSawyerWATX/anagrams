def are_anagrams(word1, word2):
    # convert the words to lowercase and removes whitespace
    word1 = word1.lower().replace(" ", "")
    word2 = word2.lower().replace(" ", "")

    # Checks both sorted strings if they are equal
    return sorted(word1) == sorted(word2)


# asks user for two inputs for comparison
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

# returns the result if words are or are not anagrams
if are_anagrams(word1, word2):
    print("These two words are anagrams.")
else:
    print("These words are NOT anagrams.")
