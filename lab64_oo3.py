class Car:
    vendor ='Lexus'
    valid = True

Car.function = True
print(Car.vendor,Car.valid,Car.function)
myCar =Car()
myCar.color = 'red'
print(myCar.color,myCar.vendor,myCar.valid,myCar.function)

yourCar = Car()
yourCar.capacity = 7
print(yourCar.capacity,yourCar.vendor,yourCar.valid,yourCar.function)
Car.max = 10000
print(Car.max,myCar.max,yourCar.max)