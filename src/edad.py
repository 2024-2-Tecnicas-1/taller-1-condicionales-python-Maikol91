from time import localtime


def evaluar(dia, mes, anno):
    t = localtime()
    dia_actual = t.tm_mday
    mes_actual = t.tm_mon
    anno_actual = t.tm_year 
    diferencia_anno= anno_actual-anno

    if (mes_actual<=mes):
        if (dia>dia_actual):
            diferencia_anno-=1
    return "Usted tiene " + str(diferencia_anno) + " años"


if __name__ == '__main__':
    print("Ingrese su fecha de nacimiento")
    print("Día:", end="")
    dia = int(input())
    print("Mes:", end="")
    mes = int(input())
    print("Año:", end="")
    anno = int(input())
        
    respuesta = evaluar(dia, mes, anno)
    print(respuesta)
