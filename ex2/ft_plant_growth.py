class Plant:
    def __init__(self, name: str, heigh_cm: float, age_days: int, g_rate: str) -> None:
        self.name = name
        self.heigh_cm = heigh_cm
        self.age_days = age_days
        self.g_rate = g_rate

    def show(self) -> None:
        print(f"{self.name}: {self.heigh_cm:.2f}cm, {self.age_days} days old")

    def grow(self, days: int) -> None:
        growth_by_day: float = 0
        if Plant.g_rate == "slow":
            growth_by_day = 0.8
        elif Plant.g_rate == "medium":
            growth_by_day = 1.1
        elif Plant.g_rate == "high":
            growth_by_day = 1.5
        self.heigh_cm += days * growth_by_day

    def age(self, days: int) -> None:
        self.age_days += days


def print_days(plant: Plant, days: int) -> None:
    print("=== Garden Plant Growth ===")
    d: int = 1
    while days > 0
    print(f"=== Day {d} ===")
    Plant.show(plant)


def main() -> None:
    rose = Plant("Rose", 25, 30, "medium")
    sunflower = Plant("Sunflower", 80, 45, "fast")
    cactus = Plant("Cactus", 15, 120, "slow")
    days: int = 7
    i: int = 1
    print("=== Garden Plant Growth ===")
    while days > 0:
        print_days(rose)


if __name__ == "__main__":
    main()
