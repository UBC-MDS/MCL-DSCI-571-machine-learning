---
type: slides
---

# Multi-class Classification

Notes: <br>

---

``` python
data = datasets.load_wine()
X = pd.DataFrame(data['data'], columns=data["feature_names"])
y = data['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=2021)
```

``` python
X_train
```

```out
     alcohol  malic_acid   ash  alcalinity_of_ash  magnesium  total_phenols  flavanoids  nonflavanoid_phenols  proanthocyanins  color_intensity   hue  od280/od315_of_diluted_wines  proline
36     13.28        1.64  2.84               15.5      110.0           2.60        2.68                  0.34             1.36             4.60  1.09                          2.78    880.0
77     11.84        2.89  2.23               18.0      112.0           1.72        1.32                  0.43             0.95             2.65  0.96                          2.52    500.0
131    12.88        2.99  2.40               20.0      104.0           1.30        1.22                  0.24             0.83             5.40  0.74                          1.42    530.0
159    13.48        1.67  2.64               22.5       89.0           2.60        1.10                  0.52             2.29            11.75  0.57                          1.78    620.0
4      13.24        2.59  2.87               21.0      118.0           2.80        2.69                  0.39             1.82             4.32  1.04                          2.93    735.0
..       ...         ...   ...                ...        ...            ...         ...                   ...              ...              ...   ...                           ...      ...
109    11.61        1.35  2.70               20.0       94.0           2.74        2.92                  0.29             2.49             2.65  0.96                          3.26    680.0
128    12.37        1.63  2.30               24.5       88.0           2.22        2.45                  0.40             1.90             2.12  0.89                          2.78    342.0
57     13.29        1.97  2.68               16.8      102.0           3.00        3.23                  0.31             1.66             6.00  1.07                          2.84   1270.0
85     12.67        0.98  2.24               18.0       99.0           2.20        1.94                  0.30             1.46             2.62  1.23                          3.16    450.0
116    11.82        1.47  1.99               20.8       86.0           1.98        1.60                  0.30             1.53             1.95  0.95                          3.33    495.0

[133 rows x 13 columns]
```

``` python
y_train
```

```out
array([0, 1, 2, 2, 0, 2, 1, 1, 0, 2, 1, 2, 1, 0, 1, 0, 2, 2, 2, 1, 2, 1, 0, 2, 2, 0, 2, 1, 0, 2, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 2, 2, 1, 0, 0, 2, 2, 1, 0, 2, 1, 2, 1, 0, 1, 1, 0, 0, 2, 0, 2, 1, 0, 0, 2, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 0, 0, 2, 1, 1, 0, 1, 1, 2, 1, 0, 1, 0, 0, 0, 1, 0, 1, 2, 2, 1, 0, 2, 2, 2, 1, 2, 2, 0, 1, 2, 1, 0, 2, 0, 1, 2, 1, 1, 0, 0, 1, 0, 1, 1, 2, 2, 1, 0, 2, 1, 0, 1, 1, 1, 0,
       1, 1])
```

Notes:

The classification problems we have looked at so far in this module have
had binary labels (2 possible labels)

But we’ve seen that target label’s are not restricted to this. Often we
will have classification problems where we have multiple labels such as
this wine dataset we are going to use in this section.

Here you can see that we have 3 classes: 0, 1, 2.

---

``` python
lr = LogisticRegression(max_iter=10000)
lr.fit(X_train, y_train);
```

``` python
lr.predict(X_test[:5])
```

```out
array([0, 1, 0, 2, 1])
```

``` python
lr.coef_
```

```out
array([[ 0.53342904,  0.43649341,  0.38582143, -0.04885916, -0.02585522,  0.54321457,  0.87592263, -0.00720518, -0.09294391,  0.21028243,  0.03196909,  0.61413713,  0.0110249 ],
       [-0.70188933, -0.80597707, -0.45969471, -0.09128562, -0.03501895, -0.0638047 ,  0.26557322,  0.14184983,  0.78434756, -0.9226091 ,  0.25697492, -0.03074428, -0.00911649],
       [ 0.16846029,  0.36948366,  0.07387328,  0.14014478,  0.06087417, -0.47940986, -1.14149585, -0.13464466, -0.69140365,  0.71232667, -0.28894401, -0.58339285, -0.00190841]])
```

Notes:

For some models, like a decision trees, we don’t have to think about
anything differently at all, but for our linear classifier, on the other
hand, things are a bit different.

What is going on here?

---

``` python
lr.coef_.shape
```

```out
(3, 13)
```

``` python
lr_coefs = pd.DataFrame(data=lr.coef_.T, index=X_train.columns, columns=lr.classes_)
lr_coefs
```

