# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 09:26:40 2021

@author: WINDOWS
"""

#Dim aturan(4, 1) As String
aturan(0, 0) = "suhu badan naik"
aturan(0, 1) = "demam"
aturan(1, 0) = "batuk dan sering bersin"
aturan(1, 1) = "flu"
aturan(2, 0) = "badan lemas"
aturan(2, 1) = "suhu badan naik"
aturan(3, 0) = "tenggorokan gatal / sakit"
aturan(3, 1) = "batuk"
aturan(4, 0) = "sering bersin"
aturan(4, 1) = "sering bersin"

#%%Contoh 1 FORWARD CHAINING
'Aturan 3
If input = "y" Then jawaban = aturan(2, 1)
'Aturan 1
If input2 = "y" And jawaban = "suhu badan naik" Then jawaban = aturan(0, 1)
'Aturan 4
If input = "n" And input2 = "y" Then jawaban = aturan(3, 1)
'Aturan 5
If input3 = "y" And jawaban = "batuk" Then jawaban = aturan(4, 1)
'Aturan 2
If jawaban = "sering bersin" Then jawaban = aturan(1, 1)
 
If jawaban = "demam" Or jawaban = "flu" Then
    Console.WriteLine("Penyakit yang diderita adalah " & jawaban)
End If
#%%Contoh 1 BACKWARD CHAINING
jawaban = aturan(0, 1)
'Aturan 1
If input2 = "y" And jawaban = "demam" Then jawaban = aturan(0, 0)
'Aturan 3
If input = "y" And jawaban = "suhu badan naik" Then jawaban = aturan(2, 0)
 
If jawaban = aturan(2, 0) Then
    Console.WriteLine("Penyakit yang diderita adalah " & aturan(0, 1))
    Console.ReadLine()
    Return
End If
 
jawaban = aturan(1, 1)
'Aturan 2
If input = "n" Then jawaban = aturan(1, 0)
 
Dim klausajawaban(1) As String
If jawaban = aturan(1, 0) Then
    klausajawaban(0) = aturan(3, 1)
    klausajawaban(1) = aturan(4, 1)
End If
 
'Aturan 4
If input2 = "y" And klausajawaban(0) = "batuk" Then klausajawaban(0) = aturan(3, 0)
'Aturan 5
If input3 = "y" And klausajawaban(1) = "sering bersin" Then klausajawaban(1) = aturan(4, 0)
 
If klausajawaban(0) = aturan(3, 0) And klausajawaban(1) = aturan(4, 0) Then
    Console.WriteLine("Penyakit yang diderita adalah " & aturan(1, 1))
    Console.ReadLine()
    Return
End If
#%%Contoh 2 FORWARD CHAINING
global is_changed

is_changed = True
facts = [["plant","mango"],["eating","mango"],["seed","sprouts"]]

def assert_fact(fact):
    global facts
    global is_changed
    if not fact in facts:
        facts += [fact]
        is_changed = True

while is_changed:
    is_changed = False
    for A1 in facts:
        if A1[0] == "seed":
            assert_fact(["plant",A1[1]])
        if A1[0] == "plant":
            assert_fact(["fruit",A1[1]])
        if A1[0] == "plant" and ["eating",A1[1]] in facts:
            assert_fact(["human",A1[1]])

print(facts)
#%%Contoh 2 BACKWARD CHAINING
global is_changed

is_changed = True
facts = [["plant","mango"],["eating","mango"],["seed","sprouts"]]

def assert_fact(fact):
    global facts
    global is_changed
    if not fact in facts:
        facts += [fact]
        is_changed = True

while is_changed:
    is_changed = False
    for A1 in facts:
        if A1[0] == "seed":
            assert_fact(["plant",A1[1]])
        if A1[0] == "plant":
            assert_fact(["fruit",A1[1]])
        if A1[0] == "plant" and ["eating",A1[1]] in facts:
            assert_fact(["human",A1[1]])

print(facts)
