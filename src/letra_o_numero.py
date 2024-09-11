def evaluar(caracter):
    codigo=ord(caracter)
    if (codigo >= 65 and codigo <= 90):      
        return "Es letra mayúscula"
    if (codigo >= 97 and codigo <= 122):
        return "Es letra minúscula"
    if (codigo >= 48 and codigo <= 57):
        return "Es número"
    else: 
        return "No es letra ni número"

if __name__ == '__main__':
    print("Caracter:", end='')
    caracter = input()
        
    respuesta = evaluar(caracter)
    print(respuesta)
