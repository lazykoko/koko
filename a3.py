# 组
# \d \D匹配数字
# \w 单词字符\W
# \s 空白字符\S
# . 匹配除换行符外的所有字符
import re

a = 'PythonpythonPython'
r = re.findall('(python){1}', a) # 组
print(r)
lanuage = 'PythonC#phpjava'
r1 = re.findall('c#', lanuage, re.I) # 忽略大小写
print(r1)


