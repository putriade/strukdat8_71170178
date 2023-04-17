class NodePelanggan:
    def __init__(self, namaPelanggan):
        self._namaPelanggan = namaPelanggan
     
    def getNamaPelanggan(self):
        return self._namaPelanggan
    
    def setnamaPelanggan(self, namaPelangganBaru):
        self._namaPelanggan = namaPelangganBaru
        

class Kasir:
    DEFAULT_CAPACITY = 3
    def __init__(self): #konstruktor
        self._data = [None] * Kasir.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self): #mengembalikan ukuran Queue
        return self._size

    def is_empty(self): #mengecek apakah Queue kosong ?
        return self._size == 0

    def dequeue(self): #menghapus data paling depan (front)
        if self.is_empty():
            print("Empty")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        print("\n### Pelanggan",answer.getNamaPelanggan(),"Selesai Membayar ###")
    
        listBaru = [None] * len(self._data)
        counterListBaru = 0 
        for i in range(len(self._data)):
            if self._data[i] != None:
                listBaru[counterListBaru] = self._data[i]
                counterListBaru += 1
        self._data = listBaru
        self._front = 0

    def enqueue(self, namaPelanggan): #menambah data ke list
        pelangganMasuk = NodePelanggan(namaPelanggan)
        if self._size == len(self._data):
            self.resize(2*len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = pelangganMasuk
        self._size += 1

    def resize(self, cap): #mengubah ukuran queue pada list
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0
        print("\n### Melakukan Resize ###")
    
    def printAll(self): #menampilkan daftar pelanggan dalam sebuah kasir
        print("\n=== Kasir ===")
        for i in range(len(self._data)):
            if self._data[i] != None:
                print(i+1,end=". ")
                print(self._data[i].getNamaPelanggan())
            else:
                print(i+1,end=". ")
                print("Kosong")
        

# test case program
tempatKasir = Kasir()
tempatKasir.enqueue("Haniif")
tempatKasir.enqueue("Sindu")
tempatKasir.enqueue("Dedi")
tempatKasir.printAll()

tempatKasir.enqueue("Beatrix")
tempatKasir.printAll()

tempatKasir.dequeue()
tempatKasir.printAll()

tempatKasir.enqueue("Shalom")
tempatKasir.printAll()

tempatKasir.dequeue()
tempatKasir.printAll()

