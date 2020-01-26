#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 09:05:59 2020

@author: hosseinkaragah
"""

####################
# This snippet uses bisection method to find the cube root of a number called 'cube'
# 'Cube' can be positive or negative
# 'Cube' can be smaller ot greater than one
####################
# cube = 27
# cube = -8120601
cube = -0.25

is_negative = False
# change the sign to (+) if the number is (-)
if cube < 0:
    is_negative = True
    cube = -cube

is_less_than_one = False
# use reciprocal if the number is < 1
if cube < 1:
    is_less_than_one = True
    cube = 1/cube

epsilon = 0.01  # chosen accuracy
num_guesses = 0
low = 0  # lower bound
high = cube  # upper bound
guess = (high + low)/2.0 # initial guess
while abs(guess**3 - cube) >= epsilon:
    if guess**3 < cube:
        # look only in upper half search space
        low = guess
    else:
        # look only in lower half search space
        high = guess
    # next guess is halfway in search space
    guess = (high + low)/2.0
    num_guesses += 1

# change the sign back to what is was originally
if is_negative:
    cube = -cube
    guess = -guess

# reciprocate if the number was reciprocated
if is_less_than_one:
    cube = 1/cube
    guess = 1/guess

print('num_guesses =', num_guesses)
print(guess, 'is close to the cube root of', cube)
