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
        elif self.cur_speed < 0:
            self.cur_speed = 0

    def drive(self, hours):
        self.travelled_dist += self.cur_speed * hours

cars = []
for i in range(1, 11):
    max_speed = random.randint(100, 200)
    new_car = Car(f"ABC-{i}", max_speed)
    cars.append(new_car)


race_on = True
hours = 0

while race_on:
    for car in cars:
        speed_change = random.randint(-10, 15)
        car.acceleration(speed_change)
        car.drive(1)
        if car.travelled_dist >= 10000:
            race_on = False

print(f"{'Reg. Number':<12} | {'Max Speed':<12} | {'Cur. Speed':<12} | {'Distance':<12}")
print("-" * 55)

for car in cars:
    print(f"{car.number:<12} | {car.max_speed:<12} km/h | {car.cur_speed:<12} km/h | {car.travelled_dist:<8.1f} km")