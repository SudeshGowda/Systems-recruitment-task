import base64


def e5(m):  # base64
    s = base64.b64decode(m)
    s = s.decode()
    return s


def e4(m, k=13):  # Caesar shift cipher
    m = m.lower()
    s = ""
    for i in range(len(m)):
        s += chr((ord(m[i]) - k - 97) % 26 + 97)
    return s


def e2(m, k):  # Vigenere cipher
    m = m.lower()
    k = k.lower()
    s = ""
    while len(k) < len(m):
        k += k
    for i in range(len(m)):
        s += chr((ord(m[i]) - ord(k[i])) % 26 + 97)
    return s


def key_square(k):
    k = k.lower()
    s = ""
    alphabet = "abcdefghiklmnopqrstuvwxyz"
    for i in k:
        if i not in s:
            s += i
    for j in k:
        if j not in alphabet:
            s += j
    key_sq = []
    for e in range(5):
        key_sq.append('')

    # Break it into 5*5
    key_sq[0] = s[0:5]
    key_sq[1] = s[5:10]
    key_sq[2] = s[10:15]
    key_sq[3] = s[15:20]
    key_sq[4] = s[20:25]
    return key_sq


def cipher_to_digraphs(cipher):
    i = 0
    new = []
    for x in range(len(cipher) // 2 ):
        new.append(cipher[i:i + 2])
        i = i + 2
    return new


def find_position(key_sq, letter):
    for i in range(len(key_sq)):
        s = key_sq[i]
        if s.find(letter) != -1:
            return i, s.find(letter)


def e1(m, k):  # Playfair cipher
    cipher = cipher_to_digraphs(m)
    key_matrix = key_square(k)
    plaintext = ""
    for e in cipher:
        p1, q1 = find_position(key_matrix, e[0])
        p2, q2 = find_position(key_matrix, e[1])
        if p1 == p2:
            if q1 == 4:
                q1 = -1
            if q2 == 4:
                q2 = -1
            plaintext += key_matrix[p1][q1 - 1]
            plaintext += key_matrix[p1][q2 - 1]
        elif q1 == q2:
            if p1 == 4:
                p1 = -1
            if p2 == 4:
                p2 = -1
            plaintext += key_matrix[p1 - 1][q1]
            plaintext += key_matrix[p2 - 1][q2]
        else:
            plaintext += key_matrix[p1][q2]
            plaintext += key_matrix[p2][q1]

    return plaintext

m = "d3ZucXN0b2tib2xlamp5ZW5zdnlicGpsa3VhcGx2"
m5 = e5(m)
m4 = e4(m5, 13)
m3 = e4(m4, 20) # Since both are ceaser ciphers, same function is called
m2 = e2(m3, 'cryptography')
m1 = e1(m2, 'natdszgrqhebvpmxilfywcuko')
print(m1)
