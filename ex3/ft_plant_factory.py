class Plant:
    def __init__(self, name: str, height_cm: float, age_days: int) -> None:
        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days

    def show(self) -> None:
        print(f"{self.name}: {self.height_cm:.2f}cm, {self.age_days} days old")

    def grow(self, days: int) -> None:
        growth_by_day: float = 0
        if self.name == "Cactus":
            growth_by_day = 0.8
        elif self.name == "Rose":
            growth_by_day = 1.1
        elif self.name == "Sunflower":
            growth_by_day = 1.5
        else:
            growth_by_day = 1.0
        self.height_cm += days * growth_by_day

    def age(self, days: int) -> None:
        self.age_days += days


def main() -> None:
    rose = Plant("Rose", 25, 30)
    oak = Plant("Oak", 200, 365)
    cactus = Plant("Cactus", 5, 90)
    sunflower = Plant("Sunflower", 80, 45)
    fern = Plant("Fern", 15, 120)

    plants: list[Plant] = [rose, oak, cactus, sunflower, fern]

    for plant in plants:
        print("Created:", end=" ")
        Plant.show(plant)


if __name__ == "__main__":
    main()
