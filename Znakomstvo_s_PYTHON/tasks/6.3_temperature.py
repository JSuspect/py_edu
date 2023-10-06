def convert_cel_to_far(cel):
    '''Convert cel to far'''
    far = cel * 9 / 5 + 32
    print(f'{cel} degrees CEL = {far:.2f} degrees FAR')

def convert_far_to_cel(far):
    '''Convert far to cel'''
    cel = (far - 32) * 5 / 9
    print(f'{far} degrees FAR = {cel:.2f} degrees CEL')

while True:
    c = float(input("Enter a temperature in degrees CEL:"))
    convert_cel_to_far(c)
    print('#' * 50)
    f = float(input("Enter a temperature in degrees FAR:"))
    convert_far_to_cel(f)