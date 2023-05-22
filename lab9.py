
from PIL import Image, ImageFilter
from pathlib import Path

'''Модифицируйте программу из практики 7.3 (7 лабораторная работа ) или создайте заново: 
обработать любой операцией все картинки в заданной папке, используя для обхода файлов в папке модуль os (или Pathlib). 
При этом каталог для итоговых (обработанных) изображений должен тоже создаваться с помощью модуля os или Pathlib.'''

def lab1():
    filenames = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
    current_dir = Path.cwd()
    filenames = Path(current_dir).glob('*')
    Path('new_dir').mkdir(parents=True, exist_ok=True)

    for file in filenames:
        with Image.open(file) as img:
            img.load()
            new_img = img.filter(ImageFilter.CONTOUR)
            # new_img.show()
            new_img.save(Path("new_dir/new_" + f"new_{file}"))



'''Модифицировать программу из практики 9.1, 
добавив проверку типа (расширения) файла, если в папке хранятся разные типы файлов, 
а вам нужно обработать только заданные (jpg, png).'''

def lab2():

    current_dir = ''
    filenames = Path(current_dir).glob('*')
    Path('new_dir').mkdir(parents=True, exist_ok=True)

    for file in filenames:
        if file.suffix in ['.jpg', '.png']:
            with Image.open(file) as img:
                img.load()
                new_img = img.filter(ImageFilter.CONTOUR)
                # print(Path("new_dir", file))
                new_img.save(Path("new_dir/new_" + str(file)))

'''Имеется файл с данными в формате csv:
Продукт,Количество,Цена
Молоко,2,80
Сыр,1,500
Хлеб,2,70
Напишите программу, которая считывает данные из этого файла, подсчитывает итоговую сумму расходов и выводит данные в виде:
Нужно купить:
Молоко - 2 шт. за 80 руб.
Сыр - 1 шт. за 500 руб.
Хлеб - 2 шт. за 70 руб.
Итоговая сумма: 800 руб.'''

import csv

def lab3():
    file = open("data.csv", "r")
    data = list(csv.reader(file, delimiter=","))
    print("Нужно купить:")
    for i in data:
        print(f"{i[0]} - {i[1]} шт. за {i[2]} руб.")
    print(f"Итоговая сумма: {sum([int(i[1]) * int(i[2]) for i in data])} руб.")
    file.close()


'''lab1() '''
lab2()
lab3()