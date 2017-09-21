for valor in range(1,11):
    print '\n---Tabla del '+str(valor)
    for numero in range(1,11):
        print str(valor)+' x '+str(numero)+' = '+str(valor*numero)

#ONE LINE
print '\n'.join(''.join(i) for i in [str(x)+'*'+str(y)+'='+str(x*y) for x in range(1,11) for y in range(1,11)])

