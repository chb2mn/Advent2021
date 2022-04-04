from copy import deepcopy
from pprint import pprint
part=2

def get_bit_freq(fin):
    bit_freq = []
    datum=[]
    for line in fin:
        datum.append(line)
        for i,bit in enumerate(line):
            if bit.strip() == '': continue
            try:
                bit_freq[i][bit] +=1
            except KeyError:
                bit_freq[i][bit] = 1
            except IndexError:
                bit_freq.append({bit:1})
    return bit_freq, datum

def cull_data(datum, bit, i):
    return [x for x in datum if x[i] == bit]

with open('input.txt', 'r') as fin:
    bit_freq, datum = get_bit_freq(fin)

if part==2:
    i=0
    datum2 = deepcopy(datum)
    bit_freq2 = deepcopy(bit_freq)
    while len(datum) >1:
        if len(datum) < 20:
            pprint(datum)
        datum = cull_data(datum, "0" if bit_freq[i]["0"] > bit_freq[i]["1"] else "1", i)
        bit_freq, _ = get_bit_freq(datum)
        i+=1
    o2 = datum[0].strip()
    print(o2)

    #-=-=-co2 time -=-=-=-=
    
    datum = datum2
    bit_freq=bit_freq2
    i=0
    while len(datum) >1:
        datum = cull_data(datum, "0" if bit_freq[i]["0"] <= bit_freq[i]["1"] else "1", i)
        bit_freq, _ = get_bit_freq(datum)
        i+=1
    co2 = datum[0].strip()
    print(co2)
    print(int(o2, 2), int(co2,2))
    print(int(o2, 2)* int(co2,2))

if part ==1:
    print(bit_freq)
    mcb = "".join(["0" if d["0"] > d["1"] else "1" for d in bit_freq])
    print("0b"+mcb)
    mcb = int(mcb, 2)
    lcb = mcb ^ int("1"*len(bit_freq), 2)
    print(bin(lcb))
    print (mcb)
    print(lcb)
    print(mcb*lcb)
