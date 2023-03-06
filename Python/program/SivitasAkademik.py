from Human import Human

class SivitasAkademik(Human):

    def __init__(self, nik = "", nama = "", jenkel = "", asalUniv = "", emailEdu = ""):
        super().__init__(nik, nama, jenkel)
        self._asalUniv = asalUniv
        self._emailEdu = emailEdu

    def getAsalUniv(self):
        return self._asalUniv

    def setAsalUniv(self, asalUniv):
        self._asalUniv = asalUniv

    def getEmailEdu(self):
        return self._emailEdu

    def setEmailEdu(self, emailEdu):
        self._emailEdu = emailEdu