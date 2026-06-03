bold="\033[1m"
red="\033[31m"
end="\033[0m"
green="\033[32m"
blue="\033[34m"
yellow="\033[33m"

from car_class import Car

def test_car():
    car = Car(2023,Toyota):
    return car

if __name__ == "__main__":
    car = test_car()

    print("Accelerating:")
    for i in range(5):
        car.accelerate()
        print("Current Speed:", car.get_speed())

    print("\nBraking:")
    for i in range(5):
        car.brake()
        print("Current Speed:", car.get_speed())