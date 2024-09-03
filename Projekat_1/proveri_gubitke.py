import hashlib
import os
import sys
import io

def calculate_hash(file_path):
    #SHA256 hash 
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

def compare_files(original_file, decompressed_file):
    original_hash = calculate_hash(original_file)
    decompressed_hash = calculate_hash(decompressed_file)
    
    if original_hash == decompressed_hash:
        print("Fajlovi su identični.")
    else:
        print("Fajlovi nisu identični.")
    
    # izračunavanje veličina fajlova
    original_size = os.path.getsize(original_file)
    decompressed_size = os.path.getsize(decompressed_file)
    
    # izračunavanje procenata gubitka
    if original_size > 0:
        loss_percentage = ((original_size - decompressed_size) / original_size) * 100
        print(f"Procenat gubitka: {loss_percentage:.2f}%")
    else:
        print("Originalni fajl je prazan, procenat gubitka ne može biti izračunat.")

# standardni izlaz na UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


original_file_path = 'file.txt'
decompressed_file_path_lzw = 'decompressed_lzw.bin'
decompressed_file_path_lz77 = 'decomp_lz77.bin'
compare_files(original_file_path, decompressed_file_path_lzw)
compare_files(original_file_path, decompressed_file_path_lz77)
