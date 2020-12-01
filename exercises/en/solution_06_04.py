import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder

# Loading in the data
bball_df = pd.read_csv('data/bball.csv')
bball_df = bball_df[(bball_df['position'] =='G') | (bball_df['position'] =='F')]

# Split the dataset
df_train, df_test = train_test_split(bball_df, test_size=0.2, random_state=7)
X_column = df_train[['country']]

# Build the tranformer and fit on it 
ordinal_encoder = OrdinalEncoder(dtype=int)
ordinal_encoder.fit(X_column);

# Transform the column country
country_encoded = ordinal_encoder.transform(X_column)

# Let's see which country's correspond with each encoding value
encoding_view = X_column.assign(country_enc=country_encoded).drop_duplicates()
encoding_view