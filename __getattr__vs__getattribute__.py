'''
http://python-3.ru/page/sravnenie-metodov-__getattr__-i-__getattribute__-python
Чтобы обобщить различия между методами __getattr__ и __getattribute__, в следующем примере используются оба
метода для реализации доступа к трем атрибутам, в числе которых: attr1 - атрибут класса, attr2 - атрибут экземпляра 
и attr3 - виртуальный атрибут, значение которого вычисляется при обращении к нему:

Если запустить этот пример, можно будет увидеть, что версия на основе метода __getattr__ перехватывает только попытки 
обращения к атрибуту attr3, потому что это единственный неопределенный аргумент.

С другой стороны, версия на основе метода __getattribute__ перехватывает все попытки чтения значений атрибутов и для 
получения значений неуправляемых атрибутов должна вызывать метод суперкласса, чтобы избежать зацикливания:

Несмотря на то, что метод __getattribute__ перехватывает больше операций обращения к атрибутам, чем метод __getattr__, 
тем не менее, на практике они оказываются лишь вариациями на одну тему - если атрибуты физически не сохраняются в памяти, 
эти два метода дают один и тот же эффект.

Here is the explanation on StackOverflow:
https://stackoverflow.com/questions/3278077/difference-between-getattr-vs-getattribute
'''

class GetAttr:
    attr1 = 1
    def __init__(self):
        self.attr2 = 2
    def __getattr__(self, attr):   # Только для неопределенных атрибутов
        print('get: ' + attr)      # Не attr1: наследуется от класса
        return 3                   # Не attr2: хранится в экземпляре
    
X = GetAttr()
print(X.attr1)
print(X.attr2)
print(X.attr3)
print('-' * 40)

class GetAttribute(object):
    attr1 = 1
    def __init__(self):
        self.attr2 = 2
    def __getattribute__(self, attr):  # Вызывается всеми операциями присваивания
        print('get: ' + attr)          # Для предотвращения зацикливания используется суперкласс
        if attr == 'attr3':
            return 3
        else:
            return object.__getattribute__(self, attr)
        
X = GetAttribute()
print(X.attr1)
print(X.attr2)
print(X.attr3)