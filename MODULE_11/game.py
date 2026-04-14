class Car:
    def __init__(self, reg_number, max_speed):
        self.number = reg_number
        self.max_speed = max_speed
        self.cur_speed = 0
        self.travelled_dist = 0

    def acceleration(self, acc):
        self.cur_speed += acc
        if self.cur_speed > self.max_speed:
            self.cur_speed = self.max_speed
        elif self.cur_speed < 0:
            self.cur_speed = 0

    def drive(self, hours):
        self.travelled_dist += self.cur_speed * hours


class ElectricCar(Car):
    def __init__(self, reg_number, max_speed, capacity):
        super().__init__(reg_number, max_speed)
        self.capacity = capacity

class GasolineCar(Car):
    def __init__(self, reg_number, max_speed, t_volume):
        super().__init__(reg_number, max_speed)
        self.t_volume = t_volume

class Race:
    def __init__(self, name, dist, cars):
        self.name = name
        self.dist = dist
        self.cars = cars

    def hour_passes(self):
        import random
        for c in self.cars:
            change = random.randint(-10, 20)
            c.acceleration(change)
            c.drive(1)

    def print_status(self):
        print(f"\nRace: {self.name} | Goal: {self.dist} km")
        print(f"{'Reg. Number':<12} | {'Speed':<10} | {'Distance':<12}")
        print("-" * 45)
        for c in self.cars:
            print(f"{c.number:<12} | {c.cur_speed:<3} km/h | {c.travelled_dist:<8.1f} km")

    def race_finished(self):
        for c in self.cars:
            if c.travelled_dist >= self.dist:
                return True
        return False


e_car = ElectricCar("ABC-15", 180, 52.5)
g_car = GasolineCar("ACD-123", 165, 32.3)

cars_list = [e_car, g_car]

race = Race("Grand Prix", 500, cars_list)

hours = 0
while not race.race_finished() and hours < 10:
    race.hour_passes()
    hours += 1

print(f"\n--- FINAL STATUS (After {hours} hours) ---")
race.print_status()