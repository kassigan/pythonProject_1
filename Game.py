class Warrior():

# конструктор или метод инициализации (если функция вне класса - это функция, если функция внутри класса - метод
    def __init__(self, name, health, damage, hair_color):
        self.name = name
        self.health = health
        self.damage = damage
        self.hair_color = hair_color

# методы - что может делать
    def sleep (self):
        print(f"{self.name} went to sleep")
        self.health += 2

    def eat(self):
        print(f"{self.name} is eating")
        self.health += 1

    def walk(self):
        print(f"{self.name} is going")
        self.health -= 0.5

    def hit(self):
        print(f"{self.name} is hitting")
        self.health -= 1

    def info(self):
        print(f" Warrior name -  {self.name} ")
        print(f" Hair Color - {self.hair_color}")
        print(f" Health - {self.health}")
        print(f" Damage - {self.damage}")

warrior1 = Warrior("Rogan", 20, 5, "red")
warrior2 = Warrior("Halk", 25, 7, "yellow")
print(warrior1.name)
print(warrior1.hair_color)
print(warrior1.health)
print(warrior1.damage)

print(warrior1.health)
warrior1.sleep()
print(warrior1.health)