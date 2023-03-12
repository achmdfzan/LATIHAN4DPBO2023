# LATIHAN4DPBO2023

![Untitled Diagram drawio](https://user-images.githubusercontent.com/91662639/224557742-00b9ffde-98cd-4dae-bbec-b6943f332673.png)

Alasan:
- Atribut fakultas pada class Dosen dan Mahasiswa dihilangkan, karena ada class ProgramStudi
- SivitasAkademik mewarisi Human karena semua SivitasAkademik merupakan Human (SivitasAkademik is a Human)
- Dosen dan Mahasiswa mewarisi SivitasAkademik karena Dosen dan Mahasiswa merupakan SivitasAkademik (Dosen is a SivitasAkademik and Mahasiswa is a SivitasAkadmeik)
- Sebuah Course dapat diajar oleh banyak Dosen dan dikontrak oleh banyak Mahasiswa (Course has a Dosen and Course has a Mahasiswa)
- Sebuah ProgramStudi memiliki banyak mata kuliah, banyak dosen, dan banyak Mahasiswa (ProgramStudi has a Course, Dosen, dan Mahasiswa)
