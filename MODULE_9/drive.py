class Car:
    def __init__(self, reg_number, max_speed, cur_speed=0, travelled_dist=0):
        self.number = reg_number
        self.max_speed = max_speed
        self.cur_speed = cur_speed
        self.travelled_dist = travelled_dist


    def acceleration(self, acc):
        self.cur_speed += acc
        if self.cur_speed>self.max_speed:
            self.cur_speed = self.max_speed
        elif self.cur_speed < 0:
            self.cur_speed = 0
        return

    def drive(self, hours):
        self.travelled_dist=self.cur_speed*hours
        return

my_car = Car("ABC-123", 142)

print('='*30)
print(f"For the car with number: {my_car.number}")
print(f"Max speed: {my_car.max_speed} km/h")
print(f"Current distance travelled: {my_car.travelled_dist} km")
print(f"Current speed: {my_car.cur_speed} km/h")
print('='*30)

my_car.acceleration(30)
print(f'Your current speed is {my_car.cur_speed}')

my_car.acceleration(70)
print(f'Your current speed is {my_car.cur_speed}')

my_car.acceleration(50)
print(f'Your current speed is {my_car.cur_speed}')

my_car.acceleration(-200)
print(f'Your current speed is {my_car.cur_speed}')
print('='*30)

my_car.cur_speed=60
my_car.drive(1.5)
print(f'You travelled {my_car.travelled_dist}')
print('='*30)

