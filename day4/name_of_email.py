import re

def name_of_email(addr):
    if re.match(r'^\<.+\>\s[0-9a-zA-Z\.\_]+@[0-9a-zA-Z]+\.[a-zA-Z]+$', addr):
                return re.match(r'^\<(.+)\>', addr).group(1)
    elif re.match(r'^[0-9a-zA-Z\.\_]+@[0-9a-zA-Z]+\.[a-zA-Z]+$', addr):
                  return re.match(r'^([0-9a-zA-Z\.\_]+)', addr).group(1)
    else:
        return None

assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
