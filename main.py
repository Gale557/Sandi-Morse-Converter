morse = {
    'a': "o-",
    'b': "-ooo",
    'c': "-o-o",
    'd': "-oo",
    'e': "o",
    'f': "oo-o",
    'g': "--o",
    'h': "oooo",
    'i': "oo",
    'j': "o---",
    'k': "-o-",
    'l': "o-oo",
    'm': "--",
    'n': "-o",
    'o': "---",
    'p': "o--o",
    'q': "--o-",
    'r': "o-o",
    's': "ooo",
    't': "-",
    'u': "oo-",
    'v': "ooo-",
    'w': "o--",
    'x': "-oo-",
    'y': "-o--",
    'z': "--oo",
}
def morseKeHuruf():
    print("Cara Memakai Masukan '-' sebagai strip dan 'o' sebagai titik")
    print("Contoh 'aku' = o- -o- oo-")
    sandi = str(input("Masukan sandi morse dengan tepat: "))
    sandi = sandi.split(" ")
    jawaban = []
    for i in range(len(sandi)):
        for j in range(26):
            if sandi[i] == morse[list(morse.keys())[j]]:
                jawaban.append(list(morse.keys())[j])
    return "".join(jawaban)

def hurufKeMorse():
    print("Cara Memakai Masukan '-' sebagai strip dan 'o' sebagai titik")
    print("Contoh o- -o- oo- = aku")
    sandi = str(input("Masukan sandi morse dengan tepat: "))
    sandi = [*sandi]
    jawaban = []
    for i in range(len(sandi)):
        for j in range(26):
            if sandi[i] == list(morse.keys())[j]:
                jawaban.append(morse[list(morse.keys())[j]])
    return " ".join(jawaban)

if __name__ == "__main__":
    print("===== Sandi Morse ======")
    print("[1] Morse ke Huruf")
    print("[2] Huruf Ke Morse")
    nomor = int(input("Masukan Pilihan: "))
    if nomor == 1:
        print(morseKeHuruf())
    elif nomor == 2:
        print(hurufKeMorse())


















