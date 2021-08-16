diccionario = {'a': '2', 'b': '22', 'c': '222', 'd': '3', 'e': '33', 'f': '333',
            'g': '4', 'h': '44', 'i': '444', 'j': '5', 'k': '55', 'l': '555',
            'm': '6', 'n': '66', 'o': '666', 'p': '7', 'q': '77', 'r': '777',
            's': '7777', 't': '8', 'u': '88', 'v': '888', 'w': '9', 'x': '99',
            'y': '999', 'z': '9999'}

def codificacion(mensaje):
    msjCodif, carPrev = '', ' '
    for char in mensaje:
        if char == ' ':
            msjCodif += '0'
            carPrev = '0'
        elif carPrev in diccionario[char]:
            msjCodif += (' ' + diccionario[char])
            carPrev = diccionario[char][0]
        else:
            msjCodif += (diccionario[char])
            carPrev = diccionario[char][0]
    return msjCodif

#bucle para ir solicitando texto al usuario
print("Codificar mensajes a T9 presione ctrl+c paar salir")
while True:
    #pedimos el ingreso del mensaje y lo pasamos a minusculas
    mensajeCodificar = input("un mensaje a traducir a T9: ").lower()
    #codificacion e impresion del mensaje
    print(codificacion(mensajeCodificar))
