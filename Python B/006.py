# import keyword
# print(keyword.kwlist)
# #['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# print(len(keyword.kwlist))


name="Chinmay Ranganath"
age=21
print('%s will get a job in one of the Biggest Tech company at his age of %d' % (name,age))

# String or immutables and tuples are immutables
print(name[2])
print(list(name))
print(set(name))
l=list(name)
print(type(l))
import random
random.shuffle(l)
print(l)