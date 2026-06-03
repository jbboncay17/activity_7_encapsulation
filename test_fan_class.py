from fan_class import Fan

def test_fan_one(Fan):
    fan_one = Fan()
    fan_one.set_speed('fast')
    fan_one.set_is_on(True)
    fan_one.set_radius(10.0)
    fan_one.set_color('yellow')
    return fan_one