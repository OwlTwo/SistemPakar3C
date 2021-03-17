import os


print("\t\tSelamat Datang toko komuter\t\t ")
print("\tUntuk Menentukan Spesifikasi Personal Komputer \t ")
print("Sebagai Pengambil Keputusan Dalam Pembelian Komputer")


nama=input("Masukan Nama Anda : ")
pilihan=input("\nHi, "+nama+". Apakah Anda Mau Membeli Personal Komputer? (y/n) : ")

os.system("clear")

while pilihan == "y":
  print("\nKebutuhan/Kriteria yang diinginkan (DATA 1)\n")
  print("\ta.	Dana yang di sediakan < 3 Jt")
  print("\tb.	Dana yang di sediakan  3-5 Jt")
  print("\tc.	Dana yang di sediakan > 5 Jt")
  print("\td.	Komputer untuk mengetik")
  print("\te.	Komputer untuk game")
  print("\tf.	Komputer untuk grafis")
  print("\tg.	Butuh akses internet")
  print("\th.	Ruangan ber AC")
  print("\ti.	Senang musik")
  print("\tj.	Senang menonton film\n")
  print("Pilihlah Kebutuhan/Kriteria PC yang anda inginkan")
  print("Contoh : anda membutuhkan pc dengan keriteria/kebutuhan pada point a,d,f,g,h,i,j. Maka anda hanya perlu menginputkan a,d,f,g,h,i,j\n")

  beli=input("Masukan Kebutuhan/Kriteria yang anda inginkan : ")

  if beli == "a,d,g,h,i,j" :
    print("\nPaket Ekonomis 1 dengan harga Rp. 2.450.000\n")
    print("Dengan Spesifikasi Seperti Berikut :\n")
    print("\ta.	Gigabyte GA8VM800 PMD")
    print("\tb.	Intel Celleron 2,66 GHZ")
    print("\tc.	DDR 128 Mb PC 3200")
    print("\td.	VGA Integrated")
    print("\te.	HD 80 Gb SATA")
    print("\tf.	CD ROM 52X Samsung")
    print("\tg.	CRT 15” Samsung 591")
    print("\th.	Casing ATX  400W")
    print("\ti.	Speaker Simbadda CST 6000")
    print("\tj.	Modem Prolink Internal\n")

  elif beli == "a,d":
    print("\nPaket Ekonomis 2 dengan harga Rp. 2.550.000\n")
    print("Dengan Spesifikasi Seperti Berikut :\n")
    print("\ta.	Asus P5PE-VM")
    print("\tb.	Intel Celleron 2.26 GHZ")
    print("\tc.	DDR 128 Mb PC 3200")
    print("\td.	VGA Integrated")
    print("\te.	HD 40 Gb SATA")
    print("\tf.	CD ROM 52X Samsung")
    print("\tg.	CRT 15” Samsung 591")
    print("\th.	Casing ATX  400W\n")

  elif beli== "a,e,h,i,j":
    print("\nPaket Ekonomis 3 dengan harga Rp. 2.750.000\n")
    print("Dengan Spesifikasi Seperti Berikut :\n")
    print("\ta.	Asus K8V-VM")
    print("\tb.	AMD Sempron 2800+")
    print("\tc.	DDR 256 Mb PC 3200")
    print("\td.	VGA Integrated")
    print("\te.	HD 80 GB SATA")
    print("\tf.	CD ROM 52X LG")
    print("\tg.	CRT 15” Advance")
    print("\th.	Casing ATX 400W")
    print("\ti.	Speaker Simbadda CST 6000\n")

  elif beli== "a,e,g,h,i,j":
    print("\nPaket Ekonomis 4 dengan harga Rp. 2.900.000\n")
    print("Dengan Spesifikasi Seperti Berikut :\n")
    print("\ta.	Gigabyte K8VM800")
    print("\tb.	AMD Sempron 2800+")
    print("\tc.	DDR 256 Mb PC 3200")
    print("\td.	VGA Integated")
    print("\te.	HD 80 Gb SATA")
    print("\tf.	CD ROM 52X LG")
    print("\tg.	CRT 15” Advance")
    print("\th.	Casing ATX 400W")
    print("\ti.	Speaker Simbadda CST 6000")
    print("\tj.	Modem Prolink Internal\n")



  else :
    print("Kombinasi Kebutuhan/Kriteria yang anda masukan\nbelum terdaftar pada perpustkaan pengetahuan sistem")

  print("+----------------------------------------------------+")
  pilihan=input("\nHi, "+nama+". Apakah Anda Mau Membeli Personal Komputer, Lagi? (y/n) : ")

  if pilihan=="y":
    os.system("clear")
    print("\t\tSelamat Datang toko komuter\t\t ")
    print("\tUntuk Menentukan Spesifikasi Personal Komputer \t ")
    print("Sebagai Pengambil Keputusan Dalam Pembelian Komputer")
  
  else :
    print("\n+ Terima Kasih Telah datang di toko kami")

