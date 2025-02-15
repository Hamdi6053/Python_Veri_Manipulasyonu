from PIL import Image,ImageFilter

image = Image.open("Python Resim Kırpma.jpg")
image.save("Python Resim Kırpma2.jpg")
image.rotate(180).save("Python Resim Kırpma3.jpg")
image.rotate(90).save("Python Resim Kırpma4.jpg")
image.convert(mode = "L").save("Python Resim Kırpma5.jpg")
degistir = (960,600)
image.thumbnail(degistir)
image.save("Python Resim Kırpma6.jpg")
image.filter(ImageFilter.GaussianBlur(5)).save("Python Resim Kırpma7.jpg") # Bulurlaştırmak için 5 değerini arttırdıkça daha çok bulurlaşacaktır.