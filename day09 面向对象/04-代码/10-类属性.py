"""
对象(实例对象): 通过class定义的类创建的, 即通过类实例化来的, 又称为实例, 实例对象
实例对象定义的属性称为是 实例属性. 通过实例对象(self) 定义的属性都是实例属性
实例属性: 每个实例对象中都存在一份,并且值可能是不一样的

类(类对象): 通过class定义的,又称为 类对象, 是python解释器在创建类的时候自动创建的
作用: 1. 通过类对象,去定义实例对象   2. 类对象可以保存一些属性信息,称为类属性
类属性的定义: 在类内部,方法外部定义的变量就是类属性
类属性,字内存中只有一份

如何确定一个属性是该定义为实例属性还是类属性?
先假设这个属性为实例属性,查看这个属性值对于不同的实例对象, 属性值是否都一样,并且需要同时变化.
如果是, 则可以定义为类属性
如果不是,则可以定义为实例属性
"""


class Dog(object):
    # 定义类属性, 类名
    class_name = '狗类'

    def __init__(self, name, age):
        # 定义的都是实例属性
        self.name = name
        self.age = age


# 创建Dog 类对象
dog = Dog('大黄', 2)
# print(dog.__dict__)  # 打印dog对象具有的属性

# 类名.__dict__  查看类对象具有的属性
# print(Dog.__dict__)

# 访问类属性
# 类名.类属性
print(Dog.class_name)

# 修改类属性  类名.类属性 = 属性值
Dog.class_name = 'Dog类'

print(Dog.class_name)

# 补充, 注意: 如果不存在和实例属性名相同的类属性.则可以使用实例对象访问类属性的值
# 如果存在重名,则使用实例属性访问的一定是实例属性,不是类属性
print(dog.class_name)
