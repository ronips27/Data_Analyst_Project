from prettytable import PrettyTable

### sistem login ####

namaKasirTerdaftar = 'ronips'
passwordKasirTerdaftar = 'ronips123'


while True:

    namaKasir = input("Masukkan Nama Kasir : ")

    if namaKasir == namaKasirTerdaftar :
        print(f"Silahkan lanjut verifikasi password ")
        break
    else :
        print("Maaf Username anda salah, Silahkan ulangi lagi 🙏")
        True

while True:

    passwordKasir = input("Masukkan Password Kasiristrasi : ")

    if passwordKasir == passwordKasirTerdaftar :
        print(f"Selamat datang {namaKasir} di sistem Kasir Pt.Betamart")
        break
    else :
        print("Password anda salah, Silahkan ulangi lagi 🙏")
        True

### sistem login ####

daftarBarang = [
    {
        'Nama': 'Kopi Luwak',
        'Bidang': 'Minuman',
        'Stock': 30, 
        'Harga': 13000,
        'Satuan': 'Bungkus'
    },
    {
        'Nama': 'Green Tea',
        'Bidang': 'Minuman',
        'Stock': 20,
        'Harga': 17000, 
        'Satuan': 'Box'
    },
    {
        'Nama': 'Kopi Kangen',
        'Bidang': 'Minuman',
        'Stock': 15,
        'Harga': 10000, 
        'Satuan': 'Botol'
    },
    {
        'Nama': 'Oreo',
        'Bidang': 'Makanan',
        'Stock': 20,
        'Harga': 9000, 
        'Satuan': 'Buah'
    },
    {
        'Nama': 'Nissin',
        'Bidang': 'Makanan',
        'Stock': 14,
        'Harga': 10000, 
        'Satuan': 'Bungkus'
    },
    {
        'Nama': 'Malkis',
        'Bidang': 'Makanan',
        'Stock': 21,
        'Harga': 9000, 
        'Satuan': 'Bungkus'
    },
    {
        'Nama': 'Biore',
        'Bidang': 'Perawatan',
        'Stock': 16,
        'Harga': 42000, 
        'Satuan': 'Buah'
    },
    {
        'Nama': 'Biore Men',
        'Bidang': 'Perawatan',
        'Stock': 12,
        'Harga': 40000, 
        'Satuan': 'Buah'
    },
    {
        'Nama': 'Garnier',
        'Bidang': 'Perawatan',
        'Stock': 23,
        'Harga': 35000, 
        'Satuan': 'Buah'
    },
    {
        'Nama': 'Wipol',
        'Bidang': 'Umum',
        'Stock': 12,
        'Harga': 23000, 
        'Satuan': 'Buah'
    },
    {
        'Nama': 'Hand Sanitizer',
        'Bidang': 'Umum',
        'Stock': 20,
        'Harga': 25000, 
        'Satuan': 'Buah'
    },
    {
        'Nama': 'Daia',
        'Bidang': 'Umum',
        'Stock': 15,
        'Harga': 45000, 
        'Satuan': 'Bungkus'
    },
    {
        'Nama': 'Bulpoin',
        'Bidang': 'ATK',
        'Stock': 27,
        'Harga': 7000, 
        'Satuan': 'Buah'
    },
    {
        'Nama': 'Kertas A4',
        'Bidang': 'ATK',
        'Stock': 13,
        'Harga': 50000, 
        'Satuan': 'Rim'
    },
    {
        'Nama': 'Pensil',
        'Bidang': 'ATK',
        'Stock': 24,
        'Harga': 5000, 
        'Satuan': 'Buah'
    },
    
]

indexBox = []
nameBox = []

tableAnalyst = PrettyTable()
tableStock = PrettyTable()
tableStockSpecific = PrettyTable()



###### Menampilkan Barang (Default) ######

