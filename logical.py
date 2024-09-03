# and : both
# or : at least one
# not

'''is_rainy=input('enter your value1:')
is_clear=input('enter your value2:')
if str(is_rainy)=='F' and str(is_clear)=='T':
    print("i will go to school.")
else:
    print("i willn't go to school.")'''

temp=int(input('enter the value of temperature: '))
if temp>=30:
    print("it's hot")
elif temp<15:
    print("it's cold")
else:
    print("it's a normal day")
