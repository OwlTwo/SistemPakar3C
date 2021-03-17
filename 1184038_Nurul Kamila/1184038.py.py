# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 17:38:19 2021

@author: user
"""

#%%Contoh 1 FORWARD CHAINING
global fact
global is_changed

is_changed = True
facts = [["Lesuh","Sakit"],["Meriang","Sakit"],["Bersemangat","Sehat"]]

def assert_fact(fact):
    global facts
    global is_changed
    if not fact in facts:
        facts += [fact]
        is_changed = True

while is_changed:
    is_changed = False
    for A1 in facts:
        if A1[0] == "Bersemangat":
            assert_fact(["Lesuh",A1[1]])
        if A1[0] == "Lesuh":
            assert_fact(["Flu",A1[1]])
        if A1[0] == "Lesuh" and ["Meriang",A1[1]] in facts:
            assert_fact(["Demam",A1[1]])

print(facts)
#%%Contoh 2 BACKWARD CHAINING
global fact
global is_changed

is_changed = True
facts = [["Lesuh","Sakit"],["Meriang","Sakit"],["Bersemangat","Sehat"]]

def assert_fact(fact):
    global facts
    global is_changed
    if not fact in facts:
        facts += [fact]
        is_changed = True

while is_changed:
    is_changed = False
    for A1 in facts:
        if A1[0] == "Lesuh" and ["Meriang",A1[1]] in facts:
            assert_fact(["Demam",A1[1]])
        if A1[0] == "Lesuh":
            assert_fact(["Flu",A1[1]])
        if A1[0] == "Bersemangat":
            assert_fact(["Lesuh",A1[1]])
        
        
print(facts)