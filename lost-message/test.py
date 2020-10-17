#!/usr/bin/python3

import sys, random, binascii, hashlib, re, math, os
from string import ascii_uppercase as asc
from itertools import product as d

upper = {ascii:chr(ascii) for ascii in range(65,91)}
lower = {ascii:chr(ascii) for ascii in range(97,123)}
digit = {ascii:chr(ascii) for ascii in range(48,58)}

def enc2(string, key): 
    for c in string:
        o = ord(c)
        # daca o este un caracter special sau cifra return ascii_code(litera)
        if (o not in upper and o not in lower) or o in digit:
            yield o
        else:
            # daca o este mare si ascii_code(litera) + 9 este upper
            # return ascii_code + 9
            # litere de la 65 la 82 --- A la R/Q

            if o in upper and o + key % 26 in upper:
                yield o + key % 26
            # litere de la 97 la 114----  a la r
            elif o in lower and o + key % 26 in lower:
                yield o + key % 26.
            else: 
                # restul scad 17
                # ascii_code - 17
                yield o + key % 26 -26

# cipher="Ana are mere"
# cipher = "EzFzVzGzCzRzAzDWCzNM"
pp = (enc2("EzFzVzGzCzRzAzDWCzNM", 35))
print(list(pp))

cipher = "".join(map(chr, enc2(cipher, 35)))
print(cipher)
# print("\n")
# pp2 = map(chr,pp)
# print(list(pp2))