"""
The user enters a textfile to be found.

The function word_counter() gets the file name, opens the file
reads the file and collects every word in the file in the dictionary all_words.

The function then adds the 10 most frequent words to the dictionary word_freq
and returns this dictionary.

The program then runs through the returned dictionary
and prints them inside a table
"""

import io
from os import path

def word_counter(file_path):
    all_words = {}
    word_freq = {}

    infile = open(file_path, "r")
    row_list = infile.readlines()

    for i in row_list:        
        listed_words = i.split()
        
        for each_word in listed_words:

            num = 0

            
            each_word.replace(".", "")
            each_word.replace(" ", "")
            each_word.replace("    ", "")

            each_word = each_word.upper()

            first_ltr_in_wrd = str(each_word[0])

            each_word = str(first_ltr_in_wrd.upper() + each_word.lower()[1:])

            if(each_word not in all_words.keys()):
                num += 1
                all_words[each_word] = num

            elif(each_word in all_words.keys()):
                num = all_words.pop(each_word)
                num += 1
                all_words[each_word] = num

    while (len(word_freq) < 10):
        most_freq_word = max(all_words, key = all_words.get)
        word_freq[most_freq_word] = all_words.pop(most_freq_word)
        
    return word_freq

user_file = input("Enter your file here: ")

text_dir = path.dirname(__file__)
file_path = path.join(text_dir, "./"+user_file)

print("________________________")
print("| word    | times used |")
print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")
for key, value in word_counter(file_path).items():
    table_row = "| " + key 
    table_start = "| " + key
    spaces = int(22 - len(table_start) - len(str(value)))
    if len(table_row) < spaces:        
        for i in range(spaces):
            if(len(table_row) == 10):
                table_row = table_row + "|"
            if(len(table_row) == 12):
                table_row = table_row + str(value)
            table_row = table_row + " "
        table_row = table_row + "|"
    print(table_row)
print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")