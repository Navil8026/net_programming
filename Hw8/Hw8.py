import socket
import struct
import binascii

class Udphdr:
    def __init__(self, src_port, dst_port, length, checksum):
        self.src_port = src_port
        self.dst_port = dst_port
        self.length = length
        self.checksum = checksum

    def pack_Udphdr(self):
        packed = b''
        packed += struct.pack('!2H', self.src_port, self.dst_port)  #src_port, dst_port가 2byte이므로 HH or 2H
        packed += struct.pack('!2H', self.length, self.checksum)    #length, checksum이 2byte이므로 HH or 2H
        return packed

def unpack_Udphdr(buffer):
    unpacked = struct.unpack('!4H', buffer[:8]) #2byte씩 4개이므로 HHHH or 4H
    return unpacked

def getSrcPort(unpacked_udpheader): #unpack된 결과에서 SrcPort 값을 가져오는 함수
    return unpacked_udpheader[0]

def getDstPort(unpacked_udpheader): #unpack된 결과에서 DstPort 값을 가져오는 함수
    return unpacked_udpheader[1]

def getLength(unpacked_udpheader):  #unpack된 결과에서 Length 값을 가져오는 함수
    return unpacked_udpheader[2]

def getChecksum(unpacked_udpheader):    #unpack된 결과에서 Checksum 값을 가져오는 함수
    return unpacked_udpheader[3]
udp = Udphdr(5555,80,1000,0xFFFF)
packed_udphdr = udp.pack_Udphdr()
print(binascii.b2a_hex(packed_udphdr))  #이진 출력

unpacked_udphdr = unpack_Udphdr(packed_udphdr)
print(unpacked_udphdr)  #unpack된 값 출력
#각 필드에 해당하는 값 출력
print('Source Port:{} Destination Port:{} Length:{} Checksum:{}'\
    .format(getSrcPort(unpacked_udphdr), getDstPort(unpacked_udphdr), getLength(unpacked_udphdr), getChecksum(unpacked_udphdr)))