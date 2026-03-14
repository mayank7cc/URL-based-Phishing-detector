import joblib
from feature_extractor import extract_features
from heuristic import heuristic_score
from content_analyzer import fetch_page, analyze_content

model = joblib.load("../model/phishing_model.pkl")


def predict_url(url):

    # ML score
    features = extract_features(url)

    ml_prob = model.predict_proba([features])[0][1]

    # heuristic score
    rule_score, rule_reasons = heuristic_score(url)

    # fetch webpage
    html, final_url = fetch_page(url)

    content_score, content_reasons = analyze_content(html)

    rule_score = rule_score / 100
    content_score = content_score / 100

    # final weighted score
    final_score = (
        ml_prob * 0.5 +
        rule_score * 0.25 +
        content_score * 0.25
    )

    # categorization
    if final_score > 0.8:
        category = "High Risk Phishing"

    elif final_score > 0.5:
        category = "Suspicious URL"

    else:
        category = "Safe URL"

    reasons = list(set(rule_reasons + content_reasons))

    return ml_prob, rule_score, content_score, final_score, category, reasons


if __name__ == "__main__":

    url = input("Enter URL: ")

    ml, rule, content, final, category, reasons = predict_url(url)

    print("\nML Score:", round(ml,2))
    print("Rule Score:", round(rule,2))
    print("Content Score:", round(content,2))
    print("Final Risk Score:", round(final,2))

    print("\nCategory:", category)

    print("\nReasons:")
    for r in reasons:
        print("-", r)