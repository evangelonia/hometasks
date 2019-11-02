import re

"""Write a function that takes in 
an email address from the user, 
then use regular expressions to check 
if the given string is in the right format. 

Use these rules for a valid email address: 

Usernames can contain letters (a-z), numbers (0-9), dashes (-),
 underscores (_), apostrophes (\'), and periods (.). 

Usernames cannot contain an ampersand (&), equal sign (=), brackets (<,>),
plus sign (+), 
comma (,), or more than one period (.) in a row. 

Must have one @ and only one period (.) after it.  """

regex = r"^[a-z\d.-_.']+[^&=+<>,]+@[A-Za-z]+\.[\w.]+$"


def get_email():
    email = input("Your email:")
    if (re.search(regex, email)):
        print(f"Valid Email:{email}")
    else:
        print("Invalid Email")


if __name__ == '__main__':
    get_email()
