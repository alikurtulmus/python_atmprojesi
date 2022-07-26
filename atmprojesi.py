print("Cumhuriyet Banka Hoşgeldiniz...")
print("Para Çekmek İçin: 1 \nPara Yatırmak İçin: 2 \nBakiye Sorgulamak İçin: 3 \nProgramdan Çıkmak İçin: 4 \nTuşuna basınız")
bakiye=15000
while True:
    islem = int(input("Lütfen Yapmak İstediğiniz İşlemi Seçiniz:"))
    if(islem==4):
        print("Yine bekleriz..")
        break
    elif(islem==1):
        miktar=int(input("Lütfen çekmek istediğiniz miktarı giriniz:"))
        if(bakiye-miktar<0):
            print("Bakiyeniz yetersiz. Mevcut bakiyeniz:",bakiye,"TL'dir.")
            continue
        print("Paranız hazırlanıyoz, lütfen bekleyiniz...")
        bakiye-=miktar
        print("Kalan bakiyeniz:",bakiye,"TL'dir.")
    elif(islem==2):
        miktar=int(input("Lütfen yatırmak istediğiniz miktarı giriniz:"))
        bakiye+=miktar
        print("Güncel bakiyeniz:",bakiye,"TL'dir.")
    elif(islem==3):
        print("Bakiyeniz:",bakiye,"TL'dir")
