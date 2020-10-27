---
title: 'Module 5: Preprocessing, pipelines and hyperparameter optimization'
description:
  'This model will concentrate on the steps that need to be taken before building your model. Preperation through imputation and scaling is an important steps of model building and can be done using tools such as pipelines. Next we will explore how we can tune multiple hyperparameters at once using a process called Grid Search.'
prev: /module4
next: /module6
type: chapter
id: 5
---

<exercise id="0" title="Module Learning Outcomes"  type="slides, video">

<slides source="module5/module5_00" shot="0" start="0:006" end="3:39">
</slides>

</exercise>

<exercise id="1" title="Why Preprocessing is Important" type="slides,video">

<slides source="module5/module5_01" shot="3" start="0:003" end="1:54">
</slides>

</exercise>

<exercise id="2" title= "Questions on Why">

**Question 1**  

Which model will still produce meaningful predictions with different scaled column values?

<choice id="1">

<opt text="Decision Trees" correct="true">

You are right! Decision Trees visit a single feature at a time unlike 𝑘-NN models, which calculate distances using all the features together. 

</opt>

<opt text= "𝑘-NN" >
 
Fantastic!

</opt>

<opt text="Dummy Classifier" >

Although this classifier is unaffected by different values in the feature columns, this is because this model isn't taking the feature values into it's prediction at all! This model is only predicting based on the primary target in the training set. 

</opt>

<opt text="SVM">

This works in a similar way to 𝑘-NN where distance is calculated and features are observe together and not independently of each other. 

</opt>

</choice>

**Question 2**   
*Complete the following statement*  
Preprocessing is done ____.  

<choice id="1" >

<opt text="To the model before training">

It is done before training but not to the model. 

</opt>

<opt text="To the data before training the model" correct="true">

Great!

</opt>

<opt text="To the model after training">

It's not done to the model or after training. 

</opt>

<opt text="To the data after training the model" >

You are half right but it's not done after training the model. 

</opt>

</choice>

</exercise>

<exercise id="3" title="Motivation True and False">

**True or False**     
_Columns will lower magnitudes compare to columns with higher magnitudes contribute are less important when making predictions._

<choice id="1" >
<opt text="True"  >

These types of models find examples that are most similar to the text example in the *training* set. 

</opt>

<opt text="False" correct="true">

Great! Just because a feature has smaller values does not mean it's less informative.

</opt>

</choice>

**True or False**     
*A model less sensitive to the scale makes it more robust.*

<choice id="2">
<opt text="True"  correct="true">

Nailed it!

</opt>

<opt text="False">

Models that are more sensitive to scale can be problematic. 

</opt>

</choice >

</exercise>


<exercise id="4" title="Preprocessing Questions">


**Question 1**  

`StandardScaler` is a type of what?

<choice id="1">

<opt text="Converter">

You are close but the terminology is not correct. 

</opt>

<opt text= "Categorizer" >
 
Not quite.

</opt>

<opt text="Model" >

We are not modeling with `StandardScaler` since it is *transforming* the data and not predicting on it. 

</opt>

<opt text="Transformer" correct="true">

Nice work!

</opt>

</choice>


**Question 1**  

What data does `StandardScaler` alter?

<choice id="2">

<opt text=" Training only">

It definitely alters the training set but that's not all. 

</opt>

<opt text= "Testing only" >
 
It does alter the test data but it doesn't stop there. 

</opt>

<opt text="Both training and testing" correct="true">

Nice work!

</opt>

<opt text="Nether training or testing ">

We need to scale our data though! 

</opt>

</choice>

</exercise>

<exercise id="5" title="Case Study: Preprocessing with Imputation" type="slides,video">
<slides source="module5/module5_05" shot="0" start="0:006" end="3:39">
</slides>

</exercise>

<exercise id="6" title= "Calculating Distances">


**Question 1**     

Given the following 2 feature vectors, which equation would calculate the Euclidean distance?

