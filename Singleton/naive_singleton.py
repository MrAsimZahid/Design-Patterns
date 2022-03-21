# Naive Singleton implementation

class SingletonMeta(type):
    """
    The Singleton class could be implemented in 
    different ways in python. Some possible methods
    include: base class. decorator, metaclass. We 
    will use metaclass because it is best suited for
    this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__`
        arguments do not affect the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        """
        Finally, any singleton should define some 
        business logic, which can be executed on its
        instance.
        """
        pass
if __name__ == '__main__':
    # The client code

    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, both vaiables contain the same instance.")
    else:
        print("Singleton failed, variable contain different instances.")
