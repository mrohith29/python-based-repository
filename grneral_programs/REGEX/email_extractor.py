import re

'''
** Constraints
1.It must contain the "@" symbol.
2. It must have at least one character before the "@" symbol.
3. It must have a domain name after the "@" symbol.
4. The domain name should consist of at least one period (".") and at least one character after the last period.
'''


email = input()

validity = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

valid = re.findall(validity, email)

if len(valid) > 0:
    print('Valid email address')
else:
    print('Invalid email address')