# Sistem Pakar
Sistem Pakar Foward Chain  & Backward Chain

mendefinisikan variable global dan juga menyimpan nya

global facts
global is_changed

print("Forward")
is_changed = True
facts = [["Tinju","Samsak"],["Tendang","Samsak"],["silat","beladiri"]]


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
        if A1[0] == "silat":
            assert_fact(["beladiri",A1[1]])
        if A1[0] == "Tinju":
            assert_fact(["pukulan",A1[1]])
        if A1[0] == "Tinju" and ["Tendang",A1[1]] in facts:
            assert_fact(["gerakan",A1[1]])

codingan backward untuk melakukan looping dari aturan yang ada di metode backward tersebut

while is_changed:
    is_changed = False
    for A1 in facts:
        if A1[0] == "Tinju" and ["Tendang",A1[1]] in facts:
            assert_fact(["gerakan",A1[1]])
        if A1[0] == "Tinju":
            assert_fact(["pukulan",A1[1]])
        if A1[0] == "silat":
            assert_fact(["beladiri",A1[1]])
        
Algoritma Backward Chaining, Mencari data-data berdasarkan tujuan akhir yang sudah diketahui.
Jika data paling awal sudah sesuai dengan kriteria inputan, maka tujuan akhir tersebut memang benar.