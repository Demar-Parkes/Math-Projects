import time
import os

os.system('cls')
from pyfiglet import Figlet
f = Figlet(font='slant')
print(f.renderText('Average Calculator'))


print('''How To Use:
When finished putting in number. Press C to Calculate
''')
def average():
    num = []
    while True:
        number = input("Enter number: ")
        try:
            if number.lower() == 'c':
                total = sum(num)
                av = total / len(num)
                os.system('cls')
                return f'Numbers entered: {num} And the average is {av}'
        except:
            print('You have to put a enter a number')
            continue

        if number == '':
            print('You have enter a number')
            continue
        if number == ' ':
            print('You cannot use space')
            continue


        if number.lower() == 'q':
            print('Have a good day')
            time.sleep(1)
            exit()



        try:
            num.append(int(number))
        except:
            print('Enter a valid number')

        
if __name__ == '__main__':
    try:
        print(average())
    except KeyboardInterrupt:
        os.system('cls')
        print('You pressed CTRL C...')
        time.sleep(1)
        exit()