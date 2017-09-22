#Encoding
# -*- coding: utf-8 -*-

#
#    EASY MODE
#

ip_address=raw_input("Dame una Dirección IP: ")
ip_address_split=ip_address.split('.')

if len(ip_address_split)==4:
    for segmento in ip_address_split:
        if segmento.isdigit() and len(segmento)<4:
            print 'El segmento '+str(segmento)+' es válido'
        else:
            print 'El segmento ' + str(segmento) + ' es inválido'
            break

else:
    print 'IP No Válida'

#
#   SLIM MODE
#

import re
print 'IP Valida (regex1):'+str(len(re.findall(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$',ip_address))>0)

print 'IP Valida (regex2):'+str(len(re.findall(r'^[0-2]{,1}[0-9]{1,2}\.[0-2]{,1}[0-9]{1,2}\.[0-2]{,1}[0-9]{1,2}\.[0-2]{,1}[0-9]{1,2}$',ip_address))>0)