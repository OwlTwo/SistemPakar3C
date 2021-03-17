import os

print("+.......................................+")
print("|\tSelamat Datang di Sistem Pakar\t\t|")
print("|\tDeteksi Gejala Magh dan Usus Buntu\t|")
print("+.......................................+")

nama = input("nama\t: ")
pilihan = input("Hallo "+nama+", \nApakah anda ingin melakukan diagnosa? (y/n) : ")

os.system("cls")

while pilihan == "y" :
    print("Apakah Anda merasakan gejala berikut ini ?")
    print("1. Perut Kembung")
    print("2. Mual")
    print("3. Napsu Makan Menurun")
    print("4. Perut Terasa Sakit")
    ask1 = input("Jawab (y/n) : ")
    
    if ask1 == "y" :
        print("\nApakah anda juga merasakan gejala berikut ini ? ")
        print("1. Naiknya Asam Lambung")
        print("2. Nyeri ulu Hati")
        print("3. Sulit bernapas")
        print("4. Pusing")
        ask2 = input("Jawab (y/n) : ")
            
        if ask2 == "y" :
            print("\nHai, "+nama+" Hasil Diagnosa Kamu adalah : ")
            print("Gejala Magh, Segera ke Dokter")
            
        elif ask2 == "n" :
             print("\nApakah anda juga merasakan gejala berikut ini ? ")
             print("1. Nyeri Perut")
             print("2. Mual")
             print("3. Muntah")
             print("4. Kehilangan Napsu Makan")
             ask3 = input("jawab (y/n) :")
             
             if ask3 == "y" :
                 print("\nHai, "+nama+" Hasil Diagnosa Kamu adalah : ")
                 print("Gejala Usus Buntu, Segera ke Dokter")
            
             elif ask3 == "n" :
                print("\Hi, "+nama+" Sepertinya anda sedang banyak pikiran")
             
             else :
                 print("\nHai, "+nama+" sepertinya Anda tidak perlu berobat")
                 
    elif ask1 == "n" :
        print("\nHai, "+nama+" sepertinya Anda butuh refreshing")
         
    else :
        print("\Hi, "+nama+" Sepertinya anda tidak mau berobat")
         
        print("+.......................................+")
        pilihan = input("Hallo "+nama+", \nApakah anda ingin melakukan diagnosa? (y/n) : ")
     
    if pilihan == "y" :
        os.system("clear")
        print("+.......................................+")
        print("|\tSelamat Datang di Sistem Pakar\t\t|")
        print("|\tDeteksi Gejala Magh dan Usus Buntu\t|")
        print("+.......................................+")
    else :
        print("+.............Terima Kasih...............+")
     
    