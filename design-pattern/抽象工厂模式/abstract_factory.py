from abc import ABC, abstractmethod

# 抽象工厂
class AbstractFactory(ABC):
    @abstractmethod
    def create_concreate_producta(self):
        pass
    def create_concreate_productb(self):
        pass

# 具体工厂
class ConcreateProduct1(AbstractFactory):
    def create_concreate_producta(self):
        print("ConcreateProduct1 create_concreate_producta")
        return ConcreateProductA1()

    def create_concreate_productb(self):
        print("ConcreateProduct1 create_concreate_productb")
        return ConcreateProductB1()


class ConcreateProduct2(AbstractFactory):
    def create_concreate_producta(self):
        print("ConcreateProduct2 create_concreate_producta")
        return ConcreateProductA2()
    def create_concreate_productb(self):
        print("ConcreateProduct2 create_concreate_productb")
        return ConcreateProductB2()

# 抽象产品A
class AbstarctProductA(ABC):
    @abstractmethod
    def do_something_func1(self):
        pass
# 具体产品A
class ConcreateProductA1(AbstarctProductA):
    def do_something_func1(self):
        print(f"ConcreateProductA1 do_something_func1")

class ConcreateProductA2(AbstarctProductA):
    def do_something_func1(self):
        print(f"ConcreateProductA2 do_something_func1")

# 抽象产品B
class AbstarctProductB(ABC):
    @abstractmethod
    def do_something_func2(self):
        pass
# 具体产品B
class ConcreateProductB1(AbstarctProductB):
    def do_something_func2(self):
        print(f"ConcreateProductB1 do_something_func2")

class ConcreateProductB2(AbstarctProductB):
    def do_something_func2(self):
        print(f"ConcreateProductB2 do_something_func2")

def client(factory: AbstractFactory):

    producta = factory.create_concreate_producta()
    productb = factory.create_concreate_productb()

    producta.do_something_func1()
    productb.do_something_func2()

if __name__ == "__main__":

    client(ConcreateProduct1())
    client(ConcreateProduct2())