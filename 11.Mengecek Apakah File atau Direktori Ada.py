import os

path = 'file_sample.txt'
if os.path.exists(path):
    print(f"'{path}' ditemukan.")
else:
    print(f"'{path}' tidak ditemukan.")

#Mengecek apakah file atau direktori dengan nama yang ditentukan ada.