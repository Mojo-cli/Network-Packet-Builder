from scapy.all import *
file = rdpcap('./Sample1.pcapng')
# print(file)
# print(file.show())
# f = file[0]

for f in file:
    print(f)
    # print(f.show())
    if(f.haslayer(DNS)):
        print(f[DNS].id)