def addBarangToPrettyTable() :
    tableStock.field_names = ['Index','Nama','Bidang','Stok','Harga','Satuan']
    for i in range(len(daftarBarang)) :
        tableStock.add_row([i,daftarBarang[i]['Nama'],daftarBarang[i]['Bidang'],daftarBarang[i]['Stock'],daftarBarang[i]['Harga'],daftarBarang[i]['Satuan']])
            
addBarangToPrettyTable()


def tambahIndexNama():
    for i in range(len(daftarBarang)) :
        indexBox.append(i) 
        nameBox.append(daftarBarang[i]['Nama'])

tambahIndexNama()



def pilihanSatu() :
    
    while True :
        while True:
            try:
                inputanPilihan = int(input("""
- - - - - - - - - - - - - - - - - - - - - - - -  
         Silahkan Pilih Opsi 1, 2, atau 3 
        
        1. Display All Data.
        2. Display Specific Data
        3. Back To Main Menu
                                
        Input nomor Pilihan Anda Di Sini : """))
                break
            except:
                print("Mohon Masukkan integer absolute 1,2, atau 3 sesuai opsi yang tersedia")

        if inputanPilihan == 1 :
            print(' DAFTAR BARANG BETAMART \n')
            print(tableStock)
            

        elif inputanPilihan == 2 :
            while True :
                while True:
                    try:
                        inputIndexBarang = int((input('Masukkan Index Barang yang ingin dipilih : ')))
                        break
                    except:
                        (print("Mohon Masukkan integer sesuai opsi yang tersedia"))
            
                tableStockSpecific.field_names = ['Index','Nama','Bidang','Stok','Harga','Satuan']

                if inputIndexBarang in indexBox :
                    tableStockSpecific.add_row([inputIndexBarang,daftarBarang[inputIndexBarang]['Nama'],daftarBarang[inputIndexBarang]['Bidang'],daftarBarang[inputIndexBarang]['Stock'],daftarBarang[inputIndexBarang]['Harga'],daftarBarang[inputIndexBarang]['Satuan']])
                    print(' DAFTAR BARANG BETAMART \n')
                    print(tableStockSpecific)
                    print("\n")
                    tableStockSpecific.clear_rows()
                    break    
                else:
                    print("Maaf index Barang yang anda masukkan tidak ada, silahkan input index barang yang baru")

        elif inputanPilihan == 3 :
            break
        
        else:
            print("Maaf Angka yang anda input tidak tersedia di Sub Menu, silahkan input angka 1 atau 2")

# pilihanSatu()

            
####### Menambah Barang ######

def pilihanDua() :
    while True :
        while True:
            try:
                inputpilihan2 = int(input(""" 
            - - - - - - - - - - - - - - - - - - - - - - - -  
            Silahkan Pilih Opsi 1 atau 2 
            
            1. Input Barang Baru
            2. Kembali Ke Menu Utama
                                    
            Input nomor Pilihan Anda Di Sini : """))
                break
            except:
                print("Mohon Masukkan integer absolute 1 atau 2 sesuai opsi yang tersedia")
        
        if inputpilihan2 == 1:
            namaBarang = input('Masukkan Nama Barang : ').lower()
            if namaBarang in nameBox:
                print('Maaf nama Barang Tersebut Sudah ada, Silahkan Input Nama Barang Lain')
            else :
                bidangBarang = input('Masukkan Bidang Barang : ')
                while True:
                    try:
                        stockBarang = abs(int(input('Masukkan Stock Barang : ')))
                        break
                    except:
                        print("stock barang yang diinput harus dalam bentuk INTEGER / ANGKA POSITIF")
                while True :    
                    try:    
                        hargaBarang = abs(int(input('Masukkan Harga Barang : ')))
                        break
                    except:
                        print("stock barang yang diinput harus dalam bentuk INTEGER / ANGKA POSITIF")
                
                satuanBarang = (input('Masukkan Satuan Barang (e.g. "Bungkus, Rim, Buah") : '))
        
                daftarBarang.append({
                'Nama' : namaBarang, 
                'Bidang' : bidangBarang, 
                'Stock' : stockBarang, 
                'Harga' : hargaBarang,
                'Satuan' : satuanBarang
                })
                tambahIndexNama()
                tableStock.add_row([indexBox[-1],daftarBarang[-1]['Nama'],daftarBarang[-1]['Bidang'],daftarBarang[-1]['Stock'],daftarBarang[-1]['Harga'],daftarBarang[-1]['Satuan']])
            
                print(' DAFTAR BARANG BETAMART')
                print(tableStock)
                
        
        elif inputpilihan2 == 2:
            break

        else:
            print("Maaf Angka yang anda input tidak tersedia di Sub Menu, silahkan input angka 1 atau 2")


