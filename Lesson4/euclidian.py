import math

def euclidean_dist(punto1,punto2):
    """
    Method to have euclidean distance betewwn two points (2D or 3D)
    :param punto1: Array
    :param punto2: Array
    :return: none
    """
    if len(punto1)>=2 and len(punto2)>=2:
        if len(punto1)==len(punto2):
            sum=0
            for index in range(len(punto1)):
                sum+=math.pow(float(punto2[index])-float(punto1[index]),2)
            sum=math.sqrt(float(sum))
            print 'Distancia entre puntos es: '+str(sum)
        else:
            print 'puntos en dimesiones diferentes'
    else:
        print 'puntos invalidos (2d minimo)'


punto1=raw_input('Escribre las coordenadas del primer punto, separados por comas:').split(',')
punto2=raw_input('Escribre las coordenadas del segundo punto, separados por comas:').split(',')

euclidean_dist(punto1,punto2);