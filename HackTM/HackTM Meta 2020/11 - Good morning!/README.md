# Day 11 - Good morning!

* **Event:** HackTM Meta 2020
* **Category:** 
* **Points:** 308
* **Difficulty:** 
* **Tools used:** 

### Description

Sun shines over your head as you survived the challenges of the night. It is the morning of your last day here at HackTM and you need to refill your energy bar as soon as possible to maintain the advantage gained in the last hours. Nothing does this better than a good cup of coffee, so you go and grab one.  

As you head back to your table, you trip over an extension cord. Good reflexes save you from falling, but your coffee slips out of your hand and it gets spilled all over your laptop. Someone else must have found the Chest of Electricity, because the extension cord was not there when you left.  

You quickly clean your laptop and, although it is still working, you are unable to access any of its files. It looks like the coffee messed with your computer's memory. The more you type, the more sticky your fingers get and the laptop soon becomes unusable.  

Disassemble the computer and analyze the memory to see how it got encrypted.

**Note:**

The scoring for this challenge is dynamic.

When you’ll find the flag, it will be obvious. Do not try to submit a possible answer by placing it in between curly brackets using the flag format `HackTM{your_answer}`.

### Attachment

`day11.zip`

### Solution

The challenge provided the players with 1 files: `ENCRYPTOR.elf` (a 64-bit Linux executable)

The goal of the challenge was to disassemble the executable and understand the algorithms used to encrypt the flag.  

The encrypted flag was in the binary.  

The players had to reverse the encryption algorithm and decrypt the flag.

### Flag

`HackTM{do_you_pour_your_milk_in_first_or_last?}`
