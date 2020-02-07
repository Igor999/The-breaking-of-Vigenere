def jarriquez_encryption(text, key, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ', reverse=False):
    while key <= 1000000:
        text = text.upper()
        new_text = ""
        for i in text:
            if i in alphabet:
                new_text +=i
        key_box = []
        k = 0
        while k == 0:
            for i in str(key):
                key_box.append(int(i))
                if len(key_box) == len(new_text):
                    k = 1
                    break
        result = ""
        if reverse == False:
            for i in range(len(new_text)):
                symbol = new_text[i]
                symbol_key = key_box[i]
                go = alphabet.index(symbol)
                if go+symbol_key <= len(alphabet)-1:
                    new_symbol = alphabet[go+symbol_key]
                elif go+symbol_key > len(alphabet)-1:
                    new_symbol = alphabet[go+symbol_key-(len(alphabet))]
                else:
                    new_symbol = alphabet[go+symbol_key-(len(alphabet))]
                result += new_symbol
            print(result)
            print(key)
            if ("АЛМАЗ" in result) and ("ДАКОСТА" in result):
                break
            key += 1
        else:
            for i in range(len(new_text)):
                symbol = new_text[i]
                symbol_key = key_box[i]
                go = alphabet.index(symbol)
                if 0 <= go-symbol_key <= len(alphabet)-1:
                    new_symbol = alphabet[go-symbol_key]
                else:
                    new_symbol = alphabet[(len(alphabet))+(go-symbol_key)]
                result += new_symbol
            print(result)
            print(key)
            if ("АЛМАЗ" in result) and ("ДАКОСТА" in result) :
               break
            key += 1
jarriquez_encryption(text = """ТЛБЛДУЭППТКЛФЧУВНУПБКЗИХТЛТТЫХНЛОИНУВЖММИНПФНПШОКЧЛЕРНТФНАХЖИДМЯКЛТУБЖИУЕЖЕАХЛГЩЕЕ

ЪУВНГАХИЯШПЙАОЦЦПВТЛБФТТИИНДИДНЧЮОНЯОФВТЕАТФУШБЛРЮЮЧЖДРУУШГЕХУРПЧЕУВАЭУОЙБДБНОЛСКЦБ

САОЦЦПВИШЮТППЦЧНЖОИНШВРЗЕЗКЗСБЮНЙРКПСЪЖФФШНЦЗРСЭШЦПЖСЙНГЭФФВЫМЖИЛРОЩСЗЮЙФШФДЖО

ИЗТРМООЙБНФГОЩЧФЖООКОФВЙСЭФЖУЬХИСЦЖГИЪЖДШПРМЖПУПГЦНВКБНРЕКИБШМЦХЙИАМФЛУЬЙИСЗРТЕС""", key = 1000, alphabet='АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', reverse=True
