'''
The final activity for the Advanced Python section is a drive-wide FTP-like
tool. You should be able to receive multiple connections, each on their 
own thread. You should take several commands:
DRIVESEARCH <filename>
    DRIVESEARCH looks for the given filename across the entire drive. If
    it finds the file, it sends back the drive location.
DIRSEARCH <directory> <filename>
    DIRSEARCH looks for the file in the given directory or its 
    subdirectories. If it finds the file, it sends back the location.
DOWNLOAD <filename>
    DOWNLOAD requires the full file path, or at least the relative path,
    of the file. It sends the contents of the file across the network.
UPLOAD <filename>
    UPLOAD requires the full file path, or at least the relative path,
    where the user wants to locate the file. It reads the file contents
    from across the network connection.
CLOSE
    CLOSE ends the connection
    
This activity will require you to use multithreading, ctypes, regular
expressions, and some libraries with which you're unfamiliar. ENJOY!
'''

import os, re, socket, threading, struct
from ctypes import *

def read_file(filename): #ctypes
    print 'inside read_file',filename
    file_handle=windll.Kernel32.CreateFileA(filename,0x10000000,0,0,3,0x80,0)
    if file_handle==-1:
        return 'sorry could not get file handle'
    read_data=c_int(0)
    data=create_string_buffer(4096)
    flag=windll.Kernel32.ReadFile(file_handle,byref(data),4096,byref(read_data),0)
    windll.Kernel32.CloseHandle(file_handle)
    if flag==-1:
        return 'read file operation failed'

    return data.value

def create_file(filename, data): #ctypes
    file_handle= windll.Kernel32.CreateFileA(filename,0x10000000,0,0,2,0x80,0)
    written_data=c_int(0)
    windll.Kernel32.WriteFile(file_handle,data,len(data),byref(written_data),0)
    windll.Kernel32.CloseHandle(file_handle)
    return

def recv_data(sock): #Implement a networking protocol
    data=sock.recv(1024)
    return data

def send_data(sock,data): #Implement a networking protocol
    sock.sendall(data)
    return

def search_drive(file_name): #DRIVESEARCH
    #print 'Inside : Drivesearch'+ os.path.dirname(file_name)
    file_path='NOT FOUND : '+file_name
    dirpath=os.path.dirname(os.getcwd())
    drive=dirpath.split('\\')[0]+'\\Users\\307003405\\Desktop'
    for root, subdir,files in os.walk(drive):
        #print root, files
        if os.path.basename(file_name) in files:
            file_path= 'FOUND !!! File location at : '+root+'\\'+file_name
            
    return file_path

def search_directory(file_name): #DIRSEARCH
    #print 'Inside :'+file_name
    file_path='NOT FOUND : '+file_name
    curdir=os.getcwd()
    for root, subdir,files in os.walk(curdir):
        print root, files
        if os.path.basename(file_name) in files:
            file_path= 'FOUND !!! File location at : '+root+'\\'+file_name

    return file_path

def send_file_contents(file_name,usersock,userinfo): #DOWNLOAD
    print 'Inside send file:'+file_name
    print userinfo['path']
    if file_name.strip()!='':
        data=read_file(userinfo['path'])
        print 'Inside file data sending', data
        #usersock.sendall(data)
        send_data(usersock,data)
    else:
        #usersock.sendall('No file path mentioned')
        send_data(usersock,'No file path mentioned')

    return

def receive_file_contents(file_name,usersock):#UPLOAD
    #print 'Inside :'+file_name
    return

def handle_connection(client_conn,userinfo):
    http_resp=''
    flag=True
    client_ip=userinfo['client_ip']
    space=' '
    empty=''
    usersock=''
    file_name=''
    file_path=''
    
    
    data=recv_data(client_conn)
    print data
    if data.strip().find(space)>0:
        p=re.search('(.+)\s(.+)',data)
        command=p.group(1).upper()
        path=p.group(2)
    else:
        p=re.search('(.+)',data)
        command=p.group(1).upper()
        path=empty

    userinfo['command']=c