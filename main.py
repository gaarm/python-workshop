names = ['daffy', 'bugs', 'drek']
colors = ['red', 'blue', 'yellow']

for name in names:
    print(name)

for name in reversed(names):
    print(name)

for i in range(len(names)):
    name, color = names[i], colors[i]
    print(f'{name} is {color}')

for i, name in enumerate(names):
    color = colors[i]
    print(f'{name} is {color}')

print("_________________")
for name, color in zip(names, colors):
    print(f"{name} is {color}")

"""Formatted printing"""
name, age = 'Daffy', 83
msg = '{} is {} years old'.format(name, age)
print(msg)

for line in open('road.txt'):
    # print(line, end='')
    print(line.strip())

# homework #1
i = 1
for line in open('road.txt'):
    if line.find(' it ') > 0:
        print(f'{i}: {line.strip()}')
    i = i + 1
