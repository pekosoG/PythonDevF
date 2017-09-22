#Encoding
# -*- coding: utf-8 -*-

#lista=[1,2,3,4,5,6,7]

#print lista[2]
#print lista[2:5]
#print lista[5:]
#print lista[:5]
#print lista[:]

#m=0
#for i in range(len(lista)):
#    if m<lista[i]:
#        m = lista[i]
#    print i,m
#


#lista.append("adsasd")
#lista.insert(1,'asdasdasdasdfgg')

#print lista

#lista.pop()
#lista.pop(4)
#lista.remove(7)

#print lista

#lista= []

print lista

lista= []
for index in range(input('cuantas palabras quieres?:')):
    lista.append(raw_input('Palabra #'+str(index+1)+':'))
print '\n'.join(lista)


print "\t\t".join(map(lambda x: "".join(raw_input("Dame uno elemento\t\t")) ,range(input("Dame tamaño de la lista: \t"))))