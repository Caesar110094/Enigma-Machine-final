import math
print ("Typ in wat je gecodeerd wilt hebben")
Bericht = input()
Bericht = Bericht.upper()


Gtal = []

for sign in Bericht:
    Getal = ord(sign) - 65
    Gtal.append(Getal)


RotatieI = [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
RotatieII = [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4]
RotatieIII = [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]
Reflektor = [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19]
Plugboard = [0, 24, 2, 3, 4, 5, 22, 7, 8, 9, 10, 12, 11, 16, 14, 15, 13, 17, 18, 19, 20, 21, 6, 23, 1, 25]
RotatieIstart = 7
RotatieIIstart = 24
RotatieIIIstart = 0

def shiftstart(seq, n):
    return seq[n:] + seq[:n]

def shift(seq, n, rn, numb):
    if rn == 1:
        n = -n % len(seq)

    elif rn == 2:
        n = - math.trunc(n/25) % len(seq)
        
    elif rn == 3:
        n = - math.trunc(n/675) % len(seq)
       
    return seq[n:] + seq[:n]
    
def rotorrev(seq):
    rotorrev = ['empty']*26
    for i in range(26):
        rotorrev[seq[i]] = i
    
    return rotorrev

def rotor(seq, rev, numb, rn):
    number = []
    Rotatiereverse = ['empty'] * 26
    if rev == 0:
        for i in range(len(numb)):
            rotation = shift(seq, i, rn, numb)
            number.append(rotation[numb[i]])
            
    elif rev == 1:
        for i in range(len(numb)):
            rotation = shift(seq, i, rn, numb)
            seqrev = rotorrev(rotation)
            number.append(seqrev[numb[i]])
        
    return number
   
def RefPlug(list, numbIII):
    ref = []
    for i in range(len(numbIII)):
        ref.append(list[numbIII[i]])
        
    return ref

RotorIM = shiftstart(RotatieI, RotatieIstart)
RotorIIM = shiftstart(RotatieII, RotatieIIstart)
RotorIIIM = shiftstart(RotatieIII, RotatieIIIstart)

Seq = RefPlug(Plugboard, Gtal)
SeqI = rotor(RotorIM, 0, Seq, 1)
SeqII = rotor(RotorIIM, 0, SeqI, 2)
SeqIII = rotor(RotorIIIM, 0, SeqII, 3) 
SeqIV = RefPlug(Reflektor, SeqIII)
SeqVI = rotor(RotorIIIM, 1, SeqIV, 3)
SeqVII = rotor(RotorIIM, 1, SeqVI, 2)
SeqVIII = rotor(RotorIM, 1, SeqVII, 1)
SeqIX = RefPlug(Plugboard, SeqVIII)

new_mes = []
for i in range(len(SeqIX)):
    word = chr(SeqIX[i]+65)
    new_mes.append(word)
print ("Je gecodeerde bericht van is")
print(''.join(new_mes))