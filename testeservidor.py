import socket
import os
import sys
import win32com.shell.shell as shell
    
def server(host ='localhost', port=8086):        
    ASADMIN = 'asadmin'
    if sys.argv[-1] != ASADMIN:
        script = os.path.abspath(sys.argv[0])
        params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
        shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
    fim="Fechando servidor" #caso o comando enviado seja stop server
    copydata = None
    #copyconsole = None
    data_payload = 4048 #The maximum amount of data to be received at once
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
    # Enable reuse address/port 
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to the port
    server_address = (host, port)
    print ("Iniciando servidor no host %s porta %s" % server_address)
    sock.bind(server_address)
    
    # Listen to clients, argument specifies the max no. of queued connections
    sock.listen(5) 
   # i = 0
    while True: #comunicação acontecendo entre cliente e servidor
        print ("Esperando mensagem do cliente")
        client, address = sock.accept()
        data = client.recv(data_payload) 
        #data = client.recv() 
    
        if data:
            print(data)
            copydata = str(data) #fazemos uma cópia de data como string e retiramos os caracteres desnecessários, assim tendo o "comando" que enviamos pelo client
            copydata = copydata[2:-1]
            print(copydata)
            
            if copydata == "exit": #caso o comando seja para parar o servidor
                client.send(fim.encode("UTF-8"))  
                client.close()
                break
            else:
                os.system(copydata) # trava com taskkill
                #copyconsole= os.popen(copydata).read() #salva a cópia do que foi executado no cmd
                #input("PAUSE")
                print ("Data: %s" %data)
                client.send(data)
                print ("Enviando retorno %s para %s" % (data, address))
                # end connection
                client.close()
                #data = None
                
              #  i+=1
              #  if i>=3: break
                       
server()





# https://medium.com/@urapython.community/introdução-a-sockets-em-python-44d3d55c60d0