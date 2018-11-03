age = int(input("Enter your age: "))
if age < 1:
    print("Geçersiz girdi")
    quit()
elif age >= 18:
    print("Yetişkinlere yönelik dizi ve filmleri izleyebilir")
elif age > 12 and age < 18:
    print("Aile gözetimi altında +13 dizi ve filmleri izleyebilir")
elif age < 12 and age >= 7:
    print("Aile gözetimi altında +7 dizi ve filmleri izleyebilir")
elif age < 7:
    print("Çocuklara yönelik çizgi film ve çizgi diziler hariç film ve dizi izlemesi uygun değildir")
