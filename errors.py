# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 12:41:27 2023

@author: suraj
"""
print("Ran")

def div0(a,b):
    if b==0:
        raise ValueError("Your 2nd argument is a 0 here but you shouldn't have a 0 here")
    try:
        c= a/b
        return c
    except ZeroDivisionError:
        print("not good man, dividing by 0")
    

def math(a):
    b = a-2
    try:
        c = div0(a,b)
    except ValueError:
        b=0.0000000001
        c=div0(a,b)
    print(c)


if __name__ == "__main__":
    math(2)