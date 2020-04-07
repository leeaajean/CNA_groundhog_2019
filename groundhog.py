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

values = []

def recup_input(period):
    data = []
    i = 0
    number = []
    difference = []
    while True:
        data.append(input())
        if data[i] == "STOP":
            if len(data) < period:
                exit(84)
            print("5 weirdest values are", sort_weird_values())
            break
        else:
            try:
                number.append(float(data[i]))
                if i > 0:
                    difference.append(number[i] - number[i - 1])
                if i >= period:
                    temperature_increase_average(difference, period, i)
                    relative_temperature_evolution(number, period, i)
                if i >= period - 1:
                    standard_deviation(number, period, i)
                else: 
                    print("g=nan\tr=nan%\ts=nan")
            except:
                exit(84)
            i += 1

def temperature_increase_average(difference, period, i):
    moyenne = 0
    moyenne = sum([j for j in difference[i-period:i] if j > 0]) / period
    print("g=%0.2f" % moyenne, end='\t')
    return (moyenne)

def relative_temperature_evolution(number, period, i):
    result = 0
    result = ((number[i] - number[i - period]) / number[i-period]) * 100
    print("r=%0.0f" % result, end='')
    print("%", end='\t')
    return (result)

def standard_deviation(number, period, i):
    deviation = 0
    moyenne = 0
    value = 0
    l = 0
    result = 0
    tab = number[i + 1-period:i+1]
    moyenne = sum(number[i + 1 - period: i +1]) / period

    for l in range (len(number[i + 1-period:i+1])):
        value = tab[l] - moyenne
        deviation += value ** 2
        value = 0
    result = (deviation / period) ** 0.5
    
    if i == (period - 1):
        print("g=nan\tr=nan%%\ts=%0.2f" % result)
    else:
        print("s=%0.2f" % result)
    weird_values(number, period, i, result)

def takeSecond(elem):
    return (elem[1])

def sort_weird_values():
    values.sort(key= takeSecond)
    k = len(values) - 1
    length = len(values) - 5
    weird = []
    while k >= length:
        weird.append(values[k][0])
        k -= 1
    return (weird)

def weird_values(number, period, i, deviation):
    tab = number[i + 1-period:i+1]
    moyenne = sum(number[i + 1 - period: i +1]) / period
    bh = moyenne + (2 * deviation)
    bb = abs(moyenne - (2 * deviation))

    for l in range (len(number[i + 1-period:i+1])):
        calc = (tab[l] - bb) / (bh - bb)
        values.append([tab[l], calc])
    
def main():
    if sys.argv[1] == "-h":
        print_dash_h()
    else:
        period = check_arg(sys.argv[1])
        recup_input(period)

main()