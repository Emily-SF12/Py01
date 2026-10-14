class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grows = 0
            self._ages = 0
            self._shows = 0

        def add_grow(self) -> None:
            self._grows += 1

        def add_age(self) -> None:
            self._ages += 1

        def add_show(self) -> None:
            self._shows += 1

        def display(self) -> None:
            print(f"Stats: {self._grows} grow, {self._ages} age, "
                  f"{self._shows} show")

    def __init__(self,
                 name: str,
                 height_cm: float,
                 age_days: int,
                 growth: float) -> None:
        self._name = name
        self._height_cm: float = 0.0
        self._age_days: int = 0
        self._growth = growth
        self.stats = Plant.Stats()
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
        self.stats.add_show()
        print(f"{self._name}: {self._height_cm:.1f}cm, "
              f"{self._age_days} days old")

    def grow(self, days: int, grow_cm: float) -> None:
        self.stats.add_grow()
        if days == 0:
            self._height_cm += grow_cm
        else:
            self._height_cm += days * self._growth

    def age(self, days: int) -> None:
        self.stats.add_age()
        self._age_days += days

    @staticmethod
    def is_older_than_a_year(age_days: int) -> bool:
        return age_days > 365

    @classmethod
    def unknown_plant(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0, 0.0)


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


class Seed(Flower):

    def __init__(self, name: str,
                 height_cm: float,
                 age_days: int,
                 growth: float,
                 color: str,
                 is_bloomed: bool,
                 seeds: int) -> None:
        super().__init__(name, height_cm, age_days, growth, color, is_bloomed)
        self.seeds = seeds

    def bloom(self) -> None:
        super().bloom()
        self.seeds += 42

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seeds}")


class Tree(Plant):
    class TreeStats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shades = 0

        def add_shade(self) -> None:
            self._shades += 1

        def display(self) -> None:
            super().display()
            print(f" {self._shades} shade")

    stats: "Tree.TreeStats"

    def __init__(self, name: str,
                 height_cm: float,
                 age_days: int,
                 growth: float,
                 trunk_diameter: float) -> None:
        super().__init__(name, height_cm, age_days, growth)
        self.stats = Tree.TreeStats()
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        self.stats.add_shade()
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

    def grow(self, days: int, grow_cm: float) -> None:
        super().grow(days, grow_cm)

    def age(self, days: int) -> None:
        super().age(days)
        self._nutritional_value += days


def main() -> None:
    rose = Flower("Rose", 15, 10, 1.2, "red", False)
    oak = Tree("Oak", 200, 365, 2.5, 5)
    sunflower = Seed("Sunflower", 80.0, 45, 1.5, "yellow", False, 0)
    anonymous = Plant.unknown_plant()

    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_a_year(30)}")
    print(f"Is 400 days more than a year? -> "
          f"{Plant.is_older_than_a_year(400)}")
    print("\n")
    print("=== Flower")
    rose.show()
    print("[statistics for Rose]")
    rose.stats.display()
    print("[asking the rose to grow and bloom]")
    rose.grow(0, 8.0)
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    rose.stats.display()
    print("\n")
    print("=== Tree")
    oak.show()
    print("[statistics for Oak]")
    oak.stats.display()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    oak.stats.display()
    print("\n")
    print("=== Seed")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.age(20)
    sunflower.grow(20, 0)
    sunflower.bloom()
    sunflower.show()
    print("[statistics for Sunflower]")
    sunflower.stats.display()
    print("\n")
    print("=== Anonymous")
    anonymous.show()
    print("[statistics for Unknown plant]")
    anonymous.stats.display()


if __name__ == "__main__":
    main()
