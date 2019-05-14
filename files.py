# Files open, read, write, etc

file = open('dynamic_prog.py', 'r')

print(file.read(4))

print(file.read())

lines = file.read()

file_lines = file.readlines()

file_lines

for line in file_lines:
    print(line, end='')

file.close()


file = open('newfile.txt', 'w')
file.write('test')

file.close()

file = open('newfile.txt', 'r')

print(file.read())

file.close()



file = open('newfile.txt', 'w')

file.write('test new')

dir(file)

file.close()



try:
    f = open('newfile.txt')
    print(f.read())
finally:
    f.close()

with open('newfile.txt') as f:
    print(f.read())