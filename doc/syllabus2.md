## Introduction to Machine Learning 

## Module 1

By the end of the module, students are expected to:

- Explain motivation to study machine learning.
- Differentiate between supervised and unsupervised learning.
- Differentiate between classification and regression problems.
- Explain machine learning terminology such as features, targets, training, and error.
- Use DummyClassifier/ Dummy Regressor as a baseline for machine learning problems.
- Explain the `.fit()` and `.predict()` paradigm and use `.score()` method of ML models.

## Module 2

By the end of the module, students are expected to:

- Broadly describe how decision trees make predictions.
- Use `DecisionTreeClassifier()` and `DecisionTreeRegressor()` to build decision trees using scikit-learn.
- Explain the `.fit()` and `.predict()` paradigm and use `.score()` method of ML models.
- Explain the concept of decision boundaries.
- Explain the difference between parameters and hyperparameters.
- Explain how decision boundaries change with `max_depth`.
- Explain the concept of generalization.

## Module 3 

By the end of the module, students are expected to:

- Split a dataset into train and test sets using `train_test_split` function.
- Explain the difference between train, validation, test, and "deployment" data.
- Identify the difference between training error, validation error, and test error.
- Explain cross-validation and use `cross_val_score()` and `cross_validate()` to calculate cross-validation error.
- Explain overfitting, underfitting, and the fundamental tradeoff.
- State the golden rule and identify the scenarios when it's violated.

## Module 4 

By the end of the module, students are expected to:

- Explain the notion of similarity-based algorithms.
- Broadly describe how 𝑘-NNs use distances.
- Describe the effect of using a small/large value of the hyperparameter 𝑘 when using the 𝑘-NN algorithm.
- Explain the problem of curse of dimensionality.
- Explain the general idea of SVMs with RBF kernel.
- Compare and contrast 𝑘-NNs and SVM RBFs.
- Broadly describe the relation of `gamma` and `C` hyperparameters with the fundamental tradeoff.


## Module 5 

By the end of the module, students are expected to:

- Identify when to implement feature transformations such as imputation and scaling.
- Apply `sklearn.pipeline.Pipeline` to build a preliminary machine learning pipeline.
- Use `sklearn` for applying numerical feature transformations on the data.
- Discuss the golden rule in the context of feature transformations.
- Use `sklearn.pipeline.Pipeline` to build a preliminary machine learning pipeline.
- Carry out hyperparameter optimization using `sklearn`'s `GridSearchCV` and `RandomizedSearchCV`.
- Explain optimization bias.


## Module 6 
- Categorical variables -> one-hot, Ordinal encoding 
- ColumnTransformer
- Count vectorizor/ text classification (lecture 5? in 571) (SVM for text classification)
- Explain `handle_unknown="ignore"` hyperparameter of `scikit-learn`'s `OneHotEncoder`.
- Identify when it's appropriate to apply ordinal encoding vs one-hot encoding.
- Explain strategies to deal with categorical variables with too many categories.
- Explain why text data needs a different treatment than categorical variables.
- Use `scikit-learn`'s `CountVectorizer` to encode text data.
- Explain different hyperparameters of `CountVectorizer`.
- Use `ColumnTransformer` to build all our transformations together into one object and use it with `scikit-learn` pipelines.

## Module 7

Learning Outcomes:

- Explain why accuracy is not always the best metric in ML.
- Explain components of a confusion matrix.
- Define precision, recall, and f1-score and use them to evaluate different classifiers.
- Identify whether there is class imbalance and whether you need to deal with it.
- Explain and use the following methods to deal with data imbalance - `class_weight`
- Appropriately select a scoring metric given a regression problem.
- Interpret and communicate the meanings of different scoring metrics on regression problems.
MSE, RMSE, $R^2$, MAPE


Slide decks: 
1. Questioning accuracy - confusion matrix, Type I err type II error
1. Precision, recall, f1-score. False positives
1. Multi-class -> classification_report, confusion matrix, Macro average vs weighted average 
1. imbalanced datasets, and `class_weight`
1. Regression measurements: MSE, RMSE, $R^2$, MAPE
1. Passing different scoring methods ( `cross_validate` and `GridSearchCV`)

## Module 8

- Explain the general intuition behind linear models
- Explain the predict paradigm of linear models
- Use scikit-learn's LogisticRegression classifier and ridge regression. 
- Use fit, predict, predict_proba
- Use coef_ to interpret the model weights
- Explain the advantages and limitations of linear models

Slide decks:
1. Linear regression predict paradigm (feat * coef + feat* coef ... etc)
1. Coef_
1. LogisticRegression 
1. `predict_proba`
1. Multi-class regression -> coeficients (prob scores add to one pick largest.)







