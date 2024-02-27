
print('Задача 1')
L = list(range(45, 7, -3))  # создаем список и заполняем его значениями от 45 до 7 с шагом 3
print(L)

print('Задача 2')
S = set()  # создаем множество 
n = 0      # обнуляем счетчик
for i in L:
    if i%2==0:     # проверка на кратность
        S.add(i)   # если проходит по условию, то добавляем элемент в множество
    else:
        n += 1     # если не проходит по условию, то считаем количество нечетных
print("Количество нечётных в списке:", n)
print(S)

print('Задача 3')
for i in S:
    L.append(i)  # добавляем элементы из множества в конец списка
print(L)

for i in L:
    S.add(i)     # добавляем элементы из списка в множество, если данный элемент уже есть в множестве, то повтора не будет
print(S)

print('Задача 4')
from random import randint # импортирует функцию randint из библиотеки, которая позволяет генерировать случайные числа
string = "Произвольная строка чисел от одного до тысячи" # строка с произвольным текстом
words = string.split()     # разбиваем строку на слова через пробелы и сохраняет в список 

r = randint(0, len(words)-1)   # генерирует случайное число r в диапазоне от 0 до длины списка words минус 1, это число будет использоваться для выбора случайного слова из списка
s = words.pop(r) # рор функция изымает из списка элемент под определенным номером и возвращает его в переменную s
words.insert(r+1, s) # вставляет в список элемент s под номером r+1, pop забирает слово из строки в переменную s, а затем меняет его со следующим словом

print (" ".join(words)) # объединяет все слова из списка words в строку с пробелами между ними и выводит эту строку


print('Задача 5')
from random import randint, choice
#  импортирует функции randint и choice из модуля random, которые используются для генерации случайных чисел и выбора случайных элементов из последовательности

d = dict() #создает пустой словарь d, который будет использоваться для хранения пар ключ-значение

for _ in range(randint(10, 20)):   # цикл выполняется от 10 до 20 раз (случайное количество раз)
    n = randint(1, 8)              # генерирует случайное число n от 1 до 8
    key = "".join(["A" for __ in range(n)])   # создает ключ, который состоит из буквы "A", повторенной n раз
    value = randint(1, 1000)       # генерирует случайное значение от 1 до 1000
    d[key] = value                 # добавляет в словарь d пару ключ-значение
    
print(d)


max_len = float("-inf")
min_len = float("inf")
max_value = 0
min_value = 0

for key in d.keys():

    
    if len(key) > max_len:
        max_len = len(key)
        max_value = d[key]
        
    if len(key) < min_len:
        min_len = len(key)
        min_value = d[key]

average_key_length = (max_len + min_len) / 2


def F(item):     # возвращает true, если длина ключа меньше средней длины
    key = item[0]
    return len(key) < average_key_length

d = dict(filter(F, d.items()))

print(max_len, min_len, average_key_length, max_value, min_value)
print(d)



print('Задача 6')
from random import randint, choice

string = ""  #создает пустую строку string для хранения случайно сгенерированных слов
for _ in range(randint(3, 10)): # цикл ввыполняется случайное количество раз от 3 до 10
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" # определяем алфавит
    string += "".join([choice(alphabet) for __ in range(randint(4, 9))]) # в строку соединяются (join) случайное слово из алфавита от 4 до 9 букв
    string += " " # разделяет через пробел слова 

def sortirovka(word): # определяем функцию, которая принимает слово в качестве аргумента (def-define)
    a = word[0] # присваиваем переменной а первую букву слова
    return a == a.upper() # функция возвращает результат сравнения первой буквы слова (заглавная она или нет), ответом может быть true/false
def F(s): # определяет функцию, которая принимает строку в качестве аргумента
    words = s.split() # делим слова пробелами и сохраняем в список
    result = list(filter(sortirovka, words)) # фильтрует список слов, оставляя только те, для которых функция sortirovka возвращает true
    result.sort() # сортирует по алфавиту от меньшего к большему (  ()-значит, что функция применяется, вызывается )
    return result

print(string)     
print(F(string))  

print('Задача 7')
from random import randint

result_s = [] # пустой список для хранения последовательности результатов
result_k = [] # пустой список для хранения количества подбрасываний

def F1(): # ()- функция не принимает аргумент, а выполняется
    s = "" # строка, куда записываем 0 и 1 в зависимости от того, что выпадет
    k = 0 # количество подбрасываний
    while ("000" not in s) and ("111" not in s): # выполняется до тех пор, пока в строке s не появится "000" или "111"
        s += str(randint(0,1)) # добавляет к строке s случайное число 0 или 1, преобразованное в строку
        k += 1
        
    result_s.append(s) # добавляем в конец списка
    result_k.append(k)

for _ in range(10): # функцию F1 вызываем 10 раз 
    F1()

print(sum(result_k)/len(result_k)) # sum- сумма всех элементов в списке, len- возвращает количество элементов в списке