import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, recall_score, precision_score, confusion_matrix, classification_report

# ISPS-VETA Clinical AI Simulation

data = [
    [2, 8, 8, 2, 0, 0, 0],
    [3, 7, 7, 3, 0, 0, 0],
    [5, 5, 5, 5, 1, 0, 1],
    [6, 4, 4, 6, 1, 1, 2],
    [8, 3, 3, 8, 1, 1, 3],
    [7, 4, 2, 7, 1, 1, 3],
    [4, 6, 6, 4, 0, 0, 1],
    [5, 5, 4, 6, 1, 0, 2],
    [6, 5, 3, 7, 1, 1, 2],
    [9, 2, 2, 9, 1, 1, 3],
]

df = pd.DataFrame(data, columns=[
    "stress","mood","sleep","cognitive_load",
    "repeated_distress","withdrawal","action"
])

X = df.drop("action", axis=1)
y = df["action"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Decision Tree": DecisionTreeClassifier(max_depth=4)
}

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print("\n", name)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Recall (Escalate=3):", recall_score(y_test, y_pred, labels=[3], average="macro", zero_division=0))
    print("Precision (Escalate=3):", precision_score(y_test, y_pred, labels=[3], average="macro", zero_division=0))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
