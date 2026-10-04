Nama : Syakira Aqilah Amru

NPM : 2506541622

Kelas : PBP B

Jurusan : Ilmu Komputer

# Proyek Web Portofolio - Tugas Individu Pemrograman Berbasis Platform

## Deskripsi Proyek
Website ini merupakan web portofolio pribadi yang didesain interaktif dan dikembangkan secara berkelanjutan sebagai pemenuhan kualifikasi tugas pekanan mata kuliah PBP.

### Setup & Instalasi
*Karena web ini dimodifikasi dan dikembangkan secara berkelanjutan, berikut langkah untuk setup versi terbaru*
1. Clone repository ini dan pindah ke direktori yang sesuai
    ```
    git clone <https://github.com/syakiraaqilah/myportofolio>
    cd <myportofolio>
    ```
2. Buat dan aktifkan virtual environment 
    - Windows:
    ```
    python -m venv env
    env\Scripts\activate
    ```

    - UNIX (macOS, Linux):
    ```
    python3 -m venv env 
    source env/bin/activate
    ```
3. Install semua dependencies
    ```
    pip install -r requirements.txt
    ```
4. Lakukan migrasi database
    ```
    python manage.py migrate
    ```
5. Jalankan server lokal
    ```
    python manage.py runserver
    ```
6. Buka http://localhost:8000/ di browser untuk melihat tampilan web

### Log Proses Pekanan
- Pekan 1: Inisialisasi web statis dengan HTML5 dan CSS3 (AI disclosure di Tugas 1)
- Pekan 2: Implementasi arsitektur MVT pada Django (AI disclosure di Tugas 2; log sama dengan Tugas 1)
- Pekan 3: Implementasi form & data delivery (AI disclosure di Tugas 3; log sama dengan Tugas 1)
- Pekan 4: Implementasi authentication, session, dan cookie (AI disclosure di Tugas 4)

## Tugas 1

1. Saya menggunakan sejumlah elemen semantik mulai dari header, nav, footer, main, dan section. Di antara ketiga elemen yang disebutkan pada soal, saya hanya menggunakan section. Alasan utamanya adalah karena web yang saya buat hanya memuat profile (section hero) dan skills (section skills). Keduanya adalah entitas yang tidak independen sehingga penggunaan section merupakan langkah yang tepat. Skills di sini membutuhkan informasi dari hero untuk mendefinisikan identitas pemilik skill sehingga tidak tepat untuk menggunakan article. Di sisi lain, penggunaan aside juga tidak tepat karena profil/identitas dan skill yang saya spesifikasikan dalam section di sini merupakan konten penting yang tidak bisa diabaikan; esensinya tinggi karena menopang tujuan utama dibuatnya portofolio ini (memaparkan informasi diri dan skill-skill yang menjual).

2. Saya sedikit kesulitan karena terdapat banyak aturan dan sintaks yang baru saya temui, mengingat ini adalah pertama kalinya saya menyentuh HTML dan CSS. Saya cukup tertantang saat ingin memanifestasikan desain simpel web yang ada di kepala saya; contohnya adalah saat saya menginginkan desain elemen yang menyamping dan juga berderet ke bawah, kemudian juga masalah padding dan ukuran elemen. Untuk logika umumnya, saya meminta arahan dari AI seperti sintaks atau aturan CSS yang mengizinkan perubahan tata letak dan ukuran. Selanjutnya, saya menganalisis potongan kode dan penjelasan yang diberikan, mengajukan pertanyaan dan sanggahan sebelum kemudian memodifikasinya sesuka saya. Saya sendiri juga mengevaluasi tampilan desktop dan mobile dengan toggle device toolbar, kemudian mencoba memngatur layout dengan mengubah display dan padding. Saya menentukan elemen yang perlu diubah ukuran maupun posisinya dengan memanfaatkan toggle device tersebut, kemudian mengatur ulang display, flex, dan justify-content.

3. Banyak batasan yang saya rasakan karena ini hanya sebagai web yang menyajikan informasi saya tanpa interaksi yang bermakna dengan orang yang melihatnya. Fungsionalitas yang ingin saya tambahkan di antaranya adalah fitur pencarian dan kontak (komentar dan kontak pribadi).

### Penggunaan AI

