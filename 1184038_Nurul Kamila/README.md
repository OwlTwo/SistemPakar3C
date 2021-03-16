# kecerdasanbuatan
Modul Praktikum Kecerdasan Buatan
    Sub Main()
        Console.WriteLine("Penentuan jenis penyakit")                                 #jadi ini merupakan kuisioner untuk menentukan penyakit
        Console.WriteLine("Diasumsikan ada beberapa aturan jenis penyakit, yaitu: ")  #Ada beberapa fakta  dalam menentukan jenis penyakitnya
        Console.WriteLine("1. Apabila suhu badan naik maka demam.")                   
        Console.WriteLine("2. Apabila batuk dan sering bersin maka flu.")
        Console.WriteLine("3. Apabila badan lemas maka suhu badan naik.")
        Console.WriteLine("4. Apabila tenggorokan gatal / sakit maka batuk.")
        Console.WriteLine("5. Apabila sering bersin maka sering bersin.")

        Dim aturan(4, 1) As String                                                      #Ada beberapa aturan juga atau perumpamaan dalam menentukan jenis penyakitnya
        aturan(0, 0) = "suhu badan naik"
        aturan(0, 1) = "demam"
        aturan(1, 0) = "batuk dan sering bersin"
        aturan(1, 1) = "flu"
        aturan(2, 0) = "badan lemas"
        aturan(2, 1) = "suhu badan naik"
        aturan(3, 0) = "tenggorokan gatal / sakit"
        aturan(3, 1) = "batuk"
        aturan(4, 0) = "sering bersin"
        aturan(4, 1) = "sering bersin"

        '1. Membuat Kuisioner dengan jawaban y/n                                           #Kuisioner ini dibuat dengan jawaban y/n (ya atau tidak) 
        'Data-data ini nantinya akan diproses oleh algoritma diatas.
        Dim input As String = "", input2 As String = "", input3 As String = ""

        Console.WriteLine("Apakah badan lemas? (y/n)")                           #Pertanyaan pertama yaitu "Apakah badan lemas? " 
        input = Console.ReadLine                                                 #jika anda memilih y maka pertanyaan akan beralih ke "Apakah suhu badan naik?"
        If input = "y" Then
            Console.WriteLine("Apakah suhu badan naik? (y/n)")                       #jika anda menjawab n maka solusi tidak ditemukan karena tidak ada fakta yang cocok
            input2 = Console.ReadLine
            If input2 = "n" Then
                Console.WriteLine("Solusi Tidak Ditemukan")
                Console.ReadLine()
                Return
            End If

        ElseIf input = "n" Then                                                  #Namun apabila anda menjawab n pada pertanyaan "Apakah badan lemas?" maka akan beralih 
            Console.WriteLine("Apakah tenggorokan gatal / sakit? (y/n)")         #ke pertanyaan selanjutnya yaitu "Apakah tenggorokan gatal / sakit?"
            input2 = Console.ReadLine                                            #Jika anda menjawab n maka solusi tidak ditemukan karena tidak ada fakta yg cocok
            If input2 = "n" Then
                Console.WriteLine("Solusi Tidak Ditemukan")
                Console.ReadLine()
                Return
            End If

            Console.WriteLine("Apakah sering bersin? (y/n)")                    #Namun jika anda menjawab y maka akan beralih ke pertanyaan selnjutnya
            input3 = Console.ReadLine                                           #yaitu "Apakah sering bersin?"
            If input3 = "n" Then                                                #Jika anda menjawab n maka solusi tidak ditemukan karena tidak ada fakta yg cocok
                Console.WriteLine("Solusi Tidak Ditemukan")
                Console.ReadLine()
                Return
            End If
        End If

        Dim jawaban As String = ""

        'A. Algoritma Forward Chaining
        'Membuat tujuan / kesimpulan berdasarkan dari inputan data yang sudah diketahui.
        'Hasil tujuan akan menjadi data baru dan diproses lagi sampai kepada tujuan akhir atau akhir dari permasalahan.
        Console.WriteLine("")
        Console.WriteLine("Menggunakan Metode Forward Chaining")

        'Aturan 3
        If input = "y" Then jawaban = aturan(2, 1)
        'Aturan 1
        If input2 = "y" And jawaban = "suhu badan naik" Then jawaban = aturan(0, 1)
        'Aturan 4
        If input = "n" And input2 = "y" Then jawaban = aturan(3, 1)
        'Aturan 5
        If input3 = "y" And jawaban = "batuk" Then jawaban = aturan(4, 1)
        'Aturan 2
        If jawaban = "sering bersin" Then jawaban = aturan(1, 1)

        If jawaban = "demam" Or jawaban = "flu" Then
            Console.WriteLine("Penyakit yang diderita adalah " & jawaban)
        End If

        'B. Algoritma Backward Chaining
        'Mencari data-data berdasarkan tujuan akhir yang sudah diketahui.
        'Data tersebut nantinya akan menjadi tujuan baru yang akan dicari data-data nya, sampai kepada data paling awal.
        'Jika data paling awal sudah sesuai dengan kriteria inputan, maka tujuan akhir tersebut memang benar.
        Console.WriteLine("")
        Console.WriteLine("Menggunakan Metode Backward Chaining")

        jawaban = aturan(0, 1)
        'Aturan 1
        If input2 = "y" And jawaban = "demam" Then jawaban = aturan(0, 0)
        'Aturan 3
        If input = "y" And jawaban = "suhu badan naik" Then jawaban = aturan(2, 0)

        If jawaban = aturan(2, 0) Then
            Console.WriteLine("Penyakit yang diderita adalah " & aturan(0, 1))
            Console.ReadLine()
            Return
        End If

        jawaban = aturan(1, 1)
        'Aturan 2
        If input = "n" Then jawaban = aturan(1, 0)

        Dim klausajawaban(1) As String
        If jawaban = aturan(1, 0) Then
            klausajawaban(0) = aturan(3, 1)
            klausajawaban(1) = aturan(4, 1)
        End If

        'Aturan 4
        If input2 = "y" And klausajawaban(0) = "batuk" Then klausajawaban(0) = aturan(3, 0)
        'Aturan 5
        If input3 = "y" And klausajawaban(1) = "sering bersin" Then klausajawaban(1) = aturan(4, 0)

        If klausajawaban(0) = aturan(3, 0) And klausajawaban(1) = aturan(4, 0) Then
            Console.WriteLine("Penyakit yang diderita adalah " & aturan(1, 1))
            Console.ReadLine()
            Return
        End If
    End Sub

End Module

