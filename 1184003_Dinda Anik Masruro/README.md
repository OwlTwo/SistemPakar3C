# kecerdasanbuatan
Modul Praktikum Kecerdasan Buatan
Nama : Dinda Anik Masruro
NPM : 1184003
Kelas : D4 TI 3C
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
#Kondisi dimana menerima masukkan dengan 2 pilihan y/n
'Aturan 1
If input2 = "y" And jawaban = "suhu badan naik" Then jawaban = aturan(0, 1)
#Kondisi dimana menerima masukkan dengan 2 pilihan y/n
'Aturan 4
If input = "n" And input2 = "y" Then jawaban = aturan(3, 1)
#Kondisi dimana menerima masukkan dengan 2 pilihan y/n
'Aturan 5
If input3 = "y" And jawaban = "batuk" Then jawaban = aturan(4, 1)
#Kondisi dimana menerima masukkan dengan 2 pilihan y/n
'Aturan 2
If jawaban = "sering bersin" Then jawaban = aturan(1, 1)
#Kondisi kode program yang akan dieksekusi jika Kondisi bernilai benar
If jawaban = "demam" Or jawaban = "flu" Then
    Console.WriteLine("Penyakit yang diderita adalah " & jawaban)
#Ini adalah fungsi untuk menampilkan output 
End If
#kondii digunakan untuk memilih suatu kondisi apakah bernilai benar (true) atau salah (false).
#%%Contoh 1 BACKWARD CHAINING
jawaban = aturan(0, 1)
'Aturan 1
If input2 = "y" And jawaban = "demam" Then jawaban = aturan(0, 0)
#Kondisi dimana menerima masukkan dengan 2 pilihan y/n
'Aturan 3
If input = "y" And jawaban = "suhu badan naik" Then jawaban = aturan(2, 0)
#Kondisi dimana menerima masukkan dengan 2 pilihan y/n 
If jawaban = aturan(2, 0) Then
    Console.WriteLine("Penyakit yang diderita adalah " & aturan(0, 1))
#Ini adalah fungsi untuk menampilkan output 
    Console.ReadLine()
#ini adalah fungsi untuk memberi nilai dan memasukkan data
    Return
#mengakhri eksekusi dari function
End If
#kondii digunakan untuk memilih suatu kondisi apakah bernilai benar (true) atau salah (false).
jawaban = aturan(1, 1)
'Aturan 2
If input = "n" Then jawaban = aturan(1, 0)
#Kondisi dimana menerima masukkan dengan 2 pilihan y/n
Dim klausajawaban(1) As String
#klausa jawaban alias string
If jawaban = aturan(1, 0) Then
    klausajawaban(0) = aturan(3, 1)
    klausajawaban(1) = aturan(4, 1)
#Kondisi dimana menerima masukkan dengan beberapa alias atau pilihan jawaban
End If
#kondii digunakan untuk memilih suatu kondisi apakah bernilai benar (true) atau salah (false).
'Aturan 4
If input2 = "y" And klausajawaban(0) = "batuk" Then klausajawaban(0) = aturan(3, 0)
#Kondisi dimana menerima masukkan dengan 2 pilihan y/n
'Aturan 5
If input3 = "y" And klausajawaban(1) = "sering bersin" Then klausajawaban(1) = aturan(4, 0)
#Kondisi dimana menerima masukkan dengan 2 pilihan y/n 
If klausajawaban(0) = aturan(3, 0) And klausajawaban(1) = aturan(4, 0) Then
#Kondisi dimana menerima masukkan dengan 2 pilihan y/n
    Console.WriteLine("Penyakit yang diderita adalah " & aturan(1, 1))
#Ini adalah fungsi untuk menampilkan output 
    Console.ReadLine()
#ini adalah fungsi untuk memberi nilai dan memasukkan data
    Return
#mengakhri eksekusi dari function
End If
#kondii digunakan untuk memilih suatu kondisi apakah bernilai benar (true) atau salah (false).
#%%Contoh 2 FORWARD CHAINING
global is_changed
#Untuk mendefinisikan variable secara global

is_changed = True
#variable bernilai atau sama dengan true
facts = [["plant","grape"],["eating","grape"],["seed","sprouts"]]
#untuk menampilkan fakta

def assert_fact(fact):
#Mendefinisikan fungsi asseet-fact
    global facts
#untuk mendefinisikan fakta secara global
    global is_changed
#Untuk mendefinisikan variable secara global
    if not fact in facts:
        facts += [fact]
        is_changed = True
#mendefinisikan variable jika bernilai benar

while is_changed:
#untuk nemapilkan kondisi sementara dari variable
    is_changed = False
#variable sama dengan false
    for A1 in facts:
#Untuk A1 merupakan fakta
        if A1[0] == "seed":
            assert_fact(["plant",A1[1]])
        if A1[0] == "plant":
            assert_fact(["fruit",A1[1]])
        if A1[0] == "plant" and ["eating",A1[1]] in facts:
            assert_fact(["human",A1[1]])
#merupakan beberapa pilihan pada fungsi asseet-fact
print(facts)
#hasil dari fakta

#%%Contoh 2 BACKWARD CHAINING
global is_changed
#Untuk mendefinisikan variable secara global
is_changed = True
#variable bernilai atau sama dengan true
facts = [["plant","grape"],["eating","grape"],["seed","sprouts"]]
#untuk menampilkan fakta
def assert_fact(fact):
#Mendefinisikan fungsi asseet-fact
    global facts
#untuk mendefinisikan fakta secara global
    global is_changed
#Untuk mendefinisikan variable secara global
    if not fact in facts:
        facts += [fact]
        is_changed = True
#mendefinisikan variable jika bernilai benar

while is_changed:
#untuk nemapilkan kondisi sementara dari variable
    is_changed = False
#variable sama dengan false
    for A1 in facts:
#Untuk A1 merupakan fakta
        if A1[0] == "seed":
            assert_fact(["plant",A1[1]])
        if A1[0] == "plant":
            assert_fact(["fruit",A1[1]])
        if A1[0] == "plant" and ["eating",A1[1]] in facts:
            assert_fact(["human",A1[1]])
#merupakan beberapa pilihan pada fungsi asseet-fact
print(facts)
#hasil dari fakta
