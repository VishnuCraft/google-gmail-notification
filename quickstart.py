import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Define the required Gmail API scope
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

def main():
    """Fetches emails under the specified label using Gmail API."""
    creds = None
    # The token.json stores the user's access and refresh tokens
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    # If there are no valid credentials, request the user to log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=8080)

        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        # Build the Gmail API service
        service = build("gmail", "v1", credentials=creds)

        # List available Gmail labels (optional)
        results = service.users().labels().list(userId="me").execute()
        labels = results.get("labels", [])
        if labels:
            print("Gmail Labels:")
            for label in labels:
                print(f"Label: {label['name']}")

        # Specify a label to fetch messages from
        label_id = "INBOX"  # Change to another label as needed (e.g., "CATEGORY_PROMOTIONS")

        # Fetch emails under a specific label
        results = service.users().messages().list(userId="me", labelIds=[label_id]).execute()
        messages = results.get("messages", [])

        if not messages:
            print("No emails found under the label.")
        else:
            print(f"Emails under {label_id}:")
            for message in messages[:5]:  # Limit to first 5 messages (adjust as needed)
                msg = service.users().messages().get(userId="me", id=message["id"]).execute()
                
                # Extracting the subject from the email headers
                subject = "No Subject"  # Default value if subject is not found
                for header in msg["payload"]["headers"]:
                    if header["name"] == "Subject":
                        subject = header["value"]
                        break

                # Print the message ID, subject, and snippet
                print(f"Message ID: {msg['id']}")
                print(f"Subject: {subject}")
                print(f"Snippet: {msg['snippet']}")
                print("-" * 50)

    except HttpError as error:
        print(f"An error occurred: {error}")

if __name__ == "__main__":
    main()
