PENJELASAN SISTEM PAKAR DIAGNOSA PENYAKIT KULIT 

Sistem pakar ini menggunakan python dan digunakan untuk mendiagnosa penyakit kulit menggunakan forward chaining.  
Forward Chaining merupakan strategi yang digunakan dalam Sistem Pakar untuk mendapatkan kesimpulan/keputusan dari fakta yang ada
Sistem Pakar Diagnosis bisa sangat membantu dalam mengidentifikasi penyakit tersebut dan menjelaskan metode pengobatan yang akan dilakukan.

Untuk menjalankannya harus menginstall library experta dan matplotlib

variabel global : variabel yang bisa diakses dari semua fungsi

#Gejala :

terdapat 15 fungsi yang akan menampilkan opsi Ya / Tidak untuk melanjutkan ke proses penalaran


@Rule(Fact(action='find_disease'), NOT(Fact(kulit_membengkak=W())),salience = 1)

Fact adalah unit dasar informasi Experta yang digunakan oleh sistem untuk menalar masalah yang ada.

Aturan Gejala 1:
@Rule(Fact(action='find_disease'),Fact(kulit_membengkak="yes"),Fact(benjolan_di_kulit="yes"),
		  Fact(mengeluarkan_nanah="no"),Fact(demam="no"),Fact(mata_merah="no"),Fact(kulit_kepala_berminyak="no"),
		  Fact(rasa_gatal="no"),Fact(luka_dari_bagian_mulut="no"),Fact(memiliki_gelembung_berisi_air="no"),
		  Fact(rasa_nyeri="no"),Fact(kulit_melepuh="no"),Fact(memiliki_bercak_bercak_merah="no"),Fact(iritasi_kulit="no"),
		  Fact(uban_muncul_sebelum_waktunya="no"),Fact(muncul_keringat_berlebihan="no"),
		  Fact(menimbulkan_warna_kekuningan="no"))

Maka fungsi disease_0 akan terpanggil yaitu Penyakit Kulit " Jerawat "

def disease_0(self):
		self.declare(Fact(disease="Jerawat"))

Pada sistem ini terdapat 12 diseases/ penyakit

@Rule(Fact(action='find_disease'),Fact(disease=MATCH.disease),salience = -998) 

untuk mencari penyakit dengan tingkat kecocokan yang mendekati sistem akan menemukan kemungkinan penyakit yang ada beserta saran pengobatan.
apabila fungsi tidak menunjukkan kecocokkan dengan gejala dari fakta yang ada maka diagnosis tidak dapat dilakukan dan sistem akan menampilkan penyakit tidak ditemukan

