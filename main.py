from perpus.perpustakaan import Perpustakaan
from perpus.peminjam import Peminjam
from perpus.buku import Buku

uin = Perpustakaan("Mari baca", "jl.samudra dua",8.00, 15.00)

buku1 = Buku("si kancil", "alif", "fiksi", "32 hal", "2015")
buku2 = Buku("siksa neraka", "razak", "fiksi", "14 hal", "2007")
buku3 = Buku("Ilmu alam", "fauzi", "ilmu", "64 hal", "2011")
buku4 = Buku("coding", "qodri", "ilmu", "43 hal", "2017")

pmj = Peminjam()


while True:
    print("1. info perpustakaan ")
    print("2. daftar buku ")
    print("3. tambah buku ")
    print("4. isi data peminjam ")
    print("5. pinjam buku ")
    print("6. info buku ")
    print("7. info peminjam ")
    print("8. keluar ")
    menu = input("masukkan angka: ")
    if menu == "1":
        uin.info_perpustakaan()
    elif menu == "2":
        if len(uin.daftar_buku) >= 1:
            uin.rak_buku()
        else:
            print("rak kosong")
    elif menu == "3":
        uin.tambah_buku(buku1)
        uin.tambah_buku(buku2)
        uin.tambah_buku(buku3)
        uin.tambah_buku(buku4)
    elif menu == "4":
        pmj.isi_nama_peminjam(uin)
    elif menu == "5":
        no = 1
        if pmj.waktu_peminjaman < 8.00 or pmj.waktu_peminjaman > 15.00 or pmj.waktu_peminjaman == 0.0:
            print("perpustakaan belum buka")
        else:
            if len(uin.daftar_buku) <= 0:
                print("perpustakaan belum punya buku")
            else:
                print("====== daftar buku yang tersedia =====\n")
                for i in uin.daftar_buku:
                    print(f"{no}. {i}\n")
                    no += 1
                pilih_buku = int(input(f"\npilih buku yang ingin di pinjam : "))
                if pilih_buku > len(uin.daftar_buku):
                    print("buku yang anda pilih tidak tersedia")
                else:
                    new = uin.daftar_buku[pilih_buku - 1]
                    pmj.jml_buku_pinjaman = 1
                    nilai = uin.daftar_buku.index(new)
                    uin.daftar_buku.pop(nilai)
                    pmj.pinjam_buku(new)
    elif menu == "6":
        buku1.info_buku()
    elif menu == "7":
        if pmj.daftar_pinjaman == None :
            print("belum ada peminjam buku")
        else:
            pmj.info_peminjam(new)
    elif menu == "8":
        break
    
