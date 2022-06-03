"""
Using @property decorator to write a getter/setter vs. writing a getter/setter function by hand


python -m timeit -s "from descriptors import test_custom_descriptors" "test_custom_descriptors()"
161 nsec
python -m timeit -s "from descriptors import test_descriptors" "test_descriptors()"
155 nsec

Almost no difference
"""


class CustomDescriptors():
    def __init__(self):
        self._value = 10

    def get_value(self):
        return self._value

    def set_value(self, new_value):
        self._value = new_value

class BuiltinDescriptors():
    def __init__(self):
        self._value = 10

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

cd = CustomDescriptors()
def test_custom_descriptors():
    cd.get_value()
    cd.set_value(20)

bd = BuiltinDescriptors()
def test_descriptors():
    bd.value
    bd.value = 20
