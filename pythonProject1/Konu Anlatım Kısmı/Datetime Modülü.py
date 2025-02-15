from datetime import datetime
from os import supports_effective_ids

suan = datetime.now()
print(suan.year)
print(suan.month)
print(suan.day)
print(suan.hour)

print(datetime.ctime(suan))

#strftime() fonkaiyonu şuanın ay yıl ve saat gibi parça parça almamızı sağlar

print(datetime.strftime(suan,'%x'))

suan = datetime.now()
saniye = datetime.timestamp(suan)
suan2 = datetime.fromtimestamp(saniye) # saniye cinsinden verilen değerin şuan ki zamana dönüştürülmesi.
print(saniye)
print(suan2)

tarih = datetime(2025,12,1)
tarih1 = datetime.now()
print(tarih-tarih1)