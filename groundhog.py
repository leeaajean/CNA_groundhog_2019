#!/usr/bin/env python3

import sys

def print_dash_h():
    print("SYNOPSIS")
    print("\t./groundhog period")
    print("\nDESCRIPTION")
    print("\tperiod\t the number of days defining a period")

def check_arg(arg):
    try:
        period = int(sys.argv[1])
    except:
        exit(84)
    if period <= 0:
        exit(84)
    return (period)

def recup_input(period):
    data = []
    i = 0
    number = []
    difference = []
    while True:
        data.append(input())
        if data[i] == "STOP":
            break
        else:
            try:
                number.append(float(data[i]))
                if i > 0:
                    difference.append(number[i] - number[i - 1])
                if i >= period:
                    temperature_increase_average(difference, period, i)
                    relative_temperature_evolution(number, period, i)
                else: 
                    print("g=nan\tr=nan%\ts=nan")
            except:
                continue
            i += 1
        

def temperature_increase_average(difference, period, i):
    moyenne = 0
    moyenne = sum([v for v in difference[i-period:i] if v > 0]) / period
    print("g=%0.2f" % moyenne, end='\t')
    return (moyenne)

def relative_temperature_evolution(number, period, i):
    result = 0
    result = ((number[i] - number[i - period]) / number[i-period]) * 100
    print("r=%0.0f" % result, end='')
    print("%")
    return (result)

def main():
    if sys.argv[1] == "-h":
        print_dash_h()
    else:
        period = check_arg(sys.argv[1])
        recup_input(period)

main()