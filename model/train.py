# import random
# from joblib import dump

# import numpy as np
# from sklearn.ensemble import IsolationForest

# rng = np.random.RandomState(42)

# # Generate train data
# X = 0.3 * rng.randn(500, 2)
# X_train = np.r_[X + 2, X - 2]
# X_train = np.round(X_train, 3)

# # fit the model
# clf = IsolationForest(n_estimators=50, max_samples=500,
#                       random_state=rng, contamination=0.01)
# clf.fit(X_train)

# dump(clf, './isolation_forest.joblib')

from sklearn.pipeline import Pipeline
from joblib import dump
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

# Load the training data from a CSV file
train_file_path = 'Train_data.csv'
df_train = pd.read_csv(train_file_path)

# Assuming you have a column named 'label' indicating normal (0) or anomalous (1) instances
X_train = df_train.drop('class', axis=1)
y_train = df_train['class']

# Identify categorical columns
categorical_cols = X_train.select_dtypes(include=['object']).columns.tolist()

# Create a transformer for one-hot encoding
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(), categorical_cols)
    ],
    remainder='passthrough'
)

# Instantiate the Random Forest Classifier
clf = RandomForestClassifier(n_estimators=50, random_state=42)

# Create a pipeline with preprocessing and the classifier
pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                           ('classifier', clf)])

# Fit the model on the training data
pipeline.fit(X_train, y_train)

# Save the trained model to a file using joblib
dump(pipeline, './random_forest_classifier.joblib')
