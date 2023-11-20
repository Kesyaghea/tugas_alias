from luas.segitiga import luas as ls
from luas.persegi import luas as lp
from luas.lingkaran import luas as ll
from volume.bola import hitung_volume as vb
from volume.kubik import hitung_volume as vk
from volume.prisma import hitung_volume as vp

#luas segitiga
print("menghitung luas segitiga")
print("alas = ",(9))
print("tinggi = ",(6))
print("Luas Segitiga:",ls(9,6))

#luas lingkaran
print("menghitung luas lingkaran")
print("radius = ",(26))
print("Luas Lingkaran:",ll(26))

#luas persegi
print("menghitung luas persegi")
print("sisi = ",(28))
print("Luas Persegi:",lp(28))

#volume kubik
print("menghitung volume kubik")
print("sisi = ",(10))
print("Volume kubik:",vk(10))

#volume bola
print("menghitung volume bola")
print("radius = ",(27))
print("Volume Bola:",vb(27))

#volume prisma
print("menghitung volume prisma")
print("alas_segitiga = ",(6))
print("tinggi_segitiga = ",(9))
print("tinggi_prisma = ",(28))
print("Volume Prisma:",vp(6, 9, 28))