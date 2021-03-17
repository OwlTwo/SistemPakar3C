# sistempakar
Modul Praktikum Sistem Pakar
Pada script yang sudah saya lampirkan, seperti berikut
#%%Contoh 1 FORWARD CHAINING
global fact
global is_changed

is_changed = True                                                           #Argumen akan bernilai True atau benar jika ia memenuhi kriteria fakta-fakta ini
facts = [["Lesuh","Sakit"],["Meriang","Sakit"],["Bersemangat","Sehat"]]     # jika ia lesuh maka sakit, jika ia meriang maka sakit, dan jika ia bersemangat maka sehat

def assert_fact(fact):                                                      # akan bernilai True atau benar jika memenuhi kriteria fakta di atas
    global facts
    global is_changed
    if not fact in facts:
        facts += [fact]
        is_changed = True

while is_changed:                                                           #namun akan bernilai false atau salah jika tidak memenuhi kriteria fakta di atas
    is_changed = False
    for A1 in facts:                                                        #disini,Algoritma Forward Chaining bersungsi Membuat tujuan / kesimpulan berdasarkan dari   
        if A1[0] == "Bersemangat":                                          #inputan data yang sudah diketahui.
            assert_fact(["Lesuh",A1[1]])                                    #Hasil tujuan akan menjadi data baru dan diproses lagi sampai kepada tujuan akhir atau 
        if A1[0] == "Lesuh":                                                #akhir dari permasalahan.
            assert_fact(["Flu",A1[1]])
        if A1[0] == "Lesuh" and ["Meriang",A1[1]] in facts:
            assert_fact(["Demam",A1[1]])

print(facts)

#Berbeda dengan Forward chaining, backward chaining melakukan hal sebaliknya
#Algoritma Backward Chaining, Mencari data-data berdasarkan tujuan akhir yang sudah diketahui.
#Data tersebut nantinya akan menjadi tujuan baru yang akan dicari data-data nya, sampai kepada data paling awal.
#Jika data paling awal sudah sesuai dengan kriteria inputan, maka tujuan akhir tersebut memang benar.

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
