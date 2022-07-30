import pyperclip
import re


def email_finder():
    email = re.compile(r'''(
        [a-zA-Z\d._%+-]+     
        @                      
        [a-zA-Z\d.-]+          
        (\.[a-zA-Z]{2,4}){1,2} 
        )''', re.VERBOSE)

    text = str(pyperclip.paste())
    matches = []

    for groups in email.findall(text):
        matches.append(groups[0])

    if len(matches) > 0:
        print('Copied to the clipboard:')
        print('\n'.join(matches))
    else:
        print('No e-mail address was found.')


if __name__ == "__main__":
    email_finder()
