import sqlite3
import time

class DataBase:
    def __init__(self, name ='Aquarium.db'):
        self.connect = sqlite3.connect(name)
        self.cursor = self.connect.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Aquarium(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT NOT NULL,
                name VARCHAR (40) NOT NULL,
                color TEXT NOT NULL,
                size INTEGER NOT NULL,
                speed INTEGER NOT NULL,
                hungry INTEGER DEFAULT 0
            )
        """)
    def get_swim(self,):
        self.cursor.execute("""SELECT name, speed FROM Aquarium""" )
        return self.cursor.fetchall()

    def append_fish(self, fish):
        self.cursor.execute("INSERT INTO Aquarium (type, name, color, size, speed, hungry) VALUES (?,?,?,?,?,?)", (fish.type, fish.name, fish.color, fish.size, fish.speed, fish.hungry))

        self.connect.commit()

    def del_fish(self, name):
        self.cursor.execute("""DELETE FROM Aquarium WHERE name=?""", (name,))

        self.connect.commit()

    def get_fish(self, name):
        self.cursor.execute("""SELECT * FROM Aquarium WHERE name=? """, (name,))
        return self.cursor.fetchone()

    def get_info(self):
        self.cursor.execute("""SELECT name, hungry, speed FROM Aquarium""")
        return self.cursor.fetchall()

    def get_all(self):
        self.cursor.execute("""SELECT * FROM Aquarium""")
        return self.cursor.fetchall()

    def get_hungry(self):
        self.cursor.execute("""SELECT name, hungry FROM Aquarium""")
        return self.cursor.fetchall()

    def make_hunger(self):
        self.cursor.execute("""UPDATE Aquarium SET hungry = hungry+1""")
        self.connect.commit()

    def feed_all(self):
        self.cursor.execute("""UPDATE Aquarium SET hungry=0""")

        self.connect.commit()

class Fish(DataBase):
    def __init__(self,  name, color, size, speed, hungry):
        self.name = name
        self.color = color
        self.size = size
        self.speed = speed
        self.hungry = hungry

    def swim(self, name):
        for name, speed in self.get_swim():
            print(f'{name} плавает со скоростью {speed}')

class GoldFish(Fish):
    def __init__(self, name, color='gold', size=2, speed=3, hungry=0):
        super().__init__(name, color, size, speed, hungry)
        self.name = name
        self.color = color
        self.type = 'gold fish'

class Shark(Fish):
    def __init__(self, name, color='bright', size=6, speed=5, hungry=0):
        super().__init__(name, color, size, speed, hungry)
        self.name = name
        self.type = 'shark'

class Clownfish(Fish):
    def __init__(self, name, color='colorful', size=3, speed=2, hungry=0):
        super().__init__(name, color, size, speed, hungry)
        self.name = name
        self.type = 'clown fish'



class Aquarium:
    def __init__(self, name='Aquarium.db'):
        self.db = DataBase(name)

    def add_fish(self, fish):
        self.db.append_fish(fish)
        print('Успешно!!')

    def delete_fish(self, name):
        if self.find_fish_by_name(name):
            self.db.del_fish(name)
            print(f'{name} удален')
        else:
            print('Такого не знаем')

    def find_fish_by_name(self, name):
        fish_data = self.db.get_fish(name)
        if fish_data:
            return Fish(name=fish_data[0], color=fish_data[1], size=fish_data[2], speed=fish_data[3], hungry=fish_data[4])
        else:
            return 'Не найдено'

    def watch(self):
        for name, hungry, speed in self.db.get_info():
            print(f'\n{name} плавает со скоростью {speed}\nуровень голода - {hungry}')

    def feed(self):
        if all(self.db.get_hungry()) == 0:
            print('Все рыбы уже сыты')
            return None
        else:
            self.db.feed_all()
            print('Все рыбы накормлены')

    def _hunger_all(self):
        self.db.make_hunger()
        for name, char in self.db.get_hungry():
            if char > 12:
                print(f'{name} Умер от голода :(')
                self.delete_fish(name)
                break
            elif char > 5:
                print(f'{name} очень голодна')
            elif char == 10:
                print(f'{name} сейчас умрет')


    def sumilator_hungry(self, cucle=6):
        for _ in range(cucle):
            print('Ожидаем...')
            time.sleep(2)
            self.watch()
            self._hunger_all()

    def _all_info(self):
        for id,type,name,color,size,speed,hungry in self.db.get_all():
            print(f'\n{id} - id\n{type} - type\n{name} - name\n{color} - color\n{size} - size\n{speed} - speed\n{hungry} - hungry\n')



aquarium = Aquarium()

while True:
    oper = int(input('\n1 - add fish\n2 - watch\n3 - feed\n4 - delete fish\n5 - simulator hungry\n'))
    if oper == 1:
        type = int(input('\n1 - Gold Fish\n2 - Shark\n3 - Clown Fish\n'))
        name = input('name: ')
        if type == 1:
            aquarium.add_fish(GoldFish(name))
        elif type == 2:
            aquarium.add_fish(Shark(name))
        elif type == 3:
            aquarium.add_fish(Clownfish(name))

    elif oper == 2:
        aquarium.watch()
    elif oper == 3:
        aquarium.feed()
    elif oper == 4:
        name = input('name: ')
        aquarium.delete_fish(name)
    elif oper == 5:
        aquarium.sumilator_hungry()
    elif oper == 228:
        aquarium._all_info()











