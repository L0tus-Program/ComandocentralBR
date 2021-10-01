import socket
import os

# tupla listando nossos endereços de ip e porta
enderecos = (                            
    ("Felipe",'localhost',8086),
    ("Alex", 'ip' ,1),
    ("Paula", 'ip', 2),
    ("Salmo","192.168.100.45",3),
    ("Tiago", "192.168.100.21",8080)
) 
    
#print(enderecos)
#print(enderecos[0][1])

os.system("cls")
os.system("start testeservidor.py")
#def client(host = 'localhost', port=8083): 

def client(host, port): 
    # Create a TCP/IP socket 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    # Connect the socket to the server 
    server_address = (host, port) 
    print ("Conectando a %s porta %s" % server_address) 
    sock.connect(server_address) 
    # Send data 
    try: 
        # Send data 
        #message = input("Insira o comando CMD : ") 
        message = comandos()
        print ("Sending %s" % message) 
        sock.sendall(message.encode('utf-8')) 
        
        # Look for the response 
        amount_received = 0 
        amount_expected = len(message) 
        while amount_received < amount_expected: 
            data = sock.recv(16) 
            amount_received += len(data) 
            print ("Recebido: %s" % data) 
    except socket.error as e: 
        print ("Socket error: %s" %str(e)) 
    except Exception as e: 
        print ("Other exception: %s" %str(e)) 
    finally: 
        print ("Fechando a conexão com o servidor") 
        sock.close() 


def menu():
    menu=input("Para qual usuario deseja enviar um comando?\n1- Felipe\n2- Outro\n0 - FECHAR PROGRAMA\n")

    if menu=="1":
        client(enderecos[0][1],enderecos[0][2])
        # chamar função de opções prontas de comandos CMD testados + opção de ocmando personalizado
    elif menu=="2":        
        print("Ainda não implementado")
    elif menu=="0":
        print("Saindo")
        exit(code=None)
    else:
        print("Digitou tudo certo?")




def comandos():
    cmd=input("Comandos:\n1- IPCONFIG\n2- Reinstalar SIGER\n0- CANCELAR")
    if cmd=="1":
        return "ipconfig"
    elif cmd=="2":
        print ("Executando .bat para reinstalação do SIGER no servidor")
        return "start siger.bat"
    elif cmd=="0":
        print ("Saindo")
        exit(Code=None)
    else:
        print("Digitou tudo certo?")
        




#client(enderecos[0][1],enderecos[0][2])


menu()






# temos isso como uma outra possivel alternativa
#https://websetnet.net/pt/how-to-run-powershell-command-line-on-a-remote-computer/