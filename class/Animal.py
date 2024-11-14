class Animal:
    def __init__(self, name, age, color):
        """初始化Animal对象，self类似于this指针，指向当前对象"""
        self.name = name
        self.age = age
        self.color = color
        self.is_alive = True

    def __str(self):
        """返回对象的字符串表示，方法/属性前加双下划线表示私有属性，无法被子类继承"""
        return f"Animal(name:{self.name}, age:{self.age}, color:{self.color})"

    # 类方法，返回color属性
    @classmethod
    def get_color(cls):
        return cls.color


dog = Animal("dog", 3, "black")
print(dog.__str__())


class Cat(Animal):
    def __init__(self, name, age, color, owner=""):
        super().__init__(name, age, color)
        self.owner = owner


cat = Cat("cat", 2, "white", "Tom")
print(cat.__str())
