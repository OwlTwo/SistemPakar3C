# SistemPakar
Modul Praktikum Sistem Pakar
Mauliddhia Restu Shafina 1184101 D4 TI 3C

Aturan dan Fakta

monokotil ==> dikotil
monokotil ==> nanas
monokotil, buah ==> manis
monokotil ("nanas")
buah ("nanas")
dikotil ("kentang")

#Forward Chain
untuk mendefinisikan variable dan menyimpan variabel global menggunakan kode 
global facts
global is_changed
is_changed = True
facts = [["monokotil","nanas"],["buah","nanas"],["dikotil","kentang"]]

Untuk menyimpan fakta baru, maka dibaut perulangan seperti kode dibawah ini
def assert_fact(fact):
    global facts
    global is_changed
    if not fact in facts:
        facts += [fact]
        is_changed = True

Fakta dan aturan yang telah dibuat, akan dilooping dengan kode dibawah agar bisa menemukan fakta baru 
pada metode Forward Chain
while is_changed:
    is_changed = False
    for A1 in facts:
        if A1[0] == "buah":
            assert_fact(["monokotil",A1[1]])
        if A1[0] == "dikotil":
            assert_fact(["sayur",A1[1]])
        if A1[0] == "monokotil" and ["buah",A1[1]] in facts:
            assert_fact(["manis",A1[1]])

Nah, untuk menampilkan hasil kode diatas gunakan kode print seperti dibawah ini
print("FowardChain")
print(facts)

#Backward Chain

Kode backward chain sama dengan kode forward chain, yang membedakan hanyalah kondisi loopingnya. 

Fakta dan aturan yang telah dibuat, akan dilooping dengan kode dibawah agar bisa menemukan fakta baru 
pada metode Backward Chain
while is_changed:
    is_changed = False
    for A1 in facts:
        if A1[0] == "monokotil" and ["buah",A1[1]] in facts:
            assert_fact(["manis",A1[1]])
        if A1[0] == "dikotil":
            assert_fact(["sayur",A1[1]])
        if A1[0] == "monokotil":
            assert_fact(["buah",A1[1]])
        