class Plant:
    def __init__(self,
                 name: str,
                 height_cm: float,
                 age_days: int,
                 growth: float) -> None:
        self._name = name
        self._height_cm: float = 0.0
        self._age_days: int = 0
        self._growth = growth

        if height_cm < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height_cm = height_cm
        if age_days < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age_days = age_days

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height_cm = new_height

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age_days = new_age

    def show(self) -> None:
        print(f"{self._name}: {self._height_cm:.2f}cm, {self._age_days} days old")

    def grow(self, days: int) -> None:
        self._height_cm += days * self._growth

    def age(self, days: int) -> None:
        self._age_days += days


def main() -> None:
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15, 10, 1.2)
    print("Plant created:", end=" ")
    Plant.show(rose)
    print("\n", end="")
    Plant.set_height(rose, 25)
    print(f"Height updated: {rose._height_cm}cm")
    Plant.set_age(rose, 30)
    print(f"Age updated: {rose._age_days} days\n")
    Plant.set_height(rose, -5.2)
    Plant.set_age(rose, -20)
    print(f"\nCurrent state: {rose._name}:", end=" ")
    print(f"{rose._height_cm:.2f}cm, {rose._age_days} days old")


if __name__ == "__main__":
    main()
