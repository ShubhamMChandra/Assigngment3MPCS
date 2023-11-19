#Shubham Chandra
#problem 9

#Read the file speech.txt and count the frequency of each word. To get more meaningful results of our analysis,
# we will want to remove the most commonly used words in the English language

#Write the results of your analysis out to a file by listing the twenty most frequently used words in the order from 
#most to least frequent. 
#Include the number of times they appear. Follow the format presented below:

# Done using https://stackoverflow.com/questions/8478602/convert-a-list-of-string-sentences-to-words; https://www.w3schools.com/python/ref_string_replace.asp; 

import string

with open("speech.txt", encoding='utf-8') as speech:
    lines = []
    for line in speech:
        line = line.strip()
        lines.append(line) #get all sentences in lines list
    speech_sentences = [] 
    for line in lines:
        speech_sentences.append(line.split()) #convert to words in words list
    speech_words = []
    for line in speech_sentences:
        for word in line:
            for punctuation in string.punctuation:
                word = word.replace(punctuation, "")
            speech_words.append(word.lower())



#create a dict of common words:

def process_file(filename):
    file_text = []
    with open(filename) as my_file:
        for line in my_file:
            line = line.strip().lower()
            file_text.append(line)
    return file_text

common_words = process_file("common_words.txt")

#now words list has all the words we need to count

count_dict = {}

for word in speech_words:
    if word in common_words:
        pass
    else:
        word_count = speech_words.count(word)
        count_dict[word] = word_count

#now we have to sort the count dict. Dict are immutable so we need to create a new dict
#https://www.freecodecamp.org/news/sort-dictionary-by-value-in-python/, https://www.geeksforgeeks.org/ways-sort-list-dictionaries-values-python-using-lambda-function/ kind of fudged my way through this
sorted_count_dict = dict(sorted(count_dict.items(), key=lambda item: item[1], reverse=True))

print_count = 0
for item in sorted_count_dict:
    if print_count < 20:
        print(f"{item} - {count_dict[item]}")
        print_count += 1
    else:
        break
 
