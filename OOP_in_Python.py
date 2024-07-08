
# Task 1
class Country:
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population

    def add(self, other):
        if isinstance(other, Country):
            other.population = self.population + other.population
            other.name = f"{self.name} {other.name}"
            return Country(other.name, other.population)
        else:
            raise ValueError("Can only add Country objects together")

    def __str__(self):
        return f"Name: {self.name}, population: {self.population}"


if __name__ == "__main__":
    bosnia = Country("Bosnia", 10_000_000)
    herzegovina = Country("Herzegovina", 5_000_000)
    bosnia_herzegovina = bosnia.add(herzegovina)
    print(bosnia_herzegovina)
    
#Task 2
class Country:
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population

    def __add__(self, other):
        if not isinstance(other, Country):
            raise ValueError("Can only add Country objects together")

        other.name = f"{self.name} {other.name}"
        other.population = self.population + other.population
        return Country(other.name, other.population)

    def __str__(self):
        return f"Name: {self.name}, population: {self.population}"


if __name__ == "__main__":
    bosnia = Country("Bosnia", 10_000_000)
    herzegovina = Country("Herzegovina", 5_000_000)
    bosnia_herzegovina = bosnia + herzegovina
    print(bosnia_herzegovina)

#Task 3
class Car:
    def __init__(self, brand: str, model: str, year: int, speed: int):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self, num):
        self.speed += num

    def brake(self, num):
        self.speed -= num

    def __str__(self):
        return f"Car: {self.brand} {self.model}, Year: {self.year}, Speed: {self.speed}"


if __name__ == "__main__":
    MAZDA = Car("Mazda", "CX-5", 2012, 60)
    RANGE_ROVER = Car("Range Rover", "SV", 2023, 80)

    while True:
        try:
            type_car_ride = input(
                "Choose your car ride - city or track (or type 'exit' to quit): "
            )
            if type_car_ride == "exit":
                break
            elif type_car_ride == "city":
                MAZDA.brake(5)
                RANGE_ROVER.brake(5)
            elif type_car_ride == "track":
                MAZDA.accelerate(5)
                RANGE_ROVER.accelerate(5)
            else:
                print("Invalid input. Please choose 'city' or 'track'")

            print(MAZDA)
            print(RANGE_ROVER)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

#Task 4
class Robot:
    def __init__(self, orientation, position_x, position_y):
        self.orientation = orientation
        self.position_x = position_x
        self.position_y = position_y

    def move(self, steps):
        if self.orientation == "up":
            self.position_y += steps
        elif self.orientation == "down":
            self.position_y -= steps
        elif self.orientation == "left":
            self.position_x -= steps
        elif self.orientation == "right":
            self.position_x += steps

    def turn(self, direction):
        if direction == "left":
            directions = ["up", "left", "down", "right"]
        elif direction == "right":
            directions = ["up", "right", "down", "left"]

        current_index = directions.index(self.orientation)
        self.orientation = directions[(current_index + 1) % 4]

    def display_position(self):
        print(
            f"Position: ({self.position_x}, {self.position_y}), Orientation: {self.orientation}"
        )


if __name__ == "__main__":
    robot = Robot(orientation="up", position_x=0, position_y=0)
    robot.display_position()
    robot.move(3)
    robot.turn("right")
    robot.move(2)
    robot.display_position()