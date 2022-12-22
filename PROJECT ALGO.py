import pandas as pd
import os
import time
import csv


def main_home():
    print (50*"=")
    print ("SELAMAT DATANG DI PROGRAM EASY COLECTOR".center(40))
    print (50*"=")

def menu():
    main_home()
    print("Login Sebagai:\n1. Superadmin\n2. User\n3. Exit")
    login_usr = (input("Login Sebagai: "))
    if login_usr == "1":
        os.system('cls')
        super_admin()
    elif login_usr == "2":
        os.system('cls')
        pertanyaan()
    elif login_usr == "3":
        os.system('cls')
        print(50*'=')
        print('\t\tTERIMAKASIH SEMUANYA')
        print(50*'=')
        time.sleep(3)
        os.system('cls')
        keluar()

    else:
        os.system('cls')
        salah()
    
    
def salah():
    salah1 = input("Menu Tidak Ada Klik [ENTER] untuk kembali")
    menu()

#Exit
def keluar():
    return



#superadmin
   
def super_admin():
        main_home()
        print("LOGIN SEBAGAI SUPER ADMIN\n")
        sa_usr = input("Username :")
        sa_pw = input("Password :")
        if sa_usr == "admin" and sa_pw == "admin":
            print(50*"\n")
            print("Login Berhasil")
            os.system('cls')
            sa_berhasil()
        else:
            os.system('cls')
            print(50*"=")
            print("Login Gagal")
            print(50*"=")
            print("1. Ulangi\n2. Kembali Tampilan Utama\n")
            log_back = input("")
            if log_back == "1":
                os.system('cls')
                super_admin()
            elif log_back == '2':
                os.system('cls')
                menu()
            else :
                os.system('cls')
                salah()


def sa_berhasil():
    print (50*"=")
    print('\t\tSUPER ADMIN')
    print(50*"=")
    print("1. Lihat Data Pengguna Dan admin\n2. Lihat Data\n3. Hapus Data User\n4. Kembali\n")
    sa_input = input("Tentukan Opsi: ")
    if sa_input == '1':
        os.system('cls')
        datapengguna()
        print ('Klik [ENTER] untuk kembali')
        input()
        os.system('cls')
        sa_berhasil()
    elif sa_input == '2':
        os.system('cls')
        SA_input()
    elif sa_input == '3':
        os.system('cls')
        hapus_data()
    elif sa_input == '4':
        os.system('cls')
        menu()
def hapus_data():
    while True:
        os.system('cls')
        print(50*"=")
        print("\t\tHAPUS DATA")
        print(50*"=")
        df=pd.read_csv("userdata.csv")
        print (df)
        noindex = int (input("\nMasukkan nomor data yang ingin dihapus : "))
        df.drop([noindex],axis=0,inplace=True)
        df.index = range (0,len(df))
        df.to_csv('userdata.csv', index=False)

        df=pd.read_csv('userdata.csv')
        print(df)
        break

    while True:
        pilihan_delete = input('Apakah anda ingin mengahapus data lagi? [y]/[t]')
        if pilihan_delete == 'y' or pilihan_delete == 'y':
            os.system('cls')
            hapus_data()
            os.system('cls')
            break
        if pilihan_delete == 'T' or pilihan_delete == 't':
            os.system('cls')
            sa_berhasil()
            os.system('cls')
def SA_input():
    os.system('cls')
    print("1. Lihat Data Petani\n2. Lihat Data Pengepul\n3. Lihat Data Pabrik\n4. Kembali")
    LD=input("Pilih Opsi: ")
    if LD == '1':
        os.system('cls')
        lihatdatapetani_SA()
    elif LD == '2':
        os.system('cls')
        lihatdatapengepul_SA()
    elif LD == '3':
        os.system('cls')
        lihatdatapabrik_SA()
    elif LD == '4':
        os.system('cls')
        sa_berhasil()
    else:
        SA_input()

def lihatdatapetani_SA():
    os.system('cls')
    dfpetanijagung=pd.read_csv("jagung.csv")
    dfpetanipadi=pd.read_csv('padi.csv')
    dfpetanitebu=pd.read_csv('tebu.csv')

    print(dfpetanijagung)
    print(dfpetanipadi)
    print(dfpetanitebu)
    kembali=input('Tekan [ENTER] untuk kembali')
    SA_input()

