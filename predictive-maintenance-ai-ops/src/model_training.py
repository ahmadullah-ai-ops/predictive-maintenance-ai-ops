import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load the data
data = pd.read_csv('data/sample_logs.csv')
X = data[['cpu_usage', 'memory_usage', 'network_activity']]
y = data['anomaly']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the model
import joblib
joblib.dump(model, 'model.pkl')
print("Model trained and saved successfully.")

