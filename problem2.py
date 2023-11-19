#Shubham Chandra
#problem2

#Complete the function that you worked on during Breakout Exercises and 
#write a function using pseudocode based on your list that returns True if the string argument is a number:

def is_number(string):
    try: 
        float(string)
        return True
    except:
        return False
    

#Works with decimals, whole numbers, fractions