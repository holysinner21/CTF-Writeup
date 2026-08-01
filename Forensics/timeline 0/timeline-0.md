# timeline 1


DESKRIPSI 
Can you find the flag in this disk image? Wrap what you find in the picoCTF flag format.

Download the disk image [here](https://challenge-files.picoctf.net/c_plain_mesa/aa1f8ba93409887e081435732d7037c45b30a8442853bf07c9e84fe4d0e0bc19/partition4.img.gz)


OVERVIEW
- MAC timeline adalah timestamp di disk tentang kapan file Modified/isi file diubah, Access/file diakses, Change/metadata diubah.

    untuk melihat MAC timeline di disk ini, kita menggunakan 'fls -r -m / [nama partisi]'. opsi m untuk membuat output fls menyertakan mac-nya. output dari command ini akan menghasilkan 'body file', isinya sudah lengkap, tapi susah untuk dibaca.

- mactime adalah command yang digunakan untuk membuat body file gampang dibaca. gunakan 'mactime -b [nama file]'


SOLUSI

hal yang pertama kita lihat adalah jenis file system dari partisinya, menggunakan command 'file'

sebelum tau apa itu MAC Timeline, saya mencari file flag di partisi menggunakan 'fls -f ext4 [nama partisi]', tapi tidak mendapatkan apapun

setelah melihat hint dan mencari tahu apa itu MAC timeline, saya langsung membuat file yang berisikan mac timeline

![alt text](a.png)

lalu membukanya dengan 'cat', setelah diselidiki dan dengan bantuan hint, kita tahu bahwa kita ingin melihat 'strange (very old) timestamps'. Karena format mac diurutkan berdasarkan waktu, kita tahu bahwa untuk melihat 

![alt text](b.png)

setelah membukanya dengan 'icat' dengan offset yaang sudah diketahui sebelumnya kita mendapatkan sebuah string

![alt text](c.png)

dengan melihatnya sekilas, saya tahu bahwa string ini adalah string 64bit encoded

dan setelah didecode, ternyata benar bahwa ini adalah flag yang dicari


FLAG

picoCTF{573417h13r_7h4n_7h3_1457_58527bb222}
