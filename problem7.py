#Shubham Chandra
#problem 7

#check logic of removing max and min

#The centered average is the mean average ignoring the largest and smallest values. For examples the centered average of the following collection of numbers, 
# [1,4,5,6,100] is 5.
# If there are multiple copies of the smallest value, keep only one. Likewise for the largest value.

test_numbers = [1,1,1,4,5,1,6,100,100,100,100]

def centered_average_with_iteration(numbers): 
    truncated = []
    removed = []
    for number in numbers:
        if number == max(numbers): #nested if's check to make sure there is only 1 of max and min value when duplicated
            if number in removed and number not in truncated:
                truncated.append(number)
            else:
                removed.append(number)
        elif number == min(numbers):
            if number in removed and number not in truncated:
                truncated.append(number)
            else:
                removed.append(number)
        else:
            truncated.append(number)
    return sum(truncated) / len(truncated)


def centered_average(numbers): 
    numbers.sort()
    min_val = numbers[0]
    max_val = numbers[-1]
    count_min = numbers.count(min_val)
    if count_min == 1:
        count_min = 2
    count_max = numbers.count(max_val)
    if count_max == 1:
        count_max = 2
    truncated = numbers[count_min-1:(len(numbers)-count_max+1)]
    return sum(truncated)/len(truncated)

