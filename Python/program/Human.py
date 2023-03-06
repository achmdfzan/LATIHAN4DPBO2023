class Human:

    def __init__(self, nik = "", nama = "", jenkel = ""):
        self._nik = nik
        self._nama = nama
        self._jenkel = jenkel
    
    def getNIK(self):
        return self._nik
    
    def setNIK(self, nik):
        self._nik = nik
    
    def getNama(self):
        return self._nama
    
    def setNama(self, nama):
        self._nama = nama
    
    def getJenkel(self):
        return self._jenkel
    
    def setJenkel(self, jenkel):
        self._jenkel = jenkel