import math

# pad input string with character c and modulo operand mod_op
def padWithChars(sinp,c,mod_op):
    ret_val = sinp
    if len(sinp) % mod_op == 0:
        return ret_val
    for i in range(0,mod_op-len(sinp)%mod_op):
        ret_val += c
    return ret_val

# split input string into a list where each element is a group of n characters
def getInputList(sinp,n):
    ret_val = []
    while sinp != "":
        ret_val.append(sinp[:n])
        sinp = sinp[n:]
    return ret_val

# eliminate leading 0b from string and pad with zeroes (in front) until there are 8 bits
def getFormattedBitString(binp,num_bits):
    ret_val = binp[2:]
    if ret_val == 0 and num_bits == 8:
        return "00000000"
    if ret_val == 0 and num_bits == 32:
        return "00000000000000000000000000000000"
    for i in range(0,num_bits-len(ret_val)):
        ret_val = '0' + ret_val
    return ret_val

# convert each character of string into binary string
def findBitPattern(sinp):
    ret_val = ""
    for i in range(0,len(sinp)):
        ret_val += getFormattedBitString(bin(ord(sinp[i])),8)
    return ret_val

# convert n*8 bit binary string to n ascii chars
def findAsciiPattern(sinp,n):
    ret_val = ""
    for i in range(0,n):
        ret_val += chr(int(sinp[:8],2))
        sinp = sinp[8:]
    return ret_val

# convert input number into base 85 number (as a list)	
def getBase85ValueList(dinp):
    ret_val = []
    div_dinp = dinp
    while div_dinp != 0:
        mod_dinp = div_dinp % 85
        div_dinp = int(math.floor(div_dinp / 85))
        ret_val.insert(0,str(mod_dinp))
    return ret_val

# convert base 85 to base 10
def base85ToBase10(linp):
    ret_val = 0
    digits = len(linp)
    for i in range(0,digits):
        ret_val += linp[i] * (85 ** (digits - i - 1))
    return ret_val

# add 33 to each number in list above and convert to ascii	
def add33ConvertAscii(sinp):
    ret_val = ""
    for elmt in sinp:
        ascii_int_partition = int(elmt) + 33
        ret_val += chr(ascii_int_partition)
    return ret_val

# eliminate trailing characters matching the number of trailing zeroes the input was padded with
def unpadResult(sinp,pad):
    # this was fiddled with to get it working. I need to revisit why this is the correct conditional.
    if pad % 4 == 0 or pad % 5 == 0:
       return sinp
    return sinp[:-pad]

# convert ascii to int and subtract 33 for each character; store each result in a list
def sub33NumList(sinp):
    ret_val = []
    for elmt in sinp:
        ret_val.append(int(findBitPattern(elmt),2)-33)
    return ret_val

# compute Base85 for all sets of 4 characters in input
def encodeAllSubSections(linp):
    ret_val = ""
    for elmt in linp:
        bit_pattern = findBitPattern(elmt)
        int_64bit = int(bit_pattern,2)
        list_85base = getBase85ValueList(int_64bit)
        ret_val += add33ConvertAscii(list_85base)
    return ret_val

# decode for all sets of 5 characters in input in encoded result
def decodeAllSubSections(linp):
    ret_val = ""
    for elmt in linp:
        sub_33_list = sub33NumList(elmt)
        int_64bit = base85ToBase10(sub_33_list)
        bit_pattern = getFormattedBitString(bin(int_64bit),32)
        ret_val += findAsciiPattern(bit_pattern,4)
    return ret_val

# encode sinp
def encodeAscii85(sinp):
    padded_input = padWithChars(sinp,'\0',4)
    padded_offset = 4 - (len(sinp)%4)
    input_list = getInputList(padded_input,4)
    final_result = unpadResult(encodeAllSubSections(input_list),padded_offset)
    return final_result

# decode sinp
def decodeAscii85(sinp):
    padded_input = padWithChars(sinp,'u',5)
    padded_offset = 5 - (len(sinp)%5)
    input_list = getInputList(padded_input,5)
    final_result = unpadResult(decodeAllSubSections(input_list),padded_offset)
    return final_result

