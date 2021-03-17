# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 12:27:28 2021

@author: Rizal
"""



global facts
global is_changed

print("Forward")
is_changed = True
facts = [["50","berat"],["70","berat"],["45","ringan"]]

def assert_fact(fact):
    global facts
    global is_changed
    if not fact in facts:
        facts += [fact]
        is_changed = True

while is_changed:
    is_changed = False
    for A1 in facts:
        if A1[0] == "45":
            assert_fact(["50",A1[1]])
        if A1[0] == "50":
            assert_fact(["berat",A1[1]])
        if A1[0] == "50" and ["70",A1[1]] in facts:
            assert_fact(["sangat berat",A1[1]])


print(facts)


print("Backward")
is_changed = True
facts = [["50","berat"],["70","berat"],["45","ringan"]]

def assert_fact(fact):
    global facts
    global is_changed
    if not fact in facts:
        facts += [fact]
        is_changed = True

while is_changed:
    is_changed = False
    for A1 in facts:
        if A1[0] == "50" and ["70",A1[1]] in facts:
            assert_fact(["sangat berat",A1[1]])
        if A1[0] == "50":
            assert_fact(["berat",A1[1]])
        if A1[0] == "45":
            assert_fact(["50",A1[1]])
        

print(facts)



