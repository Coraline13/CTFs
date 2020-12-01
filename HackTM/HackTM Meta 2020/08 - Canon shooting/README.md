# Day 8 - Canon shooting

* **Event:** HackTM Meta 2020
* **Category:** 
* **Points:** 164
* **Difficulty:** 
* **Tools used:** 

### Description

It's the middle of your first night here at HackTM. Your project is well on its way: the model is ready, the dataset is up, the training started and now you wait.. Waiting around at 2AM can quickly turn into sound sleeping, so you decide to stretch your legs and take a look at what other teams are doing.

A few tables away you run into an old colleague of yours who's mumbling at a... robotic arm? A weapon? A printer? It must be a printer, nothing else treats paper that way. He seems stressed, you are bored, so you decide to help. After all, you owe him for not reporting that concurrency bug years ago.

The makers of this printer studied too much string theory and now they see the world in 11 dimensions. You don't know the inner workings of the printer, but the manual comes in handy.

**Note:**

The scoring for this challenge is dynamic.

### Attachment

`day8.zip`

### Solution

First of all you will need to compute where each pixel that has to be printed ends up. The vectors V and U are along the margins of the paper, but their length is arbitrary. It would be useful to have vectors of length 1 that point along the margins. In order to do this we normalize V and U (search on google for "normalization" for more info on this). To do this we divide each component in the vector by the length of the vector. The length of the vector is the square root of the sum of the squares of all components. Let's call the normalized vectors A and B. Pixel (i, j) on the paper will end up at position `P + i*B + j*A` (remember P is the top-left corner of the paper, A is a vector of length 1 along the top margin, pointing right, and B is a vector of length 1 along the left margin, pointing down). Let's name this position Pos. Once we have this position we can get the vector pointing from the cannon to the pixel by doing `Dir = Pos - C` (remember C is the position of the cannon). To get the point on the sphere we need to start from C and go along the previously computed direction a distance of r (radius of the sphere). Again, we normalize Dir, to get a vector of length 1 on this direction. Let's call this one NormDir. Finally, the point on the sphere is `C + r*NormDir`. After we have all these vectors, all that's left is to round real values down to the nearest integer and surround the result with `HackTM{...}`.  

Solution in python:

```python
def solve(p, v, u, c, r, mat):
    v = v / np.linalg.norm(v)
    u = u / np.linalg.norm(u)

    res = []

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == '1':
                pixel_position = p + i * u + j * v
                canon_pixel_vector = pixel_position - c
                canon_pixel_direction = canon_pixel_vector / np.linalg.norm(canon_pixel_vector)
                target_on_sphere = c + canon_pixel_direction * r
                for vector_component in target_on_sphere:
                    res.append(vector_component)
    return res
```

### Flag

??
