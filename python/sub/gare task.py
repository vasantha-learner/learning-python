class Car:
    brand = "xyz"  

    def __init__(self):
        self.speed = 0
        self.gear = 0
        self.engine_on = False

    def engineStart(self):
        if not self.engine_on:
            self.engine_on = True
            print("Engine started.")
        else:
            print("Engine is already running.")

    def engineStop(self):
        if self.engine_on:
            self.engine_on = False
            self.speed = 0
            self.gear = 0
            print("Engine stopped.")
        else:
            print("Engine is already off.")

    def accelerate(self):
        if self.engine_on:
            if self.speed < 300:
                self.speed += 25
                print(f"Car accelerated. Current speed: {self.speed} kmph")
                if self.speed == 300:
                    print("Max speed reached!")
            else:
                print("Car is already at max speed!")
        else:
            print("Start the engine first!")

    def brake(self):
        if self.speed > 0:
            self.speed -= 25
            if self.speed < 0:
                self.speed = 0
            print(f"Brake applied. Current speed: {self.speed} kmph")
        else:
            print("Car is already stopped.")

    def suddenBrake(self):
        self.speed = 0
        print("Sudden brake applied! Car stopped immediately.")

    def changeGear(self):
        if self.gear < 5:
            self.gear += 1
            print(f"Gear changed. Current gear: {self.gear}")
        else:
            print("Already in top gear (5).")



car1 = Car()
car1.engineStart()
car1.accelerate()
car1.accelerate()
car1.changeGear()
car1.changeGear()
car1.brake()
car1.suddenBrake()
car1.engineStop()
