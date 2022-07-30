traktor = [35000] 
corn_sheller = [30000]
reaper = [25000]
tresher = [25000]
corn_transplanter = [30000] 
pompa_air = [50000]
voucher = ['panen raya',0.1,300000]
x=1
bayar=0
total=0
harga=0
diskon=0                                         ################# 
sisa=0                                           #SEKEDAR INFO PAK
lama=0                                           #PIN, NO TELEPON, DAN OTP SEMUANYA 123456
jumlah=0                                         #################
day=[]
day2=[]
hour=[]
hour2=[]
minute=[]
minute2=[]
linkaja=['123456','123456','123456',2000000]
e_cash=['123456','123456','123456',2000000]
#WAKTU 1 : MENCATAT SAAT PERTAMA KALI MULAI PROGRAM
import datetime
hari=datetime.datetime.today().weekday()
from datetime import datetime
saat_ini = datetime.now()
jam = saat_ini.strftime("%H")
menit= saat_ini.strftime("%M")
day.append(int(hari))
hour.append(int(jam))
minute.append(int(menit))
jumlah_jam=0
jumlah_menit=0
selisih_waktu=0


def menu(traktor,corn_sheller,reaper,tresher,corn_transplanter,pompa_air,voucher,x,bayar,total,harga,diskon,sisa,lama,jumlah,day,day2,hour,hour2,minute,minute2,linkaja,e_cash,hari,saat_ini,jam,menit,jumlah_jam,jumlah_menit,selisih_waktu):
    print("_____________")
    print("")
    print(hour[0],":",minute[0],"WITA") 
    print("""
_______________________________________________

        RENTAL ALAT & MESIN PERTANIAN
              ( ALSINTAN )
_______________________________________________
    
PROMO !!!
Diskon 10% untuk tranksaksi minimal Rp.300.000,00 hanya hari ini !!!
Kode voucher\t: panen raya !!!

DAFTAR ALSINTAN :
0.Syarat & Ketentuan
1.Traktor\t\t=\tRp.35.000,00 per hari
2.Corn Sheller\t\t=\tRp.30.000,00 per hari
3.reaper\t\t=\tRp.25.000,00 per hari
4.Tresher\t\t=\tRp.25.000,00 per hari
5.Corn Transplanter\t=\tRp.30.000,00 per hari
6.Pompa Air\t\t=\tRp.50.000,00 per hari
""")
    while x==1:
        barang=str(input("Masukkan Pilihan Barang :"))
        if barang=='0':
            print("""
Syarat % Ketentuan
1.Pengembalian barang wajib dilakukan sehari setelah masa peminjaman berakhir;
2.Akan dikenakan denda bila pengembalian barang tidak tepat waktu;
3.Kerusakan barang menjadi tanggung jawab bersama;
4.Tidak ada pengembalian uang pembayaran apabila terjadi pembatalan tranksaksi.
""")
            lagi=input("Kembali ? ?\n1.ya\n2.tidak\n==>")
            if lagi=='1' or lagi=='ya':
                x+=0
                print("")
            else:
                break
    
        elif barang=='1':
            lama=int(input("Berapa Hari\t: "))
            jumlah=jumlah+traktor[0]*lama
            lagi=input("Lagi ? ?\n1.ya\n2.Bayar\n==>")
            if lagi=='1' or lagi=='ya':
                x+=0
            elif lagi=='2' or lagi=='tidak':
                x+=1
                struk(total,jumlah,hari,saat_ini,jam,menit,voucher,day,day2,diskon,bayar,linkaja,e_cash,sisa,hour,x,hour2,minute2,minute,jumlah_jam,jumlah_menit,selisih_waktu)
            else:
                print("Input tidak tersedia")
    
        elif barang=='2':
            lama=int(input("Berapa Hari\t: "))
            jumlah=jumlah+corn_sheller[0]*lama
            lagi=input("Belanja Lagi ? ?\n1.ya\n2.Bayar\n==>")
            if lagi=='1' or lagi=='ya':
                x+=0
            elif lagi=='2' or lagi=='tidak':
                x+=1
                struk(total,jumlah,hari,saat_ini,jam,menit,voucher,day,day2,diskon,bayar,linkaja,e_cash,sisa,hour,x,hour2,minute2,minute,jumlah_jam,jumlah_menit,selisih_waktu)
                break
            else:
                print("input tidak tersedia")

        elif barang=='3':
            lama=int(input("Berapa Hari\t: "))
            jumlah=jumlah+reaper[0]*lama
            lagi=input("Belanja Lagi ? ?\n1.ya\n2.Bayar\n==>")
            if lagi=='1' or lagi=='ya':
                x+=0
            elif lagi=='2' or lagi=='tidak':
                x+=1
                struk(total,jumlah,hari,saat_ini,jam,menit,voucher,day,day2,diskon,bayar,linkaja,e_cash,sisa,hour,x,hour2,minute2,minute,jumlah_jam,jumlah_menit,selisih_waktu)
                break
            else:
                print("input tidak tersedia")

        elif barang=='4':
            lama=int(input("Berapa Hari\t: "))
            jumlah=jumlah+tresher[0]*lama
            lagi=input("Belanja Lagi ? ?\n1.ya\n2.Bayar\n==>")
            if lagi=='1' or lagi=='ya':
                x+=0
            elif lagi=='2' or lagi=='tidak':
                x+=1
                struk(total,jumlah,hari,saat_ini,jam,menit,voucher,day,day2,diskon,bayar,linkaja,e_cash,sisa,hour,x,hour2,minute2,minute,jumlah_jam,jumlah_menit,selisih_waktu)
                break
            else:
                print("input tidak tersedia")
                
        elif barang=='5':
            lama=int(input("Berapa Hari\t: "))
            jumlah=jumlah+corn_transplanter[0]*lama
            lagi=input("Belanja Lagi ? ?\n1.ya\n2.Bayar\n==>")
            if lagi=='1' or lagi=='ya':
                x+=0
            elif lagi=='2' or lagi=='tidak':
                x+=1
                struk(total,jumlah,hari,saat_ini,jam,menit,voucher,day,day2,diskon,bayar,linkaja,e_cash,sisa,hour,x,hour2,minute2,minute,jumlah_jam,jumlah_menit,selisih_waktu)
                break
            else:
                print("input tidak tersedia")
        elif barang=='6':
            lama=int(input("Berapa Hari\t: "))
            jumlah=jumlah+pompa_air[0]*lama
            lagi=input("Belanja Lagi ? ?\n1.ya\n2.Bayar\n==>")
            if lagi=='1' or lagi=='ya':
                x+=0
            elif lagi=='2' or lagi=='tidak':
                x+=1
                struk(total,jumlah,hari,saat_ini,jam,menit,voucher,day,day2,diskon,bayar,linkaja,e_cash,sisa,hour,x,hour2,minute2,minute,jumlah_jam,jumlah_menit,selisih_waktu)
                break
            else:
                print("input tidak tersedia")
        else:
            print("")
            print("Input tidak Tersedia !!!\n")
            x+=0

