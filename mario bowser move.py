from gamelib import *



  if keys.Pressed[K_LEFT] and mario.left > game.left:
        mario.moveX(-4)
    elif keys.Pressed[K_RIGHT] and mario.right < game.right:
        mario.moveX(4)



  if keys.Pressed[K_LEFT] and bowser.left > game.left:
        bowser.moveX(-4)
    elif keys.Pressed[K_RIGHT] and bowser.right < game.right:
        bowser.moveX(4)
