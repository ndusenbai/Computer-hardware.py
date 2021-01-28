print("Computer hardware")
e = str(input("write 'GO'"))
if e == "GO":
    print('start')
    p = str(input('type'))
    if p == "and":
        a = int(input('A(0 or 1): '))
        if 0 <= a <= 1:
            print('correct')
            b = int(input('B(0 or 1): '))
            if 0 <= b <=1:
                print('correct')
                if a == 0:
                    if b == 0:
                        print('answer: 0(false)')
                    elif b == 1:
                        print('answer: 0(false)')
                if a == 1:
                    if b == 0:
                        print('answer: 0(false)')
                    if b == 1:
                        print('answer: 1(true)')
            else:
                print('write correct number')
        else:
            print('write correct number')
    elif p == "or":
        a = int(input('A(0 or 1): '))
        if 0 <= a <= 1:
            print('correct')
            b = int(input('B(0 or 1): '))
            if 0 <= b <=1:
                print('correct')
                if a == 0:
                    if b == 0:
                        print('answer: 0(false)')
                    elif b == 1:
                        print('answer: 1(true)')
                if a == 1:
                    if b == 0:
                        print('answer: 1(true)')
                    if b == 1:
                        print('answer: 1(true)')
            else:
                print('write correct number')
        else:
            print('write correct number')
    elif p == "xor":
        a = int(input('A(0 or 1): '))
        if 0 <= a <= 1:
            print('correct')
            b = int(input('B(0 or 1): '))
            if 0 <= b <=1:
                print('correct')
                if a == 0:
                    if b == 0:
                        print('answer: 0(false)')
                    elif b == 1:
                        print('answer: 1(true)')
                if a == 1:
                    if b == 0:
                        print('answer: 1(true)')
                    if b == 1:
                        print('answer: 0(false)')
            else:
                print('write correct number')
        else:
            print('write correct number')
    elif p == "nand":
        a = int(input('A(0 or 1): '))
        if 0 <= a <= 1:
            print('correct')
            b = int(input('B(0 or 1): '))
            if 0 <= b <=1:
                print('correct')
                if a == 0:
                    if b == 0:
                        print('answer: 1(true)')
                    elif b == 1:
                        print('answer: 0(false)')
                if a == 1:
                    if b == 0:
                        print('answer: 0(false)')
                    if b == 1:
                        print('answer: 0(false)')
            else:
                print('write correct number')
        else:
            print('write correct number')
    elif p == "nor":
        a = int(input('A(0 or 1): '))
        if 0 <= a <= 1:
            print('correct')
            b = int(input('B(0 or 1): '))
            if 0 <= b <=1:
                print('correct')
                if a == 0:
                    if b == 0:
                        print('answer: 1(true)')
                    elif b == 1:
                        print('answer: 1(true)')
                if a == 1:
                    if b == 0:
                        print('answer: 1(true)')
                    if b == 1:
                        print('answer: 0(false)')
            else:
                print('write correct number')
        else:
            print('write correct number')
    elif p == "xnor":
        a = int(input('A(0 or 1): '))
        if 0 <= a <= 1:
            print('correct')
            b = int(input('B(0 or 1): '))
            if 0 <= b <=1:
                print('correct')
                if a == 0:
                    if b == 0:
                        print('answer: 1(true)')
                    elif b == 1:
                        print('answer: 0(false)')
                if a == 1:
                    if b == 0:
                        print('answer: 0(false)')
                    if b == 1:
                        print('answer: 1(true)')
            else:
                print('write correct number')
        else:
            print('write correct number')
    elif p == "not":
        a = int(input('A(0 or 1): '))
        if 0 <= a <= 1:
            if a == 0:
                print('answer: 1(true)')
            if a == 1:
                print('answer: 0(false)')
        else:
            print('write correct number')
    else:
        print('write correct type')
else:
    print("Pleaes, write 'GO'")
