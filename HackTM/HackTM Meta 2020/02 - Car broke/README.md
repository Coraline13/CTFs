# Day 2 - Car broke

* **Event:** HackTM Meta 2020
* **Category:** Algo
* **Points:** 127
* **Difficulty:** Medium
* **Tools used:** Python

### Description

Rushing to the location, with one eye on the sidewalk and the other on the instructions, you notice that there are way too many cars heading in that direction. You choose to ignore that for the moment but, as you look across the road, you notice a keyboard. Then a monitor. There is a group of youngsters heading in the same direction as you do and their backpacks are overfilled with cables and gadgets. They must have gotten tired of waiting in the bus station and caught up with you.

As you continue to navigate through the instructions you suddenly hear a "Ding!" coming out of your pocket. The internet connection is back on! Thinking that Starlink is good at something, you check your notifications and see that one of them is from HackTM. It says that you can join HackTM Carpool group, which you do without thinking. In a moment a car stops near you and someone calls you by your name. You soon realize that most of the traffic is filled with participants rushing to the event. You hop in and your day gets finally better!

You start chatting and suddenly there's smoke coming out from under the hood. "Everyone out", says the driver! You start investigating to see if it can be fixed and some other people stop and offer their help. Fortunately, one car is full with hardware so the probability of finding something useful through all that stuff is very high.

Word spreads on the Carpool group and an automotive engineer contacts you from the event hall. You explain the problem and it looks like he can help. All you need to do is to follow the instructions he sent.

As soon as you receive the instructions, something seems to be wrong. In a rush, the engineer who wanted to help did not have enough time to send you the complete order in which you need to place the components. Instead, he wrote whether or not one piece must be installed before another. If there is more than one component available, then their order is taken alphabetically.

**Example:**

Install Intake before installing GudgeonPin component. Install Intake before installing LightSensor component. Install GudgeonPin before installing Heater component. Install GudgeonPin before installing Joints component. Install Heater before installing KnockSensor component. Install Joints before installing KnockSensor component. Install LightSensor before installing KnockSensor component.

For the example above, you need to first install the Intake component, as it is the only one available. Its completion frees the installation for GudgeonPin and LightSensor. As GudgeonPin is the first in alphabetical order, it is the next one to be installed. Now there are 3 components which can be installed: LightSensor, Heater and Joints. As Heater is the first in alphabetical order, it is the next one to be installed. This leaves only 2 options available, LightSensor and Joints, as KnockSensor is still blocked by the previous two. Then Joints is installed and after that the LightSenor and finally, after all the its conditions have been met, the KnockSensor. The solution for this example is: Intake, GudgeonPin, Heater, Joints, LightSensor, KnockSensor.

What is the correct order in which you need to install the components?

**Note:**

By solving this challenge you will be awarded with 127 points.

### Attachment

`day2_input.txt`

### Solution

This is a [topological sorting](https://www.geeksforgeeks.org/topological-sorting) challenge. What one needs to pay attention to, is that the components are taken alphabetically if more than one is currently available.

### Flag
 
`DriveBelt, FanBelt, OverflowTank, Q3Screw, Piston, TimingTape, EngineBlock, LicencePlate, AirDuct, YOilTube, Radiator, ValveSpring, UniversalJoint, MainHarness, XShapedJoint, Heater, KnockSensor, WaterPump, StarterMotor, GudgeonPin, ZincAnode, BrakePiston, Camshaft, Joints, Intake, NeutralSafetySwitch`
