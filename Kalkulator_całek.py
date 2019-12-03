# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 21:52:45 2019

@author: Milosz
"""

def integrate(function, a, b, i):
    dx = (b - a) / i
    integr = 0
    for x in range(i):
        x = x * dx + a
        integr += dx * eval(function)
    return integr

def main(args):
    function = input("Funkcja: ")
    a = float(input("Początek przedziału: "))
    b = float(input("Koniec przedziału: "))
    i = int(input("Liczba podprzedziałów:"))
    print("Całka z funkcji {funkcjon} po przedziale od {a} do {b} = {integrate}".format(funkcjon = function, a = a, b = b, integrate = integrate(function, a, b, i)))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))