def struk(total,jumlah,hari,saat_ini,jam,menit,voucher,day,day2,diskon,bayar,linkaja,e_cash,sisa,hour,x,hour2,minute2,minute,jumlah_jam,jumlah_menit,selisih_waktu):#pembayaran

    total=total+jumlah
    #WAKTU 2 :MENCATAT WAKTU SAAT PEMBAYARAN
    import datetime
    hari=datetime.datetime.today().weekday()
    from datetime import datetime
    saat_ini = datetime.now()
    jam = saat_ini.strftime("%H")#waktu 2 mencatat waktu saat pertama masuk
    menit= saat_ini.strftime("%M")
    day2.append(int(hari))#memasukkan nilai hari kedalam list day2
    hour2.append(int(jam))#memasukkan nilai jam ke dalam list hour2
    minute2.append(int(menit))#
    jumlah_jam=(hour2[0]-hour[0])*60
    jumlah_menit=minute2[0]-minute[0]
    selisih_waktu=jumlah_jam+jumlah_menit
    print("______________________________")
    print("")
    print(hour2[0],":",minute2[0],"WITA")
    print("")
    print("PEMBAYARAN !!!")
    punya=input("""Punya Voucher ?
1.ya
2.tidak
==> """)
    if punya=='1':
        kode=input("Masukkan kode voucher : ")
        if kode==voucher[0] and day2[0]==day[0] and total>voucher[2]:
            diskon=total*voucher[1]
    else:
        diskon=0
    harga=total-diskon
    print("")
    e_money=input("""Pilih Metode Pembayaran\t:
1.Linkaja
2.e-cash
==> """)
    if e_money=='1' and selisih_waktu<60:
        print("")
        pin=input("Masukkan pin\t: ")
        tlp=input("Masukkan nomor telepon\t: ")
        if pin==linkaja[0] and tlp==linkaja[1]:
            print("kode OTP akan dikirimkan ke telepon anda dalam 5 detik !!!")
            import time
            for i in range(5,0,-1):
                time.sleep(1)
                print(i)
            otp=input("Masukkan kode OTP :")
            if otp==linkaja[2] and harga<=linkaja[3]:
                print("")
                print("Pembayaran Berhasil !!!")
                print("diskon\t\t\t:\tRp.",diskon)
                print("Total sebelum diskon\t:\tRp.",total)
                print("Total setelah diskon\t:\tRp.",harga)
                print("Saldo Anda\t\t:\tRp.",linkaja[3])
                sisa=linkaja[3]-harga
                linkaja[3]=sisa
                print("Sisa Saldo\t\t:\tRp.",sisa)
                print("")
                print("Pengembalian barang sesuai dengan syarat dan ketentuan !!!")
                print("")
                print("========================== TERIMAKASIH ==========================")
            elif otp==linkaja[2] and harga>linkaja[3]:
                print("")
                print("Saldo tidak mencukupi !!!")
                print("")
            else:
                print("Kode OTP salah")
        else:
            print("pin atau nomor telepon tidak terdaftar !!!")
    elif e_money=='2' and selisih_waktu<60 :
        print("")
        pin=input("Masukkan Pin\t: ")
        tlp=input("Masukkan nomor telepon :")
        if pin==e_cash[0] and tlp==e_cash[1]:
            print("kode OTP akan dikirimkan dalam 5 detik ke telepon anda !!!")
            import time
            for i in range(5,0,-1):
                time.sleep(1)
                print(i)
            otp=input("Masukkan kode OTP :")
            if otp==e_cash[2] and harga<=e_cash[3]:
                print("")
                print("Pembayaran Berhasil !!!")
                print("Diskon\t\t\t:\tRp.",diskon)
                print("Total sebelum diskon\t:\tRp.",total)
                print("Total setelah diskon\t:\tRp.",harga)
                print("Saldo Anda\t\t:\tRp.",e_cash[3])
                sisa=e_cash[3]-harga
                e_cash[3]=sisa
                print("sisa saldo\t\t:\tRp.",sisa)
                print("")
                print("Pengembalian barang sesuai dengan syarat dan ketentuan !!!")
                print("")
                print("\t========================== TERIMAKASIH ==========================")
            elif otp==e_cash[2] and harga>e_cash[3]:
                print("")
                print("Saldo tidak mencukupi !!!")
                print("")
            else:
                print("Kode OTP salah")
        else:
            print("pin atau nomor telepon tidak terdaftar !!!")
            
    elif e_money=='1' or e_money=='2' and selisih_waktu>60:
        print("""
Tranksaksi Gagal !!!
Keterlambatan Pembayaran Selama 1 jam
""")
                        
    else:
        print("Inputan Tidak Tersedia !!!")
        struk(total,jumlah,hari,saat_ini,jam,menit,voucher,day,day2,diskon,bayar,linkaja,e_cash,sisa,hour,x,hour2,minute2,minute,jumlah_jam,jumlah_menit,selisih_waktu)
    return struk

menu(traktor,corn_sheller,reaper,tresher,corn_transplanter,pompa_air,voucher,x,bayar,total,harga,diskon,sisa,lama,jumlah,day,day2,hour,hour2,minute,minute2,linkaja,e_cash,hari,saat_ini,jam,menit,jumlah_jam,jumlah_menit,selisih_waktu)
z=0
while z==0:
    mengulang=int(input("Mengulang lagi ?\n1.Ya\n2.Tidak\n==> "))
    if mengulang==1:
        menu(traktor,corn_sheller,reaper,tresher,corn_transplanter,pompa_air,voucher,x,bayar,total,harga,diskon,sisa,lama,jumlah,day,day2,hour,hour2,minute,minute2,linkaja,e_cash,hari,saat_ini,jam,menit,jumlah_jam,jumlah_menit,selisih_waktu)
        z=0
    elif mengulang==2:
        z=1
        break
    else:
        print("\t\tInput tidak tersedia")
        z=0
        
