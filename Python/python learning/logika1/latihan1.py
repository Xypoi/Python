#latihan legika dan komparasi

inputangka = float (input("masukkan angka\nBernilai kurang dari 3\natau\nlebih dari 10\n   :"))
print('-----===-----')
#-3
iskurangdari = (inputangka < 3)

print ("Kurang dari 3   =",iskurangdari)

#+10
islebihdari = (inputangka > 10)

print ("Lebih dari 10   =",islebihdari)

print('-----===-----')
#-3 +10
iscorrect = iskurangdari or islebihdari
print("angka yang anda masukkan =",iscorrect)


print('-----===-----')
print('')
print('-----===-----')


# 3-10

inputangka2 = float (input("masukkan angka\nBernilai lebih dari 3\natau\nkurang dari 10\n  :"))
print('-----===-----')
#+3
lebih3  = inputangka2 > 3
print("lebih dari 3     =",lebih3)

#-10
kurang10 = inputangka2 <10
print("kurang dari 10   =",kurang10)
print('-----===-----')
#3-10
correct2 = lebih3 and kurang10

print("angka yang anda masukkan =",correct2)


