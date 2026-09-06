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
