q, s, f = [], '(\))', True
for c in s:
    if c == '(' and f:
        q.insert(0,c)
    elif c == ')' and f:
        if q:
            q.pop()
        elif not q:
            q.append(')')
            break
            
    if c == '\\':
        f = False
    else:
        f = True
        
if not q:
    print('Valid')
else:
    print('Invalid')