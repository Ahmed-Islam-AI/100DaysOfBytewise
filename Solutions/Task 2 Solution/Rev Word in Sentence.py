def reverse_words(sentence):
    # Split the sentence into words
    words = sentence.split()
    # Reverse the list of words
    reversed_words = words[::-1]
    # Join the reversed words back into a single string
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

# Example usage
input_sentence = "The quick brown fox jumps over the lazy dog."
output_sentence = reverse_words(input_sentence)
print(output_sentence)
