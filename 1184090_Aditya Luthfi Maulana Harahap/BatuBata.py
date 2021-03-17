# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 12:27:28 2021

@author: Aditya Luthfi
"""

global facts
global is_changed

print("Forward")
is_changed = True
facts = [["650","mahal"],["700","mahal"],["600","standar"]]

def assert_fact(fact):
    global facts
    global is_changed
    if not fact in facts:
        facts += [fact]
        is_changed = True

while is_changed:
    is_changed = False
    for A1 in facts:
        if A1[0] == "600":
            assert_fact(["650",A1[1]])
        if A1[0] == "650":
            assert_fact(["mahal",A1[1]])
        if A1[0] == "650" and ["700",A1[1]] in facts:
            assert_fact(["sangat mahal",A1[1]])


print(facts)


print("Backward")
is_changed = True
facts = [["650","mahal"],["700","mahal"],["600","standar"]]

def assert_fact(fact):
    global facts
    global is_changed
    if not fact in facts:
        facts += [fact]
        is_changed = True

while is_changed:
    is_changed = False
    for A1 in facts:
        if A1[0] == "650" and ["700",A1[1]] in facts:
            assert_fact(["sangat mahal",A1[1]])
        if A1[0] == "650":
            assert_fact(["mahal",A1[1]])
        if A1[0] == "600":
            assert_fact(["650",A1[1]])
        

print(facts)