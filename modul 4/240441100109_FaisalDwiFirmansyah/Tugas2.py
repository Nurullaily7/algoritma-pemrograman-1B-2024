n = int(input("Masukkan bilangan desimal: "))
konvers = n
biner = ""
while n > 0:
    biner = str(n%2) + biner
    n = n//2
print("Hasil konversi bilangan desimal", konvers , "ke biner adalah", biner)
print(f"\nPola segitiga: ")
for i in range(1, len(biner) + 1):
    for j in range(len(biner) - i):
        print(' ', end=' ')
    for k in range(i):
        print(biner[k], end=' ')
    print()