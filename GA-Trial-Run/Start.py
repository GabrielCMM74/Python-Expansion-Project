#OOP

class BigObject:
    
    pass


obj1 = BigObject()
obj2 = BigObject()
obj3 = BigObject()
print(type(obj1))
print(type (None))
print(type (True))
print(type (5))
print(type (5.5))
print(type ('hi'))
print(type ([]))
print(type (()))
print(type ({}))


class PlayerCharacter: 
    membership = True # this is static
    def __init__(self, name='anything', age=0):
        
            self.name = name
            self.age = age

    def shout(self):
        print(f'my name is {self.name}')
    
    def run(self):
        print(f'my age is {self.age}')

    @classmethod
    def adding_things(cls, num1, num2):
        return cls( 'Teddy', num1 + num2)
    
    # @staticmethod
    # def adding_things(num1, num2, num3):
    #     return num1 + num2 + num3

player1 = PlayerCharacter('Sam', 45)
player2 = PlayerCharacter('Tom', 49)
player2.attack = 50

print(player1.name, player1.age, player1.run())
print(player2.name, player2.age, player2.attack, player2.shout())
print(player2.membership)
player3 = PlayerCharacter.adding_things(2, 5)
print(player3.age)



# class Cat:
#     species = 'mammal'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# cat1 = Cat('sarah', 10)
# cat2 = Cat('jerry', 12)
# cat3 = Cat('michael', 14)

# def get_oldest_cat(*args):
#     return max(args)

# print(f"The oldest cat is {get_oldest_cat(cat1.age, cat2.age, cat3.age)} years old.")


## Encapsulation is the binding of data - packaging and making a blueprint for multiple objects 

## Absraction - The privacy of keywoards and implemented function. Not knowing exactly how every aspect works.

class User: 
    def __init__(self, email):
        self.email = email    
    def sign_in(self):
        print('logged in')

    def attack(self):
        print('do nothing')

class Wizard(User):
    def __init__(self, name, power):
        # super().__init__(email)

        self.name = name 
        self.power = power

    def attack(self):
        User.attack(self)
        print(f'{self.name} is attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name 
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left- {self.num_arrows}')

    def check_arrows(self):
        return f'{self.num_arrows} remaining'

    def run(self):
        print('ran really fast')

class HybridBorg(Archer,Wizard):
    def __init__(self, name, power, num_arrows):
        Archer.__init__(self, name, num_arrows)
        Wizard.__init__(self, name, power)
        

hb1 = HybridBorg('borgie', 75, 90)
print(hb1.check_arrows())

wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 50)
print(wizard1.attack())
print(archer1.attack())
print(dir(wizard1))

print(isinstance(wizard1, Wizard))
#Inheritance but allowing shared user functionality but allowing for new things to be done based on each scenario 
# Dunder Methods 

# Polymorphism - many forms. Methods belong to objects. In which objects classes can inherit 
# different object lasses cna share different names 
print(wizard1.attack())

def player_attack(cahr):
    cahr.attack()

for cahr in [wizard1, archer1]:
    cahr.attack()





class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Billy(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#1 Add nother Cat

#2 Create a list of all of the pets (create 3 cat instances from the above)
my_cats = [ Simon(name='Simon',age=34), Sally(name='Fatty',age=78), Billy(name='Garfield',age=90) ]

#3 Instantiate the Pet class with all your cats use variable my_pets
my_pets = Pets(my_cats)
#4 Output all of the cats walking using the my_pets instance
print(my_pets.walk())



class Toy():
    def __init__(self, color, age):
        self.color = color 
        self.age = age 
        self.my_dict = {
            'name': 'yoyo',
            'has_pets' : True
        }

    def __str__(self):
        return f'{self.color}'
    
    def __len__(self):
        return 5
    
    def __call__(self):
        return ('yessss!!!')
    
    def __getitem__(self, i):
        return self.my_dict[i]


action_figure = Toy('red', 0)
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
print(action_figure())
print(action_figure['name'])


class SuperList(list):
    def __len__(self):
        return 1000
    

super_list4 = SuperList();

print(len(super_list4))
super_list4.append(5)
print(super_list4)
print(super_list4[0])
print(issubclass(SuperList, list))




#MRO 

class A:
    num = 10 

class B(A):
    pass

class C(A):
    num = 1

class D(B,C):
    pass

print(D.mro())
D.__str__


class Akiflow:
    def __init__(self, ability, power, age):
        self.ability = ability
        self.power = power
        self.age = age

    def combat(self):
        return f'I have {self.power} and I am keen'
    
aki1 = Akiflow('Flight', 'Invisible', 67)

print(aki1.combat())


















































