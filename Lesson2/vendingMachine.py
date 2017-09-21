lista_producto=[['1.- pop',2.5],
                ['2.- bip',1.4],
                ['3.- pip',4],
                ['4.- plap',1.2]]

max_money=5

def iniciar():
    imprimeProductos()
    cash=input("Mmmmoney (Max 5): ")

    if cash>max_money :
        print 'maximo 5!!'
    else:
        seleccion=input("wayuwant? : ")
        if(seleccion<=len(lista_producto)):
            precio=lista_producto[seleccion-1][1]
            if precio<=cash :
                calcula_vuelto(cash,precio)
            else :
                print 'no te alcanza, again!'
        else:
            print 'opcion invalida'


def imprimeProductos():
    for producto in lista_producto:
        print producto[0]+' $'+str(producto[1])


def calcula_vuelto(monto,precioProducto):
    print 'tu cambio es '+str(monto-precioProducto)

iniciar()