```
array([7, 0, 22, 11])
```

```
array([1, 0, 19, 9])
```

A) <img src="/module5/eq1.png"  width = "13%" alt="404 image" />

B) <img src="/module5/eq2.png"  width = "25%" alt="404 image" />

C) <img src="/module5/eq3.png"  width = "40%" alt="404 image" />

D) <img src="/module5/eq4.png"  width = "50%" alt="404 image" />


<choice id="1">

<opt text="A">

Not quite. 

</opt>

<opt text= "B" >
 
How many numbers are you performing subtraction on?

</opt>

<opt text="C" >

How many features are in each vector?

</opt>

<opt text="D"  correct="true">

Nice work.

</opt>

</choice>

**Question 2**   

What is the distance between the 2 vectors?

<choice id="2" >

<opt text="49"  >

You forgot to square root!

</opt>

<opt text="7" correct="true">

Great!

</opt>

<opt text="6">

Not quite there.

</opt>

<opt text="36">

Close but you have the target value in the feature vector.

</opt>

</choice>

</exercise>

<exercise id="6" title="Distance True or False">

**True or False**     
_Distance will always have a positive value._

<choice id="1" >
<opt text="True"  correct="true">

Yes! We are squaring all the differences which means that distance can only be a positive value. 

</opt>

<opt text="False" >

Take a look at the equation we use to calculate Euclidean distance. 

</opt>

</choice>

</exercise>

<exercise id="7" title='Calculating Euclidean Distance by "Hand"'>

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Let's calculate the Euclidean distance between 2 examples in the Pokémon dataset without using Scikit-learn. 

Tasks:     

- Subtract the two first Pokémon feature vectors and save it in an object named `sub_pk`.
- Square the difference and save it in an object named `sq_sub_pk`.
- Sum the squared difference from each dimension and save the result in an object named `sss_pk`.
- Finally, take the square root of the entire calculation and save it in an object named `pk_distance`.

<codeblock id="04_07">

- Are you importing `sqrt` from the `math` library?
- Are you using `X.iloc[1] - X.iloc[0]` to subtract the first 2 Pokémon feature vectors?
- Are you using `**2` to square the difference??
- Are you using `.sum()` to sum the differences?
- Are you using `sqrt()` to square root the sum of squared differences?

</codeblock>

</exercise>

<exercise id="8" title='Calculating Euclidean Distance with Scikit-learn'>

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

This time, let's calculate the Euclidean distance between 2 examples in the Pokémon dataset using Scikit-learn. 

Tasks:     

- Import the necessary library.
- Calculate the Euclidean distance of the first 2 Pokémon and save it in an object named pk_distance.

<codeblock id="04_08">

- Are you importing `euclidean_distances` from `sklearn.metrics.pairwise` 
- Are you making sure to use `euclidean_distances(X.iloc[:2])`
- Are you selecting the right value from the array using `[0,1]`
</codeblock>

</exercise>

<exercise id="9" title="Finding the Nearest Neighbour" type="slides,video">
<slides source="module5/module5_09" shot="0" start="0:006" end="3:39">
</slides>

</exercise>

<exercise id="10" title= "Finding Neighbours Questions">

**Question 1**  

What would happen if we didn't use `fill_diagonal()` when trying to find the closest example to an existing one?

<choice id="1">

<opt text="We would get the farthest example from the one we are trying to find instead of the closest.">

Not quite. 

</opt>

<opt text= "We would get itself as the closest example."  correct="true" >
 
Right, there is 0 distance from a point to itself. 

</opt>

<opt text="We would obtain the mean distance from all points to the current one." >

Unfortunately, the mean has nothing to do with why we fill the diagonals in.

</opt>

<opt text="We would get 0 examples." >

We would get an example but it would be the wrong one.

</opt>

</choice>

**Question 2**   

How many dimension does the input vector for `kneighbors()` need to be?

