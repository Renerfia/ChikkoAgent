import base64

from config.google_creds_config import verify_user_creds
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def read_gmail(message_count: int = 5):
    """Return Gmail messages as a list of dictionaries."""
    creds = verify_user_creds()  # Get valid Gmail login credentials.

    try:
        service = build("gmail", "v1", credentials=creds)
        # Get only the latest 5 message IDs.
        messages = service.users().messages().list(userId="me", labelIds=["CATEGORY_PERSONAL"], maxResults=message_count).execute().get("messages", [])
        result = []

        for item in messages:
            # Get full message details using the message ID.
            message = service.users().messages().get(userId="me", id=item["id"], format="full").execute()
            headers = message["payload"]["headers"]
            header = next((h["value"] for h in headers if h["name"].lower() == "from"), "")
            subject = next((h["value"] for h in headers if h["name"].lower() == "subject"), "")

            # Gmail can store the body directly or inside message parts.
            parts = message["payload"].get("parts", [])
            body_data = message["payload"].get("body", {}).get("data")
            if not body_data:
                plain_part = next((p for p in parts if p["mimeType"] == "text/plain"), None)
                if plain_part:
                    body_data = plain_part["body"].get("data")

            # Decode the Base64 Gmail body into normal text.
            body = base64.urlsafe_b64decode(body_data).decode("utf-8") if body_data else ""
            result.append({"header": header, "subject": subject, "body": body})

        return result
    except HttpError as error:
        print(f"An error occurred: {error}")
        return []


if __name__ == "__main__":
    print(read_gmail())