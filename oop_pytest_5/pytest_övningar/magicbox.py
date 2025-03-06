#Övning 6: Skapa en klass MagicBox som testar slumpmässighet

import random

class MagicBox:
    def roll_dice(self):
        return random.randint(1, 6)