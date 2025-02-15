def ip_to_byte_string(ip):
    # given ip address in string, convert it to bytes
    return bytearray(map(int, ip.split('.')))

def checksum(pseudo_header, tcp_data):
    data = pseudo_header + tcp_data
    total = 0
    offset = 0
    while offset < len(data):
        word = int.from_bytes(data[offset: offset + 2], 'big')
        offset += 2

        total += word
        total = (total & 0xffff) + (total >> 16)

    return (~total) & 0xffff

for i in range(10):
    with open(f'./tcp_data/tcp_addrs_{i}.txt', 'r') as addresses:
        source, destination = addresses.read().split()

    with open(f'./tcp_data/tcp_data_{i}.dat', 'rb') as data:
        bin_data = data.read()


    pseudo_header = ip_to_byte_string(source) # source ip address to bytes
    pseudo_header.extend(ip_to_byte_string(destination)) # destination ip address to bytes
    pseudo_header.extend(b'\x00\x06') # zero 0x00 and protocol (TCP --> 0x06)
    pseudo_header.extend(len(bin_data).to_bytes(2, 'big')) # len of the data

# print("pseudo header:", pseudo_header)

    the_original_checksum = int.from_bytes(bin_data[16:18])

# print("original: ", the_original_checksum)

    tcp_zero_cksum = bin_data[:16] + b'\x00\x00' + bin_data[18:]

    if(len(tcp_zero_cksum) % 2 == 1):
        tcp_zero_cksum += b'\x00'

    calculated_checksum = checksum(pseudo_header, tcp_zero_cksum)

# print("calculated checksum: ", calculated_checksum)

    print(the_original_checksum == calculated_checksum)
