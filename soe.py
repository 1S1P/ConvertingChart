import os
class colors:
    CEND      = '\33[0m'
    CBOLD     = '\33[1m'
    CITALIC   = '\33[3m'
    CURL      = '\33[4m'
    CBLINK    = '\33[5m'
    CBLINK2   = '\33[6m'
    CSELECTED = '\33[7m'

    CBLACK  = '\33[30m'
    CRED    = '\33[31m'
    CGREEN  = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE   = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE  = '\33[36m'
    CWHITE  = '\33[37m'

    CBLACKBG  = '\33[40m'
    CREDBG    = '\33[41m'
    CGREENBG  = '\33[42m'
    CYELLOWBG = '\33[43m'
    CBLUEBG   = '\33[44m'
    CVIOLETBG = '\33[45m'
    CBEIGEBG  = '\33[46m'
    CWHITEBG  = '\33[47m'

    CGREY    = '\33[90m'
    CRED2    = '\33[91m'
    CGREEN2  = '\33[92m'
    CYELLOW2 = '\33[93m'
    CBLUE2   = '\33[94m'
    CVIOLET2 = '\33[95m'
    CBEIGE2  = '\33[96m'
    CWHITE2  = '\33[97m'

    CGREYBG    = '\33[100m'
    CREDBG2    = '\33[101m'
    CGREENBG2  = '\33[102m'
    CYELLOWBG2 = '\33[103m'
    CBLUEBG2   = '\33[104m'
    CVIOLETBG2 = '\33[105m'
    CBEIGEBG2  = '\33[106m'
    CWHITEBG2  = '\33[107m'


os.system("title Conversion Chart\nCoded by Sip\nVersion 1.0")
os.system('cls' if os.name == 'nt' else 'clear')
print(colors.CGREEN2 + '''
..........................................................
Conversion Chart
Coded by Sip
Version 1.0
..........................................................
''')


def loop():
    try:
        print("")
        print("Type...")
        print("")
        print(".............................................................................")
        print("|1 for kph to mph | 2 for Fahrenheit(f) to Celcius(c) | 3 for lbs to kg     |")
        print("|4 for inches to cm | 5 for in. to mm | 6 for cm to mm | 7 for in. to ft    |")
        print("|8 for ft to yds | 9 for seconds to hours | 0 for Circumference of a circle.|")
        print(".............................................................................")
        print("")
        c = input("What do you wish to convert?: ")
        print("")

        if c == "1":
            print("a - Kph to Mph / b - Mph to Kph")
            c1 = input("Enter a or b: ")
            if c1 == "a":
                c2 = float(input("Type number of kilometers an hour: "))
                print("")
                print("Miles per hour:")
                print(c2 * 0.62)
            elif c1 == "b":
                c3 = float(input("Type number of miles an hour: "))
                print("")
                print("Kilometers per hour:")
                print(c3 * 1.609344)
            else:
                print("")
                print("invalid.")

        elif c == "2":
            print("c- F to C / d- C to F")
            c4 = input("Enter c or d: ")
            if c4 == "c":
                c5 = float(input("Enter how many degrees Fahrenheit: "))
                print("")
                print("Degrees Celcius (approx.):")
                print((c5 - 32) * 0.55555556)
            elif c4 == "d":
                c6 = float(input("Enter how many degrees Celcius: "))
                print("")
                print("Degrees Fahrenheit (approx.):")
                print((c6 * 1.8) + 32)
            else:
                print("")
                print("invalid.")

        elif c == "3":
            print("e- lbs to kg / f- kg to lbs")
            c7 = input("Enter e or f: ")
            if c7 == "e":
                c8 = float(input("Enter amount of lbs: "))
                print("")
                print("Amount of Kilograms (approx.):")
                print(c8 * 0.45359237)
            elif c7 == "f":
                c9 = float(input("Enter amount of kilograms: "))
                print("")
                print("Amount of pounds (approx.):")
                print(c9 * 2.20462)
            else:
                print("")
                print("invalid.")

        elif c == "4":
            print("g- in. to cm. / h- cm. to in.")
            c0 = input("enter g or h: ")
            if c0 == "g":
                c10 = float(input("Enter amount of inches: "))
                print("")
                print("Amount of centimeters (approx.):")
                print(c10 * 2.54)
            elif c0 == "h":
                c11 = float(input("Enter amount of Centimeters: "))
                print("")
                print("Amount of inches:")
                print(c11 * 0.3937008)
            else:
                print("")
                print("invalid.")

        elif c == "5":
            print("i- in. to mm / j- mm to in.")
            c12 = input("enter i or j: ")
            if c12 == "i":
                c13 = float(input("Enter amount of inches: "))
                print("")
                print("Amount of millimeters:")
                print(c13 * 25.4)
            elif c12 == "j":
                c14 = float(input("Enter amount of millimeters: "))
                print("")
                print("Amount of inches:")
                print(c14 * 0.03937008)
            else:
                print("")
                print("invalid.")
        elif c == "6":
            print("k- cm to mm / l- mm to cm")
            c15 = input("Enter k or l: ")
            if c15 == "k":
                c16 = float(input("Enter amount of cm: "))
                print("")
                print("Amount of mm: ")
                print(c16 * 10)
            elif c15 == "l":
                c17 = float(input("Enter amount of mm: "))
                print("")
                print("Amount of cm: ")
                print(c17 / 10)
            else:
                print("")
                print("invalid.")
        elif c == "7":
            print("m- in. to ft. / n- ft. to in.")
            c18 = input("Enter m or n: ")
            if c18 == "m":
                c19 = float(input("Enter amount of Inches: "))
                print("")
                print("Amount of feet:")
                print(c19 / 12)
            elif c18 == "m":
                c20 = float(input("Enter amount of Feet: "))
                print("")
                print("Amount of Inches:")
                print(c20 / 12)
            else:
                print("")
                print("invalid.")
        elif c == "8":
            print("o- ft to yds / p- yds to ft")
            c21 = input("Enter o or p: ")
            if c21 == "o":
                c22 = float(input("Enter amount of feet: "))
                print("")
                print("Amount of yards:")
                print(c22 / 3)
            elif c21 == "p":
                c23 = float(input("Enter amount of yards: "))
                print("")
                print("Amount of feet:")
                print(c23 * 3)
            else:
                print("")
                print("invalid.")

        elif c == "9":
            print("q- seconds to hours / r- hours to seconds")
            c24 = input("Enter q or r: ")
            if c24 == "q":
                c25 = float(input("Enter amount of seconds: "))
                print("")
                print("Amount of Hours:")
                print(c25 / 3600)
            elif c24 == "r":
                c26 = float(input("Enter amount of hours: "))
                print("")
                print("Amount of Seconds:")
                print(c26 * 3600)
            else:
                print("")
                print("invalid.")
        elif c == "0":
            print("formula = C = 2 * 3.14r")
            print("r = radius (half the diameter)")
            c27 = float(input("Input radius: "))
            print("")
            print("Circumference is (approx.):")
            print(2 * (3.14 * c27))

        else:
            print("")
            print("invalid.")

    except ValueError:
        print("")
        print("Not a number or invalid.")
    except ZeroDivisionError:
        print("")
        print("Cannot divide by zero.")

    print("")
    print(".............................................................................................................")
    print(loop())


print(loop())