AI yang saya gunakan adalah Claude Sonnet 5. Berikut alur prompting yang saya terapkan:

1. Menganalisis struktur dasar HTML dan CSS beserta penjelasan elemen-elemennya
2. Bertanya mengenai penerapan aturan yang tepat untuk merealisasikan rancangan desain web
3. Menganalisis jawaban dan rangkaian kode yang dicontohkan untuk kemudian dimodifikasi secara mandiri

Selanjutnya, berikut adalah spesifikasi bantuan dari AI yang saya gunakan:

1. Alur untuk mengganti font dan efek tipografi
2. Cara menambahkan subheadline dan keterkaitannya dengan penggunaan div
3. Mengubah background menjadi memiliki efek polkadot
4. Aturan membungkus teks dalam suatu box/frame/highlight sesuai properti CSS
5. Analisis penggunaan ul, li, dan span
6. Properti untuk menerapkan transformasi dan rotasi pada teks dan frame
7. Penggunaan efek saat hover dan active
8. Logika mengatur ukuran gambar
9. Analisis desain yang tepat untuk section skills; apakah perlu memisahkan antara tools dan programming language
10. Analisis perbedaan dan penggunaan elemen semantik HTML
11. Analisis alternatif untuk perubahan struktur di desktop dan mobile

```Log prompting:https://claude.ai/share/4407a4f3-24c2-42c8-b382-3c8e11c135b9```


## Tugas 2

1. Alur yang terjadi: saat user menekan/mengakses URL melalui browser, selanjutnya request akan dikirim ke server Django. Di sini, Django memetakan URL ke View melalui <urls.py>. Adapun <urls.py> di sini dibedakan menjadi <urls.py> aplikasi & projek. <urls.py> projek yang akan mengecek pertama kali;
*path('admin/', admin.site.urls)*
*path('', include('main.urls'))* 
--> mengindikasikan bahwa untuk URL yang tidak diawali admin/, maka akan dipetakan ke <main/urls.py> (<urls.py> aplikasi yang dalam hal ini aplikasi main). Nah, pemetaan ini penting untuk mencocokkan View yang akan dipanggil. View kemudian akan memproses data models apabila perlu, kemudian setelahnya memanggil render() di mana disini file html (template) akan dibaca dan digabungkan dengan context, kemudian dibungkus menjadi HttpResponse yang dikirim kembali ke browser. Setelah browser menerima response, tag <link rel="stylesheet" href="/static/css/style.css"> akan terbaca sehingga browser kembali mengirim request untuk mengambil file css tersebut yang setelahnya akan dikirim oleh server. Pada akhirnya, final rendering visual akan didisplay dengan menggabungkan html dan css.

2. Pada akhirnya, data untuk bagian portfolio (dalam hal ini <experience> dan <skill>) merupakan sesuatu yang dapat bertambah/berubah seiring berjalannya waktu. Hard-code pada template tentunya bukan hal yang tepat untuk mengatasi ini; efisiensi dan maintainability-nya perlu dipertanyakan. Dalam konteks pemeliharaan dan pengembangan aplikasi, penggunaan model akan mempermudah jika sewaktu-waktu terdapat data yang perlu diubah atau ditambah karena tidak perlu mengubahnya satu per satu di template html. Selain itu, karena data tidak ditulis langung di template, keamanan akan lebih terjamin karena user tidak bisa mengakses langsung dari source code.

3. <makemigrations> adalah ketika Django membandingkan status model saat ini dan migrasi sebelumnya; apakah terdapat perubahan atau tidak, kemudian membuat suatu file instruksi atau migration file terkait perubahan yang perlu diimplementasikan. Setelah itu barulah <migrate> yang akan menjalankan instruksi dari migration file yang dibuat oleh <makemigrations> ke database. 

### Penggunaan AI

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

## Tugas 3

1. Penggunaan <ModelForm> di sini akan memudahkan kita; dalam hal ini, bisa dikatakan kita memanfaatkan 'tools' yang sudah ada demi pekerjaan yang lebih optimal. Django akan mengendalikan sebagian besar proses di belakang layar sehingga kita tidak perlu repot-repot menanganinya. Adapun menurut dokumentasi Django sendiri, tujuan penggunaan CSRF token adalah untuk proteksi dari Cross Site Request Forgeries; suatu jenis penyerangan siber. Pada dasarnya, ini berfungsi untuk mencegah penyerang aplikasi mengubah request yang awalnya ke server Django menjadi ke suatu API yang berbahaya dan mengirimkan data request kita ke mereka.

