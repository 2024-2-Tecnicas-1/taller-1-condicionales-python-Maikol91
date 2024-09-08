def evaluar(peso, estatura, edad):
    imc = (peso) / estatura ** 2
    if (edad <= 44): 
        if (imc < 22.0):
                return "bajo"
                if (imc > 22.0):
                 return "medio"
                if(edad > 44):
                 if(imc<22.0):
                    return "medio"
                if(imc>22.0):
                    return "alto"

if __name__ == '__main__':
    print("Peso:", end="")
    peso = int(input())
    print("Estatura:", end="")
    estatura = float(input())
    print("Edad:", end="")
    edad = int(input())
        
    respuesta = evaluar(peso, estatura, edad)
    print(respuesta)
