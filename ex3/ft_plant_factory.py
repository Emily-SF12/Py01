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


def main() -> None:
    rose = Plant("Rose", 25, 30, 1.2)
    oak = Plant("Oak", 200, 365, 2.3)
    cactus = Plant("Cactus", 5, 90, 0.4)
    sunflower = Plant("Sunflower", 80, 45, 1.5)
    fern = Plant("Fern", 15, 120, 0.3)

    plants: list[Plant] = [rose, oak, cactus, sunflower, fern]

    for plant in plants:
        print("Created:", end=" ")
        Plant.show(plant)


if __name__ == "__main__":
    main()
