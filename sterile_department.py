class Sterilizer:  # blueprint of one machine (like a struct in C)

    def __init__(self, name, kind, temp, cycle_minutes):
        # constructor -- self is the new machine
        self.name = name
        self.kind = kind
        self.temp = temp
        self.cycle_minutes = cycle_minutes
        self.status = "ready"

    def start_cycle(self):
        if self.status == "running":
            print(f"{self.name} is already running.")
        else:
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


def ask_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a number.")


sterile = Department("Sterile Supply")

for i in range(1, 5):
    sterile.add(Sterilizer(f"Autoclave {i}", "steam", 134, 60))

for i in range(1, 3):
    sterile.add(Sterilizer(f"Plasma {i}", "plasma", 50, 47))

while True:
    print()
    print("1 - Show all machines")
    print("2 - Start a cycle")
    print("3 - Finish a cycle")
    print("4 - Count running machines")
    print("0 - Exit")
    option = ask_number("Choose: ")

    if option == 0:
        print("Goodbye.")
        break
    elif option == 1:
        sterile.show_all()
    elif option == 2 or option == 3:
        total = len(sterile.machines)
        choice = ask_number(f"Which machine? (1-{total}): ")
        if 1 <= choice <= total:
            machine = sterile.machines[choice - 1]
            if option == 2:
                machine.start_cycle()
            else:
                machine.finish_cycle()
        else:
            print("No such machine.")
    elif option == 4:
        print(f"Running now: {sterile.count_running()}")
    else:
        print("No such option.")
