# See the symbol table at the bottom of this page.
from math import prod
class Niswanob1:
 def __init__(fuscat1,Chri1):
  Chri2=Chri1.read()
  Niswanob2=bitboostdotcom1.fuscat2(Chri2)
  fuscat1.Chri4=0
  fuscat1.fuscat3=''
  fuscat1.fuscat3=''.join(map('{:08b}'.bitboostdotcom2,Niswanob2))

 def fuscat5(ordemo1,bitboostdotcom3):
  Chri3=int(ordemo1.fuscat3[ordemo1.Chri4:(ordemo1.Chri4 + bitboostdotcom3)],2)
  ordemo1.Chri4+=bitboostdotcom3
  return Chri3

 def Niswanob4(ordemo3):
  bitboostdotcom4=ordemo3.fuscat5(3)
  bitboostdotcom5=ordemo3.fuscat5(3)
  bitboostdotcom7=ordemo3.ordemo2(bitboostdotcom5)
  return (bitboostdotcom4,bitboostdotcom5,bitboostdotcom7)

 def Chri6(bitboostdotcom6):
  Niswanob3=0
  Chri5=16
  while (Chri5 & 16):
   Chri5=bitboostdotcom6.fuscat5(5)
   Niswanob3<<=4
   Niswanob3+=(Chri5 & 15)

  return Niswanob3

 def fuscat6(bitboostdotcom8,fuscat4):
  return [bitboostdotcom8.Niswanob4() for 
bitboostdotcom9 in       range(fuscat4)]

 def bitboostdotcomA(Niswanob5,Niswanob7):
  fuscat8=(Niswanob5.Chri4 + Niswanob7)
  fuscat7=[]
  while (Niswanob5.Chri4<fuscat8):
   fuscat7.append(Niswanob5.Niswanob4())

  return fuscat7

 def Niswanob8(Niswanob6):
  bitboostdotcomB=Niswanob6.fuscat5(1)
  if (bitboostdotcomB==1):
   return Niswanob6.fuscat6(Niswanob6.fuscat5(11))

  return Niswanob6.bitboostdotcomA(Niswanob6.fuscat5(15))

 def ordemo2(bitboostdotcomC,ordemo4):
  if (ordemo4==4):
   return bitboostdotcomC.Chri6()

  return bitboostdotcomC.Niswanob8()


def NiswanobA(ordemo6):
 (bitboostdotcomD,bitboostdotcomF,Chri7)=ordemo6
 if (bitboostdotcomF==4):
  return bitboostdotcomD

 return (bitboostdotcomD + sum(map(NiswanobA,Chri7)))

Chri8=open('16_input','r')
fuscat9=Niswanob1(Chri8)
bitboostdotcomE=fuscat9.Niswanob4()
fuscatB=NiswanobA(bitboostdotcomE)
print ('Part 1:',fuscatB)
def ordemo8(ordemo5):
 (ordemo7,Chri9,fuscatA)=ordemo5
 if (Chri9==4):
  return fuscatA

 Niswanob9=map(ordemo8,fuscatA)
 if (Chri9==0):
  return sum(Niswanob9)

 if (Chri9==1):
  return bitboostdotcom10(Niswanob9)

 if (Chri9==2):
  return min(Niswanob9)

 if (Chri9==3):
  return max(Niswanob9)

 (fuscatC,NiswanobB)=Niswanob9
 if (Chri9==5):
  return int((fuscatC>NiswanobB))

 if (Chri9==6):
  return int((fuscatC<NiswanobB))

 return int((fuscatC==NiswanobB))

ordemo9=ordemo8(bitboostdotcomE)
print ('Part 2:',ordemo9)
