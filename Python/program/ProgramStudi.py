class ProgramStudi:

    def __init__(self, namaProdi = "", kode = "", fakultas = ""):
        self.__namaProdi = namaProdi
        self.__kode = kode
        self.__fakultas = fakultas
        self.__listCourse = []
        self.__listDosen = []
        self.__listMahasiswa = []
    
    def getNamaProdi(self):
        return self.__namaProdi
    
    def setNamaProdi(self, namaProdi):
        self.__namaProdi = namaProdi
    
    def getKode(self):
        return self.__kode
    
    def setKode(self, kode):
        self.__kode = kode
    
    def getFakultas(self):
        return self.__fakultas
    
    def setFakultas(self, fakultas):
        self.__fakultas = fakultas
    
    def getListCourse(self):
        return self.__listCourse
    
    def addCourse(self, course):
        self.__listCourse.append(course)
    
    def getListDosen(self):
        return self.__listDosen
    
    def addDosen(self, dosen):
        self.__listDosen.append(dosen)
    
    def getListMahasiswa(self):
        return self.__listMahasiswa
    
    def addMahasiswa(self, mahasiswa):
        self.__listMahasiswa.append(mahasiswa)