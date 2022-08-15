## Control your PixMob wristbands via IR!

These IR codes were generated based on the reverse engineering work detailed here: [https://github.com/danielweidman/pixmob-ir-reverse-engineering](https://github.com/danielweidman/pixmob-ir-reverse-engineering). They can be used to make PixMob wristbands display various colors and do various light effects.

See demo video here: https://github.com/danielweidman/flipper-pixmob-ir-codes

### Files
1. `PixMob_main.ir`: Codes to set bracelets to any common color, and fade in or out of each color
2. `PixMob_all_colors.ir`: Codes to set bracelets to every possible color (with what reverse-engineering has found so far), but without the fade effects
3. `PixMob_special.ir`: Special codes to do things like random colors, enter motion sensitive mode on very old PixMob bracelets, and more. It is easy to mess up bracelets using these codes because some have persistent effects. I don't recommend using this unless you are willing to mess up your bracelet and require a difficult reset.

I recommend `PixMob_main.ir` as a starting place.
