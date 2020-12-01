# Day 13 - Ping, no pong

* **Event:** HackTM Meta 2020
* **Category:** 
* **Points:** 263
* **Difficulty:** 
* **Tools used:** 

### Description

The venue is quiet, everyone’s working hard. Until…  

BAM! Interwebs are no longer working… ping, no pong. The MC comes on stage and announces that somebody is downloading torrents. Nobody will admit to it, but whoever finds the culprit gets a free burger. And virtual internet points.  

We have access to all data that has been transferred through our network. It looks like the culprit has downloaded a movie, that we suspect is used to send secret messages to an external agent. If we could find which frames were altered to store hidden messages we will be one step closer to find the offender.  

Your task is to generate a bit string, one bit per frame, that says whether the frame contains a hidden message or not and submit the message corresponding to that bit string.  

Have you found the culprit yet?

**Note:**

The scoring for this challenge is dynamic.

There is no flag format. You just need to submit your answer as you find it.

### Attachment

`HackTM_day13.zip`

### Solution

The core idea is classification: whether an image contains or not a hidden message. In our solution we have used the labels 'Normal' and 'Hidden'. So label 0, will be assigned to all the images that have no hidden message, that are 'Normal' and label 1 will be assigned to all the images that have a hidden message.  

This is also a stenography problem, but we want to solve it using Deep Learning.  

We create a csv for the training data, one for the validation data and one for testing.  

We encapsulate all the information for this dataset in the class MyDataset and define the needed operations for images.  

For the classification we use a model that is state of the art: EfficientNet. We modify the last layer because we have only 2 classes.  (One can try with any architecture or define his own architecture).  

For the implementation we use pytorch, but any library can be used.   

EfficientNet learns the features for each class, what is specific for images with hidden messages and what is specific for normal images.  

For the testing phase we use the trained network to predict for each frame whether the image has or not a hidden message.


### Flag

??
