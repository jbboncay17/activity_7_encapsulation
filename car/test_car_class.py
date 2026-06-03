bold="\033[1m"
red="\033[31m"
end="\033[0m"
green="\033[32m"
blue="\033[34m"
yellow="\033[33m"

from car_class import Car
print(bold+green+"************CAR CLASS TEST************"+end)
print("")
def test_car():
    car = Car(2023,"Toyota")
    return car

if __name__ == "__main__":
    car = test_car()

    print(bold+blue+"************ACCELERATING************:"+end)
    for i in range(5):
        car.accelerate()
        print(bold+red+"Current Speed:"+end, car.get_speed())
    print("")
    print(bold+yellow+"************BRAKING************"+end)
    for i in range(5):
        car.brake()
        print(bold+red+"Current Speed:"+end, car.get_speed())