# pilihanDua()


###### Menghapus Barang ######

def pilihanTiga():
    while True :
        while True :
            try:
                inputpilihan3 = int(input(""" 
            - - - - - - - - - - - - - - - - - - - - - - - -  
            Silahkan Pilih Opsi 1 atau 2 
            
            1. Hapus Barang
            2. Kembali Ke Menu Utama
                                    
            Input nomor Pilihan Anda Di Sini : """))
                break
            except:
                print("Mohon Masukkan integer absolute 1 atau 2 sesuai opsi yang tersedia")

        if inputpilihan3 == 1:
            print(tableStock)
            while True: 
                try:
                    indexBarang = abs(int(input('Masukkan index Barang yang ingin dihapus : ')))
                except:
                    print("Index Barang yang dimasukkan harus angka absolute !")
                if indexBarang in range(len(daftarBarang)):
                    s = 'Barang {} Dengan Index Nomor {} Berhasil Dihapus 👍'.format(daftarBarang[indexBarang]['Nama'],indexBarang)
                    del daftarBarang[indexBarang]
                    tableStock.clear_rows()
                    for i in range(len(daftarBarang)) :
                        tableStock.add_row([i,daftarBarang[i]['Nama'],daftarBarang[i]['Bidang'],daftarBarang[i]['Stock'],daftarBarang[i]['Harga'],daftarBarang[i]['Satuan']])
        
                    # tableStock.del_row(indexBarang)
                    # del nameBox[indexBarang]
                    print(' DAFTAR BARANG BETAMART \n')
                    print(tableStock)
                    print(s)
                    break
                else:
                    print(f'Maaf 🙏 index nomor {indexBarang} tidak ada, silahkan input index baru!\n')
        elif inputpilihan3 == 2:
            break
        else:
            print("Maaf Nomor Opsi yang anda input tidak tersedia, mohon pilih opsi 1 atau 2 ")

# pilihanTiga()

###### Adjustment Barang ######

