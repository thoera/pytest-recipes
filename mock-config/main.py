from omegaconf import OmegaConf


class AnimalFilter:
    def __init__(self) -> None:
        self.config = OmegaConf.load("config.yaml")
        OmegaConf.set_readonly(self.config, True)

    def filter_animals(self) -> list:
        print("Filter the animals:")
        return [animal for animal in self.config.animal if len(animal) > 3]


if __name__ == "__main__":
    animals = AnimalFilter()
    print(animals.filter_animals())
