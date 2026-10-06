class Plant:
    def __init__(self, name: str, height_cm: int, age_days: int) -> None:
        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days

    def show(self) -> None:
        print(f"{self.name}: {self.height_cm}cm, {self.age_days} days old")


def main() -> None:
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    Plant.show(rose)
    Plant.show(sunflower)
    Plant.show(cactus)


if __name__ == "__main__":
    main()
