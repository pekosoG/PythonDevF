#Encoding
# -*- coding: utf-8 -*-


def timbreToily(nombre, mensaje='Hola'):
    print mensaje,nombre

#timbreToily('Pekoso')
#timbreToily('H4rry','Sup!')


def playRecursivo(intento=1):
    respuesta=raw_input("De qué color es la naranja?: ")
    if respuesta!= "naranja":
            if intento < 3:
                print "Nel carnal..."
                intento+=1
                playRecursivo(intento)
            else:
                print "Perdiste!"
    else:
        print "Ganaste wei!"

#playRecursivo()


def printing():
        a,b,c='string',25,True
        mi_tupla=('asdsdas',1233)
        texto,anio=mi_tupla
        print str(a)
        print str(b)
        print str(c)
        print str(texto)
        print str(anio)
        print str(mi_tupla)

#printing()

def the_while():
    while True:
        nombre=raw_input('gimmie your name: ')
        if nombre:
                print nombre
                break

#the_while()

def the_for():
    mi_lista=['dys','F4','KISS','Pyro']
    for nombre in mi_lista:
        print nombre
    mi_tupla= ('qweqwe','qqeqe','qweqweqwe','qweqweqweqw')
    for asd in mi_tupla:
        print asd
    for numero in range(0,1000,50):
        print numero

the_for()