def lihatdatapengepul_SA():
    os.system('cls')
    dfpetanijagung=pd.read_csv("jagung pengepul.csv")
    dfpetanipadi=pd.read_csv('padi pengepul.csv')
    dfpetanitebu=pd.read_csv('tebu pengepul.csv')
    print(50*'=')
    print(dfpetanijagung)
    print(50*'=')
    print(dfpetanipadi)
    print(50*'=')
    print(dfpetanitebu)
    kembali=input('Tekan [ENTER] untuk kembali')
    SA_input()

def lihatdatapabrik_SA():
    os.system('cls')
    dfpabrikjagung=pd.read_csv("jagung pabrik.csv")
    dfpabrikpadi=pd.read_csv('padi pabrik.csv')
    dfpabriktebu=pd.read_csv('tebu pabrik.csv')
    print(dfpabrikjagung)
    print(dfpabrikpadi)
    print(dfpabriktebu)
    kembali=input('Tekan [ENTER] untuk kembali')
    SA_input()

def datapengguna():
    readdata = pd.read_csv('userdata.csv')
    print(readdata)



#User
#login password
def pertanyaan():
    global option
    print("Apakah Anda Sudah Memiliki Akun? [y] or [n]\n")
    option = input("Pilih Opsi: ")
    if (option =="y"):
        akses(option='y')
        os.system('cls')
    elif (option == "n"):
        akses(option='n')
        os.system('cls')
        pertanyaan()



def login(username,password):
    main_home()
    sukses = False
    file = open("userdata.csv","r")
    for i in file :
        a,b = i.split(",")
        b = b.strip()
        if(a==username and b==password):
            sukses = True
            break
    file.close()
    if (sukses):
        os.system('cls')
        print('LOGIN BERHASIL')
        time.sleep(2)
        os.system('cls')
        user()
    else:
        os.system('cls')
        print('LOGIN GAGAL')
        time.sleep(2)
        os.system('cls')
        print("1.Coba Lagi\n2.Kembali Ke Menu\n\n")
        tryagain = int(input("Masukan Opsi: "))
        if tryagain == 1:
            os.system('cls')
            akses(option='y')
        elif tryagain == 2:
            os.system('cls')
            menu()

def register(username,password):
    file = open("userdata.csv","a")
    file.write("\n" +username+","+password)

def akses(option):
    global username
    if(option=="y"):
        os.system('cls')
        print(50*'=')
        print("\t\t\tUSER")
        print(50*'=')
        username = input("masukkan username :")
        password = input("Masukkan password :")
        login(username,password)
    elif(option == "n"):
        os.system('cls')
        print(50*'=')
        print("\t\tREGISTRASI")
        print(50*'=')
        print("masukkan username dan Password anda yang baru\n")
        username = input("masukkan username :")
        password = input("masukkan password :")
        if register(username,password):
            os.system('cls')
            print("register anda berhasil, silahkan mulai")
            time.sleep(2)
            os.system('cls')
            user()
        else:
            os.system('cls')
            print("register berhasil, silahkan mulai")
            time.sleep(2)
            os.system('cls')
            menu()
            return(0)

            
def user():
        print(50*'=')
        print("\t\t\tUSER")
        print(50*'=')
        print("LOGIN SEBAGAI\n1.Petani\n2.Pengepul\n3.Pabrik\n4.Kembali")
        pil = input("Masukan Opsi: ")
        if pil == '1':
            petaniuser()
        elif pil =='2':
            pengepulmain()
        elif pil == '3':
            pabrikmain()
        elif pil == '4':
            os.system('cls')
            menu()

def petaniuser():
    os.system('cls')
    print(50*"=")
    print('\tANDA MASUK SEBAGAI PETANI')
    print(50*"=")
    print("1.Lihat data\n2.Tambahkan data\n3.Kembali")
    tentukanpilihan=input('Masukan Opsi: ')   
    if tentukanpilihan =='1':
        lihatdatapetani()
    elif tentukanpilihan == '2':
       tambahkandatapetani()
    elif tentukanpilihan == '3':
        os.system('cls')
        user()
    else:
        petaniuser()
