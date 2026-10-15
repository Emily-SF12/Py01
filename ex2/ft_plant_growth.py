class Plant:
    def __init__(self,
                 name: str,
                 height_cm: float,
                 age_days: int,
                 growth: float) -> None:
        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days
        self.growth = growth

    def show(self) -> None:
        print(f"{self.name}: {self.height_cm:.1f}cm, {self.age_days} days old")

    def grow(self, days: int) -> None:
        self.height_cm += days * self.growth

    def age(self, days: int) -> None:
        self.age_days += days


def print_days(plant: Plant, days: int) -> None:
    init_size: float = plant.height_cm
    print("=== Garden Plant Growth ===")
    Plant.show(plant)
    for day in range(1, days + 1):
        print(f"=== Day {day} ===")
        Plant.grow(plant, 1)
        Plant.age(plant, 1)
        Plant.show(plant)
    print(f"Growth this week: {plant.height_cm - init_size:.1f}")


def main() -> None:
    rose = Plant("Rose", 25, 30, 0.8)
    print_days(rose, 7)
    # sunflower = Plant("Sunflower", 80, 45, 1.2)
    # print_days(sunflower, 7)
    # cactus = Plant("Cactus", 15, 120, 0.4)
    # print_days(cactus, 7)


if __name__ == "__main__":
    main()
