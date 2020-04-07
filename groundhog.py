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

# values = []
number = []
errors = []

def recup_input(period):
    data = []
    i = 0
    # number = []
    difference = []
    while True:
        try:
            data.append(input())
        except:
            exit(84)
        if data[i] == "STOP":
            if len(data) < period:
                exit(84)
            # print("5 weirdest values are", sort_weird_values())
            # try:
            #     print("Global tendency switched %d times" % nb_switch)
            #     errors.sort(key = sortThird, reverse = True)
            #     errors2 = []
            #     i = 0
            #     while (errors[i][2] >= 2 and i < 5):
            #         errors2.append(errors[i])
            #         i = i + 1
            #         errors = errors[i:]
            #     errors2.sort(key = sortSecond, reverse = True)
            #     errors.sort(key = sortSecond, reverse = True)
            #     j = 0
            #     while (i < 5):
            #         errors2.append(errors[j])
            #         j = j + 1
            #         i = i + 1
            #     i = 0
            #     print("5 weirdest values are [", end='')
            #     while (i < 5):
            #         print(errors2[i][0], end='')
            #         if (i != 4):
            #             print(", ", end='')
            #         i = i + 1
            #     print("]")
            # except:
            #     sys.exit(84)
            # break
        else:
            try:
                number.append(float(data[i]))
                if i > 0:
                    difference.append(number[i] - number[i - 1])
                if i >= period:
                    temperature_increase_average(difference, period, i)
                    relative_temperature_evolution(number, period, i)
                if i >= period - 1:
                    standard_deviation(period, i)
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
        print("g=nan\tr=nan%%\ts=%0.2f" % result)
    else:
        print("s=%0.2f" % result)
        #     weird_values(number, period, i, result)
    # aberration(len(number) - period, period, round(result, 2), moyenne)

def aberration(a, period, deviation, moyenne):
    i = 0
    
    # print("passe")
    value = number[a + period - 1]
    # print(value)
    if value >= moyenne + deviation:
        if moyenne + 2 * deviation == 0:
            p = 3000000
        else:
            p = value / (moyenne + 2 * deviation) * 100
        errors.append([value, p, 1])
    elif value <= moyenne - deviation:
        if value == 0:
            p = 3000000
        else:
            p = (moyene - 2 * deviation) / value * 100
        errors.append([value, p, 1])
    
def sortSecond(val):
    return val[1]

def sortThird(val):
    return val[2]

# def takeSecond(elem):
#     return (elem[1])

# def sort_weird_values():
#     values.sort(key= takeSecond)
#     k = len(values) - 1
#     length = len(values) - 5
#     weird = []
#     while k >= length:
#         weird.append(values[k][0])
#         k -= 1
#     return (weird)

# def weird_values(number, period, i, deviation):
#     tab = number[i + 1-period:i+1]
#     moyenne = sum(number[i + 1 - period: i +1]) / period
#     bh = moyenne + (2 * deviation)
#     bb = abs(moyenne - (2 * deviation))

#     for l in range (len(number[i + 1-period:i+1])):
#         calc = (tab[l] - bb) / (bh - bb)
#         values.append([tab[l], calc])
    
def main():
    if sys.argv[1] == "-h":
        print_dash_h()
    else:
        period = check_arg(sys.argv[1])
        recup_input(period)

main()