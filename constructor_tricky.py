# Tricky constructor
class Structure(object):
    _fields = []
    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        # Set all of the positional arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)
        # Set remaining keyword arguments
        for name in self._fields[len(args):]:
            setattr(self, name, kwargs.pop(name))
        # Check if any remaining unknown arguments
        if kwargs:
            raise TypeError('Invalid argument(s): {}'.format(','.join(kwargs)))

# Example use
if __name__ == '__main__':
    class Stock(Structure):
        _fields = ['name', 'shares', 'price']

s1 = Stock('ACME', 50, 91.1)
s2 = Stock('ACME', 50, price=91.1)
s3 = Stock('ACME', shares=50, price=91.1)



# ----------
# Extra args
class Structure(object):
    # Class variable that specified expected fields
    _fields = []
    def __init__(self, *args, **kwargs):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        # Set the arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)
        # Set the additional arguments (if any)
        extra_args = kwargs.keys() - self._fields
        for name in extra_args:
            setattr(self, name, kwargs.pop(name))
        if kwargs:
            raise TypeError('Duplicate values for {}'.format(','.join(kwargs)))

# Example use
if __name__ == '__main__':
    class Stock(Structure):
        _fields = ['name', 'shares', 'price']

s1 = Stock('ACME', 50, 91.1)
s2 = Stock('ACME', 50, 91.1, date='8/2/2012')
print(s2.date)


# ------
# Not recomended 
'''One subtle aspect of the implementation concerns 
the mechanism used to set value using the setattr() function. 
Instead of doing that, you might be inclined to directly access 
the instance dictionary. For example:

Although this works, it’s often not safe to make assumptions 
about the implementation of a subclass. If a subclass decided 
to use _slots_ or wrap a specific attribute with a property 
(or descriptor), directly acccessing the instance dictionary would break. 
The solution has been written to be as general purpose as possible and 
not to make any assumptions about subclasses.

A potential downside of this technique is that it impacts
 documentation and help features of IDEs. If a user asks for 
 help on a specific class, the required arguments aren’t described 
 in the usual way. For example:
 help(Stock)
'''


class Structure(object):
    # Class variable that specifies expected fields
    _fields= []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        # Set the arguments (alternate)
        self.__dict__.update(zip(self._fields,args))


# Hack (cool)
def init_fromlocals(self):
    import sys
    locs = sys._getframe(1).f_locals
    for k, v in locs.items():
        if k != 'self':
            setattr(self, k, v)

class Stock(object):
    def __init__(self, name, shares, price):
        init_fromlocals(self)
