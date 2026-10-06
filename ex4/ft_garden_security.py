class Plant:
    def __init__(self, name: str, height_cm: float, age_days: int) -> None:
        self.name = name
        self._height_cm: float = 0.0
        self._age_days: int = 0
        if height_cm < 0:
            print(f"{name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height_cm = height_cm
        if age_days < 0:
            print(f"{name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age_days = age_days

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height_cm = new_height

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age_days = new_age

    def show(self) -> None:
        print(f"{self.name}: {self._height_cm:.2f}cm, {self._age_days} days old")

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
        self._height_cm += days * growth_by_day

    def age(self, days: int) -> None:
        self._age_days += days


def main() -> None:
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15, 10)
    print("Plant created:", end=" ")
    Plant.show(rose)
    print("\n", end="")
    Plant.set_height(rose, 25)
    print(f"Height updated: {rose._height_cm}cm")
    Plant.set_age(rose, 30)
    print(f"Age updated: {rose._age_days} days\n")
    Plant.set_height(rose, -5.2)
    Plant.set_age(rose, -20)
    print(f"\nCurrent state: {rose.name}:", end=" ")
    print(f"{rose._height_cm:.2f}cm, {rose._age_days} days old")


if __name__ == "__main__":
    main()
