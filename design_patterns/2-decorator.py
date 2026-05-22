#!/usr/bin/env python3

class CaramelDecorator:
    def __init__(self, inner):
        self._inner = inner

    def cost(self):
        return self._inner.cost() + 15

    def description(self):
        return self._inner.description() + " + caramel"