2. JSON lebih disukai karena ukurannya yang lebih ringkas, parser yang sangat cepat, dan integrasi yang sangat natural dengan JavaScript di sisi frontend. Selain itu, format JSON sangat _readable_ baik bagi manusia maupun mesin.

3. **Alur lengkap**: Awalnya, akan dilakukan query database (di <get_projects_json> milik <views.py>) dengan hasil berupa QuerySet object Python (implementasi: <Project.objects.all()>). Karena object python ini memiliki struktur kompleks yang tidak bersifat universal, perlu adanya proses penerjemahan (dalam hal ini adalah _serialization_). Alasan kita perlu melakukan proses ini adalah untuk mentranslasi object Python menjadi suatu format sistematis (dalam hal ini adalah JSON) yang bersifat universal sehingga dapat dimengerti oleh siapa saja. Tanpa proses ini, objek Python tidak akan diterjemahkan; strukturnya yang kompleks tidak dapat dimengerti secara universal (implementasi: <serializers.serialize("json", projects)>). Nilai dari setiap fieldnya akan diekstraksi dan dikonversi ke tipe yang kompatibel di format JSON sebelum kemudian setiap instancenya akan disusun dalam dictionary terpisah yang nantinya akan dibungkus dalam satu list.

Adapun sesuai dengan <views.py>:
<return HttpResponse(projects_json, content_type="application/json")>
json_response di sini adalah suatu HttpResponse yang memberi tahu bahwa isi response tersebut adalah JSON sehingga browser tidak salah interpretasi. Response dapat dikirim langsung sebagai public API, atau dalam konteks tugas ini dipanggil/digunakan di <show_projects> untuk deserialization (parsing JSON untuk mengambil instance Python) dan kemudian di-render dan digunakan dalam loop di <project.html>. 

### Penggunaan AI

AI yang saya gunakan adalah Claude Sonnet 5. Berikut alur prompting yang saya terapkan:

1. Menganalisis struktur template html dan penggunaan form
2. Bertanya mengenai penerapan aturan yang tepat untuk merealisasikan rancangan desain web serta mengecek kesalahan kode
3. Menganalisis jawaban dan rangkaian kode yang dicontohkan untuk kemudian diimplementasi dan dimodifikasi secara mandiri

Selanjutnya, berikut adalah spesifikasi bantuan dari AI yang saya gunakan:

1. Analisis penggunaan dan perbandingan model form untuk project dan experience termasuk implementasi kodenya dalam file-file terkait
2. Analisis logika date input dan display warna yang sesuai
3. Analisis logika select widget dan restyling sesuai tema web
4. Analisis pengecekan error dalam kode
5. Analisis perubahan logika css untuk desain web berdasarkan detail preferensi
6. Analisis konsep serialization dan struktur JSON

`Note: Log prompting masih sama seperti sebelumnya.`

## Tugas 4

### Penggunaan AI
> Saya menggunakan Claude Sonnet 5 sebagai tools untuk membantu saya dalam memahami konsep & debugging kode untuk penyelesaian tugas 4. 

Berikut alur prompting yang saya terapkan:

1. Menganalisis struktur template html, main, beserta logika yang diterapkan untuk _permission_
2. Mengecek kesalahan logika/struktur kode
3. Menganalisis jawaban dan rangkaian kode yang dicontohkan untuk kemudian diimplementasi dan dimodifikasi secara mandiri

Selanjutnya, berikut adalah spesifikasi bantuan dari AI yang saya gunakan:

1. Analisis implementasi *group* & *permission* serta penggunaan *User* atau *AbstractUser*
2. Analisis struktur kode template html dan view untuk perizinan penggunaan fitur / melihat button tertentu
3. Analisis pengecekan error dalam kode
4. Analisis alokasi *user* dalam *group* melalui Django admin

`Log AI: https://claude.ai/share/e93a1214-4db9-4813-8d73-d3aafce5100b`


## Tugas 5

