# Создать переменную типа String
nameString = "new word"
# Создать переменную типа Integer
nameInteger = 70
# Создать переменную типа Float
nameFloat = 3.24
# Создать переменную типа Bytes
nameBytes = bytes(5)
# Создать переменную типа List
nameList = [2, "home", 5, 6, 2]
# Создать переменную типа Tuple
nameTuple = (12, 18, 79, "car")
# Создать переменную типа Set
nameSet = set("hello")
# Создать переменную типа Frozenset
nameFrosenset = frozenset([2, "home", 5, 6, 2, 12, 18, 79, "car"])
# Создать переменную типа Dict
nameDict = {"age": 31, "country": "Belarus"}
# Вывести в консоль все выше перечисленные переменные с добавлением типа данных
print(nameString, type(nameString))
print(nameInteger, type(nameInteger))
print(nameFloat, type(nameFloat))
print(nameBytes, type(nameBytes))
print(nameList, type(nameList))
print(nameTuple, type(nameTuple))
print(nameSet, type(nameSet))
print(nameFrosenset, type(nameFrosenset))
print(nameDict, type(nameDict))
# Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
name = "Vadim"
lastName = "Khomich"
cancat = name + lastName
print(cancat)
# Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
print("string", 256)
# Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
print("string " + "256")
