from SivitasAkademik import SivitasAkademik

class Mahasiswa(SivitasAkademik):

    def __init__(self, nik = "", nama = "", jenkel = "", asalUniv = "", emailEdu = "", nim = ""):
        super().__init__(nik, nama, jenkel, asalUniv, emailEdu)
        self.__nim = nim
    
    def getNIM(self):
        return self.__nim
    
    def setNIM(self, nim):
        self.__nim = nim