<choice id="2" >

<opt text="1" >

1d vectors will result in an error. 

</opt>

<opt text="2" correct="true">

Great!

</opt>

<opt text="3">

This will throw an error. 

</opt>

<opt text="It must be a pandas dataframe">

Close but you have the target value in the feature vector.

</opt>

</choice>

</exercise>

<exercise id="11" title="Distance True or False">

**True or False**     
_Similar to decision trees, k-NNs finds a small set of good features._

<choice id="1" >
<opt text="True"  >

K-NNs use all the features!

</opt>

<opt text="False" correct="true" >

Great work!

</opt>

</choice>

**True or False**     
_Finding the distances to a query point takes double the time as finding the nearest neighbour._

<choice id="2" >
<opt text="True"  >

This is completely made up!

</opt>

<opt text="False" correct="true" >

Great work!

</opt>

</choice>

</exercise>

<exercise id="12" title='Calculating the Distance to a Query Point'>

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Let's calculate the closet Pokémon in the training set to a Snoodle (our made-up Pokémon!

Snoodle	has the following feature vector. 

```out
[[53,  77,  43,  69,  80,  57,  379,  3]]
```
Which Pokémon in the training set, most resembles a Snoodle?

Tasks:     

- Create a model and name it `nn` (make sure you are finding the single closest Pokémon).
- Train your model on `X_train`.
- Predict your Pokémon using `kneighbors` and save it in an object named `snoodles_neighbour`.
- Which Pokémon (the name) is Snoodle most similar to? Save it in an object named `snoodle_name`.

<codeblock id="04_12">

- Are you importing ?
- Are you using ` NearestNeighbors(n_neighbors=1)`?
- Are you using `nn.fit(X_train)`?
- Are you using `nn.kneighbors(query_point)` ?
- Are you using `train_df.iloc[snoodles_neighbour[1].item()]['name']` to get the name of the closest Pokémon?

</codeblock>
</exercise>

<exercise id="13" title="𝑘 -Nearest Neighbours (𝑘-NNs) Classifier" type="slides,video">
<slides source="module5/module5_13" shot="0" start="0:006" end="3:39">
</slides>

</exercise>

<exercise id="14" title= "Classifying Examples by Hand">

Consider this toy dataset:

<center><img src="/module5/Q14.png"  width = "40%" alt="404 image" /></center>

**Question 1**  

If 𝑘=1 , what would you predict for &nbsp; &nbsp;   <img src="/module5/ans14.png"  width = "8%" alt="404 image" /> &nbsp;&nbsp;&nbsp;?

<choice id="1">

<opt text="0">

the point (2, 2) is the closest to (0, 0).
 
</opt>

<opt text= "1"  correct="true" >
 
Right, the point (2, 2) is the closest to (0, 0) and it is categorized as 1. 

</choice>

**Question 2**  

If  𝑘=3 , what would you predict for &nbsp; &nbsp;   <img src="/module5/ans14.png"  width = "8%" alt="404 image" /> &nbsp;&nbsp;&nbsp;?

<choice id="2" >

<opt text="0" correct="true">

Nice!

</opt>

<opt text= "1" >
 
The points (2, 2), (5, 2) and (4, 3) are the closest to (0, 0). Which label is more occurring?

</opt>

</choice>


</exercise>

<exercise id="15" title="K-NN Classifiers True or False">

**True or False**     
_The classification of the closest neighbour to the test example always contributes the most to the prediction._

<choice id="1" >
<opt text="True">

Not always. You can select this as an option but it is not done like this by default.

</opt>

<opt text="False" correct="true" >

Great work!

</opt>

</choice>

**True or False**     
*The `n_neighbors` hyperparameter must be less than the number of examples in the training set.*

<choice id="2" >
<opt text="True" correct="true"  >

Nice work. 

</opt>

<opt text="False" >

You can't assign `n_neighbors` to a value greater than the possible number of examples in the training set. 

