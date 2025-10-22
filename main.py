class Vector:
    #Конструктор
    def __init__(self, x, y, z): 
        self.x = x
        self.y = y
        self.z = z

    #Сложение векторов
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y 
        new_z = self.z + other.z
        return Vector(new_x, new_y, new_z)
    
    #Вычитание векторов
    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y 
        new_z = self.z - other.z
        return Vector(new_x, new_y, new_z)
    
    #Умножение векторов
    def __mul__(self, other):
        if type(other) == Vector:
            return self.x * other.x + self.y * other.y + self.z * other.z
        if type(other) == int:
            return Vector(self.x * other, self.y * other, self.z * other)
        
    #Унарный минус 
    def __neg__(self):
        return Vector(self.x * (-1), self.y * (-1), self.z * (-1))
    
    #Векторное произведение
    def __xor__(self, other):
        return Vector((self.y * other.z - self.z * other.y), ((-1)*(self.x * other.z - self.z * other.x)), (self.x * other.y - self.y * other.x))
    
    #Чтение координаты
    def __getitem__(self, key):
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        elif key == 2:
            raise IndexError("Индекс может быть 0, 1 или 2")
        else:
            print('ERROR_OF_KEY')

    #Изменение координаты 
    def __setitem__(self, key, value):
        if key == 0:
            self.x = value
        elif key == 1:
            self.y = value
        elif key == 2:
            self.z = value
        else:
            raise IndexError("Индекс может быть 0, 1 или 2")
    
    #Длина вектора
    def __abs__(self):
        return(sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2))
    
    #Строковое представление
    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'
    


a = Vector(1, 2, 9)
b = Vector(-8, 4, 7)

print(a)
print(b)

d = a + b #Сложение
c = a * 5 #Умножение на число
e = -b #Унарный минус
e[2] = 5 #Изменение координаты по Z

print(d)
print(c)
print(e)

g = a ^ b #Векторное произведение 
print(g)
