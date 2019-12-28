from View.View_Nilai import lihat,cari,header,notoption
from View.Input_Nilai import masukkan,edit,delete
header()
while True:
    print ()
    c = input("[ (L)ook, (A)dd, (E)dit, (D)elete, (S)earch , (Q)uit ]: ")
    if c.lower() == 'q':
        print("")
        print("=======THANK YOU=======")
        ext = input("\nPress ENTER to EXIT")
        if ext == '':
            break
        else:
            break

    # TAMPILKAN LIST DATA
    elif c.lower() == 'l':
        lihat()

    # MENAMBAH DATA
    elif c.lower() == 'a':
        masukkan()

    # EDIT DATA
    elif c.lower() == 'e':
        edit()

    # MENCARI DATA
    elif c.lower() == 's':
        cari()

    # HAPUS DATA
    elif c.lower() == 'd':
        delete()

    else:
        notoption()