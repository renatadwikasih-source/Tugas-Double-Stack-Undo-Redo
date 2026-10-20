# Program Double Stack: Undo dan Redo

undo_stack = []
redo_stack = []

teks = ""


def tampilkan_teks():
    print("\nTeks saat ini:", repr(teks))


def ubah_teks():
    global teks

    undo_stack.append(teks)
    redo_stack.clear()

    teks_baru = input("Masukkan teks baru: ")
    teks = teks_baru

    print("Teks berhasil diubah.")


def undo():
    global teks

    if not undo_stack:
        print("Tidak ada perubahan yang dapat dibatalkan.")
        return

    redo_stack.append(teks)
    teks = undo_stack.pop()

    print("Undo berhasil.")


def redo():
    global teks

    if not redo_stack:
        print("Tidak ada perubahan yang dapat dikembalikan.")
        return

    undo_stack.append(teks)
    teks = redo_stack.pop()

    print("Redo berhasil.")


while True:
    print("\n=== DOUBLE STACK UNDO/REDO ===")
    print("1. Tampilkan teks")
    print("2. Ubah teks")
    print("3. Undo")
    print("4. Redo")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        tampilkan_teks()
    elif pilihan == "2":
        ubah_teks()
    elif pilihan == "3":
        undo()
    elif pilihan == "4":
        redo()
    elif pilihan == "5":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
