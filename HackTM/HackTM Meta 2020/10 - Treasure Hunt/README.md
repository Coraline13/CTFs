# Day 10 - Treasure Hunt

* **Event:** HackTM Meta 2020
* **Category:** 
* **Points:** 123
* **Difficulty:** 
* **Tools used:** 

### Description

As you type in the portal's activation code and hit 'Enter', the Earth splits beneath your feet with a terrifying noise and you start falling into the darkness.  

Your head hits a hard and cold surface and your hands smash into the edges of the table making a mess as you experience a hypnic jerk. Realizing that you zoned out and it was all a dream, you start rearranging the stuff you just scattered all over the table. Looking around, you see that most of the players are resting but you need to finish your project.  

After some Google searches, you still need some information that is nowhere to be found on the internet. Luckily, we have the Tome of Knowledge device, the only device that holds all the information known to mankind. You rush to it, press the power up button and nothing happens. The first thing you do, after pressing the power up button repeatedly, is to check its power supply. Looking behind it, the extension cord used to supply the Tome of Knowledge device with electrical power is missing. Somebody took it!  

Suddenly the room gets dark and the emergency lights turn on. Emerged in your thoughts, you totally forgot about the midnight Treasure Hunt.

On a giant screen, the Treasure Hunt's objective appears: The Chest of Electricity, filled with extension cords. One by one, the other participants start leaving their seats in search for the chest. You are not the only one in need of an extension cord. With the organizers nowhere to be found, you rush to the Info Point where you find a message on a post-it with an arrow pointing to a locked door and some text.

"We know what you are looking for.  
They're in a crate, behind that door.  
Placed to your left, there is a screen,  
The eye is sharp, the eye is keen,  
But it can't catch the word it sees  
Which, at some point, it seems to freeze.  
And in a blink, nothing makes sense  
As symbols mingle, start to dance.  
Oh wait, you see that word again,  
Can you keep up with your geek brain?  
The symbols move too fast on glass,  
And if you blink, you shall not pass!"  

Near the screen you find a piece of paper. They look like coordinates, one point per line. It also has some instructions.  

You need to freeze time at the right moment and submit the message that appears in order to unlock the door and reach the Chest of Electricity.

**Note:**

The scoring for this challenge is dynamic.

Submit your solution in the following format: `HackTM{message}`

### Attachment

`day10_input.txt`
`day10_instructions.txt`

### Solution

They key to this challenge is to find the exact moment in which the points align on the screen and form a readable message. If you do not stop the execution of your code at that exact moment, the points will continue moving and you will not be able to see the word they form. You can assume that the word fits in a rectangle and when the length of the rectangle is the smallest, then you can see the message. In this case, after 2020 steps, the points form the word `"HACK"`.

### Flag

`HackTM{HACK}`
