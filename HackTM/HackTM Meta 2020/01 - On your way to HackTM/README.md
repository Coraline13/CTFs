# Day 1 - On your way to HackTM

* **Event:** HackTM Meta 2020
* **Category:** Algo
* **Points:** 65
* **Difficulty:** Easy
* **Tools used:** Python

### Description

HackTM is about to start.

Time is not in your favor and you need to get there as soon as possible. You choose to take the bus, so you head over to the pre-established pickup point knowing that the bus is going to leave in the next 5 minutes. Once you get there, the bus driver informs you that there is a traffic jam and he can't guarantee you'll arrive on time for the event.

You decide to avoid the traffic jam by going on foot as it has been a while since your last long distance walk. You reach to your pocket, take out your phone and turn on location on your device.

"No GPS signal".

The driver sees you're starting to panic and hands you a sheet of paper with the route he uses to drive to the event along with some notes:

"You start facing North. Then, following city's grid plan, you walk this path keeping in mind that you can only turn 90 degrees (R)ight or 90 degrees (L)eft and walk the corresponding number of blocks to the next intersection."

Looking over the paper you realize there is no time to walk the streets following such absurd instructions, so you decide to figure out the destination point and find out the shortest path which takes you there.

For example: L2, L2, L2 - takes you 2 steps West, 2 steps South, 2 steps East. That is 2 blocks from your starting point

How far away, measured in blocks, is the HackTM location?

### Attachment

`day1_input.txt`

### Solution

The [grid plan](https://en.wikipedia.org/wiki/Grid_plan) or grid street plan is a type of city plan in which streets run at right angles to each other, forming a grid.    

Following the given path, the shortest distance is a [Manhattan distance](https://en.wikipedia.org/wiki/Taxicab_geometry), which by definition is "The distance between two points measured along axes at right angles".  

The HackTM location, if you follow the shortest path, is 179 blocks away. 

### Flag
 
`179`
 