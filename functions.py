from collections import Counter
s = input()
di = {}
for i in range(0,len(s)):
    di[s[i]] = s.count(s[i])
print(di)
def get_key(val):
    for key,value in di.items():
        if val == value:
            temp = key
            del di[key]
            return temp
for i in sorted(di.values(),reverse = True):
    print(get_key(i),"=",i)
    
