"""Bilgisayarınızdaki tüm mp4,txt ve pdf dosyalarını
os modülüyle arayın ve bunların nerede bulunduklarını ve
isimlerini ayrı ayrı "pdf_dosyalari.txt","mp4_dosyaları.txt",
"txt_dosyaları.txt"
adlı dosyalara kaydedin."""
import os
for klasor_yolu,dosya_yolu,dosya_isimleri in os.walk("C:/"):
    for dosya_ismi in dosya_isimleri:
        if dosya_ismi.endswith(".txt"):
           tam_dosya_yolu = os.path.join(klasor_yolu, dosya_ismi)
           with open ("txt_dosyaları.txt","a",encoding="utf-8") as file:
               file.write(tam_dosya_yolu+ "\n")
               print("Dosya isminin sonu txt olan dosyalar bastırılıyor.")
        elif dosya_ismi.endswith(".pdf"):
            tam_dosya_yolu=os.path.join(klasor_yolu,dosya_ismi)
            with open ("pdf_dosyalari.txt","a",encoding="utf-8") as file:
                file.write(tam_dosya_yolu+"\n")
                print("Dosya isminin sonu pdf olan dosyalar bastırılıyor.")
        elif dosya_ismi.endswith(".mp4"):
            tam_dosya_yolu = os.path.join(klasor_yolu, dosya_ismi)
            with open("mp4_dosyaları.txt", "a", encoding="utf-8") as file:
                file.write(tam_dosya_yolu + "\n")
                print("Dosya isminin sonu mp4 olan dosyalar bastırılıyor.")
        else:
            print("Hatalı dosyaya rastlandı ve dosya ismi bastırılmadan atlanmıştır.")












