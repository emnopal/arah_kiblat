# Arah Kiblat
## Keterangan
Aplikasi untuk menentukan arah kiblat pada suatu lokasi berdasarkan algoritma matematika. Aplikasi ini menggunakan Python Django sebagai Framework web nya, Front-end nya menggunakan Bootstrap dan jQuery sedangkan Back-end nya menggunakan Django + Fast API. Aplikasi ini menggunakan model arsitektur Microservices.

## API
API yang digunakan disini adalah API yang berasal dari Nominatim ditambah dengan API buatan sendiri yang di host di Heroku. <br>
Untuk API bisa dilihat di: https://github.com/emnopal/arah_kiblat_api <br>
Untuk RestAPI bisa lakukan HTTP GET ke: <br>
`curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X GET https://arah-kiblat-api.herokuapp.com/{nama_kota}` <br>

# Web
Repository ini sudah di deploy ke website, dengan host di Heroku.<br>
Untuk Website dari repository ini dapat dilihat ke: https://arah-kiblat.herokuapp.com

