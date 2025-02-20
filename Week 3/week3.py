# Question 1: Count vowels in a string

def count_vowels(text):
    vowel_set = {'a', 'e', 'i', 'o', 'u'}
    text = text.lower()
    return sum(1 for char in text if char in vowel_set)

user_input = input("Enter a string: ")
print(f"Total vowels: {count_vowels(user_input)}")

# Question 2: Find the maximum number in a list

def find_largest(lst):
    if not lst:
        return None
    max_value = lst[0]
    for num in lst:
        if num > max_value:
            max_value = num
    return max_value

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
result = find_largest(numbers)
print(f"Largest number: {result}" if result is not None else "List is empty.")

# Question 3: Print multiplication table of a number

def generate_multiplication_table(num):
    for multiplier in range(1, 11):
        print(f"{num} x {multiplier} = {num * multiplier}")

number = int(input("Enter a number: "))
generate_multiplication_table(number)


# Question 4: Find the longest word in a sentence

def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len, default="")

sentence_input = input("Enter a sentence: ")
print(f"Longest word: {longest_word(sentence_input)}")


# Question 5: Compute the sum of all numbers in a list

def list_sum(elements):
    return sum(elements)

values = list(map(int, input("Enter numbers separated by spaces: ").split()))
print(f"Sum of numbers: {list_sum(values)}")


# Question 6: Convert a sentence to title case

def to_proper_case(sentence):
    return ' '.join(word.capitalize() for word in sentence.split())

text = input("Enter a sentence: ")
print(f"Title Case: {to_proper_case(text)}")


# Question 7: Check if a word is a palindrome

def check_palindrome(word):
    clean_word = word.lower()
    return clean_word == clean_word[::-1]

word_input = input("Enter a word: ")
print(f"Is Palindrome? {check_palindrome(word_input)}")


# Question 8: Count character frequency in a string

def character_frequency(text):
    frequency = {}
    for character in text:
        frequency[character] = frequency.get(character, 0) + 1
    return frequency

string_input = input("Enter a string: ")
print(f"Character counts: {character_frequency(string_input)}")