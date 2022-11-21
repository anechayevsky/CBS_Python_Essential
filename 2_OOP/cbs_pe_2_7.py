class Transport:
    def move(self):
        print(f"{self.name} Вжжжжжж {self.speed} км/г")



class Railway(Transport):
    pass


class Water(Transport):
    pass


class Air(Transport):
    pass


class Space(Transport):
    pass


class Ground(Transport):
    name = 'empty'


class Electric_train(Railway):
    pass


class Locomotive(Railway):
    pass


class Tank(Railway):
    pass


class Funicular(Railway):
    pass


class Tram(Railway):
    pass


class Train(Railway):
    pass


class Underground(Railway):
    pass


class Monorail(Railway):
    pass


class Ship(Water):
    pass


class Liner(Water):
    pass


class Aircraft_carrier(Water):
    pass


class Yacht(Water):
    pass


class Steamer(Water):
    pass


class Tanker(Water):
    pass


class Icebreaker(Water):
    pass


class Canoe(Water):
    pass


class Fighter(Air):
    pass


class Scout(Air):
    pass


class Bomber(Air):
    pass


class Attack_aircraft(Air):
    pass


class Launch_vehicle(Air):
    pass


class Reactive(Air):
    pass


class Piston(Air):
    pass


class Turboprop(Air):
    pass


class Orbital_systems(Space):
    pass


class Interplanetary_spacecraft(Space):
    pass


class Interstellar_spacecraft(Space):
    pass


class Intergalactic_spacecraft(Space):
    pass


class Suborbital_systems(Space):
    pass


class near_Earth_spacecraft(Space):
    pass

class Car(Ground):
    color = ''
    speed = 0

class Motorbike(Ground):
    speed = 0

honda = Motorbike()
honda.speed = 200
honda.name = 'honda'
honda.move()
kawasaki = Motorbike()
kawasaki.speed = 300
kawasaki.move()
ford = Car()
ford.name = 'Fiesta'
ford.color = 'black'
print(ford.color)
ford.move()
