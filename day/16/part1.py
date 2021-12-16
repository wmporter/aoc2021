"""The BITS transmission contains a single packet at its outermost layer which
itself contains many other packets. The hexadecimal representation of this packet
might encode a few extra 0 bits at the end; these are not part of the transmission
and should be ignored.

Every packet begins with a standard header: the first three bits encode the packet
version, and the next three bits encode the packet type ID. These two values are
numbers; all numbers encoded in any packet are represented as binary with the most
significant bit first. For example, a version encoded as the binary sequence 100
represents the number 4.

Packets with type ID 4 represent a literal value. Literal value packets encode a
single binary number. To do this, the binary number is padded with leading zeroes
until its length is a multiple of four bits, and then it is broken into groups of
four bits. Each group is prefixed by a 1 bit except the last group, which is
prefixed by a 0 bit. These groups of five bits immediately follow the packet
header. For example, the hexadecimal string D2FE28 becomes:
"""
def read_subpacket_length(packet):
    return int(packet[7:22], 2), 15

def read_subpacket_count(packet):
    return int(packet[7:18], 2), 11

def read_operator_mode(packet):
    return int(packet[6], 2), 1

def read_literals(packet):
    read = 5
    start = 6
    literal = packet[6:11]
    value = literal
    while literal[0] == '1':
        start += 5
        literal = packet[start:start+5]
        value += literal
        read += 5
    return int(value, 2), read


def read_packet_header(packet):
    ver = int(packet[:3], 2)
    id = int(packet[3:6], 2)
    return ver, id, 6

def read_packet(packet):
    ver, id, read = read_packet_header(packet[0:])
    ver_sum = ver
    read_ptr = read
    while read_ptr < len(packet)-1:
        if id == 4:
            lit_val, read = read_literals(packet[0:])
            read_ptr += read
            read_ptr += 4 - (read_ptr % 4)
        else:
            mode = read_operator_mode(ver, id, read = read_packet_header(packet[read_ptr:])

with open("input") as f:
    inp = f.readlines()

print("total =", 100)
