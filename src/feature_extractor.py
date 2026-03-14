import re
from urllib.parse import urlparse
import tldextract

def extract_features(url):

    parsed = urlparse(url)
    ext = tldextract.extract(url)

    features = []

    features.append(len(url))
    features.append(url.count('.'))
    features.append(url.count('-'))
    features.append(url.count('/'))
    features.append(url.count('?'))
    features.append(url.count('='))

    features.append(1 if parsed.scheme == "https" else 0)

    features.append(len(parsed.netloc))

    features.append(1 if re.search(r'\d', parsed.netloc) else 0)

    features.append(len(ext.subdomain))
    features.append(len(ext.domain))
    features.append(len(ext.suffix))

    suspicious_words = [
        "login","secure","bank","update",
        "account","verify","password","confirm"
    ]

    features.append(
        1 if any(word in url.lower() for word in suspicious_words) else 0
    )

    features.append(
        1 if parsed.netloc.replace('.', '').isdigit() else 0
    )

    return features