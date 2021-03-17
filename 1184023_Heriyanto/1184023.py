#%%Contoh 1 FORWARD CHAINING
global fact
global is_changed

is_changed = True
facts = [["Action","Genre"],["Romance","Genre"],["School","Film"]]

def assert_fact(fact):
    global facts
    global is_changed
    if not fact in facts:
        facts += [fact]
        is_changed = True

while is_changed:
    is_changed = False
    for A1 in facts:
        if A1[0] == "School":
            assert_fact(["Film",A1[1]])
        if A1[0] == "Action":
            assert_fact(["Thriller",A1[1]])
        if A1[0] == "Action" and ["Sadistic",A1[1]] in facts:
            assert_fact(["Surprise",A1[1]])
print("FowardChain")
print(facts)
#%%Contoh 2 BACKWARD CHAINING
global fact
global is_changed

is_changed = True
facts = [["Action","Genre"],["Romance","Genre"],["School","Film"]]

def assert_fact(fact):
    global facts
    global is_changed
    if not fact in facts:
        facts += [fact]
        is_changed = True

while is_changed:
    is_changed = False
    for A1 in facts:
        if A1[0] == "Action" and ["Kill",A1[1]] in facts:
            assert_fact(["Thriller",A1[1]])
        if A1[0] == "Action":
            assert_fact(["Sadis",A1[1]])
        if A1[0] == "Surprise":
            assert_fact(["Shock",A1[1]])
        
print("BackwardChain")     
print(facts)
#%%
from mal import AnimeSearch

print("+---------------------------------+")
print("|\tSelamat Datang di Info Anime\t |")
print("|\t\t\tBy Heriyanto\t\t\t |")
print("+---------------------------------+")

nama=input("Masukan Nama Anda : ")
pilihan=input("\nHi, "+nama+". Apakah Anda ingin melihat info anime? (y/n) : ")

while pilihan == "y":
    print("Masukkan Judul Anime yang ingin Anda Cari")
    print("Contoh : Naruto Shippuden\n")
    
    search = AnimeSearch(input("Judul : "))
    print(search.results[0].title) 
    print(search.results[0].score)
    print(search.results[0].mal_id)
    print(search.results[0].episodes)
    print(search.results[0].url)

    pilihan=input("\nHi, "+nama+". Mau lihat info lagi? (y/n) : ")

    if pilihan=="y":
        print("+---------------------------------+")
        print("|\tSelamat Datang di Info Anime\t |")
        print("|\t\t\tBy Heriyanto\t\t\t |")
        print("+---------------------------------+")

    else:
        print("\n+----------------------Terima Kasih------------------------+")
        print("+--------------Telah Berkunjung di Info Anime--------------+")
    