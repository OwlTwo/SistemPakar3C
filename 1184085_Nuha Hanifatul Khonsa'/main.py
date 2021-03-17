import os

print("+-----------------------------------------------+")
print("|\tSelamat Datang di Aplikasi Sistem Pakar\t|")
print("|\t\tKesehatan Psikologi\t\t\t|")
print("+-----------------------------------------------+")
nama = input("Nama\t: ")
pilihan = input("Hallo " +nama+",\nApakah anda ingin melakukan diagnosa ? [y/n]")

os.system("cls")

while pilihan =="y" :
    print("\nApakah anda merasa gelisah, susah tidur, pikiran kacau dan merasa takut ?")
    diagA1 = input("Jawab (y/n) : ")
    if diagA1 == "n" :
        print("\nApakah anda merasa ada perubahan suasana perasaan anda ?")
        s = input("Jawab (y/n) : ")
        if s == "y" :
            print("\nApakah Merasa dibawah kendali kesadaran anda?")
            sy = input("Jawab(y/n) :")
            #disosiatif
            if sy == "y" :
                print("\nApakah anda merasa tidak berguna?")
                s1 = input("Jawab(y/n) :")
                if s1 == "y" :
                    print("\nApakah anda ")
                    print("1. Merasa Harga dirinya rendah?\n2. Pernah berfikiran untuk mengakhiri hidupnya?")
                    print("3. sering mengalami sakit kepala?\n4. mengalami perasaan tidak nyata?")
                    k1 = input("Jawab (y/n) :")
                    if k1 == "y" :
                        print("\nHi, "+nama+" hasil awal diagnosa kamu adalah :")
                        print("Gangguan Desosiatif")
                        print("Gangguan disosiatif adalah kelainan mental yang melibatkan pemutusan dan tidak adanya kontinuitas antara pikiran, ingatan, tindakan, hingga identitas. Seseorang yang mengalami gangguan ini berusaha melarikan diri dari kenyataan dengan cara yang tidak ")
                        print("1. Terapi kesenian kreatif\n2. Terapi Kognitif\n3. Psikonalis")
                    elif k1 == "n" :
                        print("Silahkan diagnosa ulang")
                elif s1 == "n" :
                    print("\nApakah anda mudah marah?")
                    s2 = input("Jawab(y/n) :")
                    if s2 == "y" :
                        print("\nApakah anda ")
                        print("1. Sulit untuk berteman?\n2. selalu merasa sedih?")
                        print("3. selalu curiga terhadap orang lain?")
                        k2 = input("Jawab (y/n) :")
                        if k2 == "y" :
                            print("\nHi, "+nama+" hasil awal diagnosa kamu adalah :")
                            print("Gangguan Depresif")
                            print("Depresi merupakan gangguan kesehatan mental yang ditandai dengan suasana hati yang terus-menerus merasa tertekan atau kehilangan minat dalam beraktivitas, sehingga mengakibatkan penurunan kualitas hidup sehari-hari.")
                            print("1. Psikoterapi\n2. Cognitive behavior therapy (CBT)\n3. Problem-solving therapy (PST)")
                        elif k2 == "n" :
                            print("Silahkan diagnosa ulang")
                elif s2 == "n":
                    print("\nApakah Anda merasa mual?")
                    s3 = input("Jawab(y/n) :")
                    if s3 == "y" :
                        print("\nApakah anda ")
                        print("1. muntah?\n2. kembung?")
                        print("3. merasa pandangannya ganda?")
                        k3 = input("Jawab (y/n) :")
                        if k3 == "y" :
                            print("\nHi, "+nama+" hasil awal diagnosa kamu adalah :")
                            print("Gangguan Kepribadian")
                            print("Gangguan kepribadian khas adalah suatu gangguan berat dalam konstitusi karakter dan kecenderungan perilaku dari individu. Biasanya meliputi beberapa bidang dari kepribadian dan hampir selalu berhubungan dengan kekacauan pribadi dan sosial.")
                            print("Untuk mengatasi gangguan kepribadian adalah dengan melakukan terapi psikologis atau kejiwaan di bawah bimbingan psikiater dengan tujuan meningkatkan kemampuan pasien dalam mengendalikan emosi serta pikirannya secara lebih baik.")
                        elif k3 == "n" :
                            print("Silahkan diagnosa ulang")
                elif s4 == "n":
                    print("\nApakah Anda merasa cemas?")
                    s4 = input("Jawab(y/n) :")
                    if s4 == "y" :
                        print("\nApakah anda ")
                        print("1. mudah tersinggung?\n2. persepsinya berlebihan pada suatu bagian tubuhnya?")
                        print("3. merasa sakit/nyeri pada tubuh?")
                        k4 = input("Jawab (y/n) :")
                        if k4 == "y" :
                            print("\nHi, "+nama+" hasil awal diagnosa kamu adalah :")
                            print("Gangguan Somatoform")
                            print("Ciri utama gangguan ini adalah keluhan-keluhan gejala fisik yang disertai permintaan permintaan medik, meskipun sudah berkali-kali terbukti hasilnya negatif dan juga telah dijelaskan oleh dokternyabahwa tidak terjadi kelainan yang mendasari keluhannya.")
                            print("Untuk menangani gejala akibat gangguan somatoform, dianjurkan untuk mengatasi terlebih dahulu masalah kesehatan mental yang mendasarinya. Dokter bisa memberikan resep obat antidepresan, terutama bagi penderita yang mengalami kondisi psikologis tertentu, seperti depresi atau gangguan cemas")
                        elif k4 == "n" :
                            print("\nApakah anda ")
                            print("1. sering kencing?\n2. sulit kencing?")
                            print("3. sesak nafas?\n4. keringat dingin?")
                            k5 = input("Jawab (y/n) :")
                            if k5 == "y" :
                                print("\nHi, "+nama+" hasil awal diagnosa kamu adalah :")
                                print("Gangguan Cemas menyeluruh")
                                print("Gangguan cemas menyeluruh adalah suatu kekhawatiran yang berlebihan dan dihayati disertai berbagai gejala somatik, yang menyebabkan gangguan bermakna dalam fungsi sosial atau pekerjaan atau penderitaan yang jelas bagi pasien.")
                                print("Terapi untuk gangguan cemas menyeluruh adalah terapi farmakologis berupa obat anti anxietas dan psikoterapi. Prognosis penyakit ini baik, namun ini adalah kondisi yang kronis. Pada beberapa pasien dapat terjadi remisi gejala, namun dapat muncul kembali. Pada beberapa pasien dapat terjadi gangguan depresi mayor selama hidup. ")
                            elif k5 == "n" :
                                print("Silahkan diagnosa ulang")
            elif sy == "n" :
                print("\nApakah Anda sulit untuk berbicara?")
                r = input("Jawab(y/n) :")
                if r == "y" :
                    print("\nApakah anda ")
                    print("1. mengkonsumsi obat penenang?\n2. tidak mampu mengenali hal-hal yang baru?")
                    print("3. mengalami hambatan pada pekerjaan?\n4. tidak mampu membayangkan masa depan?")
                    k6 = input("Jawab (y/n) :")
                    if k6 == "y" :
                        print("\nHi, "+nama+" hasil awal diagnosa kamu adalah :")
                        print("Gangguan Amnesia")
                        print("Gangguan amnesia adalah suatu gangguan daya ingat yang ditandai adanya gangguan kemampuan mempelajari hal-hal baru atau mengingat hal-hal yang telah dipelajari sebelumnya serta menimbulkan hambatan pada fungsi sosial dan pekerjaan.")
                        print("Terapi okupasi. Terapi jenis ini mengajarkan pasien untuk mengenalkan informasi baru dengan ingatan yang masih ada.")
                    elif k6 == "n" :
                        print("\nHi, "+nama+" hasil awal diagnosa kamu adalah :")
                        print("Silahkan diagnosa ulang")
                elif r == "n" :
                    print("\nApakah Anda tidak mengenal dimana anda tinggal sekarang?")
                    r1 = input("Jawab(y/n) :")
                    if r1 == "y" :
                        print("\nApakah anda ")
                        print("1. percaya terhadap hal-hal yang aneh?\n2. mudah tersinggung?")
                        print("3. suka berhalusinasi?\n4. susah makan?")
                        print("5. sulit mandi?")
                        k7 = input("Jawab (y/n) :")
                        if k7 == "y" :
                            print("\nHi, "+nama+" hasil awal diagnosa kamu adalah :")
                            print("Gangguan Demensia")
                            print("Demensia merupakan sindrom yang ditandai oleh berbagai gangguan fungsi kognitif tanpa gangguan kesadaran. Gangguan fungsi kognitif antara lain pada inteligensi, belajar dan daya ingat, bahasa, pemecahan masalah, orientasi, persepsi, perhatian dan konsentrasi, penyesuaian dan kemampuan bersosialisasi.")
                            print("Demensia bisa diatasi dengan mengonsumsi obat-obatan tertentu, serta melakukan terapi psikologis seperti terapi stimulasi kognitif dan orientasi realitas, perilaku, okupasi, dan validasi. Selain terapi-terapi tersebut, terdapat juga beberapa terapi pendukung yang dapat dilakukan di rumah, seperti terapi musik, aromaterapi, pijat, bermain dengan hewan peliharaan, hingga melakukan aktivitas seni.")
                        elif k7 == "n" :
                            print("Silahkan diagnosa ulang")
                    elif r1 == "n" :
                        print("\nApakah Anda terganggu daya ingatnya?")
                        r2 = input("Jawab(y/n) :")
                        if r2 == "y" :
                            print("\nApakah anda ")
                            print("1. lupa dengan identitas anda?\n2. sering berilusinasi?")
                            print("3. susah berkonsentrasi?")
                            k8 = input("Jawab (y/n) :")
                            if k8 == "y" :
                                print("Gangguan Delirium")
                                print("Delirium adalah suatu sindrom dengan gejala pokok adanya gangguan kesadaran yang biasanya tampak dalam bentuk hambatan pada fungsi kognitif")
                                print("Dokter akan menyarankan untuk menghentikan atau mengurangi dosis obat tersebut. Setelah itu, penanganan ditujukan untuk menciptakan lingkungan yang sesuai bagi pemulihan tubuh dan menenangkan pikiran penderita.")
                        elif r2 == "n":
                            print("\nHi, "+nama+" hasil awal diagnosa kamu adalah :")
                            print("NORMAL")
    elif diagA1 == "y" :
        print("\nApakah Anda merasa cepat lelah?")
        b = input("Jawab(y/n) :")
        if b == "y" :
            print("\nApakah anda ")
            print("1. Suka menyendiri?\n2. Berkeinginan menjauhkan diri dari masyarakat?")
            print("3. Berprasangka buruk?\n4. Selalu merasa salah?")
            b1 = input("Jawab (y/n) :")
            if b1 == "y" :
                print("\nHi, "+nama+" hasil awal diagnosa kamu adalah :")
                print("Gangguan Afektif")
                print("Gangguan afektif adalah gangguan dengan gejala utama adanya perubahan suasana perasaan (mood) atau efek, biasanya ke arah depresi dengan atau tanpa ansietas yang menyertainya, atau ke arah elasi (suasana perasaan meningkat).")
                print("Pasien yang mengalami depresi harus diberikan perawatan dengan menjaga keamanan pasien, pemeriksaan diagnostik, menurunkan stresor pasien. Hasil maksimal diperoleh jika pasien mendapatkan perawatan beruma farmakoterapi dan psikoterapi")
            elif b1 == "n" :
                print("Silahkan diagnosa ulang")
        elif b == "n":
            print("\nApakah anda ")
            print("1. tidak mampu menampakkan emosinya?\n2. kurang dalam dorongan beraktifitas?")
            print("3. tidak dapat menikmati kegiatan yang disenanginya?\n4. Kurang mampu berbicara?")
            b2 = input("Jawab (y/n) :")
            if b2 == "y" :
                print("\nHi, "+nama+" hasil awal diagnosa kamu adalah :")
                print("Gangguan Skizofrenia")
                print("Skizofrenia adalah sekelompok gangguan psikotik dengan gangguan dasar pada kepribadian, distorsi khas proses pikir, kadang- kadang mempunyai perasaan bahwa dirinya sedang dikendalikan oleh kekuatan dari luar dirinya, waham yang yang kadang-kadang aneh, gangguan persepsi, afek abnormal yang terpadu dengan situasi nyata atau sebenarnya dan autisme")
                print("Skizofrenia dapat diobati dengan menggunakan beberapa cara, seperti mengombnasikan obat-obatan melalui terapi psikologis. Obat dengan resep pada pengobatan skizofrenia ini adalah antipsikotik yang dapat memengaruhi zat neurotransmiter didalam otak, yang bisa menurunkan rasa cemas, menurunkan atau mencegah halusinasi dan membantu menjaga kemampuan berpikir.")
            elif b2 == "n" :
                print("Silahkan diagnosa ulang")
    else :
        print("\nHi, "+nama+" silahkan pulang")
    print("+-----------------------------------------------+")
    pilihan = input("Hallo" +nama+",\nApakah anda ingin melakukan diagnosa ? [y/n]")
    if pilihan == "y" :
        os.system("cls")
    print("+----------------------Terimakasih-------------------+")
