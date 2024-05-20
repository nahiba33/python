import os
import shutil
esas_folder = "Example"
try:
 os.mkdir(esas_folder)
except FileExistsError:
 print(f"{esas_folder} directory artıq mövcuddur.")
alt_folder = f"{esas_folder}/Subdirectory"
try:
 os.mkdir(alt_folder)
except FileExistsError:
 print(f"{alt_folder} subdirectory artıq mövcuddur.")
image_text_yolu = os.getcwd()
image_fayl = 'task_10.jpg'
text_fayl = 'task10.txt'
for file_name in [image_fayl, text_fayl]:
    shutil.move(f"{image_text_yolu}/{file_name}", f"{alt_folder}/{file_name}")
for file_name in os.listdir(alt_folder):
 if file_name.endswith('.txt'):
    shutil.move(f"{alt_folder}/{file_name}", f"{esas_folder}/{file_name}")