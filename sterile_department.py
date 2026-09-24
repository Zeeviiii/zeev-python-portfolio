class Sterilizer: # Defines the template of a sterilization machine. This is the equivalent
    
    def __init__(self, name, kind, temp, cycle_minutes):    #He is the Constructor. He runs alone once a machine is created.  
        # self is followed by 4 data points that give each machine the machine that is currently being built.
        self.name = name
        self.kind = kind
        self.temp = temp
        self.cycle_minutes = cycle_minutes
        self.status = "ready"

    def start_cycle(self):
        self.status = "running"
        print(f"{self.name} started: {self.temp}C for {self.cycle_minutes} min")

    def finish_cycle(self):
        if self.status == "running":
            self.status = "ready"
            print(f"{self.name} finished. Ready to unload.")
        else:
            print(f"{self.name} is not running.")

    def __str__(self):
        return f"{self.name} | {self.kind} | {self.temp}C | {self.cycle_minutes} min | {self.status}"

class Department:

    def __init__(self, name):
        self.name = name
        self.machines = []

    def add(self, machine):
        self.machines.append(machine)

    def show_all(self):
        print(f"--- {self.name} ---")
        for machine in self.machines:
            print(machine)

    def count_running(self):
        count = 0
        for machine in self.machines:
            if machine.status == "running":
                count += 1
        return count

sterile = Department("Sterile Supply")

for i in range(1, 5):
    sterile.add(Sterilizer(f"Autoclave {i}", "steam", 134, 60))

for i in range(1, 3):
    sterile.add(Sterilizer(f"Plasma {i}", "plasma", 50, 47))

sterile.show_all()

sterile.machines[0].start_cycle()
sterile.machines[4].start_cycle()
print(f"Running now: {sterile.count_running()}")

sterile.show_all()

choice = int(input("Which machine to start? (1-6): "))
if 1 <= choice <= len(sterile.machines):
    sterile.machines[choice - 1].start_cycle()
else:
    print("No such machine.")

sterile.show_all()
    

