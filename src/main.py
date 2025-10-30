from scapy.all import *
import time

def animation_program():
    for i in range(1,7):
        sys.stdout.writelines("."*i)
        sys.stdout.flush()
        #----------------------
        sys.stdout.write('\r')
        sys.stdout.flush()
        time.sleep(0.5)
        
    sys.stdout.writelines(" "*6+'\r')
    sys.stdout.flush()
    time.sleep(0.6)


def load_packet_on_list(packet:scapy):
    tracked_packet.append(packet)
    animation_program()



 
def sniffing() -> list:
    global tracked_packet
    tracked_packet = []
    str_list = []
    try :
        print("Enpezando el restreo de paquetes por la interfaz : ")
        sniff(iface="wlp3s0",prn=lambda i: load_packet_on_list(packet=i))
    except ValueError:
        print("An error occurred")
    else:
        for i in tracked_packet:
            str_packet = str(i.show(dump=True))
            str_list.append(str_packet)
            
    return str_list


     
def main():
    lista_packet  =  sniffing()


if "__main__" == __name__:
    main()