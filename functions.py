from collections import Counter
s = input()
d = dict(Counter(s))
def get_key(val):
    for key,value in d.items():
        if val == value:
            del d[key]
            temp = key
            return temp
for x in sorted(d.values(),reverse = True):
    print(get_key(x),":",x)
    
