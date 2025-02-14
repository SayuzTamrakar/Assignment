#question 1
def process_numbers(numbers):
    for num in numbers:
        if num > 50:
            break
        if num % 5 == 0:
            continue
        print(num)

# Example usage
numbers_list = [12, 25, 33, 45, 50, 38, 52, 48, 60]
process_numbers(numbers_list)



#question 2

user_password = input("Enter your password: ")


if len(user_password) < 6 or user_password.isalpha():
    print("Weak")
elif len(user_password) >= 6 and user_password.isalnum():
    print("Moderate")
elif len(user_password) >= 8 and any(ch in "!@#$%^&*" for ch in user_password):
    print("Strong")
else:
    print("Moderate")



#question 3

sentence_input = input("Enter a sentence: ")

words_list = sentence_input.split()


modified_words = [word[::-1] if index % 2 else word for index, word in enumerate(words_list)]


final_sentence = " ".join(modified_words)
print("Modified sentence:", final_sentence)



#question 4
words_data = ["apple", "apple", "pea", "banana", "pea", "pea"]

word_count = {}
for item in words_data:
    word_count[item] = word_count.get(item, 0) + 1


duplicates_found = {key: val for key, val in word_count.items() if val > 1}
print(duplicates_found)



#question 5
library_books = {
    'BookA': 5,
    'BookB': 3,
    'BookC': 7,
    'BookD': 10,
    'BookE': 2
}
print(library_books)



#question 6
book_inventory = {
    'bookA': 7,
    'bookB': 4,
    'bookC': 10,
    'bookD': 5,
    'bookE': 6
}

if book_choice in book_inventory:
    while True:
        try:
            order_number = int(input("Number of copies you want: "))
            break
        except ValueError:
            print("Please enter a numeric value.")
    
    available_stock = book_inventory[book_choice]
    if order_number <= available_stock:
        print("The book is available.")
    else:
        print("Only", available_stock, "copies available.")
else:
    print("Sorry, the book is not available.")
requested_book = input("Enter the book name: ")



#question 7
word_list_input = input("Enter words separated by spaces: ").split()

word_frequency = {}


for single_word in word_list_input:
    formatted_word = single_word.lower()
    word_frequency[formatted_word] = word_frequency.get(formatted_word, 0) + 1

print("Word Frequency:", word_frequency)

#question 2