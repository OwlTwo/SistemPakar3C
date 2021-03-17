# kecerdasanbuatan
Modul Praktikum Kecerdasan Buatan

Tujuan perancangan sistem pakar diagnosa penyakit gigi dan mulut ini adalah untuk merancang dan membangun suatu sistem pakar yang dapat membantu user atau masyarakat untuk memberikan 
prediksi awal tentang penyakit gigi dan mulut yang dialami serta untuk mengetahui tindakan penanganan yang tepat dengan menggunakan forward chaining, yaitu penelusurandimana diketahui fakta 
yang ada untuk menunjang pengambilan kesimpulan. 
Seperti pada aplikasi ini terdapat gejala Gigi terasa ngilu','Gigi terasa berdenyut','Kepala terasa pusing','Terdapat lubang pada gigi','Gusi bengkak',
'Demam (suhu badan diatas 38 derajat)','Bau mulut','Gusi berwarna merah tua','Gusi rentan berdarah','Adanya plak/karang gigi','Mulut terasa kering','Sering dehidrasi','Lapisan lidah terasa tebal','
Cairan ludah berkurang','Adanya benjolan putih/abu','Terasa luka dan pedih','Gigi terasa sakit','Sakit saat mengunyah','Gigi terasa sensitive','Bentuk gigi tampak terkikis','Gigi terasa nyeri saat makan/minum 
panas dan dingin','Ngilu berkepanjangan (pada gigi)','Gusi menurun','Sakit setelah pencabutan gigi','Sakit sampai kepala,telinga,mata,leher','Gigi tidak sejajar','Perubahan pada wajah','Tidak nyaman ketika ngunyah dan menggigit','
Merasa tidak enak pada mulut','Gigi longgar','Lidah membesar','Nyeri pada lidah','Perubahaan warna pada lidah','Permukaan ldah licin','Warna permukaan lidah kemerahan','Gigi terlihat jarang- jarang','Gigi terlihat tonggos kedepan','
Ukuran gigi dan rahan tidak sesuai','Adanya bercak pada sudut bibir','Bercak terasa gatal nyeri dan panas pada bibir','Bila di raba, bercak terasa keras pada bibir','Kadang bercak juga bisa berdarah pada bibir','Cadel',
'Gigi sulung copot sebelum waktunya (prematur).
daftarPenyakit seperti 'Karies gigi (gigi berlubang)','Gingvitis (radang gusi)','Lidah putih','Stomatitis (sariawan)','Abses gigi (gusi bengkak/nanah)',
'Abrasi gigi (hilangnya struktur gigi)','Gigi sensitive','Alveolar osteitis (peradangan)',
'Maloklusi (gigi berdesakan)','Resesi gusi (penurunan gusi)','Gloositis (radang lidah)','Crowded (gigi berjejal)','Cheilitis (radang bibir).
olusiPenyakit = ['Tambal Gigi, Perawatan Saluran akar gigi, dan Cabut gigi','Obat pereda nyeri,Obat kumur, dan Obat antibiotik','Minum banyak air untuk membantu menghilangkan bakteri dan Menyikatnya dengan pembersih lidah khusu',
'Pengobatan stomatitis aftosa,Pengobatan stomatitis herpes','Perawatan saluran akar (root canal),Cabut gigi','Pembuatan Mahkota Gigi (Crown),Penambalan Gigi','Menggosok Gigi dengan benar,Hindari makanan dan minuman asam',
'Pemberian obat kumur atau gel antibakteri segera sebelum dan sesudah operasi,Pemberian larutan antiseptik diberikan pada luka','Pasang kawat gigi,Cabut gigi','Perawatan dengan scaling dan root planning','Menjaga kesehatan rongga 
mulut dengan cara menyikat gigi dua kali sehari (setelah sarapan dan sebelum tidur),Perubahan pola makan untuk mengatasi permasalahan nutrisi yang dapat menjadi penyebab terjadinya glositis','Perawatan orthodonsi','Salep anti jamur,Salep antibakteri'.

Cara kerja Program :
def checkGejala():
    if request.form.get('pilihan') == 'ya':
        return True
    if request.form.get('pilihan') == 'tidak':
        return False
    else:
        return checkGejala()
= Memasukka fungsi gejala apabila dari pilihan diatas benar maka akan menampilkan gejalanya 
    dan apabila salah maka tidak ada gejala.

def welcome():
   if request.method == 'POST':
      name = request.form.get('Name')
      session['namaPasien'] = name
      gejalanya = session['gejalaPasien']
      pertanyaan = daftarGejala[gejalanya]
      return render_template("welcome.html", name = name,  pertanyaan = pertanyaan, link = url_for('index'))
= fungsi diatas untuk menginput nama pasian dan gejala serta pertanyaan yang diisampaikan.

def result():
   if request.method == 'POST':
      if session['logs'] == 0 and checkGejala():
         if session['gejalaPasien'] == 0: # Gejala 1
            session['gejalaPasien'] = 1
            session['logs'] = 1
            return redirect(url_for('diagnosa'))
= Dari Fungsi result apabila mehtod post maka akan mangecek gejala apakah itu gejalan 1 atau gejala lainnya.