def lihatdatapetani():
    os.system('cls')
    dfpetanijagung=pd.read_csv("jagung.csv")
    dfpetanipadi=pd.read_csv('padi.csv')
    dfpetanitebu=pd.read_csv('tebu.csv')
    print(dfpetanijagung)
    print(dfpetanipadi)
    print(dfpetanitebu)
    kembali=input('Tekan [ENTER] untuk kembali')
    petaniuser()

def tambahkandatapetani():
    os.system('cls')
    main_home()
    print('Pilih jenis panen\n1.Jagung\n2.Padi\n3.Tebu\n4.Kembali')
    jenispanen=int(input('Masukan Opsi: '))
    if jenispanen ==1:
        jagung()
    elif jenispanen == 2:
        padi()
    elif jenispanen == 3:
        tebu()
    elif jenispanen == 4:
        petaniuser()
    else:
        petaniuser()
def kembali_petani():    
    pilihlagi = input('apakah anda ingin menambahkan data lagi?[y][n]   ')
    if pilihlagi =='y':
        os.system('cls')
        tambahkandatapetani()
    elif pilihlagi == 'n':
        os.system('cls')
        petaniuser()
    else:
        os.system('cls')
        kembali_petani()
def jagung():
    os.system('cls')
    print("Jagung")
    print(50*"=")
    jagungsum=pd.read_csv('jagung.csv')
    berapakg=input('Masukkan total yang ingin ditambahkan :')
    selisih = jagungsum.iloc[0,0] + int(berapakg)
    jagungsum.loc[0]=selisih
    jagungsum.to_csv('jagung.csv', index=False)
    time.sleep(2)
    os.system('cls')
    print('Data berhasil ditambahkan')
    kembali_petani()


def padi():
    os.system('cls')
    print("Padi")
    print(50*"=")
    jagungsum=pd.read_csv('padi.csv')
    berapakg=input('Masukkan total yang ingin ditambahkan :')
    selisih = jagungsum.iloc[0,0] + int(berapakg)
    jagungsum.loc[0]=selisih
    jagungsum.to_csv('padi.csv', index=False)
    time.sleep(2)
    os.system('cls')
    print('Data berhasil ditambahkan')
    kembali_petani()
def tebu():
    os.system('cls')
    print(50*"=")
    print("\t\tPadi")
    print(50*"=")
    jagungsum=pd.read_csv('tebu.csv')
    berapakg=input('Masukkan total yang ingin ditambahkan :')
    selisih = jagungsum.iloc[0,0] + int(berapakg)
    jagungsum.loc[0]=selisih
    jagungsum.to_csv('tebu.csv', index=False)
    time.sleep(2)
    os.system('cls')
    print('Data berhasil ditambahkan')
    kembali_petani

def pengepulmain():
    os.system('cls')
    print('\t\t\tPENGEPUL')
    print(50*'=')
    print("1.Lihat data\n2.Tambahkan data\n3.Kembali")
    mainhome=input("Masukan Opsi:")
    if mainhome == '1':
        lihatdatapengepul()
        os.system('cls')
    elif mainhome == '2':
        tambahkandatapengepul()
        os.system('cls')
    elif mainhome=="3":
        os.system('cls')
        user()
    else:
        back=input('Pilihan tidak tersedia [ENTER] untuk kembali')
        pengepulmain()
def lihatdatapengepul():
    os.system('cls')
    dfpetanijagung=pd.read_csv("jagung pengepul.csv")
    dfpetanipadi=pd.read_csv('padi pengepul.csv')
    dfpetanitebu=pd.read_csv('tebu pengepul.csv')
    print(dfpetanijagung)
    print(dfpetanipadi)
    print(dfpetanitebu)
    kembali=input('Tekan [ENTER] untuk kembali')
    pengepulmain()

