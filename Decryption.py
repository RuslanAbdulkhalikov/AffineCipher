def Decryption(source_text, alphabet, replace_choice):
    result = ""
    temp = []
    do = []
    if replace_choice in "ДадаYesyes":
        a = int(input("Ключ A: "))
        b = int(input("Ключ B: "))
        MultiA = [x for x in range(1, 50) if 1 == (x * a) % len(alphabet)][0]
        for i in range(len(source_text)):
            for j in range(len(alphabet)):
                if source_text[i].lower() == alphabet[j].lower():
                    temp.append(MultiA * (j + len(alphabet) - b) % len(alphabet))

        for i in range(len(temp)): result += str(alphabet[temp[i]])

        return result.upper()
    elif replace_choice in "НетнетNono":
        alone = []
        print("Введите замены\na\n|\nb\n...\n")
        c, d, e, f = input(), input(), input(), input()
        for i in range(100):
            for j in range(26):
                if (alphabet.lower().index(c.lower()) * i + j) % len(alphabet) == alphabet.lower().index(d.lower()) \
                        and (alphabet.lower().index(e.lower()) * i + j) % len(alphabet) == alphabet.lower().index(
                    f.lower()):
                    alone.append(i)
                    alone.append(j)

        MultiA = [x for x in range(1, 50) if 1 == (x * alone[0]) % len(alphabet)][0]
        for i in range(len(source_text)):
            for j in range(len(alphabet)):
                if source_text[i].lower() == alphabet[j].lower():
                    temp.append(MultiA * (j + len(alphabet) - alone[1]) % len(alphabet))

        for i in range(len(temp)):
            result += str(alphabet[temp[i]]).upper()

        do.append(alone[0])
        do.append(alone[1])
        print(alone[0], alone[1])
        print(result)

        MultiA_1 = [x for x in range(1, 50) if 1 == (x * do[0]) % len(alphabet)][0]
        input_1 = input("Есть ли при этом преобразования?: ")
        result_1 = ""
        temp_1 = []
        if input_1 in "ДадаYesyes":
            word = input("Введите текст: ")
            for i in range(len(word)):
                for j in range(len(alphabet)):
                    if word[i].lower() == alphabet[j].lower():
                        temp_1.append(MultiA_1 * (j + len(alphabet) - do[1]) % len(alphabet))

            for i in range(len(temp_1)): result_1 += str(alphabet[temp_1[i]])
            return result_1.upper()


print(Decryption(input("Текст для расшифрования: "),
           input("Алфавит: "),
           input("Известны ли ключи?: ")))