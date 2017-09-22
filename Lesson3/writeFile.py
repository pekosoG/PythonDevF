def escribeArchivo():
    file = open('archivillo.txt', 'w')
    file.write('Lorep Ipsum')
    file.close()

escribeArchivo()