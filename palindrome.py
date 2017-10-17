import re

def is_palindrome(string):
    '''Function to check whether string is palindrome or not'''
    #Check if varaiable is a string
    if type(string) != str:
        return False
    string = string.upper()
    #Get rid of non-alphanumeric characters
    new_string = re.findall(r'\w', string)
    string_clean = ''.join(new_string)
    #reverse the string
    string_reverse = string_clean[::-1]
    if string_clean == string_reverse:
        #print("The string is a palindrome")
        return True
    return False
        
print (is_palindrome("1A Toyota's a Toyota1"))

