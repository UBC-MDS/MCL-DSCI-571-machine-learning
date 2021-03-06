---
type: slides
---

# Introducing decision trees

Notes: <br>

---

## Improving the baseline model

Examples:

<center>
<img src="/module2/quiz2-grade-toy.png"  width = "85%" alt="404 image" />
</center>

Notes:

So we have built a baseline model, but can we do better than that?

We’re going to bring back this data set that we saw previously which is
the classification dataset for whether or not a student will get an A+
on the second quiz given that there are multiple other columns here.

If you are asked to write a program to predict whether a student gets an
A+ or not in quiz2, how would you go for it?

In our dummy model we only predicted the most occurring value in this
Quiz 2 column on our new test data, so for example, if A+ was most
occurring, then on any new test data, it would just predict A+ no matter
what all of these other column values were.

We have all of these features that we could use to help with our
predictions. To make things initially more understandable, we are going
to change our dataset a little bit so they are expressed in binary
values. 1 = yes and 0 = no or 1=A+ 0=Not A+.

---

## A program for prediction using a set of rules with *if/else* statements

<center>
<img src="/module2/quiz2-grade-toy.png" height="600" width="600">
</center>

-   How about a rule-based algorithm with several *if/else*
    statements?  

<!-- -->

    if class attendance == 1 and quiz1 == 1:
        quiz2 == "A+"
    elif class attendance == 1 and lab3 == 1 and lab4 == 1:
        quiz2 == "A+"
    ...

Notes:

Now that we have a model where our features are 1 of 2 options, how
about we have a rule-based algorithm with several *if/else*
statements?  
We learned about conditions and *if/else* statements in module 5 of
***Programming in Python for Data Science***, now let’s incorporate this
concept into a machine learning problem.

Looking at the first example we have `class_attendance=1` and `quiz1=1`
as well. That gives us in our training data an A+ as the target. We
could write a rule where if `class_attendance=1` and `quiz1=1` we
predict quiz2 =A+ since there are no other examples in the data.

In our next example, we could make an if-else statement where
`class_attendance=1` and `lab3=1` and `lab4=1` then quiz2=A+ since there
are no other examples in this dataset.

    if class attendance == 1 and quiz1 == 1:
        quiz2 == "A+"
    elif class attendance == 1 and lab3 == 1 and lab4 == 1:
        quiz2 == "A+"
    ...

We can continue making these rules until we have many rules.

Since we have 7 features each with 2 possibilities, the total possible
different rules could be 128 different statements but neither of us
wants to write all these, which is where decision trees come into play.

---

``` python
classification_df = pd.read_csv("data/quiz2-grade-toy-classification.csv")
classification_df.head(3)
```

```out
   ml_experience  class_attendance  lab1  lab2  lab3  lab4  quiz1   quiz2
0              1                 1    92    93    84    91     92      A+
1              1                 0    94    90    80    83     91  not A+
2              0                 0    78    85    83    80     80  not A+
```

``` python
X = classification_df.drop(columns=["quiz2"])
X.head(3)
```

```out
   ml_experience  class_attendance  lab1  lab2  lab3  lab4  quiz1
0              1                 1    92    93    84    91     92
1              1                 0    94    90    80    83     91
2              0                 0    78    85    83    80     80
```

``` python
y = classification_df["quiz2"]
y.head(3)
```

```out
0        A+
1    not A+
2    not A+
Name: quiz2, dtype: object
```

Notes:

Let’s take our 𝑋 and 𝑦 from our `quiz2` data that we had before.

---

``` python
X_binary = X.copy()
columns = ["lab1", "lab2", "lab3", "lab4", "quiz1"]
for col in columns:
    X_binary[col] = X_binary[col].apply(
        lambda x: 1 if x >= 90 else 0)
X_binary.head()    
```

```out
   ml_experience  class_attendance  lab1  lab2  lab3  lab4  quiz1
0              1                 1     1     1     0     1      1
1              1                 0     1     1     0     0      1
2              0                 0     0     0     0     0      0
3              0                 1     1     1     1     1      0
4              0                 1     0     0     1     1      0
```

Notes:

Now let’s binarize the features in `X` as we discussed. Don’t worry too
much about this code.

We can see that each column now only has a value of either `0` or `1`.

Now that we have this data in a preferred way we can try and make our
predictions with rules and that’s where our decision trees come in.

---

## Decision trees

<center>
<img src="/module2/nature.png"  width = "85%" alt="404 image" />
</center>

Notes:

The decision tree models use an algorithm that derives such rules from
data in a principled way.

---

## Decision trees terminology

<center>
<img src="/module2/lingo_tree.png"  width = "85%" alt="404 image">
</center>

Note:

Before we go forward with learning about decision tree classifiers and
reggressors we need to understand the structure of a decision tree. Here
is the key terminology that you will have to know:

-   **Root**: Where we start making our conditions.
-   **Branch**: A branch connects to the next node (statement). Each
    branch represents either true or false.
-   **Internal node**: conditions within the tree.  
-   **Leaf**: the value predicted from the conditions.
-   **Tree depth**: The longest path from the root to a leaf.

With the decision tree algorithm in machine learning, the tree can have
at most two **nodes** resulting from it, also known as **children**.

This tree would have a depth of 2.

---

<center>
<img src="/module2/example3.png"  width = "85%" alt="404 image">
</center>

Note:

Using our quiz2 dataset as an example, a tree may look something like
this.

This tree has a depth of 3.

Trees do not need to be balanced.

---

## Decision Stump

<br> <br>
<center>
<img src="/module2/stump.png"  width = "60%" alt="404 image">
</center>

Note:

This tree has a depth of 1.

A decision tree that has a depth of 1 is called a ***decision stump***.

---

# Let’s apply what we learned!

Notes: <br>
