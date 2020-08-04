import socket, random

# initial values
options=['save','load']
HOST, PORT = 'localhost', 50001
filename="../dictionary.txt"
wordmap=dict()
lineindex=0
http_response='Hi there!'
# read from dictionary
with open(filename,'r') as messagefile:
    for line in messagefile:
        wordmap[lineindex]=line
        lineindex+=1
        
mapsize=len(wordmap)

#open socket    
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print 'Serving HTTP on port %s ...' % PORT

#listen to clients
while True:
    client_connection, client_address = listen_socket.accept()
    requestoption = client_connection.recv(4)
    print requestoption
   
   # Save request
    if requestoption==options[0]:
        request = client_connection.recv(8)
        options.append(request)
        http_response=request+' included successfully : '+str(options)
   
    # Load request
    if requestoption==options[1]:
        request = client_connection.recv(8)
        #...
        http_response=request+' loaded successfully'
    
    

    #http_response =wordmap[random.randint(0,mapsize)]
    client_connection.sendall(http_response)
    client_connection.close()