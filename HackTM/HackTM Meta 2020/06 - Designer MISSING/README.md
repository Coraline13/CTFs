# Day 6 - Designer MISSING

* **Event:** HackTM Meta 2020
* **Category:** 
* **Points:** 137
* **Difficulty:** Hard
* **Tools used:** [RSA decryption tool](https://www.devglan.com/online-tools/rsa-encryption-decryption)

### Description

Yess, your awesome project idea looks like a winner. You’re sure no other team can compete with it. You chose the best frameworks, it will work on the web, Android, iOS AND Windows Phone with a single codebase. Who can stop you now?

You all start coding and coding and deploying. As the first build goes up, your eye catches the screen of another team and you FREEZE. Their app has no real features but looks AMAZING. Beautiful lines, minimal and environmentally friendly logo... if they code half as well as you, they’ll still sell better.

In desperation, you realize you need a designer to pimp your defaults.

They made you sign an NDA, but in the end the organisers selflessly gave you a list with all event participants so you can find an available designer yourself. Your job is to find the one who goes by a nickname.

**Note:**

The format of the flag is `HackTM{nickname}`.

The scoring for this challenge is dynamic.

When you’ll find the flag, it will be obvious. Do not try to submit a possible answer by placing it in between curly brackets using the flag format `HackTM{your_answer}`.

### Attachment

`day6_input.csv`

### Solution

You need to look for a designer. So you filter the dataset by `'Profession'`, where profession is 'Designer'. This only leaves 5 entries.  

All designers have missing values in the `'Age'` column. Therefore, the 'MISSING' written in capitals from the title.  

Although the values are missing, these `'designers'` are quite popular (i.e. Bruce Willis) and you can easily find their age with a quick google search.  
 
After the missing part has almost been handled, you have a hint saying that it likes ASCII. Their ages converted to ASCII characters form the string `'ACHKT'`.  

Sorting the data alphabetically by `'FirstName'` reorders the letters and `'ACHKT'` becomes `'HACKT'`, whick is almost the name of the event you are taking part in. `M` is MISSING. `M` is `77`.  

There is a group of people having the age `77`. They are a bit old considering that `77` years ago, the world's first electronic digital programmable computer, named Colossus, was made.  

Sort (alphabetically) this group of people as well.  

You are left with 2 groups of people: one forming `'HACKT'` and one having the age of `77`. Their invitation codes are base64 strings, and RSA encryption could be a good guess.  
 
Concatenate the invitation codes from the first group to get your encrypted flag.  

Concatenate the invitation codes from the latter one to get your private key.  

Use a free online RSA decryption tool to get your flag.

### Flag
 
`HackTM{J4ke_P3ral7a_d3tect!ve_sl4sh_g3nius}`
 