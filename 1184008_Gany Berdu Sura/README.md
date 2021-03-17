A. Pengertian forward chaining
sistem pelacakan ke depan yang memulai dari sekumpulan fakta-fakta dengan mencari kecocokan dengan dugaan/hipotesa yang ada menuju kesimpulan. Seringkali disebutjua bottom-up reasoning atau pertimbangan dari bawah ke atas, karena melihat bukti-bukti atau fakta-fakta dilevel bawah, menuju ke kesimpulan pada level atas yang berdasarkan pada fakta-fakta tersebut

B. rulesnya
1. membuat data dengan value terkait dengan data hewan yang akan dibuat seperti dibawah ini
{ 
        'hair' : True,
        'milk' : False,
        'meat' : False,
        'pointedteeth' : False,
        'claws' : False,
        'forwardeyes' : False,
        'carnivore' : False,
        'mammal' : False,
        'hooves' : False,
        'ungulate' : False,
        'cud' : True,
        'tawny' : False,
        'darkspots' : True,
        'blackstripes' : False,
        'longneck' : True,
        'tiger' : False,
        'giraffe' : False,
        'zebra' : False,
        'cheetah' : False
        }
2.lalu buat logika dengan values yang ada yang bernilai True atau False untuk mendapatkan hasil akhir 
R1 : if hair and mammal than mammal
R2 : if milk and mammal than mammal
R3 : if meat and carnivor than carnivor
dst hingga R10
yang dimana menggunakan Metode append untuk menambahkan satu item ke daftar yang ada. Itu tidak mengembalikan daftar item baru tetapi akan mengubah daftar asli dengan menambahkan item ke akhir daftar. Setelah menjalankan metode, tambahkan pada daftar ukuran daftar bertambah satu. 
Kemudian pada file rbes.py akan membandingkan rule secara forward chaining, sebelum itu sudah di masukan kondisi elif sehingga menyeleksi beberapa kemungkinan yang bisa terjadi pada rules yang sudah dibuat. 
contoh : semisal ditemukan kesamaan value yang memungkinakan antara R1, R6 , dan R9 maka akan di temukan hewan Girrafe begitu juga dengan kesamaan pada value lainnya.


