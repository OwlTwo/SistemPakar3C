# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 08:57:28 2021

@author: Yusuf Jordan El Anwar
"""
# Rules

# mamalia (A) ==> bertulang belakang (A).
# bertulang belakang (A) ==> hewan (A).
# bertulang belakang (A), terbang (A) ==> burung (A).
# bertulang belakang ("bebek").
# terbang ("bebek").
# mamalia ("Kucing").

#FowardChain
global facts
global is_changed

is_changed = True
facts = [["bertulang belakang","bebek"],["terbang","bebek"],["mamalia","kucing"]]

def assert_fact(fact):
    global facts
    global is_changed
    if not fact in facts:
        facts += [fact]
        is_changed = True

while is_changed:
    is_changed = False
    for A1 in facts:
        if A1[0] == "mamalia":
            assert_fact(["bertulang belakang",A1[1]])
        if A1[0] == "bertulang belakang":
            assert_fact(["hewan",A1[1]])
        if A1[0] == "bertulang belakang" and ["terbang",A1[1]] in facts:
            assert_fact(["burung",A1[1]])

print("FowardChain")
print(facts)

#Backwardchain


is_changed = True
facts = [["bertulang belakang","bebek"],["terbang","bebek"],["mamalia","kucing"]]

def assert_fact(fact):
    global facts
    global is_changed
    if not fact in facts:
        facts += [fact]
        is_changed = True

while is_changed:
    is_changed = False
    for A1 in facts:
        if A1[0] == "bertulang belakang" and ["terbang",A1[1]] in facts:
            assert_fact(["burung",A1[1]])
        if A1[0] == "bertulang belakang":
            assert_fact(["hewan",A1[1]])
        if A1[0] == "mamalia":
            assert_fact(["bertulang belakang",A1[1]])
        
print("BackwardChain")
print(facts)

