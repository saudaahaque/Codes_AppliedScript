from magicbox import MagicBox

def test_dice():
    assert 1 <= MagicBox().roll_dice() <= 6