def pilihanEmpat():

    while True:
        while True:
            try:
                inputPilihanADJ = int(input(""" 
            - - - - - - - - - - - - - - - - - - - - - - - -  
                    Silahkan Pilih Opsi 1 atau 2 
                    
                    1. Adjustment Barang
                    2. Kembali Ke Menu Utama
                                            
                    Input nomor Pilihan Anda Di Sini : """))
                break
            except:
                 print("Mohon Masukkan integer absolute 1 atau 2 sesuai opsi yang tersedia")

        if inputPilihanADJ == 1:

            while True :
                print(tableStock)

                while True:
                    try:
                        indexADJ = int(input("Masukkan nomor index yang ingin disesuaikan : "))
                        break
                    except:
                        print("Mohon masukkan sesuai nomor index yang tersedia 🙏")
                
                if indexADJ not in indexBox:
                    print('Maaf Index Barang Tersebut Belum Ada, Silahkan Input Index Lain Atau Tambahkan Barang Baru di Menu Tambah Barang Baru')
                else:
                    namaUpdate = input("Masukkan Nama Barang Terupdate : ")
                    bidangUpdate = input("Masukkan Bidang Barang Terupdate : ")
                    while True:
                        try:
                            stockUpdate = abs(int(input("Masukkan Stock Barang Terupdate : ")))
                            break
                        except:
                            print("stock barang yang diinput harus dalam bentuk ABSOLUTE INTEGER ")
                    while True:
                        try:
                            hargaUpdate = abs(int(input("Masukkan Harga Barang Terupdate : ")))
                            break
                        except:
                            print("harga barang yang diinput harus dalam bentuk ABSOLUTE INTEGER ")
                    satuanUpdate = input("Masukkan Satuan Barang Terupdate : ")
                    
                    daftarBarang[indexADJ].update({
                        'Nama' : namaUpdate, 
                        'Bidang' : bidangUpdate, 
                        'Stock' : stockUpdate, 
                        'Harga' : hargaUpdate,
                        'Satuan' : satuanUpdate
                    })
                    tambahIndexNama()
                    # print(daftarBarang)
                    
                    tableStock.clear_rows()
                    for i in range(len(daftarBarang)) :
                        tableStock.add_row([i,daftarBarang[i]['Nama'],daftarBarang[i]['Bidang'],daftarBarang[i]['Stock'],daftarBarang[i]['Harga'],daftarBarang[i]['Satuan']])
                    print(' DAFTAR BARANG BETAMART \n')
                    print(tableStock)
                    break
        elif inputPilihanADJ == 2:
            break

        else:
            print("Maaf Nomor Opsi yang anda input tidak tersedia, mohon pilih opsi 1 atau 2 ")


# pilihanEmpat()


###### Analisa Revenue Barang #####

