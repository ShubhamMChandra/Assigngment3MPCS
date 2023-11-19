#shubham chandra, problem 5
#Using your solution to Problem 3 and information provided in Problem 4, 
#crack the following Caesar Cipher encrypted message.

#What is the key and what is the message?

#mpwtpgp jzf nly lyo jzf lcp slwqhlj espcp
#Write out your approach and any assumptions you made as a comment at the top of the file.

phrase = "mpwtpgp jzf nly lyo jzf lcp slwqhlj espcp"

#To solve, we test all possible ranges for the key between 0 and 26 adjustments. (below) 


#take in previous functions from problem 3
import string 

possible_letters = string.ascii_lowercase

og_key = {} #the original letter mappings created below

count = 0
for i in range(len(possible_letters)):
    count +=1
    og_key[possible_letters[i]] = count

print(og_key)

#create the new cipher key with numbers as the key
def key_adjustment(key):
    new_key = {}
    for letter in og_key:
        shifted_position = (og_key[letter] - key - 1) % 26 + 1
        new_key[letter] = possible_letters[shifted_position - 1]
    return new_key

def caesar_encrypt(key, message):
    # Use the adjusted key to encrypt the message directly
    new_key = key_adjustment(key)
    ciphered_message = ""
    for letter in message:
        if letter == " ":
            ciphered_message += " "
        elif letter.lower() in new_key:
            if letter.isupper():
                ciphered_message += new_key[letter.lower()].upper()
            else:
                ciphered_message += new_key[letter]
        else:
            ciphered_message += letter
    return ciphered_message


#print(caesar_encrypt(2,"hello   world!")) #we confirm this works

#now we decrypt, using the original function but reversing the shift 

def caesar_decrypt(key, encrypted):
    return caesar_encrypt(26 - key, encrypted)

#print(caesar_decrypt(2, "fcjjm   umpjb!")) #we confirm this works


#We test all possible ranges for the key between 0 and 26 adjustments. 

for i in range (0,26):
    print(caesar_decrypt(i,phrase))
    print(i)

#We find that 15 is the one that creates a readable text

print(caesar_decrypt(15,phrase))

