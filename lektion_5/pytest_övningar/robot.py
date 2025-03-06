#modul

class Robot:
    def __init__(self, name, battery):
        self.name = name
        self.battery = battery
        self.started = False

    def start(self):
        self.started = True

    def stop(self):
        self.started = False

#övning 2:
    def charge(self):
        self.battery = 100    

#övning 3: 
    def move(self, distance_in_meters):
       for i in range(distance_in_meters): 
          self.battery -=10
          if self.battery <= 0:
            break

#övning 5:

    def introduce(self):
        return f"Hello, I am {self.name}."
 
#övning 7:

    def moving(self, distance):
        if distance < 0:
            raise ValueError("Ett fel har uppstått!")
        print(f"Robot rör sig {distance} steg")


#övning 9:

    
