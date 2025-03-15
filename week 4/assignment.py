#Classwork 1

def sum_of_odd_numbers(numbers_list):
  odd_numbers = list(filter(lambda x: x % 2 != 0, numbers_list))
  return sum(odd_numbers)
numbers = [3, 4, 77, 65, 54, 22, 33, 19, 23, 19]
result = sum_of_odd_numbers(numbers)
print(f"The sum of odd numbers: {result}")

#Classwork 2

word_count = 0
with open("sayuz.txt", "r") as file:
  for line in file:
    words = line.split()
    word_count += len(words)
print(f"Word Count Equals: {word_count}")

#Classwork 3

def read_file(file_path):
  try:
    with open(file_path, "r") as file:
      content = file.read()
      return content
  except FileNotFoundError:
    print("No files found")
  except PermissionError:
    print("Denied permission")
  except Exception as e:
    print(f"Error: {e}")
file_path = "hello.txt"
content = read_file(file_path)
print(f"The file content is: {content}")

#Question 1

def read_file_content(file_path):
    with open(file_path, "r") as file:
      content = file.read()
    return content

def write_to_file(file_path, content):
    with open(file_path, 'w') as file:
      file.write(content)

file_path = "mmm.txt"
write_to_file(file_path, "I am coming")
content = read_file_content(file_path)
print(f"Content of the file: {content}")

#Question 2

import re
def find_longest_word(file_path):
    with open(file_path, "r") as file:
        content = file.read()
        print(f"The content of file: {content}")
        words = re.findall(r'\b\w+\b', content)
        print(f"extracted words: {words}")

        if not words:
            return "No words"

        longest_word = max(words, key=len)
        print(f"The longest word: {longest_word}")
        return longest_word


file_path = "sayuz.txt"
longest_word = find_longest_word(file_path)
print(f"Longest word: {longest_word}")

#Question 3

import os
def check_file_empty(file_path):
  try:
    return os.path.getsize(file_path) == 0
  except FileNotFoundError:
    print("File not found.")
    return False
  except Exception as e:
    print(f"Error: {e}")
    return False

file_path = "sayuz.txt"
is_empty = check_file_empty(file_path)
print(f"Is the file empty? {is_empty}")

#Question 4

def reverse_file_content(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            print(f"Original content: {content}")
        reversed_content = content[::-1]
        print(f"Reversed content: {reversed_content}")
        with open("reversed.txt", "w") as reversed_file:
            reversed_file.write(reversed_content)
        print("The content has been reversed and written to 'reversed.txt'.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")


file_path = "hello.txt"
reverse_file_content(file_path)

#Question 5

def convert_to_uppercase():
  strings_input = str(input("Enter list of strings: "))
  strings_list = strings_input.split(",")
  uppercase_strings = list(map(lambda s: s.strip().upper(), strings_list))
  return uppercase_strings

uppercase_strings = convert_to_uppercase()
print(f"uppercase strings are: {uppercase_strings}")

#Question 6

def filter_even_length_words():
  words_input = input("Enter list of words: ")
  words_list = words_input.split(",")
  even_length_words = list(filter(lambda word: len(word.strip()) % 2 == 0, words_list))
  return even_length_words

even_length_words = filter_even_length_words()
print(f"The words with even length: {even_length_words}")

#Question 7

def process_file_with_lambda(file_path):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
        processed_lines = [' '.join(map(lambda word: word.upper(), line.split())) for line in lines]
        print("the processed content: ")
        print(processed_lines)
        with open(file_path, "w") as file:
            file.writelines(processed_lines)
        print(f"The file '{file_path}' has been processed and updated.")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error has occurred: {e}")

file_path = "hi.txt"
process_file_with_lambda(file_path)