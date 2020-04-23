#PROGRAM PENASIHAT ROMANSA
import random
import header
def saran1():
    bijak1    =["kurangi bermalas-malasan, jadilah pribadi yang rajin merawat diri!",
               "pahami kelebihan dan kekurangan diri, serta lebih percaya diri!",
               "Perbaiki skill human relation, time management, dan jadwal olharagamu!",]
    hasil1= random.choice(bijak1)
    print (hasil1)
def saran2():
    bijak2    =["berbuat baiklah kepada semua orang, bahkan ke musuh-musuh yang akan kau temui!",
               "bekerja dengan sungguh-sungguh dan melakukan hal yang menurutmu bermanfaat!",
               "memahami bahwa jalan yang kamu tempuh memang berat, tetapi bukan jadi alasan untuk berhenti!",]
    hasil2= random.choice(bijak2)
    print (hasil2)
def saran3():
    bijak3    =["memperluas jaringan hubungan dan jangan pernah takut untuk mencoba suatu hal baru!",
               "rajinlah menabung dan berlatih memanajemen keuangan!",
               "menjadi kaya karena akan menarik perhatian pribadi kaya yang lain!"]
    hasil3= random.choice(bijak3)
    print (hasil3)
def output():
    print ("Halo ",n,". Karena kamu ",u,"tahun, dan tipe",h," ideal yang kamu cari adalah",i,",")
    print ("maka yang harus kamu lakukan adalah")

header.identitas()
n = str (input("Nama : "))
u = int (input("Umur : " ))
jk= int (input("(1)Laki-laki (2)Perempuan   : "))
if(jk==1):
    g="Laki-Laki"
    h="perempuan"
elif(jk==2):
    g="Perempuan"
    h="laki-laki"
else:
    g="Alien"
    h="UFO"
print ()
print ("Menurutmu, kriteria utama ", h, " ideal dilihat dari...")
ik = int (input("[1]Parasnya  [2]Sifatnya  [3]Hartanya  : "))
print("Generating Answer...")
o= 0
while(o<=100):
    print ("loading",o,"%")
    p=o+25
    o=p
print ("---------------HASIL---------------")
if (ik == 1):
    i="parasnya"
    output()
    saran1()
    print ("Tetaplah yakin karena jodoh ada di tangan tuhan :)")
    print()
elif (ik==2):
    i="sifatnya"
    output()
    saran2()
    print ("Tetaplah yakin karena jodoh ada di tangan tuhan :)")
    print()
elif (ik==3):
    i="hartanya"
    output()
    saran3()
    print ("Tetaplah yakin karena jodoh ada di tangan tuhan :)")
    print()
else:
    print ("PROGRAM ERROR 404")