1. Jelaskan apa itu debouncing dan mengapa teknik ini penting diterapkan pada fitur pencarian yang menggunakan AJAX!
> **Debouncing** di sini merupakan teknik untuk menunda suatu fungsi hingga waktu jeda yang diterapkan berlalu tanpa _event_ baru. Menilik fungsi *fetchProjects()* dan *fetchExperiences()* yang langsung pada _event_ **input** (sehingga membuat browser mengirim _request_ per karakter),  **Debouncing** di sini penting supaya selama _user_ mengetik di kolom pencarian, _timer_ akan di-_reset_; ini mengimplikasi _browser_ akan men-_delay_ API _request_ dan hanya mengirim _request_ setelah _user_ berhenti mengetik sejenak (terdapat jeda waktu). Dengan demikian, hal ini akan mencegah _server traffic_ dan dan menjaga agar UI tetap mulus.

2. Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
>  **fetch()** di sini merupakan API untuk _HTTP request_ dengan sintaks yang lebih sederhana dan mengembalikan sebuah **Promise**. **Promise** sendiri akan selesai saat _header_ respons diterima atau bisa juga ditolak jika ada _network error_. Dengan menggunakan _keyword_ **await** sebelum **Promise**, fungsi akan ditunda hingga **Promise** _settle_ sebelum kemudian mengembalikan objek **Response** sebagai hasil. Tanpa **await**, variabel hanya berisi **Promise** (masih _pending_), dan baris kode selanjutkan akan dijalankan dalam keadaan data belum tersedia. 

3. Jelaskan apa itu serangan XSS (Cross-Site Scripting) dan mengapa data yang ditampilkan melalui AJAX/JavaScript lebih rentan terhadap serangan ini daripada data yang ditampilkan langsung melalui template Django!
> **Cross-Site Scripting (XSS)** merupakan serangan ketika seseorang berhasil menyisipkan kode JavaScript miliknya ke dalam halaman web yang kemudian dijalankan di _browser_ _user_ lain. Salah satu jenisnya adalah _stored_ XSS, yaitu ketika kode berbahaya disimpan ke _database_ (misalnya sebagai judul suatu _project_) lalu ikut dijalankan setiap kali data tersebut ditampilkan. 

> Template Django melakukan _auto-escaping_ pada setiap **{ variabel }**. Karakter seperti < dan > diubah menjadi &lt; dan &gt; sehingga browser menampilkannya sebagai teks biasa, bukan sebagai tag HTML. Nah, tetapi, perlindungan itu hilang karena peralihan ke AJAX. Pada **buildProjectCardElement(item)** dan **buildExperienceCardElement(item)**, data dari JSON disisipkan ke dalam _template_ literal lalu dipasang lewat **innerHTML**. Tidak ada Django yang melakukan _escaping_ sehingga _browser_ akan memperlakukan setiap tag HTML di dalam data sebagai kode sungguhan. Oleh karena itu, data yang ditampilkan melalui AJAX/JavaScript lebih rentan terhadap serangan XSS.

> Demi mengatasi hal tersebut, kita harus melakukan _escaping_ HTML di JavaScript dengan menyiapkan fungsi **escapeHtml(value)** untuk mengubah karakter HTML menjadi serupa dengan yang di-_escape_ Django. Kemudian, setiap _value_ JSON yang disisipkan akan dibungkus dengan fungsi ini. 

### Penggunaan AI
> Saya menggunakan Claude Sonnet 5 sebagai tools untuk membantu saya dalam memahami konsep & _debugging_ kode untuk penyelesaian tugas 5. 

Berikut alur prompting yang saya terapkan:

1. Menganalisis struktur template html, main, beserta logika yang diterapkan untuk _web interactivity_ dengan JavaScript
2. Mengecek kesalahan logika/struktur kode
3. Menganalisis jawaban dan rangkaian kode yang dicontohkan untuk kemudian diimplementasi dan dimodifikasi secara mandiri

Selanjutnya, berikut adalah spesifikasi bantuan dari AI yang saya gunakan:

1. Analisis kebenaran implementasi notifikasi _toast_, AJAX, Debouncing, dan Modal Form
2. Analisis struktur kode template, static, dan main untuk mengecek error dan inkonsistensi dalam kode
3. Analisis kebenaran logika terkait urgensi penggunaan **await** pada **fetch()**

`Log AI: https://claude.ai/share/3407de40-9394-4971-84f0-3fb0420727b0`