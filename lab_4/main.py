import csv

from functools import reduce


"""
Файл phe_healthcare.csv содержит данные о числе пациентов в Лондоне и оставшейся части королевства.
Требуется посчитать максимальное число пациентов в госпитале за все время в остальной части британии(rest of England)
"""

with open("phe_healthcare.csv",mode='r',encoding='UTF-8') as file:
    csv_reader = csv.reader(file)

    #Получаем записи, где часть королевства='Rest of England' и Местонахождение(исправить) пациентов = 'Patients in Hospital'
    #А еще нужно, чтобы последний столбец, где хранятся значения был не пустым
    filtered_rest_of_england = filter(
        lambda x: x[1] == 'Rest of England' and x[2] == 'Patients in Hospital' and x[-1] != '',csv_reader)
    #Отбрасываем все столбцы, кроме последнего. Конвертируем строки в числа
    #Переход от множества списков из строк к множеству чисел
    mapped_rest_of_england = map(lambda x : int(x[-1]),filtered_rest_of_england)
    #Находим максимальное значение среди последовательности mapped_rest_of_england
    #Получается что-то вроде res=max(x[0],max(x[1],max(x[2]...max(x[n-1],x[n]))))...)
    result = reduce(max,mapped_rest_of_england)
    # max(1,max(2,/))

with open("result.txt",'w') as file:
    file.write(str(result))