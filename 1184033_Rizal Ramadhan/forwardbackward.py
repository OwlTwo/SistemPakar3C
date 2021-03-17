# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 12:27:28 2021

@author: Rizal
"""



global facts
global is_changed

print("Forward")
is_changed = True
facts = [["180","tinggi"],["190","tinggi"],["150","pendek"]]

def assert_fact(fact):
    global facts
    global is_changed
    if not fact in facts:
        facts += [fact]
        is_changed = True

while is_changed:
    is_changed = False
    for A1 in facts:
        if A1[0] == "150":
            assert_fact(["180",A1[1]])
        if A1[0] == "180":
            assert_fact(["tinggi",A1[1]])
        if A1[0] == "180" and ["190",A1[1]] in facts:
            assert_fact(["sangat tinggi",A1[1]])


print(facts)


print("Backward")
is_changed = True
facts = [["180","tinggi"],["190","tinggi"],["150","pendek"]]

def assert_fact(fact):
    global facts
    global is_changed
    if not fact in facts:
        facts += [fact]
        is_changed = True

while is_changed:
    is_changed = False
    for A1 in facts:
        if A1[0] == "180" and ["190",A1[1]] in facts:
            assert_fact(["sangat tinggi",A1[1]])
        if A1[0] == "180":
            assert_fact(["tinggi",A1[1]])
        if A1[0] == "150":
            assert_fact(["180",A1[1]])
        

print(facts)



