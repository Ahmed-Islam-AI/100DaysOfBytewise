def is_palindrome(word):
    # Remove spaces and convert to lowercase
    cleaned_word = word.lower().replace(" ", "")
    # Check if the cleaned word is equal to its reverse
    if cleaned_word == cleaned_word[::-1]:
        return f"{word} is a palindrome."
    else:
        return f"{word} is not a palindrome."

# Example usage
input_word = input("Enter a word: ")
print(is_palindrome(input_word))