def pilihanLima():
    cartRevenue = 0
    while True:
        while True:
            try:
                inputPilihanAnalis = int(input(""" 
    - - - - - - - - - - - - - - - - - - - - - - - -  
            Silahkan Pilih Opsi 1,2, atau 3. 
            
            1. Tampilkan Forecast Gross Revenue
            2. Tampilkan total revenue per Bidang
            3. Tampilkan total revenue per Item
            4. Kembali Ke Menu Utama
                                    
            Input nomor Pilihan Anda Di Sini : """))
                break
            except:
                print("Mohon Masukkan integer absolute 1,2,3 atau 4 sesuai opsi yang tersedia")
        
        if inputPilihanAnalis == 1 :
            tableAnalyst.field_names = ['Nama','Stok','Harga','Gross Revenue']
            for i in range(len(daftarBarang)) :
                tableAnalyst.add_row([daftarBarang[i]['Nama'],daftarBarang[i]['Stock'],daftarBarang[i]['Harga'],daftarBarang[i]['Stock'] * daftarBarang[i]['Harga']])                            

            for i in range(len(daftarBarang)) :
               cartRevenue += daftarBarang[i]['Stock'] * daftarBarang[i]['Harga']

            tableAnalyst.add_row(['','','',''],divider=True)
            tableAnalyst.add_row(['FORECAST GROSS REVENUE','--','---',cartRevenue])
            print(tableAnalyst)
            print(f"Perkiraan Pendapatan Retail adalah {cartRevenue} ")
            # print(daftarBarang)
            cartRevenue = 0
            tableAnalyst.clear()

        elif inputPilihanAnalis == 2 :

            tableAnalyst.field_names = ['Nama','Bidang','Stok','Harga','Gross Revenue']
            stages = False
            bidangBox = []
            
            while True :
                namaBidangPilihan = input("Masukkan Nama Bidang yang ingin diforecast : ")

                for i in range(len(daftarBarang)) :
                    bidangBox.append(daftarBarang[i]['Bidang'].lower())

                if namaBidangPilihan.lower() in bidangBox:
                    stages = True
                    break
                else: 
                    print("Maaf Bidang yang anda pilih tidak ada, silahkan input bidang yang tersedia 🙏")

            if stages == True:
                for i in range(len(daftarBarang)) :
                    if namaBidangPilihan.lower() == daftarBarang[i]['Bidang'].lower(): 
                        tableAnalyst.add_row([daftarBarang[i]['Nama'],daftarBarang[i]['Bidang'],daftarBarang[i]['Stock'],daftarBarang[i]['Harga'],daftarBarang[i]['Stock'] * daftarBarang[i]['Harga']])                            
                        cartRevenue += daftarBarang[i]["Stock"] *daftarBarang[i]['Harga']
                    
                tableAnalyst.add_row(['','','','',''],divider=True)
                tableAnalyst.add_row(['FORECAST FIELD REVENUE','---','---','---',cartRevenue])
                print(tableAnalyst)
                cartRevenue = 0
                tableAnalyst.clear()

        elif inputPilihanAnalis == 3 :

            tableAnalyst.field_names = ['Nama','Bidang','Stock','Harga','Gross Revenue']
            ItemBox = []
            checknamabox = []
            print(tableStock)

            for i in range(len(daftarBarang)) :
                        ItemBox.append(daftarBarang[i]['Nama'].lower())

            while True:

                while True :
                    namaItemPilihan = input("Masukkan Nama Item yang ingin diforecast : ").lower()
                    if namaItemPilihan in ItemBox:
                        pass
                    else: 
                        print("Maaf Item yang anda pilih tidak ada, silahkan input Item yang tersedia 🙏")
                        
                    if namaItemPilihan not in checknamabox: 
                        break
                    else:
                        print("Item Tersebut telah anda masukkan, mohon masukkan item lain.")
                        
                for i in range(len(daftarBarang)) :
                    if namaItemPilihan == daftarBarang[i]['Nama'].lower():
                            tableAnalyst.add_row([daftarBarang[i]['Nama'], daftarBarang[i]['Bidang'], daftarBarang[i]['Stock'], daftarBarang[i]['Harga'], daftarBarang[i]['Stock'] * daftarBarang[i]['Harga']])                            
                            cartRevenue += daftarBarang[i]["Stock"] * daftarBarang[i]['Harga']
                            checknamabox.append(daftarBarang[i]['Nama'].lower())
                            print(checknamabox)
                                
                                
                z = input("ketik 'ya' untuk tambah item, ketik 'print' untuk cetak table analyst & kembali ke submenu : ").lower()
                        
                if z == 'ya':
                    True

                elif z == 'print':
                    tableAnalyst.add_row(['','','','',''],divider=True)
                    tableAnalyst.add_row(['FORECAST ITEM REVENUE','---','---','---',cartRevenue])
                    print(tableAnalyst)
                    cartRevenue = 0
                    tableAnalyst.clear()
                    break

                else:
                    print("Maaf input yang anda berikan salah, mohon ketik 'ya' atau 'print' !")
                    

        elif inputPilihanAnalis == 4 :
            break
        else:
            print(f'Maaf 🙏 index nomor {inputPilihanAnalis} tidak ada, silahkan input index baru!\n')


# pilihanLima()



while True:
    while True:
        try:
            pilihanMenu = int(input(""" 
    #------------------------------------------------------------#    
            Selamat Datang di Menu-mini Kasir Beta-mart
            
            List Menu :
            1. Menampilkan Daftar Barang
            2. Menambah Barang Baru
            3. Menghapus Barang
            4. Adjustment Barang
            5. Analisa Revenue Barang                    
            6. Exit Program
            
            Masukkan nomor program yang ingin dijankan (1-6) : """))
            break
        except:
            print("Maaf pilihan yang anda masukkan tidak ada, silahkan pilih nomor 1-6")
    if pilihanMenu == 1 :
        pilihanSatu()
    elif pilihanMenu == 2 :
        pilihanDua()
    elif pilihanMenu == 3:
        pilihanTiga()
    elif pilihanMenu == 4 :
        pilihanEmpat()
    elif pilihanMenu == 5 :
        pilihanLima()
    elif pilihanMenu == 6 :
        break
    else:
        print('Maaf 🙏 , input yang anda kirim salah, mohon masukan 1-6 sesuai dengan pilihan menu program')



