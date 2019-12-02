class A(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return 'A({0.x!r}, {0.y!r})'.format(self)
    
    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)

a = A(10, 20)

a

str(a)

repr(a)
# Specifically, the special !r formatting code indicates that 
# the output of _repr_() should be used instead of _str_(), 
# the default. You can try this experiment with the preceding class to see this:
print('a is {0!r}'.format(a))
print('a is {0}'.format(a))

eval(repr(a)) == a

_formats = {
    'ymd': '{d.year}-{d.month}-{d.day}',
    'mdy': '{d.month}/{d.day}/{d.year}',
    'dmy': '{d.day}/{d.month}/{d.year}'
}

class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        
    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)

d = Date(2012, 12, 21)

format(d)

format(d, 'mdy')

'The date is {0:ymd}'.format(d) # Read also about % (C style)

'The date is {:mdy}'.format(d)



di = {'name': 1, 'sname':2}

di.pop('name')

di