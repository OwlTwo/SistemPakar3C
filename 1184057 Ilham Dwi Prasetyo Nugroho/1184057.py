# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 13:12:15 2021

@author: ASUS
"""


#%%Contoh 1 FORWARD CHAINING
global fact
global is_changed

is_changed = True
facts = [["Diam","Sedih"],["Galau","Sedih"],["Ketawa","Senang"]]

def assert_fact(fact):
    global facts
    global is_changed
    if not fact in facts:
        facts += [fact]
        is_changed = True

while is_changed:
    is_changed = False
    for A1 in facts:
        if A1[0] == "Ketawa":
            assert_fact(["Senang",A1[1]])
        if A1[0] == "Diam":
            assert_fact(["Merana",A1[1]])
        if A1[0] == "Diam" and ["Galau",A1[1]] in facts:
            assert_fact(["Murung",A1[1]])
print("FowardChain")
print(facts)
#%%Contoh 2 BACKWARD CHAINING
global fact
global is_changed

is_changed = True
facts = [["Diam","Sedih"],["Galau","Sedih"],["Ketawa","Senang"]]

def assert_fact(fact):
    global facts
    global is_changed
    if not fact in facts:
        facts += [fact]
        is_changed = True

while is_changed:
    is_changed = False
    for A1 in facts:
        if A1[0] == "Diam" and ["Galau",A1[1]] in facts:
            assert_fact(["Merana",A1[1]])
        if A1[0] == "Diam":
            assert_fact(["Merana",A1[1]])
        if A1[0] == "Senang":
            assert_fact(["Sedih",A1[1]])
        
print("BackwardChain")     
print(facts)