# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 22:13:45 2021

@author: Asus
"""
#%%Contoh 1 FORWARD CHAINING
global facts
global is_changed

is_changed = True
facts = [["gitar","dipetik"],["ukulele","dipetik"],["gendang","dipukul"]]

def assert_fact(fact):
    global facts
    global is_changed
    if not fact in facts:
        facts += [fact]
        is_changed = True

while is_changed:
    is_changed = False
    for A1 in facts:
        if A1[0] == "gendang":
            assert_fact(["dipukul",A1[1]])
        if A1[0] == "gitar":
            assert_fact(["gesekan",A1[1]])
        if A1[0] == "gitar" and ["ukulele",A1[1]] in facts:
            assert_fact(["alat musik",A1[1]])

print(facts)


#%%Contoh 2 BACKWARD CHAINING

is_changed = True
facts = [["gitar","dipetik"],["ukulele","dipetik"],["gendang","dipukul"]]

def assert_fact(fact):
    global facts
    global is_changed
    if not fact in facts:
        facts += [fact]
        is_changed = True

while is_changed:
    is_changed = False
    for A1 in facts:
        if A1[0] == "gitar" and ["ukulele",A1[1]] in facts:
            assert_fact(["alat musik",A1[1]])
        if A1[0] == "gitar":
            assert_fact(["gesekan",A1[1]])
        if A1[0] == "gendang":
            assert_fact(["dipukul",A1[1]])



print("BackwardChain")
print(facts)
