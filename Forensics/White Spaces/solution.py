with open("Forensics\White Spaces\whitepages.txt", "rb") as f:
    content = f.read()

em_space = b"\xe2\x80\x83"
space = b" "

binary_str = ""
for i in range(len(content)):
    if content[i:i+3] == em_space:
        binary_str += "0"
    elif content[i:i+1] == space:
        binary_str += "1"

# Ubah string biner ke teks ASCII per 8-bit
text = ""
for i in range(0, len(binary_str), 8):
    byte = binary_str[i:i+8]
    if len(byte) == 8:
        text += chr(int(byte, 2))

print("-->", text)

