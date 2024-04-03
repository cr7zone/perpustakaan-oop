class Perpustakaan:
    def __init__(self, nama_perpus, alamat, buka, tutup):
        self.nama_perpus = nama_perpus
        self.alamat_perpus = alamat
        self.daftar_buku = []
        self.waktu_buka = buka
        self.waktu_tutup = tutup


    def tambah_buku(self, buku):
        self.daftar_buku.append(buku.judul)
        print(f'buku dengan judul "{buku.judul}" berhasil di tambahkan di rak ')

    def info_perpustakaan(self):
        print(f"Perpustakaan {self.nama_perpus} yang berlokasi di {self.alamat_perpus} ")
        print(f"Perpustakaan ini buka dari {self.waktu_buka} - {self.waktu_tutup} ")

    def rak_buku(self):
        for i in self.daftar_buku:
            print(i)
