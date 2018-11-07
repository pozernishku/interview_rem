def to_right(a=''):
    '''Transform the left language format to the right format'''
    
    #Prepare input. Add spaces after parentheses ')' --> ') '
    a = a.replace(' ', '')
    a = list(a.replace(')', ') '))
    
    #Walk through list with conditions
    #These spaces will be filled in with signs
    digits, signs, lst = '0123456789', '+/-*', []
    for i in range(len(a)-1):
        if a[i] in signs and a[i+1] in digits:
            a[i], a[i+1] = a[i+1], a[i]
        elif a[i] in signs and a[i+1] == '(':
            lst.append(a[i])
            a[i] = ''
        elif a[i] == ' ' and a[i+1] in signs:
            a[i] = ''
        elif a[i] == ' ' and a[i+1] not in signs:
            a[i] = lst.pop()
    return ''.join(a).strip()

if __name__ == '__main__':
    result = to_right('((((1/(23))+((2)/3))+((1/2)+(2/3))) / ((((1)/(2) )+(2/3))+((1/2)+(2/3)))  )')
    print(result)

# (1+3) --> (13+)
# ((1*3)+4) --> ((13*)4+)
# ((1/2)+(2/3)) --> ((12/)(23/)+)
# (5-7) --> (57-)
# (5+(23)) --> (5(23)+)