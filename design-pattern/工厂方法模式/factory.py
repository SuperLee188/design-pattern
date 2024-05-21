from abc import ABC, abstractmethod

# 抽象工厂
class ProductFactory(ABC):
    @abstractmethod
    def produce(self):
        pass

# 具体工厂
class ConcreateProductFactoryA(ProductFactory):
    def produce(self):
        return ConcreateProductA()

class ConcreateProductFactoryB(ProductFactory):
    def produce(self):
        return ConcreateProductB() 


# 抽象产品
class Product(ABC):
    @abstractmethod
    def create(self):
        pass

# 具体产品
class ConcreateProductA(Product):
    def create(self):
        print('create ConcreateProductA')

class ConcreateProductB(Product):
    def create(self):
        print('create ConcreateProductB')


def client_test(creator :ProductFactory):
    p = creator.produce()
    print(type(p))


if __name__ == "__main__":
    p1 = client_test(ConcreateProductFactoryA())
    p2 = client_test(ConcreateProductFactoryB())
