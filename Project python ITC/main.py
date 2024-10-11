print("[==================]")
print("[  KALKULATOR BMI  ]")
print("[==================]")

nama = input("\n Isi Nama Anda di sini : ")
print("\n[~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~]")
print(f"  Halooo {nama}, selamat datang di Kalkulator BMI kami      ")
print("[~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~]")

print("\n{~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~}")
print("{ Tolong isi Usia, tinggi badan dan berat badan anda di bawah ini yaaa }")
print("{        Usahakan isi seperti yang sudah kami beri contoh!!            }")   
print("{~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~}") 

usia = int(input("\nMasukan Usia Anda (Contoh: 16) : "))
tinggi = float(input("Masukan tinggi badan dengan cm (Contoh: 165) : "))
berat_badan = float(input("Masukan berat badan dengan Kg (Contoh: 60) : "))

print("\n{~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~}")
print("{Terimah kasih telah mengisi dengan benar, berikut ini hasil dari kalkulator BMI untuk anda}")
print("{~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~}\n")

tinggi_meter = tinggi / 100
bmi = berat_badan / (tinggi_meter ** 2)

if usia < 14:
  kategori_umur = "anak-anak";
elif usia < 60:
  kategori_umur = "dewasa";
else:
  kategori_umur = "lansia";

if kategori_umur == "anak-anak":
  if bmi < 18.5:
    kategori_bmi = "kekurangan berat badan";
  elif 18.5 <= bmi <24.9:
    kategori_bmi = "normal";
  else:
    kategori_bmi = "obesitas";
  print("BMI anak perlu di konsultasikan dengan dokter, atau menggunakan kalkulator BMI khusus anak-anak")

elif kategori_umur == "dewasa":
  if bmi < 18.5:
    kategori_bmi = "kekurangan berat badan";
  elif 18.5 <= bmi <24.9:
    kategori_bmi = "normal";
  else:
    kategori_bmi = "obesitas";
elif kategori_umur == "lansia":
  if bmi < 22:
    kategori_bmi = "kekurangan berat badan";
  elif 22 <= bmi < 27:
    kategori_bmi = "normal";
  else:
    kategori_bmi = "obesitas";

print("[===============================================================================================================]")
print(f"  Kategori usia anda adalah {kategori_umur}")
print(f"  BMI anda adalah {bmi:.1f}, kategori BMI anda adalah {kategori_bmi}.")

if kategori_bmi == "kekurangan berat badan":
  print("  Cobalah meningkatkan kalori dan konsultasikan dengan dokter gizi                                              ")
elif kategori_bmi == "obesitas":
  print("  pertimbangkan untuk meningkatkan aktivitas fisik dan menjaga pola makan                                       ")
else:
  print(" Anda sudah berada di jalur yang tepat! Pastikan untuk terus menjaga pola makan seimbang dan rutin berolahraga.")
print("[===============================================================================================================]\n")

if kategori_bmi == "normal":
  print("Terima kasih telah menggunakan kalkulator kami")
else:
  print("Apakah anda ingin mencapai target normal BMI anda?")
  input_target_bmi = input("Jika anda berkenan ketik 1, dan jika tidak berkenan ketik 2 disini : ")

if input_target_bmi == "1":
  if kategori_bmi == "kekurangan berat badan":
    print("\n{~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~}")
    print("{BMI Normal untuk anak - anak dan dewasa adalah 18.5 - 24.9, dan 22 - 27 untuk lansia}")
    print("{~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~}\n")
    target_bmi = float(input("Masukan target BMI anda"))
    berat_target = target_bmi * (tinggi_meter ** 2)
    print(f"untuk mencapai BMI {target_bmi}, berat badan anda harus sekitar {berat_target:.1f} Kg.")
    print("Terima kasih!!")
  elif kategori_bmi == "obesitas":
    print("\n{~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~}")
    print("{BMI Normal untuk anak - anak dan dewasa adalah 18.5 - 24.9, dan 22 - 27 untuk lansia}")
    print("{~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~}\n")
    target_bmi = float(input("Masukan target BMI anda : "))
    berat_target = target_bmi * (tinggi_meter ** 2)
    print(f"untuk mencapai BMI {target_bmi}, berat badan anda harus sekitar {berat_target:.1f} Kg.")
    print("Terima kasih!!")
  else:
    print("\n")
elif input_target_bmi == "2":
  print("Baik, terima kasih!!")
else:
  print("masukan perintah dengan benar.")

print("\n{~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~}")
print("{Karya Saya : Moch. Rafi Andi Prayitno}")
print("{~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~}")