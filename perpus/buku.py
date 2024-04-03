class Buku:
    def __init__(self, judul_buku, penulis, jenis_buku, halaman, tahun_terbit):
        self.judul = judul_buku
        self.penulis = penulis
        self.jenis = jenis_buku
        self.jml_halaman = halaman  
        self.tahun_terbit = tahun_terbit

    def info_buku(self):
        print("\n=========== info buku ===========")
        print(f"judul buku      : {self.judul}")
        print(f"penulis         : {self.penulis}")
        print(f"jenis           : {self.jenis}")
        print(f"jumlah halaman  : {self.jml_halaman}")
        print(f"tahun terbit    : {self.tahun_terbit}")
        print("=================================")
        print("                                 \n")

