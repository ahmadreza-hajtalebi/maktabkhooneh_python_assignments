class animal:
    zoo_name = "zooko"

    def __init__(self, name, species, age, sound):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound
        print(
            f"The {self.name} successfully added to animal with {
                self.species} species and {self.age} year old and his sound is {self.sound}"
        )

    def make_sound(self):
        print(self.sound)

    def info(self):
        return f"here is {animal.zoo_name} and there is {self.name} with {self.species} species and {self.age} year old and his sound is {self.sound}"

    def __str__(self):
        return self.info()


class bird(animal):
    def __init__(self, wing_span, name, species, age, sound):
        super().__init__(name, species, age, sound)
        self.wing_span = wing_span

    def get_wing_span(self):
        print(self.wing_span)

    def sound(self):
        print(self.sound)


l = animal("lion", "savage", 12, "khor")
l.make_sound()
print(l.info())
print(l)
