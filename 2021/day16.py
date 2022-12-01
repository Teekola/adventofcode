from time import perf_counter as pfc


"""
Parse the hierarchy of the packets
Add upp all of the version numbers


The first step of decoding the message is to convert the hexadecimal representation into binary. Each character of hexadecimal corresponds to four bits of binary data
"""

def readInput(fileName):
    with open(fileName, 'r') as f:
        hex_str = f.readline().strip()
    
    return hex_str


# Helpers
def hexToBinary(hex_str) -> str:
    bin_str = ""
    lookup_table = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111",
    }

    for char in hex_str:
        bin_str += lookup_table[char]
    
    return bin_str

def parse(transmission, i, j=-1, rem=-1):
    """
    Parse the data
        - starting at index i
        - ending at j
        - with rem packets left
    
    Return
        - version of current packet
        - index of the next packet's start
    """
    # There are no more operator subpackets
    if rem == 0:
        return None, None
    if i == j:
        return None, None

    # Not useful bits anymore
    if i > len(transmission) - 4:
        return None, None
    
    version = int(transmission[i:i+3], base=2)
    typeID = int(transmission[i+3:i+6], base=2)

    # Literal packet
    if typeID == 4:
        i += 6
        num_str = ""
        end = False
        while not end:
            if transmission[i] == "0":
                # Last packet
                end = True
            
            num_str += transmission[i+1:i+5]
            i += 5
        
        version = int(num_str, base=2)
        return version, i

    # Operator packet
    sub_packs = []
    next_start = None # A value to return

    lenID = transmission[i+6]
    if lenID == "0":
        # 15 bits representing how many bits are inside
        num_bits = int(transmission[i+7:i+22], base=2)
        end = i + 22 + num_bits
        index = i + 22
        prev_index = None
        while index != None:
            prev_index = index
            x, index = parse(transmission, index, j=end)
            sub_packs.append(x)
        sub_packs = sub_packs[:-1] # Remove last None
        next_start = prev_index
    else:
        # 11 bits representing how many packets are inside
        rem_sub_packs = int(transmission[i+7:i+18], base=2)
        index = i+ 18
        while rem_sub_packs > 0:
            x, index = parse(transmission, index)
            rem_sub_packs -= 1
            sub_packs.append(x)
        next_start = index
    
    # Process the operations
    return sub_packs, next_start

def solvePuzzle(puzzleInput) -> int:
    hex_str = readInput(puzzleInput)

    transmission = hexToBinary(hex_str)

    

    return sum(parse(transmission, 0)[0][0][0])

if __name__ == '__main__':
    start_time = pfc()
    print(solvePuzzle("input16.txt"))
    print(pfc() - start_time)



"""
FAILED TRY

def binaryToDecimal(bin_str) -> int:
    decimal = 0
    end = len(bin_str)-1
    for i in range(end, -1, -1):
        decimal += int(bin_str[i]) * 2**(end-i)
    return decimal

# Universal Packet Methods
def getPacketVersion(packet) -> int:
    return binaryToDecimal(packet[:3])

def getPacketType(packet) -> int:
    return "L" if binaryToDecimal(packet[3:6]) == 4 else "O0" if binaryToDecimal(packet[6]) == "0" else "O1"

# Operator Packet Methods
def getBitCount(O0) -> int:
    return binaryToDecimal(O0[7:22])

def getPacketCount(O1) -> int:
    return binaryToDecimal(O1[7:18])

def getNextPacketO0(packet) -> int:
    return 22

def getNextPacketO1(packet) -> int:
    return 18

# Literal methods
def getLiteralEnd(packet) -> int:
    index = 6
    while packet[index] != "0":
        index += 5
    return index + 5 - 1


def parsePackets(transmission, start, end, parsed=set()):

    packet = transmission[start : end]

    # End condition
    if end - start < 8:
        parsed.add(transmission)
        return "END"

    # 'L', 'O0' or 'O1'
    packet_type = getPacketType(packet)

    # Base case
    if packet_type == "L":
        parsed.add(packet)
        return packet

    # Recursive cases
    elif packet_type == "O0":
        outer_start = start

        # Get all the O0 packets' subpackets
        bits = 0
        bit_count = getBitCount(packet)
        while bits < bit_count:
            packet = transmission[getNextPacketO0(packet):end]
            print(packet)
            start += len(packet)
            bits += len(packet)
        
        # Add the O0 packet to the parsed packets
        outer_end = start
        parsed.add(transmission[outer_start:outer_end])

    elif packet_type == "O1":
        outer_start = start
        # Get all the 01 packets' subpackets
        packets = 0
        packet_count = getPacketCount(packet)
        while packets < packet_count:
            packet = transmission[getNextPacketO1(packet):end]
            parsePackets(packet, start, end, parsed)
            start += len(packet)
            packets += 1

        # Add the O1 packet to the parsed packets
        outer_end = start
        parsed.add(transmission[outer_start:outer_end])

    else:
        print("ERROR")

"""