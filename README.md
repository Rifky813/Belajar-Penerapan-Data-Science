# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Maju merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000. Ia memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri. 

Walaupun telah menjadi menjadi perusahaan yang cukup besar, Jaya Jaya Maju masih cukup kesulitan dalam mengelola karyawan. Hal ini berimbas tingginya attrition rate (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan) hingga lebih dari 10%.

Untuk mencegah hal ini semakin parah, manajer departemen HR meminta bantuan divisi Data Scientist untuk mengidentifikasi berbagai faktor yang mempengaruhi tingginya attrition rate tersebut.

### Permasalahan Bisnis

Jaya Jaya Maju menghadapi tingkat attrition rate karyawan yang cukup tinggi, yakni lebih dari 10%. Tingginya angka tersebut berpotensi mengganggu stabilitas operasional perusahaan, meningkatkan biaya rekrutmen dan pelatihan, serta menurunkan produktivitas secara keseluruhan. Namun, perusahaan masih belum memahami secara pasti faktor-faktor utama penyebab karyawan keluar dari perusahaan.

### Cakupan Proyek

1. Menganalisis data HR untuk mengetahui karakteristik karyawan yang keluar.
2. Mengidentifikasi fitur/variabel penting yang memengaruhi attrition menggunakan machine learning.
3. Membuat dashboard interaktif di Google Looker Studio untuk membantu pengambilan keputusan.

### Persiapan

Sumber data: Sumber data: (https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/employee_data.csv)

Setup environment:
Menggunakan environment conda dengan versi python 3.12
1. Install python v3.12 di conda
```
conda create -n py312 python=3.12
```
2. Aktifkan env tersebut
```
conda activate py312
```
3. Install library yang dibutuhkan
```
pip install -r requirements.txt
```

## Business Dashboard

<img width="1491" height="1060" alt="Screenshot 2025-09-21 185744" src="https://github.com/user-attachments/assets/301ca7cd-a17f-4a58-8367-7ee68d4521d7" />


Dashboard ini menyajikan analisis Employee Attrition dengan beberapa insight utama:
- Attrition Rate sebesar 17% (179 karyawan keluar dari 1.058).
- Attrition lebih banyak pada laki-laki (58.6%) dan kelompok usia 18–31 tahun (90 orang).
- Mayoritas attrition berasal dari karyawan dengan Travel_Rarely (65.4%).

Perbedaan gaji signifikan antar posisi, dengan jabatan rendah cenderung berpenghasilan kecil.

Berikut link dashboard: https://lookerstudio.google.com/reporting/b9cc41c2-d1fe-484a-9185-fc8becd2d0d9

## Conclusion

- Faktor gender, pola perjalanan dinas, dan kompensasi berpotensi memengaruhi tingkat attrition.
- Attrition paling banyak terjadi pada usia muda (18–31 tahun), yang menunjukkan kemungkinan tingginya tingkat mobilitas karier atau ketidakpuasan awal.
- Karyawan dengan status Travel_Rarely (Jarang Bepergian) justru paling banyak keluar, yang mungkin berkaitan dengan ekspektasi pekerjaan atau kurangnya tantangan.
- Faktor kompensasi juga dapat menjadi salah satu penyebab, terutama di jabatan dengan gaji relatif rendah (misalnya Sales Representative, Research Scientist).

### Rekomendasi Action Items 

Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.

- Tingkatkan retensi karyawan muda melalui program pengembangan karier.
- Evaluasi kebijakan perjalanan dinas.
- Perbaiki kompensasi/benefit untuk posisi bergaji rendah.
