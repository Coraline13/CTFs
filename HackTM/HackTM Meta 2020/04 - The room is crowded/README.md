# Day 4 - The room is crowded

* **Event:** HackTM Meta 2020
* **Category:** Algo
* **Points:** 163
* **Difficulty:** Medium
* **Tools used:** Python

### Description

As you get your QR code scanned, you find yourself in a hall filled with round tables, cables, hardware, flying sharks, all kinds of unfinished robots running away from the noise while trying to avoid collisions and lots and lots of people.

While trying to find a place to sit, it seems that there are only a few empty seats at the tables. You see a couple of empty spots here and there, but there isn't enough space for you and your team members, which should arrive soon.

You need to find the most effective way to move the other teams around such that there is enough room for yours.

The teams are disposed on a circle. Each team has a certain size, which translates into an arc occupied from that circle. In order to find a place for your team, you might have to move the other teams around. Moving a team of size alpha over an arc beta costs alpha * beta. At no time can two teams overlap. For each team already present on the site you are given the size of the team (the size of the arc they occupy on the circle, in degrees) and the position of the middle of the team on the circle (also in degrees). Fig. 1 exemplifies this.

The input file, namely teams.in, contains a positive integer n on the first line, representing the number of teams on the circle. The next n lines contain two real numbers each: the size and the position of the i-th team. The teams are given in counter clockwise order. Finally, on the last line there is one real number, namely the size of your team.

The solution string is `HackTM{R, X, Y, L}`, where R is the last team you had to push clockwise, your team goes between teams X and Y, and L is the last team you had to push counter-clockwise. If you don't need to push any team in one of the directions just take R = X or L = Y accordingly. Note that team indices start from 1.

The solution for the example would be `HackTM{1, 1, 2, 3}`.

**Note:**

The scoring for this challenge is dynamic.

Make sure you follow the exact flag format (i.e. add whitespace after comma).

### Attachment

`day4.rar`

### Solution

One solution to this problem is to see the cost of inserting your team between any two teams, and pick the minimum out of those.  

To get the best cost when trying to insert your team between teams i and i+1 you will push teams on the left further to the left and teams on the right further to the right to make more space between i and i+1.  

Except for the last push, you will always push teams until they unite with the next team, forming two clusters of teams, one on the left and one on the right. You must keep track of four variables: the space between i and i+1, the size of each cluster and the total cost.  

While the space is smaller than the size of your team you will always push the cluster with the smaller size up to the next team. Afterwards you add the size of that team to the size of the cluster and you increase the space between the clusters by the amount that you pushed. If the space between the last team in a cluster and the next team is more than what you need to fit your team between i and i+1 you only push the exact quantity that you need to push, rather than pushing all the way to the next team. For each push you add the cost of the push (size of the pushed cluster multiplied with the distance between the last team in the cluster and the next team) to the total cost.  

A pitfall is to consider the last team in a cluster as the last team pushed. That is only true for one side, since on the other side you only united your cluster with the last team, but didn't actually push that last team.

### Flag

`HackTM{28 35 36 44}`
