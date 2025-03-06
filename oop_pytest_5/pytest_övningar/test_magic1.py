
from magic_box import Magic_box

class Test_magic_box:
    def setup_method (self):
        self.magic_box = Magic_box()
    def test_generate_number(self):
        assert 1 <= self.magic_box.generate_number() <= 6

