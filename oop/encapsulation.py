class Car:

    def __init__(self):
        self.__updateSoftware()

    def drive(self):
        print('driving')

    def __update_software(self):
        print('updating software')


red_car = Car()
red_car.drive()
# red_car.__updateSoftware()  not accessible from object.
