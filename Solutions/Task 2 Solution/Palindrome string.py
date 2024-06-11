def is_palindrome_sentence(sentence):
    cleaned_sentence = ''.join(c.lower() for c in sentence if c.isalnum())
    return cleaned_sentence == cleaned_sentence[::-1]

input_sentence = input("Enter a sentence: ")
if is_palindrome_sentence(input_sentence):
    print(f"{input_sentence} is a palindrome.")
else:
    print(f"{input_sentence} is not a palindrome.")
