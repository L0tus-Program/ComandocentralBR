import socket
import os
import time

os.system("cls")
#os.system("start testeservidor.py")


def client(host = 'localhost', port=8083): 
   # time.sleep(5)
    message=None
    stop_server = "exit"
    # Create a TCP/IP socket 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    # Connect the socket to the server 
    server_address = (host, port) 
    print ("Connecting to %s port %s" % server_address) 
    sock.connect(server_address) 
    # Send data 
    
    while message!="exit":
        time.sleep(2)
        print("Inicio while")
        try: 
        # Send data 
            message = input("Insira o comando CMD: ") 
            if message == "exit":
                print("Conexão encerrada")
                sock.sendall(stop_server.encode("utf-8")) #encodar string funciona?
                sock.close()
                
                break
            else:
                print ("Sending %s" % message) 
                sock.sendall(message.encode("utf-8")) 
        
            
        # Look for the response 
            amount_received = 0 
            amount_expected = len(message) 
            while amount_received < amount_expected: 
                data = sock.recv(64) 
                amount_received += len(data) 
                print ("Received: %s" % data)
            sock.close() 
        except socket.error as e:  #estou caindo aqui na segunda execução: "[WinError 10038] Foi tentada uma operação em algum item que não é um soquete"
            print ("Socket error: %s" %str(e)) 
        except Exception as e: 
            print ("Other exception: %s" %str(e)) 
        finally: 
            print ("Fechando conexão com o servidor") 
            sock.close() 


   

client()




# https://medium.com/@urapython.community/introdução-a-sockets-em-python-44d3d55c60d0


# para rodar varios clientes em paralelo 
# https://medium.com/grupo-de-resposta-a-incidentas-de-segurança/trabalhando-com-redes-ii-em-python-f12449aa58d0