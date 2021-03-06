import numpy as np
import pandas as pd
import scipy
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
from sklearn.model_selection import train_test_split, cross_validate, GridSearchCV
from sklearn.linear_model import Ridge
from sklearn.metrics import  mean_squared_error, r2_score
from scipy.stats import randint
from sklearn.metrics import make_scorer

# Loading in the data
bball = pd.read_csv('data/bball.csv')
bball = bball[(bball['draft_year'] != 'Undrafted') & (bball['draft_round'] != 'Undrafted') & (bball['draft_peak'] != 'Undrafted')]

train_df, test_df = train_test_split(bball, test_size=0.2, random_state=1)

X_train = train_df[['height']]
y_train = train_df['weight']
X_test = test_df[['height']]
y_test = test_df['weight']

## Define mape function 
def mape(true, pred):
    return 100.*np.mean(np.abs((pred - true) / true))

## Create a mape scorer where lower number are better 
neg_mape_scorer = make_scorer(mape, greater_is_better=False)

# Create a set of values for alpha
param_dist = {
    "alpha": [0.1, 1, 10, 100, 1000, 10000]}

# Build a Ridge model called ridge_bb
ridge_bb = Ridge()

## Use GridSearchCV to hyperparameter tune. 
grid_search = GridSearchCV(
    ridge_bb, param_dist, cv=5,
    n_jobs=-1,
    scoring=neg_mape_scorer)

# Fit your grid search on the training data
grid_search.fit(X_train, y_train)

# What is the best value for alpha?
# Save it in an object named best_alpha
best_alpha = grid_search.best_params_
print(best_alpha)

# What is the best MAPE score?
# Save it in an object named best_mape
best_mape = grid_search.best_score_
print(best_mape)
