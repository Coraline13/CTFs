# Day 12 - 

* **Event:** HackTM Meta 2020
* **Category:** Steganography
* **Points:** 244
* **Difficulty:** Medium
* **Tools used:** -

### Description

It’s brunch time and you’re feeling tired and bored and tired and don’t really know what to do with your life. All this disassembling procedure got you on edge, so you decide to take a break and socialize, for a change.  

Rumor has it, one can find really cool swag at Flex’s sponsor booth.

**Note:**

The scoring for this challenge is dynamic.

When you’ll find the flag, it will be obvious. Do not try to submit a possible answer by placing it in between curly brackets using the flag format `HackTM{your_answer}`.

### Attachment

none

### Solution

This is a steganography challenge.  

The sponsor booth can be found on HackTM site at the [sponsors page](https://2020.hacktm.ro/sponsors).

There is a big and obvious logo which is Flex’s. At first, there seems nothing wrong about it, but if you inspect it with a Hex editor you may find that at the end of the .png file there is somethig more. The end of a .png can be found by searching for `'IEND'`. After you found it, skip the next 4 bytes until you reach `'PK'`, which are the initials of Phil Katz, the invertor of the Zip file. One can also observe that there is a `'psst.txt'` file at the end of the .png.  

Create a new file with the remaining bytes, starting with `'PK'`, and save it with the .zip extension. Open it and you will find your flag.

### Flag

`HackTM{!oh_no!_ign0re_m3_IamA_r0b0t_bl33p_bl00p}`
