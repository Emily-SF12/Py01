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
        print(f"{self._name}: {self._height_cm:.1f}cm, "
              f"{self._age_days} days old")

    def grow(self, days: int) -> None:
        self._height_cm += days * self._growth

    def age(self, days: int) -> None:
        self._age_days += days


class Flower(Plant):
    def __init__(self, name: str,
                 height_cm: float,
                 age_days: int,
                 growth: float,
                 color: str,
                 is_bloomed: bool) -> None:
        super().__init__(name, height_cm, age_days, growth)
        self._color = color
        self._is_bloomed = is_bloomed

    def bloom(self) -> None:
        self._is_bloomed = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._is_bloomed is False:
            print(f" {self._name} has not bloomed yet")
        else:
            print(f" {self._name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str,
                 height_cm: float,
                 age_days: int,
                 growth: float,
                 trunk_diameter: float) -> None:
        super().__init__(name, height_cm, age_days, growth)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of "
              f"{self._height_cm:.1f}cm",
              f"long and {self._trunk_diameter:.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(self, name: str,
                 height_cm: float,
                 age_days: int,
                 growth: float,
                 harvest_season: str,
                 nutritional_value: int) -> None:
        super().__init__(name, height_cm, age_days, growth)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")

    def grow(self, days: int) -> None:
        super().grow(days)

    def age(self, days: int) -> None:
        super().age(days)
        self._nutritional_value += days


def main() -> None:
    rose = Flower("Rose", 15, 10, 1.2, "red", False)
    oak = Tree("Oak", 200, 365, 2.5, 5)
    tomato = Vegetable("Tomato", 5, 10, 2.1, "April", 0)
    print("=== Garden Plant Types ===")
    print("=== Flower")
    Flower.show(rose)
    print("[asking the rose to bloom]")
    Flower.bloom(rose)
    Flower.show(rose)
    print("\n=== Tree")
    Tree.show(oak)
    print("[asking the oak to produce shade]")
    Tree.produce_shade(oak)
    print("\n=== Vegetable")
    Vegetable.show(tomato)
    print("[make tomato grow and age for 20 days]")
    Vegetable.grow(tomato, 20)
    Vegetable.age(tomato, 20)
    Vegetable.show(tomato)


if __name__ == "__main__":
    main()