def tambahkandatapengepul():
    os.system('cls')
    dfpetanijagung=pd.read_csv("jagung.csv",)
    dfpetanipadi=pd.read_csv('padi.csv')
    dfpetanitebu=pd.read_csv('tebu.csv')
    print('List jagung')
    print(50*'=')
    print(dfpetanijagung)
    print(50*'=')
    print('List padi')
    print(dfpetanipadi)
    print(50*'=')
    print('List tebu')
    print(dfpetanitebu)
    pilihbarang=input('Pilih jenis panen yang ingin ditambahkan :')
    if pilihbarang == 'jagung':
        kurangjagung()
    elif pilihbarang == 'padi':
        kurangpadi()
    elif pilihbarang == 'tebu':
        kurangtebu()
    else:
        print('barang tidak tersedia')
        os.system('cls')
        tambahkandatapengepul()

def kembali_pengepul():    
    pilihlagi = input('apakah anda ingin menambahkan data lagi?[y][n]   ')
    if pilihlagi =='y':
        tambahkandatapengepul()
    elif pilihlagi == 'n':
        pengepulmain()
    else:
        os.system('cls')
        kembali_pengepul()

def kurangjagung():
    jagungsum=pd.read_csv('jagung.csv')
    jagungpengepul=pd.read_csv('jagung pengepul.csv')
    berapakg=input('Masukkan total yang ingin ditambahkan :')
    selisih = jagungsum.iloc[0,0] - int(berapakg)
    jagungsum.loc[0]=selisih
    if jagungsum.iloc[0,0] < 0:
        selisih = 0
        time.sleep(2)
        os.system('cls')
        print('Stok Tidak Tersedia')
        kembali_pengepul()
    else:
        jagungsum.to_csv('jagung.csv', index=False)
        jumlahdata = jagungpengepul.iloc[0,0] + int(berapakg)
        jagungpengepul.loc[0]=jumlahdata
        jagungpengepul.to_csv('jagung pengepul.csv', index=False)
        time.sleep(2)
        os.system('cls')
        print('Data berhasil ditambahkan')
        kembali_pengepul()

def kurangpadi():
    padisum=pd.read_csv('padi.csv')
    padipengepul=pd.read_csv('padi pengepul.csv')
    berapakg=input('Masukkan total yang ingin ditambahkan :')
    selisih = padisum.iloc[0,0] - int(berapakg)
    padisum.loc[0]=selisih
    if padisum.iloc[0,0] < 0:
        selisih = 0
        time.sleep(2)
        os.system('cls')
        print('Stok Tidak Tersedia')
        kembali_pengepul()
    else:
        padisum.to_csv('padi.csv', index=False)
        jumlahdata = padipengepul.iloc[0,0] + int(berapakg)
        padipengepul.loc[0]=jumlahdata
        padipengepul.to_csv('padi pengepul.csv', index=False)
        time.sleep(2)
        os.system('cls')
        print('Data berhasil ditambahkan')
        kembali_pengepul()

def kurangtebu():
    tebusum=pd.read_csv('tebu.csv')
    tebupengepul=pd.read_csv('tebu pengepul.csv')
    berapakg=input('Masukkan total yang ingin ditambahkan :')
    selisih = tebusum.iloc[0,0] - int(berapakg)
    tebusum.loc[0]=selisih
    if tebusum.iloc[0,0] < 0:
        selisih = 0
        time.sleep(2)
        os.system('cls')
        print('Stok Tidak Tersedia')
        kembali_pengepul()
    else:
        tebusum.to_csv('tebu.csv', index=False)
        jumlahdata = tebupengepul.iloc[0,0] + int(berapakg)
        tebupengepul.loc[0]=jumlahdata
        tebupengepul.to_csv('tebu pengepul.csv', index=False)
        time.sleep(2)
        os.system('cls')
        print('Data berhasil ditambahkan')
        kembali_pengepul()

def pabrikmain():
    main_home()
    os.system('cls')
    print('Pabrik')
    print(50*'=')
    print("1.Lihat data\n2.Tambahkan data\n3.Kembali")
    pilihanpabrik=int(input('Masukkan opsi: '))
    if pilihanpabrik == 1 :
        lihatdatapabrik()
    elif pilihanpabrik == 2:
        tambahkandatapabrik()
    elif pilihanpabrik==3:
        os.system('cls')
        user()
    else:
        kembali=input('Tekan [ENTER] untuk kembali')
        pabrikmain()

