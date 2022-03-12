from __future__ import annotations
from abc import ABC, abstractmethod

class Creator(ABC):
    """
    The Creator class declares the factory method that is supposed
    to return an object of a Product class. The Creator's subclasses 
    usually provide the implementation of this method.
    """

    @abstractmethod
    def factory_method(self):
        """
        Note that the Creator may also provide some default 
        implementation of the factory method.
        """
        pass

    def some_operation(self):
        # call the factory method to create a Product object.
        product = self.factory_method()

        # Now, use the product.
        result = f"Creator: The same creator's code has just worked with {product.operation()}"
        return result

class ConcreteCreator1(Creator):

    def factory_method(self):
        return ConcreteProduct1()

class ConcreteCreator2(Creator):

    def factory_method(self):
        return ConcreteProduct2()

class Product(ABC):
    """
    The Product interface declares the operations that all
    concrete product must implement.
    """

    @abstractmethod
    def operation(self):
        pass

"""
concrete Products provide various implementations of the 
Product interface.
"""

class ConcreteProduct1(Product):
    def operation(self):
        return "Result of the ConcreteProduct1"

class ConcreteProduct2(Product):
    def operation(self):
        return "Result of the ConcreteProduct2"


def client_code(creator: Creator):
    """
    The client code works with an instance of a concrete creator,
    albeit through its base interface. As long as the client keeps
    working with the creator via the base interface, you can pass
    it any creator's subclass.
    """

    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")


if __name__ == '__main__':
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())