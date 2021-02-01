import pandas as pd
from sklearn.tree import DecisionTreeRegressor

# Loading in the data
canucks = pd.read_csv('data/canucks_subbed.csv')

# Define X and y
X = canucks.loc[:, ['No.', 'Age', 'Height', 'Weight', 'Experience']]
y = canucks['Salary']

# Create a model
reg_tree = DecisionTreeRegressor(random_state=1, max_depth=8)

# Fit your data 
reg_tree.fit(X,y)

# Score the model
tree_score = reg_tree.score(X, y)
tree_score