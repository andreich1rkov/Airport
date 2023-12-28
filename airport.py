import random
import time

class Plane:  #занять полосу, пополнить топливо, взлететь\сесть
              #Вид самолета. название, время посадки
    def __init__(self, serial_number, fuel_percentage, condition, name, landing_time):
        self.serial_number = serial_number
        self.fuel_percentage = fuel_percentage
        self.condition = condition
        self.name = name
        self.landing_time = landing_time

    def occupy_Polosa(self, polosa):
        if polosa.status == "free":
            polosa.status = "occupied"
            polosa.plane_occupying = self
            polosa.time_occupying = self.landing_time if self.landing_time > 2 else 2
        else:
            print("Эта полоса уже занята")

    def takeoff_plane(self, polosa):
        if polosa.status == "occupied" and polosa.plane_occupying == self:
            time.sleep(polosa.time_occupying)
            polosa.status = "free"
            polosa.plane_occupying = False
            print(f"Самолёт {self.name} взлетел.")
        else:
            print(f"Самолет {self.name} взлетел.")
    
    def land_plane(self, polosa):
        if polosa.status == "free":
            polosa.status = "occupied"
            polosa.plane_occupying = self
            print(f"Самолет {self.name} приземлился.")
        else:
            print(f"Эта полоса сейчас занята")

    def repair_refuel_plane(self, plane):
        time.sleep(2)
        plane.fuel_percentage = 100
        plane.condition = 1
        self.planes_to_takeoff.append(plane)

class Polosa:  # Занята, Кем занята, Время занятости
    def __init__(self, status, plane_occupying, time_occupying):
        self.status = status
        self.plane_occupying = plane_occupying
        self.time_occupying = time_occupying

class Airport:  #Список полос, Список приземл самол., Список желающ взл\приземл.                                
    def __init__(self):
        self.Polosas = []
        self.planes_landed = []
        self.planes_to_land = []
        self.planes_to_takeoff = []

    def InFO(airport):
        print("Название аэропорта: Пулково ")
        print(f"Кол-во полос: {len(Pulkovo.Polosas)}")
        print(f"Самолетов в аэропорту: {len(Pulkovo.planes_landed)}")


def check_runways(self):
        for polosa in self.Polosas:
            if polosa.status == "free" and self.planes_to_land:
                worst_plane = max(self.planes_to_land, key=lambda plane: plane.condition)
                self.planes_to_land.remove(worst_plane)
                worst_plane.occupy_Polosa(polosa)
            elif polosa.status == "occupied":
                polosa.time_occupying -= 1
                if polosa.time_occupying == 0:
                    polosa.plane_occupying.land_plane(polosa)

def check_planes(self):
        if self.planes_to_land:
            worst_plane = max(self.planes_to_land, key=lambda plane: plane.condition)
            if any(polosa.status == "free" for polosa in self.Polosas):
                free_runway = next(polosa for polosa in self.Polosas if polosa.status == "free")
                worst_plane.occupy_Polosa(free_runway)
                self.planes_to_land.remove(worst_plane)
            else:
                worst_plane.condition -= 1
                worst_plane.fuel_percentage -= 10
        
        if self.planes_to_takeoff:
            worst_plane = max(self.planes_to_takeoff, key=lambda plane: plane.condition)
            if any(polosa.status == "free" for polosa in self.Polosas):
                free_runway = next(polosa for polosa in self.Polosas if polosa.status == "free")
                worst_plane.takeoff_plane(free_runway)
                self.planes_to_takeoff.remove(worst_plane)
            else:
                worst_plane.condition -= 1
                worst_plane.fuel_percentage -= 10

def add_plane_to_list(plane, plane_list, probability):
        if random.random() < probability:
            plane_list.append(plane)
    
def simulate(self):
    while True:
        self.check_runways()
        self.check_planes()
        self.add_plane_to_list(Plane("43655", 15, 1, "Airbus A320", 3), self.planes_to_land, 0.4)
        self.add_plane_to_list(Plane("89407", 25, 3, "Cessna 172", 1), self.planes_to_land, 0.4)




Pulkovo = Airport()
polosa1 = Polosa("free", False, 0)
polosa2 = Polosa("free", False, 0)
Pulkovo.Polosas.append(polosa1)
Pulkovo.Polosas.append(polosa2)
plane1 = Plane("43655", 15, 1, "Airbus A320", 3)
plane2 = Plane("89407", 25, 3, "Cessna 172", 1)
plane3 = Plane("11245", 80, 2, "Gulfstream G550", 2)
plane4 = Plane("03274", 98, 1, "Airbus A380", 3)
plane5 = Plane("20456", 79, 4, "Boeing 747", 5)

Pulkovo.InFO()
plane3.occupy_Polosa(polosa1)
plane3.takeoff_plane(polosa1)