</opt>

</choice>

</exercise>

<exercise id="16" title='Predicting with a KNN-Classifier'>

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Let's try to classify some Pokémon from the Pokémon dataset. How well does our model do on the training data?

Tasks:     

- Create a `KNeighborsClassifier` model with `n_neighbors` equal to 5 and name it `model`.
- Train your model on `X_train` and `y_train` (Hint: you may want to use `.to_numpy()`).
- Score your model on the training set using `.score()` and save it in an object named `train_score`.
- Score your model on the test set using `.score()` and save it in an object named `test_score`.

<codeblock id="04_16">

- Are you importing `KNeighborsClassifier`?
- Are you using ` KNeighborsClassifier(n_neighbors=5)`?
- Are you using `model.fit(X_train, y_train.to_numpy())`?
- Are you using `model.score(X_train, y_train)` to find the training score?
- Are you using `model.score(X_test, y_test)` to find the test score?

</codeblock>
</exercise>

<exercise id="17" title="Choosing 𝑘 (n_neighbors)" type="slides,video">
<slides source="module5/module5_17" shot="0" start="0:006" end="3:39">
</slides>

</exercise>

<exercise id="18" title= "Choosing K for Your Model">

Consider this graph:

<center><img src="/module5/Q18a.png"  width = "80%" alt="404 image" /></center>

**Question 1**  

What value of `n_neighbors` would you choose to train your model on? 

<choice id="1">

<opt text="0">

This is not a valid value for `n_neighbors`.
 
</opt>

<opt text= "1" >
 
Although this may have the highest training score, this does not have the highest cross-validation score. 

</opt>

<opt text= "12"  correct="true" >
 
Nice work. 

</opt>

<opt text= "16" >
 
Almost. There is a value with a higher score

</opt>

<opt text= "29">
 
You shouldn't pick the highest `n_neighbors` without the cv-score being the highest.  

</opt>

</choice>

**Question 2**  

Up to which value of `n_neighbors` is there overfitting?

<choice id="2">

<opt text="The model never overfits">

When the training score is greater than the CV score, the model is overfitting.

</opt>

<opt text= "12" >
 
There is overfitting still occurring after this value. 

</opt>

<opt text= "26" >
 
Is the training score greater than the CV score after this value?

</opt>

<opt text= "29" correct="true">

Now it appears that the model is underfitting! 

</opt>

</choice>

</exercise>

<exercise id="19" title="Curse of Dimensionality and Choosing K True or False">

**True or False**     
_With  𝑘 -NN, setting the hyperparameter  𝑘  to larger values typically increase training score._

<choice id="1" >
<opt text="True">

Have you tried it out? It could be a good idea to see this in action!

</opt>

<opt text="False" correct="true" >

Great work!

</opt>

</choice>

**True or False**     
_𝑘 -NN may perform poorly in high-dimensional space (say, d > 100)._

<choice id="2" >
<opt text="True" correct="true"  >

Nice work. 

</opt>

<opt text="False" >

Having more features in some cases is less helpful to the model.

</opt>

</choice>

</exercise>

<exercise id="20" title='Hyperparameter Tuning'>

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

In the last exercise, we classified some Pokémon from the Pokémon dataset but we were not using the model that could have been the best! Let's try hyperparameter tuning.

First, let's see which hyperparameter is the most optimal. 

Tasks:     

Fill in the code for  a `for` loop that does the following:
- iterates over the values 1-50 in increments of 5.
- Builds a  `KNeighborsClassifier` model with `n_neighbors` equal to each iteration.
- Uses `cross_validate` on the model with a `cv=10` and `return_train_score=True`.
- Appends the k value to the `n_neighbors` list in the dictionary `results_dict`.
- Appends the `test_score` to the `mean_cv_score` list in the dictionary. 
- Appends the `train_score` to the `mean_train_score` list in the dictionary. 

