import re

string = "1A Toyota's a Toyota1"
string = string.upper()
new_string = re.findall(r'\w', string)
print(new_string)
string_clean = ''.join(new_string)
'''for letter in new_string:
    string_clean += letter'''
#string_clean = [letter for letter in new_string]
print(string_clean)
'''string_reverse = string_clean[::-1]
print(string_reverse)
if string_clean == string_reverse:
    print("The string is a palindrome")
else:
    print("The string is a not palindrome")'''
    

    