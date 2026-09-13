Nama : Syakira Aqilah Amru

NPM : 2506541622

Kelas : PBP B

Jurusan : Ilmu Komputer

### Tugas 1

1. Saya menggunakan sejumlah elemen semantik mulai dari <header>, <nav>, <footer>, <main>, dan <section>. Di antara ketiga elemen yang disebutkan pada soal, saya hanya menggunakan <section>. Alasan utamanya adalah karena web yang saya buat hanya memuat profile (section hero) dan skills (section skills). Keduanya adalah entitas yang tidak independen sehingga penggunaan <section> merupakan langkah yang tepat. Skills di sini membutuhkan informasi dari hero untuk mendefinisikan identitas pemilik skill sehingga tidak tepat untuk menggunakan <article>. Di sisi lain, penggunaan <aside> juga tidak tepat karena profil/identitas dan skill yang saya spesifikasikan dalam <section> di sini merupakan konten penting yang tidak bisa diabaikan; esensinya tinggi karena menopang tujuan utama dibuatnya portofolio ini (memaparkan informasi diri dan skill-skill yang menjual).

2. Saya sedikit kesulitan karena terdapat banyak aturan dan sintaks yang baru saya temui, mengingat ini adalah pertama kalinya saya menyentuh HTML dan CSS. Saya cukup tertantang saat ingin memanifestasikan desain simpel web yang ada di kepala saya; contohnya adalah saat saya menginginkan desain elemen yang menyamping dan juga berderet ke bawah, kemudian juga masalah padding dan ukuran elemen. Untuk logika umumnya, saya meminta arahan dari AI seperti sintaks atau aturan CSS yang mengizinkan perubahan tata letak dan ukuran. Selanjutnya, saya menganalisis potongan kode dan penjelasan yang diberikan, mengajukan pertanyaan dan sanggahan sebelum kemudian memodifikasinya sesuka saya. Saya sendiri juga mengevaluasi tampilan desktop dan mobile dengan toggle device toolbar, kemudian mencoba memngatur layout dengan mengubah display dan padding. Saya menentukan elemen yang perlu diubah ukuran maupun posisinya dengan memanfaatkan toggle device tersebut, kemudian mengatur ulang display, flex, dan justify-content.

3. Banyak batasan yang saya rasakan karena ini hanya sebagai web yang menyajikan informasi saya tanpa interaksi yang bermakna dengan orang yang melihatnya. Fungsionalitas yang ingin saya tambahkan di antaranya adalah fitur pencarian dan kontak (komentar dan kontak pribadi).

## Penggunaan AI

AI yang saya gunakan adalah Claude Sonnet 5. Berikut alur prompting yang saya terapkan:

1. Menganalisis struktur dasar HTML dan CSS beserta penjelasan elemen-elemennya
2. Bertanya mengenai penerapan aturan yang tepat untuk merealisasikan rancangan desain web
3. Menganalisis jawaban dan rangkaian kode yang dicontohkan untuk kemudian dimodifikasi secara mandiri

Selanjutnya, berikut adalah spesifikasi bantuan dari AI yang saya gunakan:

1. Alur untuk mengganti font dan efek tipografi
2. Cara menambahkan subheadline dan keterkaitannya dengan penggunaan <div>
3. Mengubah background menjadi memiliki efek polkadot
4. Aturan membungkus teks dalam suatu box/frame/highlight sesuai properti CSS
5. Analisis penggunaan <ul>, <li>, dan <span>
6. Properti untuk menerapkan transformasi dan rotasi pada teks dan frame
7. Penggunaan efek saat hover dan active
8. Logika mengatur ukuran gambar
9. Analisis desain yang tepat untuk <section> skills; apakah perlu memisahkan antara tools dan programming language
10. Analisis perbedaan dan penggunaan elemen semantik HTML
11. Analisis alternatif untuk perubahan struktur di desktop dan mobile

Log prompting: https://claude.ai/share/4407a4f3-24c2-42c8-b382-3c8e11c135b9


### Tugas 2

1. Alur yang terjadi: saat user menekan/mengakses URL melalui browser, selanjutnya request akan dikirim ke server Django. Di sini, Django memetakan URL ke View melalui <urls.py>. Adapun <urls.py> di sini dibedakan menjadi <urls.py> aplikasi & projek. <urls.py> projek yang akan mengecek pertama kali;
*path('admin/', admin.site.urls)*
*path('', include('main.urls'))* 
--> mengindikasikan bahwa untuk URL yang tidak diawali admin/, maka akan dipetakan ke <main/urls.py> (<urls.py> aplikasi yang dalam hal ini aplikasi main). Nah, pemetaan ini penting untuk mencocokkan View yang akan dipanggil. View kemudian akan memproses data models apabila perlu, kemudian setelahnya memanggil render() di mana disini file html (template) akan dibaca dan digabungkan dengan context, kemudian dibungkus menjadi HttpResponse yang dikirim kembali ke browser. Setelah browser menerima response, tag <link rel="stylesheet" href="/static/css/style.css"> akan terbaca sehingga browser kembali mengirim request untuk mengambil file css tersebut yang setelahnya akan dikirim oleh server. Pada akhirnya, final rendering visual akan didisplay dengan menggabungkan html dan css.

2. Pada akhirnya, data untuk bagian portfolio (dalam hal ini <experience> dan <skill>) merupakan sesuatu yang dapat bertambah/berubah seiring berjalannya waktu. Hard-code pada template tentunya bukan hal yang tepat untuk mengatasi ini; efisiensi dan maintainability-nya perlu dipertanyakan. Dalam konteks pemeliharaan dan pengembangan aplikasi, penggunaan model akan mempermudah jika sewaktu-waktu terdapat data yang perlu diubah atau ditambah karena tidak perlu mengubahnya satu per satu di template html. Selain itu, karena data tidak ditulis langung di template, keamanan akan lebih terjamin karena user tidak bisa mengakses langsung dari source code.

3. <makemigrations> adalah ketika Django membandingkan status model saat ini dan migrasi sebelumnya; apakah terdapat perubahan atau tidak, kemudian membuat suatu file instruksi atau migration file terkait perubahan yang perlu diimplementasikan. Setelah itu barulah <migrate> yang akan menjalankan instruksi dari migration file yang dibuat oleh <makemigrations> ke database. 

## Penggunaan AI

AI yang saya gunakan adalah Claude Sonnet 5. Berikut alur prompting yang saya terapkan:

1. Menganalisis struktur template html dan penggunaan model
2. Bertanya mengenai penerapan aturan yang tepat untuk merealisasikan rancangan desain web
3. Menganalisis jawaban dan rangkaian kode yang dicontohkan untuk kemudian diimplementasi dan dimodifikasi secara mandiri

Selanjutnya, berikut adalah spesifikasi bantuan dari AI yang saya gunakan:

1. Analisis perbandingan <experience.html> dan <skills.html> dari segi struktur kode html (apakah tepat untuk menggunakan implementasi tag yang berbeda)
2. Analisis implementasi logika untuk kategorisasi Skills menjadi: programming & web, development tools, dan design & editing.
3. Analisis implementasi logika untuk durasi experience menggunakan DateField
4. Analisis perubahan logika css untuk desain web berdasarkan detail preferensi
5. Analisis detail alur routing URL hingga display html dan css di layar

`Log prompting masih sama seperti sebelumnya.`