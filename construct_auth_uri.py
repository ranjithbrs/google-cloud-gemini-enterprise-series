"""
Construct OAuth 2.0 Authorization URI for Gemini Enterprise ADK Agent.
"""
import urllib.parse

# Replace with your OAuth 2.0 Web Application Client ID
CLIENT_ID = "847135957020-20pask95ja318hv1gc1oumhg0opavppe.apps.googleusercontent.com"
REDIRECT_URI = "https://vertexaisearch.cloud.google.com/static/oauth/oauth.html"
SCOPES = ["https://www.googleapis.com/auth/bigquery"]

params = {
    "client_id": CLIENT_ID,
    "redirect_uri": REDIRECT_URI,
    "include_granted_scopes": "true",
    "response_type": "code",
    "access_type": "offline",
    "prompt": "consent",
    "scope": " ".join(SCOPES),
}

auth_url = f"https://accounts.google.com/o/oauth2/v2/auth?{urllib.parse.urlencode(params)}"

if __name__ == "__main__":
    print("Auth URI:\n")
    print(auth_url)
