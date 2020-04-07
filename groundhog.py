#!/usr/bin/env python3

import sys

number = []
weird = []

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

def takeSecond(elem):
    return elem[1]

def takeThird(elem):
    return elem[2]

def calc_moyenne(a, period):
    moyenne = 0
    i = 0
    while (i < period):
        moyenne = moyenne + number[a + i]
        i = i + 1
    moyenne = moyenne / period
    return (moyenne)

def abberation(a, period, deviation):
    i = 0
    moyenne = calc_moyenne(a, period)

    value = number[a + period - 1]
    if value <= moyenne - deviation:
        if value != 0:
            percent = (moyenne - 2 * deviation) / value * 100
        else:
            percent = 3000000
        weird.append([value, percent, 1])
    elif value >= moyenne + deviation:
        if moyenne + 2 * deviation != 0:
            percent = value / (moyenne + 2 * deviation) * 100
        else:
            percent = 3000000
        weird.append([value, percent, 1])
    return (weird)

def recup_input(period):
    data = []
    i = 0
    difference = []
    old_ratio = 0
    nb_switch = 0
    switch = 0
    deviation = 0
    while True:
        try:
            data.append(input())
        except:
            exit(84)
        if data[i] == "STOP":
            if len(data) < period:
                exit(84)
            try:
                print("Global tendency switched %d times" % nb_switch)
                weird.sort(key = takeThird, reverse = True)
                final_weird = []
                i = 0
                while (weird[i][2] >= 2 and i < 5):
                    final_weird.append(weird[i])
                    i = i + 1
                    weird = weird[i:]
                final_weird.sort(key = takeSecond, reverse = True)
                weird.sort(key = takeSecond, reverse = True)
                j = 0
                while (i < 5):
                    final_weird.append(weird[j])
                    j = j + 1
                    i = i + 1
                i = 0
                print("5 weirdest values are [", end='')
                while (i < 5):
                    print(final_weird[i][0], end='')
                    if (i != 4):
                        print(", ", end='')
                    i = i + 1
                print("]")
            except:
                sys.exit(84)
            break
        else:
            try:
                number.append(float(data[i]))
                if i > 0:
                    difference.append(number[i] - number[i - 1])
                if i >= period:
                    temperature_increase_average(difference, period, i)
                    ratio = relative_temperature_evolution(number, period, i)
                    if ratio > 0 and old_ratio < 0:
                        switch = 1
                    elif ratio < 0 and old_ratio > 0:
                        switch = 1
                    else:
                        switch = 0
                    old_ratio = ratio
                if i >= period - 1:
                    deviation = standard_deviation(period, i)
                    if len(number) > period:
                        weird = abberation(len(number) - period, period, round(deviation,2))
                    if switch == 1:
                        print("\t\ta switch occurs")
                        nb_switch += 1
                    else:
                        print("")
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
    old_value = number[i-period]
    actual_value = number[i]
    if old_value != 0:
        result = ((actual_value - old_value) / old_value) * 100
        if old_value < 0:
            result *= -1
    else:
        result = 999.9
    print("r=%0.0f" % result, end='')
    print("%", end='\t')
    return (result)

def standard_deviation(period, i):
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
        print("g=nan\tr=nan%%\ts=%0.2f" % result, end='')
    else:
        print("s=%0.2f" % result, end = '')
    return (result)
    
def main():
    if sys.argv[1] == "-h":
        print_dash_h()
    else:
        period = check_arg(sys.argv[1])
        recup_input(period)

main()