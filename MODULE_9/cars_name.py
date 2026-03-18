class Car:
    def __init__(self, reg_number, max_speed, cur_speed=0, travelled_dist=0):
        self.number = reg_number
        self.max_speed = max_speed
        self.cur_speed = cur_speed
        self.travelled_dist = travelled_dist


my_car = Car("ABC-123", 142)

print('='*30)
print(f"For the car with number {my_car.number}")
print(f"Max speed: {my_car.max_speed} km/h")
print(f"Current distance travelled: {my_car.travelled_dist} km")
print(f"Current speed: {my_car.cur_speed} km/h")
print('='*30)

