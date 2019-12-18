import binascii

modulus = '''00:df:3b:b9:bc:d0:e1:9f:93:a4:fd:42:aa:6b:ff:10:91:ba:a0:93:7b:1a:f3:f0:70:63:9b:c3:7f:b7:28:c7:55:50:97:70:91:5a:83:46:66:35:e0:fd:2d:2d:17:57:c3:68:62:f1:5e:57:5e:4b:84:8e:ef:9d:8c:7b:93:ef:35:d4:77:48:88:a8:8a:e6:27:78:74:7c:04:0b:e4:01:c4:f7:ae:d3:5f:01:30:5f:c9:3a:8b:17:f8:6c:cf:f3:d3:34:e7:15:18:89:94:a1:e0:96:38:7d:24:23:ff:f3:f4:6b:d7:11:a0:04:da:95:3b:ff:24:0b:3d:68:7c:9a:c9'''
n = int(modulus.translate(None,'\n :'),16)
hn  = hex(n)

e = 0x10001
m = 0x02
c = pow(m,e,n)
hc = hex(c)

print("n = ", n)
print("hex n = ", hn)
print("hex c=",hc)

m3 = 0x03
c3 = pow(m3,e,n)
hc3 = hex(c3)
print("hex c3=",hc3)

c6 = (c3*c)%n

b =  binascii.unhexlify('%0256x' % c6) # converts to
f = open("multiplicative.out","w")
f.write(b)
f.close()

m4 = 0x10
m5= 0x11
print(bin(m4),bin(m5))