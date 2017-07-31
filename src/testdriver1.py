import ascii85
import random

def runTests():
    num_passed = 0
    for i in range(0,100):
        input_string = ""
        num_chars = random.randint(1,1000)
        for j in range(0,num_chars):
            input_string += chr(random.randint(33,117))
        encoded = ascii85.encodeAscii85(input_string)
        decoded = ascii85.decodeAscii85(encoded)
        if (decoded == input_string):
            num_passed = num_passed + 1
    print(str(num_passed) + "/100 passed!")

def main():
    runTests()

if __name__ == '__main__':
    main()

