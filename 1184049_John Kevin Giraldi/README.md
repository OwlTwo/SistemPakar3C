# kecerdasanbuatan
Modul Praktikum Kecerdasan Buatan


Tugas 1 Sistem Pakar

Aturan berat badan
1.45 (A) <= 50 (A).
2.50 (A) <= berat (A).
3.50 (A), 70 (A) <= sangat berat (A).
4.50 ("berat").
5.70 ("berat").
6.45 ("ringan").

kode di bawah ini untuk mendefinisikan variable global dan juga menyimpan nya

global facts
global is_changed

print("Forward")
is_changed = True
facts = [["50","berat"],["70","berat"],["45","ringan"]]


dibawah ini untuk menangkap data data baru

def assert_fact(fact):
    global facts
    global is_changed
    if not fact in facts:
        facts += [fact]
        is_changed = True

dibawah ini adalah code forward fungsinya untuk melooping aturan yang di tetapkan metode forward

while is_changed:
    is_changed = False
    for A1 in facts:
        if A1[0] == "45":
            assert_fact(["50",A1[1]])
        if A1[0] == "50":
            assert_fact(["berat",A1[1]])
        if A1[0] == "50" and ["70",A1[1]] in facts:
            assert_fact(["sangat berat",A1[1]])

dibawah ini adalah codingan backward untuk melooping aturan  metode backward

while is_changed:
    is_changed = False
    for A1 in facts:
        if A1[0] == "50" and ["70",A1[1]] in facts:
            assert_fact(["sangat berat",A1[1]])
        if A1[0] == "50":
            assert_fact(["berat",A1[1]])
        if A1[0] == "45":
            assert_fact(["50",A1[1]])