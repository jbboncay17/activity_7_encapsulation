bold="\033[1m"
red="\033[31m"
end="\033[0m"
green="\033[32m"
blue="\033[34m"
yellow="\033[33m"
from fan_class import Fan
print("")
print(bold+green+"************************FAN CLASS TESTING*********************"+end)
print("")
def test_fan_one():
    fan_one = Fan()
    fan_one.set_speed("fast")
    fan_one.set_on(True)
    fan_one.set_radius(10.0)
    fan_one.set_color("yellow")
    return fan_one


def test_fan_two():
    fan_two = Fan()
    fan_two.set_speed("medium")
    fan_two.set_on(False)
    fan_two.set_radius(5.0)
    fan_two.set_color("blue")
    return fan_two


if __name__ == "__main__":
    fan_one = test_fan_one()
    fan_two = test_fan_two()
    print(bold+blue+"*********FAN ONE*********"+end)
    print(bold+"Speed:", fan_one.get_speed())
    print(bold+"Radius:", fan_one.get_radius())
    print(bold+"Color:", fan_one.get_color())
    print(bold+red+"Is On:", fan_one.get_on())
    print(bold + blue + "*************************" + end)
    print("")
    print(bold + yellow + "*********FAN TWO*********" + end)
    print(bold+"Speed:", fan_two.get_speed())
    print(bold+"Radius:", fan_two.get_radius())
    print(bold+"Color:", fan_two.get_color())
    print(bold+red+"Is On:", fan_two.get_on())
    print(bold + yellow + "*************************" + end)
