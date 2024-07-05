import os

# Path folder tempat file-file berada
folder_path = r'D:\14. All Asisten-Riset-AR\1. Marker Baru Lagi\Marker Terbaru Agustus'
	

# Daftar file dalam folder
file_list = os.listdir(folder_path)

# Loop melalui setiap file dalam folder
for filename in file_list:
    if filename.endswith('.jpg') and filename.startswith('2'):  # Ganti dengan ekstensi dan pola nama yang sesuai
        old_filepath = os.path.join(folder_path, filename)
        
        # Mengubah nama file
        new_filename = filename.replace('2', '', 1)
        new_filepath = os.path.join(folder_path, new_filename)
        
        # Rename file
        os.rename(old_filepath, new_filepath)
        print(f'Renamed: {filename} -> {new_filename}')
