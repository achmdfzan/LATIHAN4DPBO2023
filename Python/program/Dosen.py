from SivitasAkademik import SivitasAkademik

class Dosen(SivitasAkademik):

    def __init__(self, nik = "", nama = "", jenkel = "", asalUniv = "", emailEdu = "", nip = "", pendAkhir = "", keahlian = ""):
        super().__init__(nik, nama, jenkel, asalUniv, emailEdu)
        self.__nip = nip
        self.__pendAkhir = pendAkhir
        self.__keahlian = keahlian
    
    def getNIP(self):
        return self.__nip
    
    def setNIP(self, nip):
        self.__nip = nip

    def getPendAkhir(self):
        return self.__pendAkhir
    
    def setPendAkhir(self, pendAkhir):
        self.__pendAkhir = pendAkhir
    
    def getKeahlian(self):
        return self.__keahlian
    
    def setKeahlian(self, keahlian):
        self.__keahlian = keahlian