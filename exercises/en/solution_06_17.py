import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_validate
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer, make_column_transformer
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.neighbors import KNeighborsRegressor

# Loading in the data
bball_df = pd.read_csv('data/bball_imp.csv').dropna(subset=['salary'])

# Split the dataset
df_train, df_test = train_test_split(bball_df, test_size=0.2, random_state=7)

X_train = df_train[["weight", "height", "draft_year", "draft_round",
                     "draft_peak", "team", "position", "country"]]
X_test = df_test[["weight", "height", "draft_year", "draft_round",
                     "draft_peak", "team", "position", "country"]]
y_train = df_train['salary']
y_test = df_test['salary']


# Split the numeric and categorical features 
numeric_features = [ "weight",
                     "height",
                     "draft_year",
                     "draft_round",
                     "draft_peak"]

categorical_features = ["team", "position", "country"]

# Build a numeric pipeline
numeric_transformer = make_pipeline(
    SimpleImputer(strategy="median"),
    StandardScaler())

# Build a categorical pipeline
categorical_transformer = make_pipeline(
    SimpleImputer(strategy="most_frequent"),
    OneHotEncoder(handle_unknown="ignore"))

# Build a categorical transformer
col_transformer = make_column_transformer(
    (numeric_transformer, numeric_features),
    (categorical_transformer, categorical_features))

# Build a main pipeline
main_pipe = make_pipeline(
    col_transformer,
    KNeighborsRegressor())

# Cross validate
with_categorical_scores = cross_validate(main_pipe, X_train, y_train, return_train_score=True)
pd.DataFrame(with_categorical_scores)