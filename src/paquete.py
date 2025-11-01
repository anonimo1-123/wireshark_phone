string = "###[ Ethernet ]###\n  dst       = 40:3f:8c:c1:d8:1c\n  src       = 10:02:b5:0a:65:d6\n  type      = IPv4\n###[ IP ]###\n     version   = 4\n     ihl       = 5\n     tos       = 0x0\n     len       = 52\n     id        = 27712\n     flags     = DF\n     frag      = 0\n     ttl       = 64\n     proto     = tcp\n     chksum    = 0x9c16\n     src       = 192.168.0.103\n     dst       = 2.20.111.74\n     \\options   \\\n###[ TCP ]###\n        sport     = 38554\n        dport     = https\n        seq       = 187216235\n        ack       = 3526800346\n        dataofs   = 8\n        reserved  = 0\n        flags     = A\n        window    = 280\n        chksum    = 0x943e\n        urgptr    = 0\n        options   = [('NOP', None), ('NOP', None), ('Timestamp', (2271410508, 96095637))]\n"


#Funcion encargada de buscar en toda el string de los datos del paquete un atibuto en comun 
def search_package_attribute(str_packet:str,atribut_find:tuple) -> dict:
    attribute_match = {}
    split_1 = str_packet.split("\n")
    for atributo in atribut_find:
        len_string = len(atributo)
        for i in split_1:
            for index,e in enumerate(i):
                if e == atributo[0]:
                    if atributo == i[index:(index+(len_string))]:
                        attribute_match[atributo]=i[(index+11):]
                        break
    return attribute_match
                        

tupla = ("dst","src")
print(search_package_attribute(string,tupla))