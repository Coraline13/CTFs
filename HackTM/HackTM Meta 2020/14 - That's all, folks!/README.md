# Day 14 - That's all, folks!

* **Event:** HackTM Meta 2020
* **Category:** Steganography
* **Points:** 275
* **Difficulty:** hard
* **Tools used:** base64 decoder/encoder

### Description

After a couple of days of emotional roller coaster, this HackTM edition comes to an end. Everyone goes from table to table to see what cool projects the other teams made in this time.

The MC walks on stage to hold a wrap up speech and to congratulate the participants. Before she finishes, a round of applause from a group of overly enthusiastic people interrupts her speech and, next thing you know, she gets down from the stage without you hearing what she said.

What does the MC say? :)

**Note:**  

The scoring for this challenge is dynamic.

There is no flag format. You just need to submit your answer as you find it.

### Attachment

`day14_input.zip`

### Solution

Another steganography challenge. 

Decoding the **base64** input, there are two quotes from Edward Snowden. The first quote is about the nothing to hide argument, while the second one is about technological tyranny. 
Although there is something hidden, it can only be seen if you reencode the text.
The first anomaly appears while decoding and encoding the third line:

**input:**  
`dG8gc3VycmVuZGVyIHlvdXIgb3duIHByaXZhY3kgaXMgcmVhbGx5IHRvIHN1cnJlbmRlciB=`  
**decode:**  
`to surrender your own privacy is really to surrender`  
**reencode:**  
`dG8gc3VycmVuZGVyIHlvdXIgb3duIHByaXZhY3kgaXMgcmVhbGx5IHRvIHN1cnJlbmRlciA=`

The last character before `'='` is `'B'` in your input. After decoding and encoding it again, `'B'` becomes `'A'`. 
Base64 encoding is done by splitting the original text in groups of 3 characters, which are represented on 8 bits (=24 bits), in 4 characters encoded on 6 bits. If at the end the last group from the original text has 2 characters we have: 2chars x 8bits (=16bits), encoded by 3 x 6bit chars (=18 bits) and the `'='` character is added.

Notice the difference of 2 bits from original vs encoded? That's right, those 2 bits is where the magic happens.

**For example:**  
```
c      i      B      =
011100 100010 000001 ======
01110010 00100000 01 ======
r        (space)  ^^
	 hidden bits
```  

**Note:** `'surrender '` - there is a space after `'surrender'`, so the last 2 chars are `'r'` and `' '`.

The same rules apply to the lines with `"=="` at the end. The difference is that twice as many hidden bits can fit in there.

### Flag

`THANK YOU`
