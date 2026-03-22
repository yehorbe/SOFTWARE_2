import random


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
        elif self.cur_speed <= 0:
            self.cur_speed = 0

    def drive(self, hours):
        self.travelled_dist += self.cur_speed * hours


class Race:
    def __init__(self, name, dist, cars):
        self.name = name
        self.dist = dist
        self.cars = cars

    def hour_passes(self):
        for c in self.cars:
            speed_change = random.randint(-10, 15)
            c.acceleration(speed_change)
            c.drive(1)

    def print_status(self):
        print(f"Race: {self.name} | Distance: {self.dist} km")
        print(f"{'Reg. Number':<12} | {'Max Speed':<12} | {'Cur. Speed':<12} | {'Distance':<12}")
        print("-" * 65)
        for c in self.cars:
            print(f"{c.number:<12} | {c.max_speed:<8} km/h | {c.cur_speed:<8} km/h | {c.travelled_dist:<8.1f} km")

    def race_finished(self):
        for c in self.cars:
            if c.travelled_dist >= self.dist:
                return True
        return False


cars_list = []
for i in range(1, 11):
    max_speed = random.randint(100, 200)
    cars_list.append(Car(f"ABC-{i}", max_speed))

race = Race("Grand Demolition Derby", 8000, cars_list)

hours = 0
while not race.race_finished():
    race.hour_passes()
    hours += 1

    if hours % 10 == 0:
        print(f"--- Status at hour {hours} ---")
        race.print_status()

print(f"--- FINAL STATUS (Race finished in {hours} hours) ---")
race.print_status()