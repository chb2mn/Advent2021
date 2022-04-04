from icecream import ic
import math

def hex2bin(h):
    return "".join([bin(int(c,16))[2:].zfill(4) for c in h])

with open('input.txt', 'r') as fin:
    for line in fin:
        bstring = "".join([hex2bin(x) for x in line.strip()])

class Packet:
    def __init__(self, _version, _type, _subpackets, total_len):
        self.version = int(_version,2)
        self.type = int(_type,2)
        self.subpackets = _subpackets
        self.total_len = total_len

    def __repr__(self):
        if isinstance(self.subpackets, int):
            return f"V:{self.version}-T:{self.type}, value:{self.subpackets}"
        return f"V:{self.version}-T:{self.type}, packets:{[str(x) for x in self.subpackets]}"
def parse_packet(bstring):
    '''Takes telemetry and returns the first packet with any trailing 0's'''
    version = bstring[:3]
    bstring = bstring[3:]
    type_id = bstring[:3]
    bstring = bstring[3:]
    if type_id == "100":
        total_len = 6
        '''literal value'''
        annie = ""
        elphie = "1" 
        while elphie == "1":
            elphie = bstring[0]
            annie += bstring[1:5]
            bstring = bstring[5:]
            total_len+=5
        annie = int(annie,2)
        return Packet(version, type_id, annie, total_len)
    else:
        l_type = bstring[0]
        bstring = bstring[1:]
        total_len = 7
        sub_p = []
        if l_type == "0":
            pack_len = int(bstring[:15],2)
            bstring=bstring[15:]
            sub_b = bstring[:pack_len]
            bstring = bstring[pack_len:]
            total_len += 15+pack_len
            while(len(sub_b) >6):
                sub_p.append(parse_packet(sub_b))
                sub_b = sub_b[sub_p[-1].total_len:]
                bstring = bstring[sub_p[-1].total_len:]
        if l_type == "1":
            pack_len = int(bstring[:11],2)
            bstring = bstring[11:]
            total_len += 11
            for i in range(pack_len):
                sub_p.append(parse_packet(bstring))
                bstring = bstring[sub_p[-1].total_len:]
                total_len += sub_p[-1].total_len
        return Packet(version, type_id, sub_p, total_len)

'''
#TEST PART !
p = parse_packet(hex2bin("D2FE28"))
ic(p)
p = parse_packet(hex2bin("38006F45291200"))
ic(p)
p = parse_packet(hex2bin("EE00D40C823060"))
ic(p)
bstring = hex2bin("8A004A801A8002F478")
bstring = hex2bin("620080001611562C8802118E3")
bstring = hex2bin("C0015000016115A2E0802F182340")
bstring = hex2bin("A0016C880162017C3686B18A3D4780")
'''

'''
#TEST PART 2
bstring = hex2bin("C200B40A82")
bstring = hex2bin("04005AC33890")
bstring = hex2bin("880086C3E88112")
bstring = hex2bin("CE00C43D881120")
bstring = hex2bin("D8005AC2A8F0")
bstring = hex2bin("F600BC2D8F")
bstring = hex2bin("9C005AC2F8F0")
bstring = hex2bin("9C0141080250320F1802104A08")
'''       


ic(bstring)
packets = []
while bstring.find("1") >= 0:
    packets.append(parse_packet(bstring))
    bstring = bstring[packets[-1].total_len:]

#ic(packets)

#Part 1
def sum_versions(packets):
    my_sum = 0
    for p in packets:
        if isinstance(p.subpackets, int):
            my_sum += p.version
        else:
            my_sum += p.version + sum_versions(p.subpackets)
    return my_sum

ic(sum_versions(packets))

#Part 2
def do_packet_math(packet):
    if packet.type == 0:
        return sum([do_packet_math(x) for x in packet.subpackets])
    elif packet.type == 1:
        return math.prod([do_packet_math(x) for x in packet.subpackets])
    elif packet.type == 2:
        return min([do_packet_math(x) for x in packet.subpackets])
    elif packet.type == 3:
        return max([do_packet_math(x) for x in packet.subpackets])
    elif packet.type == 4:
        return packet.subpackets #value
    elif packet.type == 5:
        return do_packet_math(packet.subpackets[0]) > do_packet_math(packet.subpackets[1])
    elif packet.type == 6:
        return do_packet_math(packet.subpackets[0]) < do_packet_math(packet.subpackets[1])
    elif packet.type == 7:
        return do_packet_math(packet.subpackets[0]) == do_packet_math(packet.subpackets[1])

def debug_packet_math(packet):
    if packet.type == 0:
        return f"sum({[do_packet_math(x) for x in packet.subpackets]})"
    elif packet.type == 1:
        return f"math.prod({[do_packet_math(x) for x in packet.subpackets]})"
    elif packet.type == 2:
        return f"min({[do_packet_math(x) for x in packet.subpackets]})"
    elif packet.type == 3:
        return f"max({[do_packet_math(x) for x in packet.subpackets]})"
    elif packet.type == 4:
        return packet.subpackets #value
    elif packet.type == 5:
        return f"{do_packet_math(packet.subpackets[0])} > {do_packet_math(packet.subpackets[1])}"
    elif packet.type == 6:
        return f"{do_packet_math(packet.subpackets[0])} < {do_packet_math(packet.subpackets[1])}"
    elif packet.type == 7:
        return f"{do_packet_math(packet.subpackets[0])} == {do_packet_math(packet.subpackets[1])}"

ic(len(packets))
ic(do_packet_math(packets[0]))
ic(debug_packet_math(packets[0]))
