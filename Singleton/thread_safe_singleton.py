from threading import Lock, Thread

class SingletonMeta(type):
    """
    This is the thread-safe implementation of singleton.
    """

    _instances = {}

    _lock: Lock = Lock()
    """
    We now have a lock object that will be used to
    synchronize threads during first access to the 
    Singleton.
    """

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__`
        argument do not affect the returned instance.
        """
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
            return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    value: str = None
    """
    We'll use this property to prove that our
    Singleton really works.
    """

    def __init__(self, value: str) -> None:
        self.value = value
    
    def some_business_logic(self):
        """
        Finally, any singleton should define some
        business logic, which can be executed on its
        instance.
        """
        pass

def test_singleton(value: str) -> None:
    singleton = Singleton(value)
    print(singleton.value)

if __name__ == "__main__":
    # The client code

    print("If you see the same value, then singleton was resused (yay!)\n"
    "if you see different values,"
    "then 2 singletons were created (booo!) \n\n"
    "Result: \n")

    process1 = Thread(target=test_singleton, args=("FOO",))
    process2 = Thread(target=test_singleton, args=("BAR",))
    process1.start()
    process2.start()