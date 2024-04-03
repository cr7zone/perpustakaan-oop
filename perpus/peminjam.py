class Peminjam:
    def __init__(self):
        self.nama_peminjam  = None
        self.waktu_peminjaman = 0.00
        self.daftar_pinjaman = None
        self.jml_buku_pinjaman = None

    def pinjam_buku(self, buku):
        self.daftar_pinjaman = buku
        print(f"{self.nama_peminjam} berhasil meminjam buku {buku} pada pukul {self.waktu_peminjaman}")

    def isi_nama_peminjam(self,batas):
        nama = input("masukkan nama : ")
        waktu = float(input("masukkan waktu : "))
        if waktu <= 8.00 or waktu >= 15.00:
            print("belum buka")
        else:
            self.nama_peminjam = nama
            self.waktu_peminjaman = waktu
    def info_peminjam(self, buku):
        print(f"nama peminjam       : {self.nama_peminjam}")
        print(f"buku yang dipinjam  : {buku}")  
        print(f"jumlah buku yang dipinjam  : {self.jml_buku_pinjaman}")
        print(f"waktu peminjaman : {self.waktu_peminjaman}")