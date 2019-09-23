import random
import time
from termcolor import colored
while 1:
    a = random.randint(0, 20)
    b = random.randint(0, 20)
    c = random.randint(0, 20)
    d = random.randint(0, 20)
    print("Signal 1 count = ", a)
    print("Signal 2 count = ", b)
    print("Signal 3 count = ", c)
    print("Signal 4 count = ", d)
    numbers = [('s1',a),('s2',b),('s3',c),('s4',d)]
    def sortSecond(val):
        return val[1]
    numbers.sort(key = sortSecond,reverse = True)
    print(numbers)
    i=0
    while i<4:
        if numbers[i][0] == 's1':
            print(f"Signal one: ",colored('green','green' ) + "      Signal two: ",colored('red','red' ) + "       Signal three: ",colored('red','red' ) + "       Signal four: ",colored('red','red' ) + "\n")
            print("Signal one: ",colored('yellow','yellow' ) + "     Signal two: ",colored('red','red' ) + "        Signal three: ",colored('red','red' ) + "       Signal four: ",colored('red','red' ) + "\n")

            time.sleep(3)
        elif numbers[i][0] =='s2':
            print("Signal one: ",colored('red','red' ) + "        Signal two: ",colored('green','green' ) + "       Signal three: ",colored('red','red' ) + "         Signal four: ",colored('red','red' ) + "\n")
            print("Signal one: ",colored('red','red' ) + "        Signal two: ",colored('yellow','yellow' ) + "      Signal three: ",colored('red','red' ) + "          Signal four: ",colored('red','red' ) + "\n")

            time.sleep(3)
        elif numbers[i][0]=='s3':
            print("Signal one: ",colored('red','red' ) + "        Signal two: ",colored('red','red' ) + "         Signal three: ",colored('green','green' ) + "     Signal four: ",colored('red','red' ) + "\n")
            print("Signal one: ",colored('red','red' ) + "        Signal two: ",colored('red','red' ) + "         Signal three: ",colored('yellow','yellow' ) + "    Signal four: ",colored('red','red' ) + "\n")

            time.sleep(3)
        else :
            print("Signal one: ",colored('red','red' ) + "       Signal two: ",colored('red','red' ) + "          Signal three: ", colored('red','red' ) + "        Signal four: ",colored('green','green' ) + "\n")
            print("Signal one: ",colored('red','red' ) + "        Signal two: ",colored('red','red' ) + "         Signal three: ",colored('red','red' ) + "       Signal four: ",colored('yellow','yellow' ) + "\n")

        i=i+1
    #time .sleep(10)







