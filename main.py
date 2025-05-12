
import time

from game_field import GameField

field = GameField(20, 10)

try:
    while True:
        field.handle_input()
        field.render()
        field.update()
        time.sleep(0.2)
except KeyboardInterrupt:
    # TODO: please use either English or Urkainian :)
    print("\nGame over")
    
# TODO: General recomendation - separate logic, classes by modules (python files)