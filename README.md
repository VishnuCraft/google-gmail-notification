**Gmail Email Fetcher (Python)**

A simple Python script to fetch emails from a Gmail account using the Gmail API.

**Features**
Authenticate via Google OAuth 2.0.

Fetch and display email snippets, subject, and sender.

**Requirements**

Python 3.6+

**Install dependencies:**

pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

**Google Cloud Setup:**

Enable the Gmail API on [Google Cloud Console](https://console.cloud.google.com/).

Create OAuth 2.0 credentials and download credentials.json.

Run the Script:

Place credentials.json in the project directory.

**Run the script:**

python gmail_fetcher.py

Authorize via browser and get access to Gmail.
