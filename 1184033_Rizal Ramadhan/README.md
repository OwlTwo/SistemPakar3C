# kecerdasanbuatan
Modul Praktikum Kecerdasan Buatan


Tugas 1 Sistem Pakar

Aturan tinggi badan
1.150 (A) <= 180 (A).
2.180 (A) <= tinggi (A).
3.180 (A), 190 (A) <= sangat tinggi (A).
4.180 ("tinggi").
5.190 ("tinggi").
6.150 ("pendek").

kode di bawah ini untuk mendefinisikan variable global dan juga menyimpan nya

global facts
global is_changed

print("Forward")
is_changed = True
facts = [["180","tinggi"],["190","tinggi"],["150","pendek"]]


dibawah ini untuk menangkapa data data baru

def assert_fact(fact):
    global facts
    global is_changed
    if not fact in facts:
        facts += [fact]
        is_changed = True

dibawah ini adalah codingan forward fungsinya untuk melooping aturan yang di tetapkan metode forward

while is_changed:
    is_changed = False
    for A1 in facts:
        if A1[0] == "150":
            assert_fact(["180",A1[1]])
        if A1[0] == "180":
            assert_fact(["tinggi",A1[1]])
        if A1[0] == "180" and ["190",A1[1]] in facts:
            assert_fact(["sangat tinggi",A1[1]])

dibawah ini adalah codingan backward untuk melooping aturan  metode backward

while is_changed:
    is_changed = False
    for A1 in facts:
        if A1[0] == "180" and ["190",A1[1]] in facts:
            assert_fact(["sangat tinggi",A1[1]])
        if A1[0] == "180":
            assert_fact(["tinggi",A1[1]])
        if A1[0] == "150":
            assert_fact(["180",A1[1]])