from __future__ import annotations
from abc import ABC, abstractmethod


class Abstraction:
    """
    The Abstraction defines the interface for the 
    "control" part of the two class hierarchies. It 
    maintains a reference to an object of the 
    Implementation hierarchy and delegates all of the
    real work to this object.
    """

    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation

    def operation(self) -> str:
        return (f"Abstraction: Base operation with:\n"
        f"{self.implementation.operation_implementation()}")

class ExtendedAbstraction(Abstraction):
    """
    You can extend the Abstraction without changing the 
    Implementation classes.
    """

    def operation(self) -> str:
        return (f"ExtendedAbstraction: Extended operation with:\n"
        f"{self.implementation.operation_implementation()}")

class Implementation(ABC):
    """
    """

    @abstractmethod
    def operation_implementation(self) -> str:
        pass


"""
Each Concrete Implementation corresponds to a specific platform
and implements the Implementation interface using that platform's 
API. 
"""

class ConcreteImplementationA(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationA: Here's the resulr on the platform A."


class ConcreteImplementationB(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementaionB: Here's the result on the platform B."

def client_code(abstraction: Abstraction) -> None:
    """
    Except for the initialization phase, where an Abstraction
    object gets linked with a specific Implementation object, 
    the client code should only depend on the Abstraction 
    class. This way the client code can support any 
    abstraction-implementation combination.
    """

    print(abstraction.operation(), end="")
    

if __name__ == "__main__":
    """
    The client code should be able to work with any 
    pre-configured abstraction-implementation combination. 
    """

    implementation = ConcreteImplementationA()
    abstraction = Abstraction(implementation)
    client_code(abstraction)

    print("\n")

    implementation = ConcreteImplementationB()
    abstraction = ExtendedAbstraction(implementation)
    client_code(abstraction)