def lihatdatapabrik():
    os.system('cls')
    dfpabrikjagung=pd.read_csv("jagung pabrik.csv")
    dfpabrikpadi=pd.read_csv('padi pabrik.csv')
    dfpabriktebu=pd.read_csv('tebu pabrik.csv')
    print(dfpabrikjagung)
    print(dfpabrikpadi)
    print(dfpabriktebu)
    kembali=input('Tekan [ENTER] untuk kembali')
    pabrikmain()

def kembali_pabrik():    
    pilihlagi = input('apakah anda ingin menambahkan data lagi?[y][n]   ')
    if pilihlagi =='y':
        tambahkandatapabrik()
    elif pilihlagi == 'n':
        pabrikmain()
    else:
        os.system('cls')
        kembali_pabrik()

def tambahkandatapabrik():
    os.system('cls')
    dfpengepuljagung=pd.read_csv("jagung pengepul.csv")
    dfpengepulpadi=pd.read_csv('padi pengepul.csv')
    dfpengepultebu=pd.read_csv('tebu pengepul.csv')
    print(dfpengepuljagung)
    print(dfpengepulpadi)
    print(dfpengepultebu)
    pilihbarang=input('Pilih jenis panen yang ingin ditambahkan :')
    if pilihbarang == 'jagung':
        jagungpabrik()
    elif pilihbarang == 'padi':
        padipabrik()
    elif pilihbarang == 'tebu':
        tebupabrik()
    else:
        print('barang tidak tersedia')
        os.system('cls')
        pabrikmain()
    
def jagungpabrik():
    jagungsum=pd.read_csv('jagung pengepul.csv')
    jagungpabrik=pd.read_csv('jagung pabrik.csv')
    berapakg=input('Masukkan total yang ingin ditambahkan :')
    selisih = jagungsum.iloc[0,0] - int(berapakg)
    jagungsum.loc[0]=selisih
    if jagungsum.iloc[0,0] < 0:
        selisih = 0
        time.sleep(2)
        os.system('cls')
        print('Stok Tidak Tersedia')
        kembali_pabrik()
    else:
        jagungsum.to_csv('jagung pengepul.csv', index=False)
        jumlahdata = jagungpabrik.iloc[0,0] + int(berapakg)
        jagungpabrik.loc[0]=jumlahdata
        jagungpabrik.to_csv('jagung pabrik.csv', index=False)
        time.sleep(2)
        os.system('cls')
        kembali_pabrik()

def padipabrik():
    padisum=pd.read_csv('padi pengepul.csv')
    padipabrik=pd.read_csv('padi pabrik.csv')
    berapakg=input('Masukkan total yang ingin ditambahkan :')
    selisih = padisum.iloc[0,0] - int(berapakg)
    padisum.loc[0]=selisih
    if padisum.iloc[0,0] < 0:
        selisih = 0
        time.sleep(2)
        os.system('cls')
        print('Stok Tidak Tersedia')
        kembali_pabrik()
    else:
        padisum.to_csv('padi pengepul.csv', index=False)
        jumlahdata = padipabrik.iloc[0,0] + int(berapakg)
        padipabrik.loc[0]=jumlahdata
        padipabrik.to_csv('padi pabrik.csv', index=False)
        time.sleep(2)
        os.system('cls')
        kembali_pabrik()

def tebupabrik():
    tebusum=pd.read_csv('tebu pengepul.csv')
    tebupabrik=pd.read_csv('tebu pabrik.csv')
    berapakg=input('Masukkan total yang ingin ditambahkan :')
    selisih = tebusum.iloc[0,0] - int(berapakg)
    tebusum.loc[0]=selisih
    if tebusum.iloc[0,0] < 0:
        selisih = 0
        time.sleep(2)
        os.system('cls')
        print('Stok Tidak Tersedia')
        kembali_pabrik()
    else:
        tebusum.to_csv('tebu pengepul.csv', index=False)
        jumlahdata = tebupabrik.iloc[0,0] + int(berapakg)
        tebupabrik.loc[0]=jumlahdata
        tebupabrik.to_csv('tebu pabrik.csv', index=False)
        time.sleep(2)
        os.system('cls')
        kembali_pabrik()


os.system('cls')
menu()
