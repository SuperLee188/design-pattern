from threading import Lock, Thread

class Singleton(type):
    """
    python中所有的类都是由type类创建的。
    可以使用type()函数并指定类名、父类（多个父类组成元组）以及类的属性和方法等信息来动态创建一个新类。
    元类的__call__方法用于创建类的实例。
    在__call__方法中，首先检查当前类是否已经在_instances字典中，如果不在，则通过调用父类的__call__方法创建一个实例，并将其添加到_instances字典中。
    如果类已经在_instances字典中，则直接返回该实例。
    """
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class MySingleton(metaclass=Singleton):
    def do_something(self):
        pass


class ThreadSafeSingleton(type):
    _instance = {}
    _lock = Lock()  # 互斥锁
    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instance:
                instance = super().__call__(*args, **kwargs)
                cls._instance[cls] = instance
        return cls._instance[cls]

class MyThreadSafeSingleton(metaclass=ThreadSafeSingleton):

    def __init__(self, value) -> None:
        self.value = value
    
    def do_something(self):
        pass


def test_singleton(value):
    singleton = MyThreadSafeSingleton(value)
    print(singleton.value)


if __name__ == "__main__":
    s1 = MySingleton()
    s2 = MySingleton()
    if id(s1) == id(s2):
        print("Singleton works")
    else:
        print("Singleton failed")

    # 如果输出了不同的值，说明单例模式实现有问题
    process1 = Thread(target=test_singleton, args=("p1",))
    process2 = Thread(target=test_singleton, args=("p2",))
    process1.start()
    process2.start()

    process1.join()
    process2.join()

