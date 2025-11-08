import numpy as np
from sklearn.ensemble import IsolationForest

# lightweight in-memory model; for production, train separately and load model file
def compute_anomaly_score(feature_vector: list):
    # expect list of numeric features (length 3 recommended)
    X = np.random.normal(0.5, 0.2, (200, len(feature_vector)))
    clf = IsolationForest(contamination=0.05, random_state=42)
    clf.fit(X)
    score = float(clf.decision_function(np.array([feature_vector]))[0])
    pred = int(clf.predict(np.array([feature_vector]))[0])
    # normalize score between 0..1 roughly
    norm_score = (score + 0.5) / 1.5
    return max(0.0, min(1.0, round(norm_score, 3))), pred  # (score, pred)
