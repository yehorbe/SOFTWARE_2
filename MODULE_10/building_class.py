class Elevator:
    def __init__(self, top_f, bottom_f, cur_f):
        self.top_f=top_f
        self.bottom_f=bottom_f
        self.cur_f=cur_f

    def floor_up(self):
        if self.cur_f!=self.top_f:
            self.cur_f+=1
        return

    def floor_down(self):
        if self.cur_f!=self.bottom_f:
            self.cur_f-=1
        return

    def go_to_floor(self, floor):
        if self.cur_f>floor:
            print("="*30)
            print("You are going down")
            print(f"Your current floor is {self.cur_f}")
            times_down=self.cur_f-floor
            for td in range(times_down):
                self.floor_down()
                print(f"Moved to the {self.cur_f} floor")
        if self.cur_f<floor:
            print("=" * 30)
            print("You are going up")
            print(f"Your current floor is {self.cur_f}")
            times_up=floor-self.cur_f
            for tup in range(times_up):
                self.floor_up()
                print(f"Moved to the {self.cur_f} floor")

class Building:
    def __init__(self, top_f, bottom_f, elevators_n):
        self.top_f=top_f
        self.bottom_f=bottom_f
        self.elevators_n=elevators_n
        self.elevators = [Elevator(top_f, bottom_f, bottom_f) for e in range(elevators_n)]

    def run_elevator(self, el_num, dest_floor):
        print("=" * 30)
        print(f"Calling Elevator {el_num} to floor {dest_floor}...")
        self.elevators[el_num - 1].go_to_floor(dest_floor)



print("=" * 30)
top_floor=int(input("Enter the top floor: "))
bottom_floor=int(input("Enter the bottom floor: "))
el_n=int(input("Enter the number of the elevators: "))
print("=" * 30)

b=Building(top_floor, bottom_floor, el_n)

b.run_elevator(1,5)
b.run_elevator(2,3)
b.run_elevator(1,bottom_floor)

