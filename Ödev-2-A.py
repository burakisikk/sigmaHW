def asal(num):
    if (num == 2 or num == 3 or num == 5 or num == 7):
        print(num, "asaldır.")
    elif (num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0):
        print(num, "asaldır.")
    else:
        print(num, "asal değildir.")

girdi = int(input("Bir sayı giriniz: "))

asal(girdi)