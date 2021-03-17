# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 14:07:08 2021

@author: Tuf Gaming
"""

#%%Contoh 1 FORWARD CHAINING
global facts
global is_changed

is_changed = True
facts = [["Tinju","Samsak"],["Tendang","Samsak"],["silat","beladiri"]]

def assert_fact(fact):
    global facts
    global is_changed
    if not fact in facts:
        facts += [fact]
        is_changed = True

while is_changed:
    is_changed = False
    for A1 in facts:
        if A1[0] == "silat":
            assert_fact(["beladiri",A1[1]])
        if A1[0] == "Tinju":
            assert_fact(["pukulan",A1[1]])
        if A1[0] == "Tinju" and ["Tendang",A1[1]] in facts:
            assert_fact(["gerakan",A1[1]])

print(facts)


#%%Contoh 2 BACKWARD CHAINING

is_changed = True
facts = [["Tinju","Samsak"],["Tendang","Samsak"],["silat","beladiri"]]

def assert_fact(fact):
    global facts
    global is_changed
    if not fact in facts:
        facts += [fact]
        is_changed = True

while is_changed:
    is_changed = False
    for A1 in facts:
        if A1[0] == "Tinju" and ["Tendang",A1[1]] in facts:
            assert_fact(["gerakan",A1[1]])
        if A1[0] == "Tinju":
            assert_fact(["pukulan",A1[1]])
        if A1[0] == "silat":
            assert_fact(["beladiri",A1[1]])
        
        
        
print("BackwardChain")
print(facts)
