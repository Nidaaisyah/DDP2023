class Animal:
 def _init_(self, name, makanan, hidup, berkembangbiak):
    self.name = name
    self.makanan = makanan
    self.hidup = hidup
    self.berkembangbiak = berkembangbiak

class Badak(Animal):
 def _init_(self, name, makanan, hidup, berkembangbiak, berat, tinggi):
     super()._init_(name, makanan, hidup, berkembangbiak)
     self.berat = berat
     self.tinggi = tinggi

class Ikan(Animal):
 def _init_(self, name, makanan, hidup, berkembangbiak, air, jenis):
    super()._init_(name, makanan, hidup, berkembangbiak)
    self.air = air
    self.jenis = jenis

class Ular(Animal):
    def _init_(self, name, makanan, hidup, berkembangbiak, panjang, yaotipisatautebal):
        super()._init_(name, makanan, hidup, berkembangbiak)
        self.panjang = panjang
        self.bentuk = yaotipisatautebal