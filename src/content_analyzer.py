import requests
from bs4 import BeautifulSoup

PHISHING_TERMS = [
    "verify account",
    "confirm password",
    "bank login",
    "security alert",
    "update payment",
    "confirm identity",
    "account suspended",
    "login required"
]

def fetch_page(url):

    try:
        r = requests.get(url, timeout=5)
        return r.text, r.url
    except:
        return "", url


def analyze_content(html):

    if html == "":
        return 0, ["Page not reachable"]

    soup = BeautifulSoup(html, "html.parser")

    text = soup.get_text().lower()

    score = 0
    reasons = []

    for word in PHISHING_TERMS:
        if word in text:
            score += 20
            reasons.append(f"Phishing phrase detected: '{word}'")

    forms = soup.find_all("form")

    if forms:
        score += 20
        reasons.append("Page contains form inputs")

    inputs = soup.find_all("input")

    if len(inputs) > 10:
        score += 10
        reasons.append("Page has many input fields")

    if "password" in text:
        score += 20
        reasons.append("Password field detected")

    if "credit card" in text:
        score += 20
        reasons.append("Requests financial information")

    return min(score,100), reasons