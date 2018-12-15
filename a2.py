import re
qq = '12345678900'
r = re.findall('\d{1,11}', qq)    #匹配
r1 = re.findall('^\d{1,10}$',qq)  #完全匹配
print(r1)
print(r)
