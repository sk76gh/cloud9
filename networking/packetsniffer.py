
import socket, struct,binascii

class packet:
    ether=dict()
    ipv4=dict()
    tcp=dict()
    udp=dict()
    #ethernet frame values ################################3
    def setsrcmac(self,srcmac):
        self.ether['src_mac']=srcmac[0:2]+':'+srcmac[2:4]+':'+srcmac[4:6]+':'+srcmac[6:8]+':'+srcmac[8:10]+':'+srcmac[10:12]
        return
    
    def setdestmac(self,destmac):
        self.ether['dest_mac']=destmac[0:2]+':'+destmac[2:4]+':'+destmac[4:6]+':'+destmac[6:8]+':'+destmac[8:10]+':'+destmac[10:12]
        return
    
    def setetherproto(self, proto):
        self.ether['proto']=proto
        return
    
    #IPv4 values ###################
    
    def setsrcip(self,src_ip):
        self.ipv4['src_ip']=src_ip
        return
    
    def setdestip(self,dest_ip):
        self.ipv4['dest_ip']=dest_ip
        return
    
    def setnextproto(self,nextproto):
        self.ipv4['proto']=nextproto
        return
    
    def settotlen(self,tot_len):
        self.ipv4['tot_len']=tot_len
        return
    
    #tcp values##########################
    def setsrcport(self, src_prt):
        self.tcp['src_prt']=src_prt
        return
    
    def setdestport(self,dest_prt):
        self.tcp['dest_prt']=dest_prt
        return
    
    def settcpctrlbits(self,ctrl_bits):
        flag=list()
        
        urg_flag=ctrl_bits & 0x20
        if urg_flag>0:
            flag.append('URG/')
        ack_flag=ctrl_bits & 0x10
        if ack_flag>0:
            flag.append('ACK/')
        psh_flag=ctrl_bits & 0x08
        if psh_flag>0:
            flag.append('PSH/')
        rst_flag=ctrl_bits & 0x04
        if rst_flag>0:
            flag.append('RST/')
        syn_flag=ctrl_bits & 0x02
        if syn_flag>0:
            flag.append('SYN/')
        fin_flag=ctrl_bits & 0x01
        if fin_flag>0:
            flag.append('FIN/')
        
        self.tcp['control_flags']=''.join(flag)
        
        return 
    
    #upd values#############################
    def setudpsrcport(self, src_prt):
        self.udp['src_prt']=src_prt
        return
    
    def setudpdestport(self,dest_prt):
        self.udp['dest_prt']=dest_prt
        return
    
    def printpacketrow(self):
        etherstring=self.ether['src_mac']+'\t'+self.ether['dest_mac']+'\t'+self.ether['proto']
        ipv4string=self.ipv4['src_ip']+'\t'+self.ipv4['dest_ip']+'\t'+self.ipv4['proto']
        if self.ipv4['proto']=='tcp':
            tcpstring=self.tcp['src_prt']+'\t'+self.tcp['dest_prt']+'\t'+self.tcp['control_flags']
            print etherstring+'\t'+ipv4string+'\t'+tcpstring
        if self.ipv4['proto']=='udp':
            udpstring=self.udp['src_prt']+'\t'+self.udp['dest_prt']
            print etherstring+'\t'+ipv4string+'\t'+udpstring
        return
    
    def printetherrow(self):
        etherstring=self.ether['src_mac']+'\t'+self.ether['dest_mac']+'\t'+self.ether['proto']
        print etherstring
        return
    
    def printetherheaders(self):
        return
    
    def analyze_ether_header(self,data):
        ip_bool=False
        eth_hdr=struct.unpack('!6s6sH',data[:14])
        
        dest_mac=binascii.hexlify(eth_hdr[0])
        src_mac=binascii.hexlify(eth_hdr[1])
        proto=hex(eth_hdr[2])
        
        self.setsrcmac(src_mac)
        self.setdestmac(dest_mac)
        
        #print '#########Ethernet Frame##########'
        #print 'Destination MAC  : ',dest_mac[0:2],':',dest_mac[2:4],':',dest_mac[4:6],':',dest_mac[6:8],':',dest_mac[8:10],':',dest_mac[10:12],eth_hdr[0]
        #print 'Source MAC       : ',src_mac[0:2],':',src_mac[2:4],':',src_mac[4:6],':', src_mac[6:8],':',src_mac[8:10],':',src_mac[10:12]
        #print 'Ether Proto            : ',proto
        if proto=='0x800':
            #print 'Next Protocol is IPv4'
            self.setetherproto('IPv4')
            ip_bool=True
        elif proto=='0x86dd':
            #print 'Next Protocol is IPv6'
            self.setetherproto('IPv6')
        elif proto=='0x0806':
            #print 'Next Protocol is ARP'
            self.setetherproto('ARP')
            
        
        return ip_bool,data[14:]
        
    def analyze_ip_header(self,data):
        next_proto=False
        
        ip_hdr=struct.unpack('!6H4s4s',data[:20])
        ver=ip_hdr[0] >> 12 # Version:  4 bits The Version field indicates the format of the internet header
        ihl=(ip_hdr[0]>>8) & 0x0f # IHL:  4 bits Internet Header Length is the length of the internet header in 32 bit words
        typ_srv=ip_hdr[0] & 0x00ff # Type of Service:  8 bits The Type of Service provides an indication of the abstract parameters of the quality of service desired
        tot_len=ip_hdr[1] # Total Length:  16 bits
        ident = ip_hdr[2] # Identification:  16 bits Total Length is the length of the datagram, measured in octets,including internet header and data.
        flags= ip_hdr[3]>>13 #Flags:  3 bits    Various Control Flags.
        frg_ofset=ip_hdr[3] & 0x1fff #  Fragment Offset:  13 bits This field indicates where in the datagram this fragment belongs.
        time_to_live=ip_hdr[4]>>8 #Time to Live:  8 bits This field indicates the maximum time the datagram is allowed to   remain in the internet system.
        proto=ip_hdr[4] & 0x00ff #Protocol:  8 bits This field indicates the next level protocol used in the data portion of the internet datagram
        hdr_crc=ip_hdr[5] # Header Checksum:  16 bits
        src_ip=socket.inet_ntoa(ip_hdr[6])
        dest_ip=socket.inet_ntoa(ip_hdr[7])
      
        
        self.setsrcip(src_ip)
        self.setdestip(dest_ip)
        self.settotlen(tot_len)
        
        #print '#########IPv2####################'
        #print 'Version                  : ',ver
        #print 'Internet Header length   : ',ihl
        #print 'Type of service          : ',typ_srv
        #print 'Total Length             : ',tot_len
        #print 'Identification           : ',ident
        #print 'Flags                    : ',flags
        #print 'Fragment offset          : ',frg_ofset
        #print 'Time to Live             : ',time_to_live
        #print 'Protocol                 : ',proto
        #print 'Header Checksum          : ',hdr_crc
        #print 'Source IP                : ',src_ip
        #print 'Destination IP           : ',dest_ip
        
        if proto==6:
            #print 'Next Protocol is TCP'
            next_proto='tcp'
            self.setnextproto(next_proto)
        elif proto==1:
            #print 'Next Protocol is ICMP'
            next_proto='icmp'
            self.setnextproto(next_proto)
        elif proto==17:
            #print 'Next Protocol is UDP'
            next_proto='udp'
            self.setnextproto(next_proto)
        else:
            next_proto==str(proto)
        
        return next_proto, data[20:]
    
    def analyze_tcp_header(self,data):
        
        tcp_hdr=struct.unpack('!2H2I4H',data[:20])
        src_prt=tcp_hdr[0] #Source Port:  16 bits
        dest_prt=tcp_hdr[1] #Destination Port:  16 bits
        seq_num=tcp_hdr[2] #Sequence Number:  32 bits
        ack_num=tcp_hdr[3] #Acknowledgment Number:  32 bits
        data_ofset=tcp_hdr[4]>>12 #Data Offset:  4 bits
        ctrl_bits=tcp_hdr[4] & 0x003f #Control Bits:  6 bits (from left to right)
        urg_flag=ctrl_bits & 0x20
        ack_flag=ctrl_bits & 0x10
        psh_flag=ctrl_bits & 0x08
        rst_flag=ctrl_bits & 0x04
        syn_flag=ctrl_bits & 0x02
        fin_flag=ctrl_bits & 0x01
        window=tcp_hdr[5] # Window:  16 bits
        chk_sum=tcp_hdr[6] # Checksum:  16 bits
        urg_prt=tcp_hdr[7] #Urgent Pointer:  16 bits
        
        
        self.setsrcport(str(src_prt))
        self.setdestport(str(dest_prt))
        self.settcpctrlbits(ctrl_bits)
        #print '#########TCP#####################'
        #print 'Source Port                  : ',src_prt
        #print 'Destination Port             : ',dest_prt
        #print 'Sequence Number              : ',seq_num
        #print 'Acknowledgement Number       : ',ack_num
        #print 'Data Offset                  : ',data_ofset
        #print 'Control Bits                 : ',ctrl_bits
        #print 'URG Flags                    : ',urg_flag
        #print 'ACK Flags                    : ',ack_flag
        #print 'PSH Flags                    : ',psh_flag
        #print 'RST Flags                    : ',rst_flag
        #print 'SYN Flags                    : ',syn_flag
        #print 'FIN Flags                    : ',fin_flag
        #print 'Window                       : ',window
        #print 'Checksum                     : ',chk_sum
        #print 'Urgent Pointer               : ',urg_prt
        return data[20:]
    
    def analyze_udp_header(self,data):
        udp_hdr=struct.unpack('!4H',data[:8])
        src_prt=udp_hdr[0] #Source Port:  16 bits
        dest_prt=udp_hdr[1] #Destination Port:  16 bits
        length=udp_hdr[2]
        chk_sum=udp_hdr[3]
        
        self.setudpsrcport(str(src_prt))
        self.setudpdestport(str(dest_prt))
        #print '#########UDP#####################'
        #print 'Source Port                  : ',src_prt
        #print 'Destination Port             : ',dest_prt
        #print 'Length                       : ',length
        #print 'Check Sum                    : ',chk_sum
        
        
        return data[8:]
    
def main():
    packobj=packet()
    
    sniffersocket=socket.socket(socket.PF_PACKET,socket.SOCK_RAW,socket.htons(0x0003))
    recv_data=sniffersocket.recv(2048)
    ip_bool, data=packobj.analyze_ether_header(recv_data)
    
    if ip_bool:
        next_proto, data=packobj.analyze_ip_header(data)
    else:
        next_proto='Not IPv4'
        packobj.printetherrow()
    
    if next_proto=='tcp':
        data=packobj.analyze_tcp_header(data)
    elif next_proto=='udp':
        data=packobj.analyze_udp_header(data)
    elif next_proto=='icmp':
        print 'icmp request'

        
    packobj.printpacketrow()
    
for x in range(100):
    main()