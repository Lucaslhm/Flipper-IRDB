Experimental space for trying to capture the region unlock codes from a One For All remote.

Original procedure:
https://www.videohelp.com/dvdhacks/sony-bdp-s5100/12108

Magic 994 is referred to as "key magic" and allows assigning missing functions to a button.
https://www.oneforall.com/en-us/support/faq/urc7955-urc7980-how-can-i-program-missing-function-my-smart-control

# Relevant O4A codes

00189 - SIRC (A:0x00 C:0x7F)

00255 - SIRC (A:0x00 C:0x65)

00095 - SIRC (A:0x00 C:0x55)

00221 - SIRC (A:0x00 C:0x5F)

00079 - SIRC (A:0x00 C:0x15)

# Procedure for programming a key magic code

Hold Magic until LED blinks

Select device (has to roughly match the real world device - use DVD) - LED should blink twice (if not, the device code was rejected)

Enter 994 (two blinks)

Press magic

Enter key magic code

Press the button to assign it to. LED will blink twice.

# Remote Reset

Hold Magic until LED blinks twice

Enter 981

Wait until TV blinks 4 times

# Observations

Key Magic functions manually added will persist until they are replaced with different key magic or the remtoe is reset. *Simply entering a new device code will not replace the key magic functions*

The device that's programmed has an effect on the key magic function that's added.  Examples:

DVD set up as code 1633, button 1 (default) = SIRC20 A:0x093A C:0x00

DVD set up as code 1633, button 1 key magic 00189 = SIRC A:0x00 C:0x7F

DVD set up as code 0741, button 1 (default) = Samsung32 A:0x2D C:0x3B

DVD set up as code 0741, button 1 key magic 00189 = Samsung32 A:0x2D C:0x80

**DVD set up as code 1516, button 1 (default) = SIRC20 A:0x1C5A C:0x00**

**DVD set up as code 1516, button 1 key magic 00189 = SIRC A:0x00 C:0x7F**

DVD set up as code 4009, button 1 does nothing. Power = SIRC20 A:0x12FA C:0x15

DVD set up as code 4009, button 1 key magic 00189 = SIRC20 A:0x12FA C:0x7F

DVD set up as code 0772, button 1 (default) = SIRC20 A:0x093A C:0x00

**DVD set up as code 0864, button 1 (default) = SIRC20 A:0x0A7A C:0x2A**

**DVD set up as code 0864, button 1 key magic 00189 = SIRC20 A:0x0A7A C:0x7F**

DVD set up as code 1033, button 1 (default) = SIRC20 A:0x093A C:0x00

DVD set up as code 1033, button 1 key magic 00189 = SIRC A:0x00 C: 0x7F

# Resources

https://www.eliztech.com/remotes/codelists/sony-dvd-codes-for-ofa
