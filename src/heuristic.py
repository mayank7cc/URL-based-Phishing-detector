import re

def heuristic_score(url):

    score = 0
    reasons = []

    url = url.lower()

    if "@" in url:
        score += 20
        reasons.append("URL contains '@' symbol")

    if len(url) > 75:
        score += 15
        reasons.append("URL length unusually long")

    if url.count('-') > 3:
        score += 10
        reasons.append("Too many hyphens in URL")

    if re.search(r'\d', url):
        score += 10
        reasons.append("Digits present in URL")

    suspicious_words = [
        "login","verify","secure",
        "bank","update","account"
    ]

    if any(word in url for word in suspicious_words):
        score += 20
        reasons.append("Suspicious phishing keywords detected")

    if "http://" in url:
        score += 10
        reasons.append("Uses HTTP instead of HTTPS")

    if "//" in url[7:]:
        score += 10
        reasons.append("URL contains redirection pattern")

    return min(score,100), reasons