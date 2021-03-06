---
type: slides
---

# Types of machine learning

Notes:

This course is about supervised machine learning. In fact, all the
examples we saw in the last section are examples of supervised machine
learning, but what other types of machine learning are there?

---

Typical learning problems:

-   **Supervised learning (this course)**
    (<a href="https://support.google.com/a/answer/2368132?hl=en" target="_blank">Gmail
    spam filtering</a>)
    -   Training a model from input data and its corresponding labels to
        predict new examples.  
-   Unsupervised learning
    (<a href="https://news.google.com/" target="_blank">Google News</a>)
    -   Training a model to find patterns in a dataset, typically an
        unlabeled dataset.
-   Reinforcement learning
    (<a href="https://deepmind.com/research/case-studies/alphago-the-story-so-far" target="_blank">AlphaGo</a>)
    -   A family of algorithms for finding suitable actions to take in a
        given situation in order to maximize a reward.
-   Recommendation systems
    (<a href="https://www.cs.umd.edu/~samir/498/Amazon-Recommendations.pdf" target="_blank">Amazon
    item recommendation system</a>)
    -   Predict the “rating” or “preference” a user would give to an
        item.

Notes:

Some typical types of learning problem include:

-   **Supervised learning (this course)**
    (<a href="https://support.google.com/a/answer/2368132?hl=en" target="_blank">Gmail
    spam filtering</a>) which consists of training a model from input
    data and its corresponding labels to predict new examples.  
-   Unsupervised learning
    (<a href="https://news.google.com/" target="_blank">Google News</a>)
    We are not given a target column.
-   Reinforcement learning
    (<a href="https://deepmind.com/research/case-studies/alphago-the-story-so-far" target="_blank">AlphaGo</a>)
    is about teaching agents to interact in the real world..
-   Recommendation systems
    (<a href="https://www.cs.umd.edu/~samir/498/Amazon-Recommendations.pdf" target="_blank">Amazon
    item recommendation system</a>) fall under the unsupervised paradigm
    but with a specific focus on predicting ratings or preferences a
    user would to certain items.

As mentioned before, this particular course focuses on supervised
machine learning.

---

## Supervised learning

<center>
<img src="/module1/sup-learning.png" height="1000" width="1000">
</center>

Notes:

Let’s talk about some terminology.

In supervised machine learning, we have a set of observations usually
denoted with an uppercase `X`.

We also have a set of corresponding targets usually denoted with a
lowercase `y`.

Our goal is to define a function that relates `X` to `y`.

We then use this function to predict the targets of new examples.

Here is an example, where our `X` contains emoticons of cats and dogs
and our `Y` contains labels associated with these emoticons. We have our
learning algorithm which is a classification algorithm in this case.
Using this algorithm we learn the mapping between `X` and `y`. Once we
had this model we applied it to unseen test data to get predictions.

In this particular case, our unseen data contains the emoticons of a cat
and a dog. Our predictions are the labels of cat and dog respectively.

---

``` python
from toy_classifier import classify_image

img = Image.open("alpaca.jpg")
img
```

``` out
```

<img src="/module1/alpaca.jpg" alt="This image is in /static" width="20%">

Notes:

The example we saw before classifying images, is an example of
supervised machine learning.

In our example, our model was trained on a large number of images and
their targets.

We can apply this morning on unseen images, in this particular case, our
unseen image is an image of an alpaca.

---

<img src="/module1/alpaca.jpg" alt="This image is in /static" width="20%">

``` python
classify_image(img, 3)
```

```out
Class, Probability
llama, 0.72
Eskimo dog, husky, 0.06
Norwich terrier, 0.05
```

Notes:

We apply our model to this image and we get these predictions and
probabilities scores associated with them. Our model here predicted that
this is a picture of a llama with 72% confidence.

---

## Unsupervised learning

<center>
<img src="/module1/unsup-learning.png" alt="" height="900" width="900">
</center>

Notes:

In unsupervised learning, we are not given targets and are only given
observations `X`.

We apply some clustering algorithms to create a model that finds
patterns in our data and groups together similar characteristics from
our data.

In this particular example, our `X` contains emoticons of cats and dogs.
We apply our clustering algorithm on this data and as we get images of
dogs and cats clustered together in groups.

---

## Machine Learning Libraries

<br>

### <a href="https://scikit-learn.org/stable/index.html" target="_blank">scikit-learn</a>

<center>
<img src="/module1/sk-learn.png" alt="" height="900" width="900">
</center>

Notes:

There are several machine learning libraries available to use but for
this course, we will be using the `sklearn` library, which is a popular
(41.6k stars on Github) Machine Learning library for Python.

---

## What we know so far…

-   In supervised learning, we are given a set of observations (𝑋) and
    their corresponding targets 𝑦 and we wish to find a model function
    that relates 𝑋 to 𝑦.
-   In unsupervised learning, we are given a set of observations (𝑋) and
    we wish to group similar things together in 𝑋.

Notes:

So far we have seen that in supervised learning we are given a set of
observations `X` and their corresponding targets `Y`.

We wish to find a corresponding model function that relates `X` to `y`.

In unsupervised learning, we are given a set of observations `X` and we
wish to group similar examples together.

---

# Let’s apply what we learned!

Notes: <br>
