from PIL import Image, ImageDraw, ImageFont, ImageFilter

def vod_znak(a,b):
    img = Image.open('img.png')
    idraw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial", size=b)
    idraw.text((10, 10), a, font=font)
    img.save('result.png')

def osvet(a):
    img = Image.open("img.png")
    width,height = img.size
    for i in range(width):
        for j in range(height):
            r, g ,b = img.getpixel((i,j))
            img.putpixel((i,j),(int(a * r),int(a * g),int(a * b)))

    img.save("result.png")

def cvadrat(a,b):
    img = Image.open('img.png')
    for i in range(0,a): #сколько рядов мы меняем
        for j in range(0,b):  #заполняем ряд по ширине
            img.putpixel((i, j), (0, 255 , 0)) 
    img.save("result.png")

def chb():
    img = Image.open("img.png")
    width,height = img.size

    for i in range(width):
        for j in range(height):
            r,g,b = img.getpixel((i,j))
            img.putpixel((i,j),(int(r*0.212+g*0.715+b*0.0746),int(r*0.212+g*0.715+b*0.0746),int(r*0.212+g*0.715+b*0.0746)))

    img.save("result.png")

def negative():
    img = Image.open("img.png")
    width,height = img.size

    for i in range(width):
        for j in range(height):
            r,g,b = img.getpixel((i,j))
            img.putpixel((i,j),(int(255 - r),int(255 - g),int(255 - b)))

    img.save("result.png")

def converter(a):
    img = Image.open('img.png')
    if a == 'jpg':
        img.save("result.jpg")
    if a == 'png':
        img.save("result.png")

def croppp(a, b, c, d):
    img = Image.open('img.png')
    result = img.crop((a, b, c, d))
    result.save("result.png")

def resizer(a, b):
    img = Image.open('img.png')
    result = img.resize(((int(a),int(b))))
    result.save("result.png")

def vstr_filters(a):
    img = Image.open('img.png')
    if a == 1: 
        coef = int(input('На сколько сильно применить фильтр (только для blur): '))
        result = img.filter(ImageFilter.GaussianBlur(coef))
        result.save("result.png")
    if a == 2:
        result = img.filter(ImageFilter.DETAIL)
        result.save("result.png")
    if a == 3:
        result = img.filter(ImageFilter.CONTOUR)
        result.save("result.png")
    if a == 4:
        result = img.filter(ImageFilter.EDGE_ENHANCE)
        result.save("result.png")
    if a == 5:
        result = img.filter(ImageFilter.EMBOSS)
        result.save("result.png")
    if a == 6:
        result = img.filter(ImageFilter.SHARPEN)
        result.save("result.png")
    if a == 7:
        result = img.filter(ImageFilter.SMOOTH)
        result.save("result.png")


print(""" Что делать с картинкой?
1 - Обрезать
2 - Изменить размер
3 - Наложить улучшающий фильтр
4 - Конвертировать в другой формат (png/jpg)
5 - Наложить негатив
6 - Сделать фото ЧБ
7 - Зелёный квадратик(метка)
8 - Засвет
9 - Водяной знак
""")
answer = int(input())

if answer == 1:
    x1 = int(input('x1: '))
    y1 = int(input('y1: '))
    x2 = int(input('x2: '))
    y2 = int(input('y2: '))
    croppp(x1,y1,x2,y2)
    print('Всё ок обрезали')

if answer == 2:
    width = int(input('Введи ширину картинки: '))
    height = int(input('Введи высоту картинки: '))
    resizer(width,height)
    print('Всё изменили')

if answer == 3:
    print(""" Все фильтры:
    1) BLUR/GaussianBlur - РАЗМЫТИЕ ФОТОГРАФИЙ
    2) DETAIL - ДЕТАЛИЗАЦИЯ ФОТО
    3) CONTOUR - КОНТУРИЗАЦИЯ ФОТО
    4) EDGE_ENHANCE -ВЫДЕЛЕНИЕ КОНТУРОВ
    5) EMBOSS - ТИСНЕНИЕ
    6) SHARPEN - УВЕЛИЧЕНИЕ РЕЗКОСТИ
    7) SMOOTH - СГЛАЖИВАНИЕ
    """)
    name_filter = int(input("Введи название фильтра из предложенных: "))
    vstr_filters(name_filter)
    print('Фильтр применён')

if answer == 4:
    formaat = input('Введи формат: ')
    converter(formaat)

if answer == 5:
    negative()

if answer == 6:
    chb()
if answer == 7:
    width = int(input('Введи ширину квадрата: '))
    height = int(input('Введи высоту квадрата: '))
    cvadrat(width,height)
if answer == 8:
    osv = int(input("На сколько повысить яркость :"))
    osvet(osv)
if answer == 9:
    text = input('Введи текст который будет на картинке:')
    size = int(input('Введи размер шрифта: '))
    vod_znak(text,size)