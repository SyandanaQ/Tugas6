# Fungsi enkripsi
def encrypt(plaintext, key):
    # Mengubah semua karakter menjadi huruf kecil
    plaintext = plaintext.lower()
    
    # Menghilangkan spasi dan karakter non-alphabet
    plaintext = ''.join(c for c in plaintext if c.isalpha())
    
    # Menambahkan "x" ke dua karakter yang sama berurutan
    i = 0
    while i < len(plaintext) - 1:
        if plaintext[i] == plaintext[i + 1]:
            plaintext = plaintext[:i+1] + "x" + plaintext[i+1:]
        i += 1
    
    # Menambahkan "x" ke akhir jika panjang kata ganjil
    if len(plaintext) % 2 == 1:
        plaintext += "x"
    
    # Membuat matriks kunci
    key_matrix = []
    for r in range(5):
        key_matrix.append([])
        for c in range(5):
            key_matrix[r].append(key[r * 5 + c])
    
    # Enkripsi teks
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        p1, p2 = plaintext[i], plaintext[i+1]
        r1, c1 = get_position(key_matrix, p1)
        r2, c2 = get_position(key_matrix, p2)
        
        if r1 == r2:
            # Jika karakter terletak di baris yang sama, karakter yang terdekripsi adalah kolom sebelah kanan kedua karakter
            c1 = (c1 + 1) % 5
            c2 = (c2 + 1) % 5
        elif c1 == c2:
            # Jika karakter terletak di kolom yang sama, karakter yang terdekripsi adalah baris di bawah kedua karakter
            r1 = (r1 + 1) % 5
            r2 = (r2 + 1) % 5
        else:
            # Jika karakter terletak di kotak yang berbeda, karakter yang terdekripsi adalah karakter di kolom yang sama dengan karakter lain
            c1, c2 = c2, c1
        
        # Menambahkan karakter yang terdekripsi ke ciphertext
        ciphertext += key_matrix[r1][c1] + key_matrix[r2][c2]
    
    return ciphertext

# Fungsi dekripsi
def decrypt(ciphertext, key):
    # Membuat matriks kunci
        key_matrix = []
    for r in range(5):
        key_matrix.append([])
        for c in range(5):
            key_matrix[r].append(key[r * 5 + c])
    
    # Dekripsi teks
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        c1, c2 = ciphertext[i], ciphertext[i+1]
        r1, c1 = get_position(key_matrix, c1)
        r2, c2 = get_position(key_matrix, c2)
        
        if r1 == r2:
            # Jika karakter terletak di baris yang sama, karakter yang terdekripsi adalah kolom sebelah kiri kedua karakter
            c1 = (c1 - 1) % 5
            c2 = (c2 - 1) % 5
        elif c1 == c2:
            # Jika karakter terletak di kolom yang sama, karakter yang terdekripsi adalah baris di atas kedua karakter
            r1 = (r1 - 1) % 5
            r2 = (r2 - 1) % 5
        else:
            # Jika karakter terletak di kotak yang berbeda, karakter yang terdekripsi adalah karakter di kolom yang sama dengan karakter lain
            c1, c2 = c2, c1
        
        # Menambahkan karakter yang terdekripsi ke plaintext
        plaintext += key_matrix[r1][c1] + key_matrix[r2][c2]
    
    return plaintext

# Fungsi untuk mencari posisi karakter dalam matriks kunci
def get_position(key_matrix, ch):
    for r in range(5):
        for c in range(5):
            if key_matrix[r][c] == ch:
                return r, c

# Contoh penggunaan
plaintext = "Syandana Qatrunada"
key = "Kediri"
ciphertext = encrypt(plaintext, key)
print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted plaintext:", decrypt(ciphertext, key))

