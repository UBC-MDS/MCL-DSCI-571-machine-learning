---
type: slides
---

# Passing Different Scoring Methods

Notes: <br>

---

``` python
housing_df = pd.read_csv("data/housing.csv")
train_df, test_df = train_test_split(housing_df, test_size=0.1, random_state=123)
```

``` python
X_train = train_df.drop(columns=["median_house_value"])
y_train = train_df["median_house_value"]
X_test = test_df.drop(columns=["median_house_value"])
y_test = test_df["median_house_value"]

numeric_features = [ "longitude", "latitude",
                     "housing_median_age",
                     "households", "median_income",
                     "rooms_per_household",
                     "bedrooms_per_household",
                     "population_per_household"]
                     
categorical_features = ["ocean_proximity"]

X_train.head()
```

```out
       longitude  latitude  housing_median_age  households  median_income ocean_proximity  rooms_per_household  bedrooms_per_household  population_per_household
6051     -117.75     34.04                22.0       602.0         3.1250          INLAND             4.897010                1.056478                  4.318937
20113    -119.57     37.94                17.0        20.0         3.4861          INLAND            17.300000                6.500000                  2.550000
14289    -117.13     32.74                46.0       708.0         2.6604      NEAR OCEAN             4.738701                1.084746                  2.057910
13665    -117.31     34.02                18.0       285.0         5.2139          INLAND             5.733333                0.961404                  3.154386
14471    -117.23     32.88                18.0      1458.0         1.8580      NEAR OCEAN             3.817558                1.004801                  4.323045
```

Notes:

We now know about all these metrics; how do we implement them?

We are lucky because it’s relatively easy and can be applied to both
classification and regression problems.

Let’s start with regression and our regression measurements.

This means bringing back our California housing dataset.

---

``` python
numeric_transformer = Pipeline(
    steps=[("imputer", SimpleImputer(strategy="median")), 
           ("scaler", StandardScaler())]
)

categorical_transformer = Pipeline(
    steps=[("imputer", SimpleImputer(strategy="constant", fill_value="missing")),
           ("onehot", OneHotEncoder(handle_unknown="ignore"))]
)

preprocessor = make_column_transformer(
(numeric_transformer, numeric_features),
        (categorical_transformer, categorical_features), 
    remainder='passthrough')

pipe_regression = make_pipeline(preprocessor, KNeighborsRegressor())
```

Notes:

We need to build our pipelines as usual.

---

## Cross-validation

``` python
pd.DataFrame(cross_validate(pipe_regression, X_train, y_train, return_train_score=True, scoring = 'neg_root_mean_squared_error'))
```

```out
   fit_time  score_time    test_score   train_score
0  0.064406    0.338107 -62462.584290 -51440.540539
1  0.049501    0.304557 -63437.715015 -51263.979666
2  0.048282    0.281229 -62613.202523 -51758.817852
3  0.040053    0.284780 -64204.295214 -51343.743586
4  0.033643    0.221234 -59217.838633 -47325.157312
```

Notes:

Normally after building our pipelines, we would now either do
cross-validation or hyperparameter tuning but let’s start with the
`cross_validate()` function.

All the possible scoring metrics that this argument accepts is available
<a href="https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter" target="_blank">here</a>.

In this case, if we wanted the RMSE measure, we would specify
`neg_mean_squared_error` and the negated value of the metric will be
returned in our dataframe.

---

``` python
from sklearn.metrics import make_scorer
```

``` python
def mape(true, pred):
    return 100.*np.mean(np.abs((pred - true)/true))
```

``` python
mape_scorer = make_scorer(mape)
```

``` python
pd.DataFrame(cross_validate(
    pipe_regression, X_train, y_train, return_train_score=True, scoring=mape_scorer))
```

```out
   fit_time  score_time  test_score  train_score
0  0.038291    0.278258   22.709732    18.420969
1  0.034654    0.271351   22.754570    18.469125
2  0.034678    0.272321   22.236869    18.674964
3  0.035442    0.283257   23.016666    18.510766
4  0.032455    0.223162   21.033519    16.951021
```

Notes:

Sometimes they don’t have the scoring measure that we want and that’s
ok.

We can make our own using the `make_scorer` from sklearn.

We must first make our own measurement function and convert it into a
format that the `scoring` argument will understand.

First, we import `make_scorer` from `Sklearn`.

Next, we can make a function calculating our desired measurement. In
this case, we are making a function that has the true and predicted
values as inputs and then returns the Mean Absolute percentage Error.

We can turn this into something that the `scoring` argument will
understand but putting our created MAPE function as an input argument in
`make_scorer()`.

Now when we cross-validate, we can specify the new `mape_scorer` as our
measure.

---

``` python
scoring={
    "r2": "r2",
    "mape_score": mape_scorer,
    "neg_rmse": "neg_root_mean_squared_error",    
    "neg_mse": "neg_mean_squared_error",    
}

pd.DataFrame(cross_validate(pipe_regression, X_train, y_train, return_train_score=True, scoring=scoring))
```

