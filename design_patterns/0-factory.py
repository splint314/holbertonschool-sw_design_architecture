#!/usr/bin/env python3

"""Factory pattern using a registry for vehicle creation."""


class Vehicle:
    """Base vehicle class."""

    def mode(self):
        raise NotImplementedError("Subclasses must implement mode()")


class Bus(Vehicle):
    def mode(self):
        return "road"


class Train(Vehicle):
    def mode(self):
        return "rails"


class Bike(Vehicle):
    def mode(self):
        return "lane"


class Scooter(Vehicle):
    def mode(self):
        return "scooter_lane"


class VehicleFactory:
    """Factory using a registry."""

    def __init__(self):
        self._registry = {}

    def register_kind(self, name, cls):
        """Register a new vehicle type."""
        self._registry[name] = cls

    def create(self, kind):
        """Create a vehicle based on kind."""
        if kind not in self._registry:
            raise ValueError(f"Unknown vehicle type: {kind}")
        return self._registry[kind]()


def main():
    factory = VehicleFactory()

    factory.register_kind("bus", Bus)
    factory.register_kind("train", Train)
    factory.register_kind("bike", Bike)

    factory.register_kind("scooter", Scooter)

    print(factory.create("bus").mode())
    print(factory.create("train").mode())
    print(factory.create("bike").mode())
    print(factory.create("scooter").mode())


if __name__ == "__main__":
    main()
