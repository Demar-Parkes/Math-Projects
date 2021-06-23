##solving quadratic equations
##Formula 



def solve():
    while True:
        ##declare variables
        a = input('a: ')
        b = input('b: ')
        c = input('c: ')


        try:
            a = int(a)
            b = int(b)
            c = int(c)
        except:
            print('You entered a letter')
            continue

        x = (-1 * (b) + (b**2 - 4*a*c) ** 1/2) / 2*a
        print(x)
solve()