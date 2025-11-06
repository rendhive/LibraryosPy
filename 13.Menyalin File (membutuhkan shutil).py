import os
import shutil

with open('file_asli.txt', 'w') as f:
    f.write("Ini adalah file asli.")

shutil.copy('file_asli.txt', 'file_salinan.txt')
print("File 'file_asli.txt' telah disalin menjadi 'file_salinan.txt'.")

#Menyalin file dari satu lokasi ke lokasi lain. memerlukan tamoabahan library import shutil