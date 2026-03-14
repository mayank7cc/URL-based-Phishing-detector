# URL Phishing Detection System

This project implements a machine learning based cybersecurity system designed to detect malicious or phishing URLs. The system analyzes URLs using a combination of machine learning prediction, heuristic security rules, and webpage content inspection. It evaluates the risk associated with a URL, assigns a threat category, and provides explainable reasons for why a URL may be suspicious or malicious.

The goal of this system is to simulate real-world phishing detection mechanisms used in email security filters, browser security tools, and automated cybersecurity monitoring systems.

---------------------------------------------------------------------

## System Overview

The system processes a URL through multiple analysis layers. First, structural features of the URL are extracted. These features are used by a trained machine learning model to estimate the probability that the URL is malicious. Then heuristic rules are applied to detect common phishing indicators such as suspicious keywords, abnormal URL structure, or insecure protocols. Finally, the system inspects the webpage content to identify forms, password fields, or phishing phrases.

The outputs of these components are combined to generate a final risk score and threat category along with human readable explanations.

---------------------------------------------------------------------

## Architecture

URL Input  
↓  
Feature Extraction  
↓  
Machine Learning Prediction  
↓  
Heuristic Security Analysis  
↓  
Webpage Content Analyzer  
↓  
Risk Score Calculation  
↓  
Threat Categorization  
↓  
Explainable Detection Reasons

---------------------------------------------------------------------

## Project Structure

url-phishing-detector

data  
urldata.csv  

model  
phishing_model.pkl  

src  
train_model.py  
predict.py  
feature_extractor.py  
heuristic.py  
content_analyzer.py  

README.md

---------------------------------------------------------------------

## Installation

Clone the repository

git clone https://github.com/yourusername/url-phishing-detector.git

Navigate to the project directory

cd url-phishing-detector

Install required dependencies

pip install pandas scikit-learn requests beautifulsoup4 tldextract joblib

---------------------------------------------------------------------

## Training the Model

The machine learning model is trained using a dataset containing labeled URLs. The training process extracts structural features from URLs and uses a Random Forest classifier to learn patterns associated with phishing websites.

Run the training script

cd src  
python train_model.py

The training process will

Load the dataset  
Extract URL structural features  
Train the Random Forest model  
Evaluate model accuracy  
Save the trained model

Example output

Accuracy: 0.94  
Model saved successfully

---------------------------------------------------------------------

## Running URL Detection

To analyze a URL, run the prediction script

python predict.py

Enter the URL when prompted

Enter URL: https://example.com

The system will fetch the webpage, analyze the URL structure, apply heuristic checks, inspect the webpage content, and return a risk score and classification.

---------------------------------------------------------------------

## Example Safe URL

Input

https://www.google.com

Output

ML Score: 0.03  
Rule Score: 0.02  
Content Score: 0.00  

Final Risk Score: 0.02  
Category: Safe URL  

Reasons  
No suspicious indicators detected

---------------------------------------------------------------------

## Example Suspicious URL

Input

https://secure-login-update-account.com

Output

ML Score: 0.61  
Rule Score: 0.40  
Content Score: 0.15  

Final Risk Score: 0.49  
Category: Suspicious URL  

Reasons  
Suspicious phishing keywords detected  
URL length unusually long

---------------------------------------------------------------------

## Example Malicious URL

Input

http://bit.ly/login-bank-update

Output

ML Score: 0.82  
Rule Score: 0.70  
Content Score: 0.45  

Final Risk Score: 0.73  
Category: High Risk Phishing  

Reasons  
Uses HTTP instead of HTTPS  
Suspicious phishing keywords detected  
URL contains redirection pattern  
Page contains form inputs

---------------------------------------------------------------------

## Detection Indicators

The system evaluates URLs using multiple indicators.

URL Structural Features

URL length  
Number of subdomains  
Domain structure  
Digits present in domain  
Presence of suspicious keywords  

Heuristic Indicators

Use of HTTP instead of HTTPS  
Excessive hyphens in URL  
Redirection patterns  
Presence of special characters such as @  
Suspicious keyword patterns  

Content Analysis Indicators

Presence of login forms  
Password input fields  
Credential request forms  
Phishing phrases such as verify account or confirm password  
Requests for financial or personal information

---------------------------------------------------------------------

## Threat Categories

Risk Score 0.00 to 0.49  
Category Safe URL  

Risk Score 0.50 to 0.79  
Category Suspicious URL  

Risk Score 0.80 to 1.00  
Category High Risk Phishing

---------------------------------------------------------------------

## Use Cases

Email phishing detection systems  
Browser security extensions  
Cybersecurity automation workflows  
Email security pipelines  
Integration with automation platforms such as n8n

---------------------------------------------------------------------

## Future Improvements

Domain reputation checking  
WHOIS domain age analysis  
Real time phishing database integration  
Browser extension deployment  
Integration with email threat detection systems

---------------------------------------------------------------------

## License

This project is licensed under the MIT License.

---------------------------------------------------------------------

## Contributing

Contributions are welcome.  
Issues and pull requests can be submitted to improve the phishing detection system.
