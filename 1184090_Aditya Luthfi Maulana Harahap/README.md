# kecerdasanbuatan
Modul Praktikum Kecerdasan Buatan

Tugas 1

Harga batu bata satuan buah
1.600 (A) <= 650 (A).
2.650 (A) <= mahal (A).
3.650 (A), 700 (A) <= sangat mahal (A).
4.650 ("mahal").
5.700 ("mahal ").
6.600 ("standar").

Penjelasan kode python :

1. Kode di bawah ini untuk mendefinisikan variable global dan juga menyimpan nya

global facts
global is_changed

print("Forward")
is_changed = True
facts = [["650","mahal"],["700","mahal"],["600","standar"]]


2. Kode dibawah ini untuk menangkapa data data baru

def assert_fact(fact):
    global facts
    global is_changed
    if not fact in facts:
        facts += [fact]
        is_changed = True

3. Codingan forward fungsinya untuk melooping(perulangan) aturan yang di tetapkan metode forward

while is_changed:
    is_changed = False
    for A1 in facts:
        if A1[0] == "600":
            assert_fact(["650",A1[1]])
        if A1[0] == "650":
            assert_fact(["mahal",A1[1]])
        if A1[0] == "650" and ["700",A1[1]] in facts:
            assert_fact(["sangat mahal",A1[1]])

4. Codingan backward untuk melooping(perulangan) aturan  metode backward

while is_changed:
    is_changed = False
    for A1 in facts:
        if A1[0] == "650" and ["700",A1[1]] in facts:
            assert_fact(["sangat mahal",A1[1]])
        if A1[0] == "650":
            assert_fact(["mahal",A1[1]])
        if A1[0] == "600":
            assert_fact(["650",A1[1]])

