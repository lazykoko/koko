import re
lanuage = 'pythonC#javaC#phpC#'
def convert(value):
    matched = value.group()
    return '??'+matched+'??'

r = re.sub('C#',convert,lanuage,) #sub的替换
print(r)