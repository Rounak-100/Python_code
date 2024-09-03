'''for x in range(3):
    for y in range(2):
        print(f"({x},{y})")'''

'''numbers=[5,2,5,2,2]
for i in numbers:
    print('x'*i)'''

numbers=[5,2,5,2,2]
for x_ct in numbers:
    output=''
    for ct in range(x_ct):
        output+='x'
    print(output)