We have given you code that wrangles this dictionary and transforms it into a state ready for plotting.

Finish off by filling in the blank to create a line graph that plots the train and validation scores for each value of k.      
(Note: we have edited the limits of the y-axis so it's easier to read)

<codeblock id="04_20a">

- Are you importing `KNeighborsClassifier`?
- Are you using ` KNeighborsClassifier(n_neighbors=11)`?
- Are you using `model.fit(X_train, y_train.to_numpy())`?
- Are you using `cross_validate(model, X_train, y_train, cv=10, return_train_score=True)`?
- Are you using `alt.Chart(results_df).mark_line()` to create your plot?

</codeblock>


**Question 1**    
To which depth would you set your `n_neighbors` hyperparameter?

<choice id="1" >
<opt text="1" >

There are other `n_neighbors` values that have a higher cross-validation score than at this value. 

</opt>

<opt text="11" correct="true">

Great! The CV score is highest at this value. 

</opt>

<opt text="24"   >

Are you sure this is the n_neighbors with the highest cross-validation score possible?

</opt>

<opt text="31">

Are you sure this is the n_neighbors with the highest cross-validation score possible?

</opt>

</choice>

Tasks:     

Now that we have found a suitable value for `n_neighbors`, let's build a new model and let this hyperparameter value. How well does your model do on the test data?

Tasks:     

- Build a model using `KNeighborsClassifier()` using the optimal `n_neighbors`. 
- Save this in an object named `model`. 
- Fit your model on the objects `X_train` and `y_train`.
- Evaluate the test score of the model using `.score()` on `X_test` and `y_test` and save the values in an object named `test_score` rounded to 4 decimal places.

<codeblock id="04_20b">

- Are using `KNeighborsClassifier(n_neighbors=11)`?
- Are you using the model named `model`?
- Are you calling `.fit(X_train, y_train)` on your model?
- Are you scoring your model using `model.score(X_test, y_test)`?
- Are you rounding to 4 decimal places?
- Are you calculating `test_score` as  `round(model.score(X_test, y_test), 4)` )

</codeblock>

</exercise>

<exercise id="21" title="𝑘 -Nearest Neighbours Regressor" type="slides,video">
<slides source="module5/module5_21" shot="0" start="0:006" end="3:39">
</slides>

</exercise>

<exercise id="22" title= "Choosing K for Your Model">

Consider this toy dataset:

<center><img src="/module5/Q14.png"  width = "40%" alt="404 image" /></center>

**Question 1**  

If 𝑘=1 , what would you predict for &nbsp; &nbsp;   <img src="/module5/ans14.png"  width = "8%" alt="404 image" /> &nbsp;&nbsp;&nbsp; if we were doing regression rather than classification?

<choice id="1">

<opt text="0">

The points (2, 2), (5, 2) and (4, 3) are the closest to (0, 0) and so we must take the average of all the values. 
 
</opt>

<opt text= "1"  >
 
The points (2, 2), (5, 2) and (4, 3) are the closest to (0, 0) and so we must take the average of all the values.

<opt text= "1/3"  correct="true" >
 
You got it!

<opt text= "3">
 
We must take the average of the 3 nearest examples. 

</choice>

**Question 2**  

**True or False**     
_K-NN with Regression can only be done in a 1-dimensional space._

<choice id="2" >

<opt text="True"  >

K-NN can be done with just as many dimensions as classification

</opt>

<opt text="False" correct="true"  >

Nice work. 

</opt>

</choice>


</exercise>

<exercise id="23" title='Building a KNN-Regressor'>

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Let's bring in this Pokémon dataset again, but this time we are not going to be predicting a Pokémon’s capture rate (`capture_rt`) instead of its `legendary` classification.

We did the same process of cross validation and scoring as we did before but we obtain this plot: 

<center><img src="/module5/Q23.png"  width = "90%" alt="404 image" /></center>

