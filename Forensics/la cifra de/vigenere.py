alphabet = "abcdefghijklmnopqrstuvwxyz"

# Vigenere adalah metode encrypt menggunakan key, keynya akan diitereasikan sehingga tiap karakter pada message
# mempunyai pasangan karakter dari key. hasil encryptnya hanyalah penjumlahan antara  Alphabet[ ( message[i] +  key yang sudah dimap dengan message[i] ) % 26] 

# Membuat key stream sesuai dengan plain_text;
# key stream adalah mapping antara key dengan tiap karakter plain_text yang bersesuaian dengan index
def make_key_stream(key, plain_text):
    
    n = len(plain_text)
    k = len(key)
    key_stream = []
    
    j = 0
    for i in range(n):
        
        if (not plain_text[i].isalpha()):
            key_stream.append("*")
        else:
            key_stream.append(key[j % k])
            j += 1
    
    return key_stream

# Mengencypt plain_text dengan key yang diberikan
def encrypt_message():
    
    plain_text = input("Masukkan plain text: ").strip().lower()
    n = len(plain_text)
    key = input("Masukkan key yang ingin digunakan: ").strip()
    key_stream = make_key_stream(key, plain_text)
    
    cipher = ""
    for i in range(n):
        
        if (not plain_text[i].isalpha()):
            cipher += plain_text[i]
        else:
            cipher += alphabet[(alphabet.index(plain_text[i]) + alphabet.index(key_stream[i])) % 26]
        print(cipher)
    
    print(f"Hasil encypt: {cipher}")
    return cipher

def decrypt_message():
    
    cipher_text = input("Masukkan cipher text: ").strip().lower()
    n = len(cipher_text)
    key = input("Masukkan key yang ingin digunakan: ").strip()
    key_stream = make_key_stream(key, cipher_text)

    plain_text = ""
    for i in range(n):
        
        if (not cipher_text[i].isalpha()):
            plain_text += cipher_text[i]
        else:
            plain_text += alphabet[alphabet.index(cipher_text[i]) - alphabet.index(key_stream[i])]
    
    print(f"Hasil encypt: {plain_text}")
     
    return plain_text

if __name__ == "__main__":
    
    print("Vigenere Cipher")
    print()

    while True:
        
        print()
        print("1. encrypt")
        print("2. decrypt")
        print("x. keluar")
        opsi = input("Masukkan opsi menu yang ingin digunakan: ").strip()
        
        if opsi not in "12x":
            continue
        
        if opsi == '1':
            encrypt_message()
        elif opsi == '2':
            decrypt_message()
        else: 
            break
            
        
        
        
        