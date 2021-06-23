import sys
import os
import time

##Set empty list
even = []
odd = []

##clear screen
os.system('cls')

##Print Screen
from pyfiglet import Figlet
f = Figlet(font='slant')
print(f.renderText('Even & Odd'))


##Where the action happens
def Even_odd():
    while True:
        n1 = input('Enter the number: ')
        if n1.lower() == 'q':
            os.system('cls')
            print(f.renderText('EXITING..'))
            time.sleep(1)
            sys.exit()
    
        
        n2 = input('Enter the second number: ')
        if n2.lower() == 'q':
            os.system('cls')
            print(f.renderText('EXITING..'))
            time.sleep(1)
            sys.exit()
    
    
        try:
            n1 = int(n1)
            n2 = int(n2)
        except:
            print('Enter a valid number...ONLY LETTER IS AVAILABLE IS Q TO EXIT')
            continue

        for i in range(n1, n2):
            if i % 2 == 0 :
                if i not in even:
                    even.append(i)
            elif i % 2 != 0:
                if i not in odd:
                    odd.append(i)
                os.system('cls')

        print('Even:', even)
        print('Odd:', odd)

        even.clear()
        odd.clear()

if __name__ == '__main__':
    try:
        Even_odd()
    except KeyboardInterrupt:
        os.system('cls') 
        print('You pressed CTRL C')
        time.sleep(1)
        exit()