```out
   fit_time  score_time   test_r2  train_r2  test_mape_score  train_mape_score  test_neg_rmse  train_neg_rmse  test_neg_mse  train_neg_mse
0  0.036338    0.291813  0.695818  0.801659        22.709732         18.420969  -62462.584290   -51440.540539 -3.901574e+09  -2.646129e+09
1  0.034947    0.253969  0.707483  0.799575        22.754570         18.469125  -63437.715015   -51263.979666 -4.024344e+09  -2.627996e+09
2  0.039101    0.267516  0.713788  0.795944        22.236869         18.674964  -62613.202523   -51758.817852 -3.920413e+09  -2.678975e+09
3  0.033594    0.273241  0.686938  0.801232        23.016666         18.510766  -64204.295214   -51343.743586 -4.122192e+09  -2.636180e+09
4  0.032988    0.230674  0.724608  0.832498        21.033519         16.951021  -59217.838633   -47325.157312 -3.506752e+09  -2.239671e+09
```

Notes: We can also return many scoring measures by first making a
dictionary and then specifying the dictionary in the `scoring` argument.

---

## What about hyperparameter tuning?

``` python
pipe_regression = make_pipeline(preprocessor, KNeighborsRegressor())

param_grid = {"kneighborsregressor__n_neighbors": [2, 5, 50, 100]}
```

``` python
grid_search = GridSearchCV(pipe_regression, param_grid, cv=5, return_train_score=True, n_jobs=-1, scoring= mape_scorer);
grid_search.fit(X_train, y_train);
```

``` python
grid_search.best_params_
```

```out
{'kneighborsregressor__n_neighbors': 100}
```

``` python
grid_search.best_score_
```

```out
24.63336199650092
```

Notes:

We can do exactly the same thing we saw above with `cross_validate()`
but instead with `GridSearchCV` and `RandomizedSearchCV`.

Ok wait hold on, let’s think about this again.

The way that `best_params_` works is that it selects the parameters
where the scoring measure selected is the highest measure, the problem
with that is MAPE is an error, and we want the parameter with the lowest
value, not the highest.

---

``` python
neg_mape_scorer = make_scorer(mape, greater_is_better=False)
```

``` python
param_grid = {"kneighborsregressor__n_neighbors": [2, 5, 50, 100]}

grid_search = GridSearchCV(pipe_regression, param_grid, cv=5,
                           return_train_score=True, verbose=1,
                           n_jobs=-1, scoring= neg_mape_scorer)
grid_search.fit(X_train, y_train);
```

```out
Fitting 5 folds for each of 4 candidates, totalling 20 fits

[Parallel(n_jobs=-1)]: Using backend LokyBackend with 8 concurrent workers.
[Parallel(n_jobs=-1)]: Done  20 out of  20 | elapsed:   19.1s finished
```

``` python
grid_search.best_params_
```

```out
{'kneighborsregressor__n_neighbors': 5}
```

``` python
grid_search.best_score_
```

```out
-22.350271196169718
```

Notes:

We can create a new MAPE scorer by adding the argument
`greater_is_better=False`. Now our `best_params_` will return the
parameters will the lowest MAPE (least amount of error).

That’s better\!

---

## Classification

``` python
cc_df = pd.read_csv('data/creditcard.csv', encoding='latin-1')
train_df, test_df = train_test_split(cc_df, test_size=0.3, random_state=111)

X_train, y_train = train_df.drop(columns=["Class"]), train_df["Class"]
X_test, y_test = test_df.drop(columns=["Class"]), test_df["Class"]
```

Notes:

Let’s bring back our credit card data set and build our pipeline.

---

``` python
dt_model = DecisionTreeClassifier(random_state=123, class_weight='balanced')
```

``` python
param_grid = {"max_depth": scipy.stats.randint(low=1, high=100)}
```

``` python
grid_search = RandomizedSearchCV(dt_model, param_grid, cv=5, return_train_score=True,
                           verbose=1, n_jobs=-1, scoring= 'f1', n_iter = 6)
grid_search.fit(X_train, y_train);
```

```out
Fitting 5 folds for each of 6 candidates, totalling 30 fits

[Parallel(n_jobs=-1)]: Using backend LokyBackend with 8 concurrent workers.
[Parallel(n_jobs=-1)]: Done  30 out of  30 | elapsed:   44.5s finished
```

``` python
grid_search.best_params_
```

```out
{'max_depth': 36}
```

``` python
grid_search.best_score_
```

```out
0.7212894838664344
```

Notes:

This time we are going to use `class_weight='balanced'` in our
Classifier.

Now we can tune our model for the thing we care about, in this case we
are specifying the `f1` score.

---

# Let’s apply what we learned\!

Notes: <br>
