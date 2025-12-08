
def even_odd(start,end):
    for num in range(10,20):
        num=int(input("Enter a number: "))
        if num %2==0:
            print(f'{num} is even')
        else:
            print(f'{num} is odd')

even_odd(10,20)