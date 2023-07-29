class MyIterator:
    def __init__(self, data):
        self.data = data #Данные по которым мы будем итерироваться
        self.index = 0 #Текущий индекс элемента

    def __iter__(self): #Метод который возвращает объект итератора
        return self

    def __next__(self):  #Метод который реализует саму итерацию, пройдемся по всему листу и вывеем на экран
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value

my_list = [1, 2, 3, 4, 5]
my_iterator = MyIterator(my_list)

for item in my_iterator:
    print(item)