```out
                                     0         1         2
alcohol                       0.533429 -0.701889  0.168460
malic_acid                    0.436493 -0.805977  0.369484
ash                           0.385821 -0.459695  0.073873
alcalinity_of_ash            -0.048859 -0.091286  0.140145
magnesium                    -0.025855 -0.035019  0.060874
total_phenols                 0.543215 -0.063805 -0.479410
flavanoids                    0.875923  0.265573 -1.141496
nonflavanoid_phenols         -0.007205  0.141850 -0.134645
proanthocyanins              -0.092944  0.784348 -0.691404
color_intensity               0.210282 -0.922609  0.712327
hue                           0.031969  0.256975 -0.288944
od280/od315_of_diluted_wines  0.614137 -0.030744 -0.583393
proline                       0.011025 -0.009116 -0.001908
```

``` python
lr_coefs.loc["alcohol", 1]
```

```out
-0.701889329444353
```

Notes:

What’s happening here is that we have one coefficient per feature *per
class*.

The interpretation is a feature importance for predicting a certain
class.

This means that if alcohol is larger , it’s more likely to predict class
1.

The specific interpretation depends on the way the logistic regression
is implementing multi-class.

---

``` python
lr.predict_proba(X_test)[:5]
```

```out
array([[9.95266458e-01, 4.01748516e-03, 7.16056845e-04],
       [1.63653956e-04, 9.98254060e-01, 1.58228563e-03],
       [9.99727436e-01, 6.51962873e-05, 2.07367268e-04],
       [2.63305550e-05, 1.06213479e-05, 9.99963048e-01],
       [6.05493238e-06, 9.99151569e-01, 8.42375943e-04]])
```

``` python
lr.predict_proba(X_test[:5]).sum(axis=1)
```

```out
array([1., 1., 1., 1., 1.])
```

Notes:

If we look at the output of `predict_proba` you’ll also see that there
is a probability for each class and each row adds up to 1 as we would
expect (total probability = 1).

We can also sum them up per row and we can see they add up to 1 as well.

---

``` python
confusion_matrix(y_test, lr.predict(X_test))
```

```out
array([[19,  0,  0],
       [ 1, 16,  0],
       [ 0,  1,  8]])
```

``` python
plot_confusion_matrix(lr, X_test, y_test, display_labels=lr.classes_, cmap='Blues', values_format='d');
plt.show()
```

<img src="/module8/module8_17/unnamed-chunk-14-1.png" width="60%" style="display: block; margin: auto;" />

Note: Like we saw in Module 7, we can still create confusion matrices
but now they are greater than a 2 X 2 grid.

---

``` python
print(classification_report(y_test, lr.predict(X_test)))
```

```out
              precision    recall  f1-score   support

           0       0.95      1.00      0.97        19
           1       0.94      0.94      0.94        17
           2       1.00      0.89      0.94         9

    accuracy                           0.96        45
   macro avg       0.96      0.94      0.95        45
weighted avg       0.96      0.96      0.96        45
```

Notes:

Precision, recall, etc. don’t apply directly. But like we said before,
if we pick one of the classes as positive, and consider the rest to be
negative, then we can.

---

``` python
x_train_2d = X_train[['alcohol','malic_acid']]
x_train_2d.head()
```

```out
     alcohol  malic_acid
36     13.28        1.64
77     11.84        2.89
131    12.88        2.99
159    13.48        1.67
4      13.24        2.59
```

<img src="/module8/module8_17/unnamed-chunk-17-1.png" width="90%" style="display: block; margin: auto;" />

Notes:

We can also make the plots we made earlier in the course, but this time
with more classes.

In order for us to be able to plot this we need to select 2 features so
we are picking `alcohol` and `malic_acid`.

In this plot the colours are inconsisten wit the shapes. - The red
triangles correspond to the light blue predictions. - The black X’s
correspond to the red predictions/ - The blue circles (correctly)
correspond to the blue circles.

---

<img src="/module8/module8_17/unnamed-chunk-18-1.png" width="90%" style="display: block; margin: auto;" />

``` python
plot_classifier(x_train_2d, y_train, lr_2d,  ax=plt.gca(), ticks=True)
plt.xticks(fontsize= 14);
plt.yticks(fontsize= 14);
plt.xlabel("latitude", fontsize=14); plt.ylabel("logitude", fontsize=14)
plt.title("Logistic regression -multi classifications", fontsize=16)
```

<img src="/module8/module8_17/unnamed-chunk-19-1.png" width="1536" />

Notes:

## We can plot multi-class problems with other classifiers too. Here we can see the boundaries of the decision tree classifier as well as SVM with an RBF kernel.

# Let’s apply what we learned\!

Notes: <br>
