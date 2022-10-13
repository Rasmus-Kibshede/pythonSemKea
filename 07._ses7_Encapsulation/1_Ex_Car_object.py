class Car:
    def __init__(self, make, model, bhp, mph):
        self.make = make
        self.model = model
        self.bhp = bhp
        self.mph = mph

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, make):
        if type(make) == str:
            self.__make = make
        else:
            self.__make = None

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if type(model) == str:
            self.__model = model
        else:
            self.__model = None

    @property
    def bhp(self):
        return self.__bhp

    @bhp.setter
    def bhp(self, bhp):
        if type(bhp) == int:
            self.__bhp = bhp
        else:
            self.__bhp = None

    @property
    def mph(self):
        return self.__mph

    @mph.setter
    def mph(self, mph):
        if type(mph) == int:
            self.__mph = mph
        else:
            self.__mph = None


car = Car("Audi", "R8", 500, 1000)

print(car.model)

car.model = 123

print(car.model)