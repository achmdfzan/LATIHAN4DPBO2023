
#   Saya Achmad Fauzan NIM 2108061 mengerjakan soal Latihan Praktikum 4 dalam mata
#   kuliah Desain dan Pemrograman Berorientasi Objek untuk keberkahanNya maka saya
#   tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.

from Course import Course
from Dosen import Dosen
from Mahasiswa import Mahasiswa
from ProgramStudi import ProgramStudi

m1 = Mahasiswa("123", "ojan", "cowok", "UPI", "ojan@upi.edu", "2108061")
m2 = Mahasiswa("234", "anan", "cewek", "UPI", "anan@upi.edu", "2101114")
m3 = Mahasiswa("345", "bintang", "cwk", "UBI", "bintang@upi.edu", "2102665")
m4 = Mahasiswa("456", "yasin", "cowok", "UPI", "yasin@upi.edu", "2100137")
m5 = Mahasiswa("567", "azzahra", "cewek", "UPI", "azzahra@upi.edu", "2101234")
m6 = Mahasiswa("678", "amida", "cewek", "UPI", "amida@upi.edu", "2101010")
m7 = Mahasiswa("789", "rayhan", "cowok", "UPI", "rayhan@upi.edu", "2102102")
m8 = Mahasiswa("890", "jalu", "jalu", "UPI", "jalu@upi.edu", "2100001")

d1 = Dosen("987", "spongebob", "spons", "UPI", "spongebob@upi.edu", "0000001", "sekolah mengemudi", "memasak")
d2 = Dosen("876", "patrick", "bintang laut", "UPI", "patrick@upi.edu", "0000002", "ga sekolah", "semuanya")
d3 = Dosen("765", "squidward", "cumi/gurita", "UPI", "squidward@upi.edu", "0000003", "sekolah musik", "gaada")
d4 = Dosen("654", "tuan crab", "kepiting", "UPI", "crab@upi.edu", "0000004", "ga sekolah", "ngitung duit")

c1 = Course("Desain dan Pemrograman Berorientasi Objek")
c1.addDosen(d1)
c1.addMahasiswa(m1)
c1.addMahasiswa(m2)

c2 = Course("Pemrograman Visual dan Piranti Bergerak")
c2.addDosen(d2)
c2.addMahasiswa(m3)
c2.addMahasiswa(m4)

c3 = Course("Pengantar Pendidikan")
c3.addDosen(d3)
c3.addMahasiswa(m5)
c3.addMahasiswa(m6)

c4 = Course("Animasi")
c4.addDosen(d4)
c4.addMahasiswa(m7)
c4.addMahasiswa(m8)

p1 = ProgramStudi("Ilmu Komputer", "IK", "FPMIPA")
p1.addCourse(c1)
p1.addCourse(c2)
p1.addDosen(d1)
p1.addDosen(d2)
p1.addMahasiswa(m1)
p1.addMahasiswa(m2)
p1.addMahasiswa(m3)
p1.addMahasiswa(m4)

p2 = ProgramStudi("Pendidikan Ilmu Komputer", "PIK", "FPMIPA")
p2.addCourse(c3)
p2.addCourse(c4)
p2.addDosen(d3)
p2.addDosen(d4)
p2.addMahasiswa(m5)
p2.addMahasiswa(m6)
p2.addMahasiswa(m7)
p2.addMahasiswa(m8)

listProdi = [p1, p2]

for p in listProdi:

    print()

    print("Program Studi :")
    print(p.getNamaProdi() + " " + p.getKode())
    print()

    print("    Dosen " + p.getNamaProdi() + " :")
    for d in p.getListDosen():
        print("    " + d.getNama() + " " + d.getNIP())
    print()
 
    print("    Mahasiswa " + p.getNamaProdi() + " :")
    for m in p.getListMahasiswa():
        print("    " + m.getNama() + " " + m.getNIM())
    print()

    print("    Mata Kuliah " + p.getNamaProdi() + " :")
    for c in p.getListCourse():
        print("    " + c.getNamaMatkul())
        print("        Dosen : ")
        for d in c.getListDosen():
            print("        " + d.getNama())
        print("        Mahasiswa : ")
        for m in c.getListMahasiswa():
            print("        " + m.getNama())
    print()