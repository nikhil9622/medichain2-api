import hashlib
from typing import List, Tuple


def _float_from_hash(h: str) -> float:
    # Convert a hex digest slice into a deterministic float in [0,1)
    return int(h[:16], 16) / float(0xFFFFFFFFFFFFFFFF)


def compute_anomaly_score(feature_vector: List[float]) -> Tuple[float, int]:
    """
    Lightweight deterministic anomaly scorer that avoids heavy native deps.

    Returns (score, pred) where score is 0..1 and pred is 1 (likely authentic)
    or -1 (suspicious). This is a heuristic used for demo/testing only.
    """
    # Create a stable representation of the features
    s = ",".join(str(x) for x in feature_vector).encode("utf-8")
    h = hashlib.sha256(s).hexdigest()
    score = _float_from_hash(h)

    # Heuristic: treat values in the lower tail as more likely anomalous.
    # Thresholds are arbitrary for demo; tune or replace with a real model later.
    pred = 1 if score > 0.2 else -1
    return round(score, 3), pred
