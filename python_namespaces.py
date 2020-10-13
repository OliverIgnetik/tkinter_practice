# illustration why importing everything from tkinter is a bad idea
# the namespace is absolutely cluttered
################################################

num1 = 5
num2 = 3.142
s = 'hello'


def add_two(num1, num2):
    print('function/local namespace')
    print(dir())
    return num1+num2


sum_of_numbers = add_two(1, 2)

print()
print(f'sum of numbers: {sum_of_numbers}')
print()
print('Check the global namespace')
namespace = dir()
print(namespace)
print()
print(f'__file__: {__file__}')
print(f'__name__: {__name__}')
