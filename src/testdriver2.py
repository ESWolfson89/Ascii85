import ascii85

def runTest():
    # load file.txt into string
    with open('file.txt', 'r') as fl:
        input_string = fl.read().replace('\n', '')
    # encode string
    encoded = ascii85.encodeAscii85(input_string)
    # decode string
    decoded = ascii85.decodeAscii85(encoded)
    print("Encoded Ascii85 Result from file.txt: \n" + encoded)
    print("Decoded back to original text: \n" + decoded)

def main():
    runTest()

if __name__ == '__main__':
    main()

