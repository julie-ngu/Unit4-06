# Created by: Julie Nguyen
# Created on: Nov 2017
# Created for: ICS3U
# This program checks to see if two strings the user inputs are the same

def check_if_true(first_string, second_string):
    # user enters two strings, function checks if strings are the same and returns either True or False
    
    first_string = string_1.upper()
    second_string = string_2.upper()
    
    if first_string == second_string:
        return True
    else:
        return False

# input
string_1 = raw_input("Enter string: ")
string_2 = raw_input("Enter next string: ")

# process
answer = check_if_true(string_1, string_2)

# output
print answer
