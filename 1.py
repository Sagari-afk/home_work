class Car:
    def __init__(self, **patterns):
        self.patterns = patterns

    def start_engine(self):
        print(self.patterns["brand"], ": start engine")

    def stop_engine(self):
        print(self.patterns["brand"], ": stop engine")

    def switch_gear(self):
        print(self.patterns["brand"], ": switch gear")

    def push_brake(self):
        print(self.patterns["brand"], ": push brake")

    def tuning(self, part, new_part):   # тюнинг авто
        # part - деталь, которую нужно заменить, new_part - название новой детали
        self.patterns[part] = new_part

    def information(self):
        print("Information about this car:")
        for pattern, name in self.patterns.items():
            print(pattern, ":", name)


if __name__ == '__main__':
    first = Car(brand="Honda", color="red")

    first.start_engine()
    first.stop_engine()
    first.switch_gear()
    first.push_brake()

    first.tuning("transmission", "Jatco")
    first.tuning("brakes", "Brembo")
    first.information()
