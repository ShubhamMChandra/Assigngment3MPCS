#problem1
#Shubham Chandra

#Create a robust temperature converter program that takes input in Fahrenheit and converts to Celsius. 
#You program should make no assumptions about the user input. 
#Use the try/except pattern to ensure that the user has entered valid input.

#Think of all the possible ways this could fail. We will try our best to break your program.
# used eval function from https://stackoverflow.com/questions/63554871/how-do-i-take-a-fraction-as-an-input-in-python-and-use-the-fractions-value-for


while True:
    f_temp = input("Please enter a temperature: ")
    try:
        f_temp_int = float(eval(f_temp))
        c_temp = ((f_temp_int - 32) * 5/9)
        c_temp_round = str(round(c_temp,2))
        print(f"The temperature is {c_temp_round} in Celsius")
    except:
        print("Please enter a valid temperature.")
        
