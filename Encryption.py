def Encryption(source_text, alphabet, a, b):
    result = ""
    for i in range(len(source_text)):
        if source_text[i] == " ":
            result += " "
        for el in range(len(alphabet)):
            if source_text[i].lower() == alphabet[el].lower():
                result += str(alphabet[(a * el + b) % len(alphabet)])

    return result.upper()


print(Encryption(input("Текст для шифрования: "),
           input("Алфавит: "),
           int(input("Ключ A: ")), int(input("Ключ B: "))))