This model didn't end up having a clear best score when we hyperparameter tuned but in the end, we decided to use `n_neighbors=12`.

Let's build a KNeighborsRegressor with this hyperparameter value and see how well does your model do on the test data?

Tasks:     

- Build a model using `KNeighborsRegressor()` using the optimal `n_neighbors`. 
- Save this in an object named `model`. 
- Fit your model on the objects `X_train` and `y_train`.
- Evaluate the test score of the model using `.score()` on `X_test` and `y_test` and save the values in an object named `test_score` rounded to 4 decimal places.

<codeblock id="04_23b">

- Are using `KNeighborsRegressor(n_neighbors=11)`?
- Are you using the model named `model`?
- Are you calling `.fit(X_train, y_train)` on your model?
- Are you scoring your model using `model.score(X_test, y_test)`?
- Are you rounding to 4 decimal places?
- Are you calculating `test_score` as  `round(model.score(X_test, y_test), 4)` )

</codeblock>

</exercise>

<exercise id="24" title="Support Vector Machines (SVMs) with RBF Kernel" type="slides,video">
<slides source="module5/module5_24" shot="0" start="0:006" end="3:39">
</slides>

</exercise>

<exercise id="25" title= "Testing your RBF Knowledge">

These two boundary plots were made using SVM with an RBF kernel and the other with K-Nearest Neighbours. 
<center><img src="/module5/Q25.png"  width = "90%" alt="404 image" /></center>

<br>

**Question 1**  

Which plot more likely visualizes the boundaries of the SVM model?

<choice id="1">

<opt text="Left">

Which plot has smoother boundaries?
 
</opt>

<opt text= "Right"  correct="true" >
 
Nice

</choice>


</exercise>

<exercise id="26" title="SVM True or False">

**True or False**     
_In Scikit Learn’s SVC classifier, large values of gamma tend to result in higher training score but probably lower validation score._

<choice id="1" >
<opt text="True “correct="true">

Great work!

</opt>

<opt text="False"  >

As we increase gamma, since our model is becoming more complex, our training score should increase. Since the model is more specific to the training data, the test score may decrease.

</opt>

</choice>

**True or False**     
_If we increase both `gamma` and `C`, we can't be certain if the model becomes more complex our less complex._

<choice id="2" >
<opt text="True"  >

Increasing both `C` and `gamma` makes the model more complex in both cases so the model will be increasing in complexity. 

</opt>

<opt text="False" correct="true" >

Great work. 

</opt>

</choice>

</exercise>

<exercise id="27" title='Predicting with an SVM Classifier'>

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

We've used K-Nearest Neighbours to classify Pokémon from the Pokémon dataset so now let's try to do the same thing with an RBF kernel!

Tasks:     

- Create an `SVM` model with `gamma` equal to 0.1 and `C` equal to 10cand name it `model`.
- Train your model on `X_train` and `y_train` (Hint: you may want to use `.to_numpy()`).
- Score your model on the training set using `.score()` and save it in an object named `train_score`.
- Score your model on the test set using `.score()` and save it in an object named `test_score`.

<codeblock id="04_27">

- Are you importing `SVM`?
- Are you using ` SVM(gamma=0.1, C=10)`?
- Are you using `model.fit(X_train, y_train.to_numpy())`?
- Are you using `model.score(X_train, y_train)` to find the training score?
- Are you using `model.score(X_test, y_test)` to find the test score?

</codeblock>

**Question 1**    
Does this model give similar results to K-NN?

<choice id="1" >
<opt text="Yes" >

We got around .80 with K-NN, do you think that this is close enough?

</opt>

<opt text="No" correct="true">

It seems like we have some hyperparameters to tune and/or this may not be the best model for us this time.

</opt>

</choice>

</exercise>

<exercise id="28" title="What Did We Just Learn?" type="slides, video">
<slides source="module5/module5_end" shot="0" start="0:003" end="1:54">
</slides>
</exercise>

