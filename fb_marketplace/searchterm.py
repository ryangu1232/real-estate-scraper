import csv

def write_word_to_csv(word):
    with open('words.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([word])

user_word = input("Enter a search term: ")

write_word_to_csv(user_word)