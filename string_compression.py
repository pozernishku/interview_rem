# add any symbol to end of the string

s, cnt, res = 'aadabbbbccddb|', 0, ''
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if cnt+1 == 1:
            res += s[i]
        else:
            res += s[i] + str(cnt+1)
        cnt = 0
    else: 
        cnt += 1
    
print(res)