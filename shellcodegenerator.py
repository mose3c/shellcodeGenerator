import sys, os

if len(sys.argv) < 3:
    print ('usage: ' + sys.argv[0] + ' intfile outfile language\n')
    sys.exit(0)

shellcode = ''
Tshellcode = ''
bytes = 0

for b in open(sys.argv[1], 'r').read():

    if(bytes % 12 ==0):
        Tshellcode+= '\n'
    Tshellcode += '0x' + b.encode("utf-8").hex()
    Tshellcode += ','
    

    bytes += 1
  
shellcode = ''

if("c#" in sys.argv[3]):
    print("c#")
    shellcode += 'byte[] rawData = {'  
    shellcode +=Tshellcode
    shellcode += '}'
elif("cpp" in sys.argv[3]):
    print("c++")
    shellcode += 'int powerDllLen ='+str(bytes)+';\n'
    shellcode += 'unsigned char rawData['+str(bytes)+']={'
    shellcode +=Tshellcode
    shellcode += '}'

fp=open(sys.argv[2], "w")
fp.write(shellcode)
fp.close()
