class Solution(object):
    def reverseWords(self, s):
        # Split the input string into words
        split_words = s.split()

        # Initialize an empty list to store reversed words
        reversed_words = []

        # Iterate through each word in the split string
        for i in range(len(split_words)):
            # Reverse the characters of each word
            inverse = split_words[i][::-1]

            # Append the reversed word to the list
            reversed_words.append(inverse)

        # Join the reversed words back together with whitespace
        reversed_string = " ".join(reversed_words)

        # Return the final reversed string
        return reversed_string
