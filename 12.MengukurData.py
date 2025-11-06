import os

# Membuat file untuk mengukur ukurannya
with open('file_sample.txt', 'w') as f:
    f.write("Ini adalah file contoh untuk mengukur ukuran.")

file_size = os.path.getsize('file_sample.txt')
print("Ukuran file 'file_sample.txt':", file_size, "byte")


#Mengambil ukuran file dan menampilkannya dalam byte.