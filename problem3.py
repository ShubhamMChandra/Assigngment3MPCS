#Shubham Chandra
#problem 3

#The Caeser cipher is a simple encryption technique where each letter is shifted in the alphabet. 
#For example, with a shift of 1, A would replaced by B, 
#B would be replaced by C, and so on. This cipher was used by Julius Caesar to communicate with his generals.

# to generate OG_key, used https://stackoverflow.com/questions/63915659/create-dictionary-with-alphabet-characters-mapping-to-numbers 

import string 

possible_letters = string.ascii_lowercase

og_key = {} #the original letter mappings created below

count = 0
for i in range(len(possible_letters)):
    count +=1
    og_key[possible_letters[i]] = count

#print(og_key)

#create the new cipher key with numbers as the key
def key_adjustment(key):
    new_key = {}
    for letter in og_key:
        shifted_position = (og_key[letter] - key - 1) % 26 + 1 #modular to avoid going over 26 and restart count
        new_key[letter] = possible_letters[shifted_position - 1]
    return new_key

def caesar_encrypt(key, message):
    # Use the adjusted key to encrypt the message directly
    new_key = key_adjustment(key)
    ciphered_message = ""
    for letter in message:
        if letter.lower() in new_key:
            if letter.isupper():
                ciphered_message += new_key[letter.lower()].upper() #preserve uppercase if
            else:
                ciphered_message += new_key[letter]
        else: #for non letter characters
            ciphered_message += letter
    return ciphered_message


print(caesar_encrypt(4,"helLo   world!")) #we confirm this works
#now we decrypt, using the original function but reversing the shift (base 26 compliment of key becomes unencryption key)

def caesar_decrypt(key, encrypted):
    return caesar_encrypt(26 - key, encrypted)

print(caesar_decrypt(4, "dahHk   sknhz!")) #we confirm this works
