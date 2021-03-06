from Model.Daftar_Nilai import data

def header():
    print("|==========================================================================|")
    print("|==================== PROGRAM INPUT DATA MAHASISWA ========================|")
    print("|==========================================================================|")
    print("|   (L)ook   |   (A)dd   |  (E)dit  |  (D)elete   |  (S)earch  |  (Q)uit   |")
    print("|==========================================================================|")


def notoption():
    print("|===========================================================================|")
    print("|======================= PILIH MENU YANG TERSEDIA ==========================|")
    print("|===========================================================================|")
    print("  [ (L)ook      (A)dd       (E)dit      (D)elete     (S)earch     (Q)uit ] : ")


def lihat():
     print("|=========================================================================|")
     print("|========================= DAFTAR DATA MAHASISWA =========================|")
     print("|=========================================================================|")
     print("| NO |      NAMA       |       NIM       | TUGAS |  UTS  |  UAS  | AKHIR  |")
     print("|=========================================================================|")
     i=0
     for x in data.items():
        i+=1
        print("| {7:2} | {1:15} | {2:15} | {3:5d} | {4:5d} | {5:5d} | {6:6.2f} |"
              .format(x[0],x[1][0],x[1][1],x[1][2],x[1][3],x[1][4],x[1][5],i))
     print("|=========================================================================|")



def cari():
    from View.Input_Nilai import cari
    cari()
