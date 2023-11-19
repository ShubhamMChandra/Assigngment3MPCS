#Shubham Chandra
#problem 4


#Write a function that processes a text file. The function should take the filename as its only argument. 
#The function should read in the file, remove any whitespace and put the contents into a list that is sorted. 
#You may use Python's built-in sorting methods. Make sure that you do any necessary error handling or validation 
#that is required to gracefully (ie. not crash) handle any potential issues with running your code.

# for tuple: https://stackoverflow.com/questions/16730339/python-add-item-to-the-tuple 

def process_file(filename):
    file_text = []
    with open(filename) as my_file:
        for line in my_file:
            line = line.strip().lower()
            file_text.append(line)
    file_text.sort()
    sorted_tuple = tuple(file_text)
    return (filename, sorted_tuple, len(sorted_tuple))

#print tuple, I think this is what it's asking for? 
print(process_file("common_words.txt"))

