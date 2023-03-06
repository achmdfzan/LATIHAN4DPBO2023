class Course:

    def __init__(self, namaMatkul = ""):
        self.__namaMatkul = namaMatkul
        self.__listDosen = []
        self.__listMahasiswa = []
    
    def getNamaMatkul(self):
        return self.__namaMatkul
    
    def setNamaMatkul(self, namaMatkul):
        self.__namaMatkul = namaMatkul
    
    def getListDosen(self):
        return self.__listDosen
    
    def addDosen(self, dosen):
        self.__listDosen.append(dosen)
    
    def getListMahasiswa(self):
        return self.__listMahasiswa
    
    def addMahasiswa(self, mahasiswa):
        self.__listMahasiswa.append(mahasiswa)