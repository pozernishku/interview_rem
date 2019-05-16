sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})
sorted('1333000')

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]

student_tuples

sorted(student_tuples, key=lambda student: student[2]) 

student_objects = [
    Player('john', 95),
    Player('jane', 12),
    Player('dave', 70),
    Player('xdave', 70)
]

sorted(student_objects, key=lambda student: student.score)   # sort by score
from operator import itemgetter, attrgetter
sorted(student_tuples, key=itemgetter(2))
sorted(student_objects, key=attrgetter('name'))
sorted(student_tuples, key=itemgetter(1,2))
sorted(student_objects, key=attrgetter('score', 'name'))
sorted(student_tuples, key=itemgetter(2), reverse=True)
sorted(student_objects, key=attrgetter('score', 'name'), reverse=True)

# ## Sort Stability and Complex Sorts
data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
sorted(data, key=itemgetter(0))
student_objects
s = sorted(student_objects, key=attrgetter('name'))     # sort on secondary key
sorted(s, key=attrgetter('score'), reverse=True)       # now sort on primary key, descending

# ## The Old Way Using Decorate-Sort-Undecorate
decorated = [(student.score, i, student) for i, student in enumerate(student_objects)]
decorated
decorated.sort()
decorated
[student for grade, i, student in decorated]

# ## The Old Way Using the cmp Parameter

def numeric_compare(x, y):
    return x - y
# sorted([5, 2, 4, 1, 3], cmp=numeric_compare)

def reverse_numeric(x, y):
    return y - x
# sorted([5, 2, 4, 1, 3], cmp=reverse_numeric)

sorted([5, 2, 4, 1, 3], key=cmp_to_key(reverse_numeric))

# ## Odd and Ends

data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
data

standard_way = sorted(data, key=itemgetter(0), reverse=True)
standard_way

double_reversed = list(reversed(sorted(reversed(data), key=itemgetter(0))))
double_reversed

assert standard_way == double_reversed

Player.__lt__ = lambda self, other: self.score < other.score

student_objects
sorted(student_objects)

students = ['dave', 'john', 'jane']
newgrades = {'john': 'F', 'jane':'A', 'dave': 'C'}

sorted(students, key=newgrades.__getitem__)

from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self):
        return repr((self.name, self.score))
        
    def comparator(a, b):
        return 
#         key=lambda student: student.age

data = [['Anton', 1], ['Ann', 2], ['Den', 0], ['Ben', 0]]
data
p = Player('Jig', 50)
p
data = sorted(data, key=cmp_to_key(Player.comparator))
