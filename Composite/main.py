from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    """
    The base Component class declares common operations 
    for both simple and complex objects of a composition.
    """

    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        """
        Optionally, the base Component can declare an 
        interface for setting and accessing a parent of the 
        component in a tree structure. It can also provide some 
        default implementation for these methods.
        """

        self._parent = parent

    """
    In some cases, it would be beneficial to define the 
    child-management operations right in the base Component
    class. This way, you won't need to expose any concrete
    implementation details to the client. In this way, the
    base Component class can remain simple, since the client
    doesn't need to know about all possible children
    implementations.
    """

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:
        """
        You can provide a method that lets the client code
        figure out whether a component can bear children.
        """

        return False

    @abstractmethod
    def operation(self) -> str:
        """
        The base Component may implement some default
        behavior or leave it to concrete classes (by
        declaring the method containing the behavior as
        "abstract").
        """

        pass

class Leaf(Component):
    """
    """

    def operation(self) -> str:
        return "Leaf"


class Composite(Component):
    """
    """

    def __init__(self) -> None:
        self._children: List[Component] = []

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        """
        """

        results = []
        for child in self._children: 
            results.append(child.operation())
        return f"Brnach({'+'.join(results)})"


def client_code(component: Component) -> None:
    """
    """
    print(f"RESULT: {component.operation()}", end="")


def client_code2(component1: Component, component2, Component) -> None:
    """
    """

    if component1.is_composite():
        component1.add(component2)

    print(f"RESULT: {component1.operation()}", end="")


if __name__ == "__main__":
    """
    """

    simple = Leaf()
    print("Client: I get a simple component:")
    client_code(simple)
    print("\n")

    tree = Composite()
    b1 = Composite()
    b1.add(Leaf())
    b1.add(Leaf())
    tree.add(b1)
    tree.add(Leaf())
    print("Client: Now I've got a composite tree:")
    client_code(tree)
    print("\n")

    print("Client: I don't need to check the components classes even when managing the tree:")
    client_code2(tree, simple, simple)
    print("\n")