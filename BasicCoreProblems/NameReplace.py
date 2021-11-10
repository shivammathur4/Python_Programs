"""
@Author: Shivam Mathur
@Date: 2021-11-08 
@Last Modified by: Shivam Mathur
@Last Modified time: 2021-11-08 
@Title = 'User Input and Replace String Template “Hello <<UserName>>, How are you?”'
"""
stringToChange = "“Hello <<UserName>>, How are you?”"
print("Enter the name to change : ")
name = input()

# using string replace method to replace string
if len(name) > 3:
    StringReplace = stringToChange.replace("<<UserName>>", name)
    print(StringReplace)
else:
    print("Enter name which has more than three letters.")