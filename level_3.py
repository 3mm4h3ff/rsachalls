#!/usr/bin/python3
# -*- coding: utf-8 -*-

from Crypto.PublicKey import RSA

"""
What are the values of n,d and e in this private key?

Submit your flag in the following format: ZD{n,e,d} ...where n,d,e are large decimal numbers
"""

f = open('mykey2','r')

key = RSA.importKey(f.read())

flag =  "ZD{" + (str(key.n) + "," + str(key.e) + "," + str(key.d)) + "}"

print (flag)


