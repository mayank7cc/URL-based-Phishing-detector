import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from feature_extractor import extract_features

# Load dataset
data = pd.read_csv("../data/urldata.csv")

# normalize column names
data.columns = data.columns.str.strip().str.lower()

print("Detected columns:", data.columns)

# detect URL column automatically
if "url" not in data.columns:
    
    for col in data.columns:
        if "url" in col or "domain" in col or "website" in col:
            data["url"] = data[col]
            break

# detect label column automatically
if "label" not in data.columns:

    if "result" in data.columns:
        data["label"] = data["result"]

    elif "type" in data.columns:
        data["label"] = data["type"].map({
            "benign":0,
            "phishing":1,
            "malware":1
        })

    else:
        raise Exception("No label column found")

# remove empty rows
data = data.dropna()

print("Dataset size:", data.shape)

# extract features
data["features"] = data["url"].apply(extract_features)

X = pd.DataFrame(data["features"].tolist())
y = data["label"].astype(int)

# split
X_train, X_test, y_train, y_test = train_test_split(
    X,y,test_size=0.2,random_state=42
)

# model
model = RandomForestClassifier(
    n_estimators=200,
    max_depth=25,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train,y_train)

pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test,pred))

# save model
joblib.dump(model,"../model/phishing_model.pkl")

print("Model saved successfully")