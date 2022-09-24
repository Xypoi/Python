#Operasi Logika/Boolean

# not, or, and, xor



#NOT




print ('=== NOT ===')
a=True
c= not a
print ('data a  =',a)
print ('------------  NOT')
print ('data c  =',c)



#OR (Jika salah 1 nilai True = True)

print ('=== OR ===')
a=False
b=False
c=b or a
print (a,'or',b,'=',c)

a=True
b=False
c=b or a
print (a,'or',b,'=',c)

a=False 
b=True
c=b or a
print (a,' or',b,'=',c)

a=True
b=True
c=b or a
print (a,'or',b,'=',c)



#AND (Jika 2 buah nilai True = True)

print ('=== AND ===')
a=False
b=False
c=b and a
print (a,'AND',b,'=',c)

a=True
b=False
c=b and a
print (a,'AND',b,'=',c)

a=False 
b=True
c=b and a
print (a,'AND',b,'=',c)

a=True
b=True
c=b and a
print (a,'AND',b,'=',c)



#XOR 

print ('=== XOR ===')
a=False
b=False
c=b ^ a
print (a,'XOR',b,'=',c)

a=True
b=False
c=b ^ a
print (a,'XOR',b,'=',c)

a=False 
b=True
c=b ^ a
print (a,'XOR',b,'=',c)

a=True
b=True
c=b ^ a
print (a,'XOR',b,'=',c)

