import pandas as pd
from sklearn.model_selection import train_test_splitfrom
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib

# Load the collected Reddit data from the CSV file

# Feature engineering
features = ['num_comments', 'upvote_ratio', 'hour', 'day_of_week', 'elapsed_time']
target = 'score'

# Split data into training and testing sets
X = df[features]
y = df[target]
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Initialize and train the RandomForest model
model = RandomForestRegressor(n_estimators=100, random_stat=42)
model.fit(X_train, y_train)

# Predict on the test set and calculate mean squared error
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}') # Print the model performance

# Save the trained model to a file
joblib.dump(model, 'model.pkl')