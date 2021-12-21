try:
    path = input(r"Path: ")
    kunci = int(input("Kunci: "))
    print(f"\nFile Path: {path}")
    print(f"Kunci Enkripsi/Deskripsi: {kunci}\n")

    file = open(path, 'rb')
    data = file.read()
    file.close()

    data = bytearray(data)
    for index, nilai in enumerate(data):
        data[index] = nilai ^ kunci

    file = open(path, 'wb')
    file.write(data)
    file.write
    print("Enkripsi/Deskripsi File Selesai \n")
except:
    print("terjadi kesalahan")