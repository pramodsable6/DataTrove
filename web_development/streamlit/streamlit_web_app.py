import streamlit as st
import pandas as pd
import os
from datetime import datetime
from authlib.integrations.requests_client import OAuth2Session
import requests

# Configuration
OIDC_CLIENT_ID = "xxxxxxxxx"
OIDC_CLIENT_SECRET = "xxxxxxxxxxxx"
OIDC_AUTH_URL = "https://accounts.google.com/o/oauth2/v2/auth"  # Replace with your provider's auth URL
OIDC_TOKEN_URL = "https://oauth2.googleapis.com/token"  # Replace with your provider's token URL
OIDC_REDIRECT_URI = "http://localhost:8501"  # Streamlit default URI
OIDC_USER_INFO_URL = "https://openidconnect.googleapis.com/v1/userinfo"  # Replace with your provider's user info endpoint
# File path to store data
DOWNLOAD_PATH = '/root/Work/Repositories/study_notes/training/web_development/streamlit/data.csv'

# Initialize OAuth client
oauth_client = OAuth2Session(
    OIDC_CLIENT_ID,
    OIDC_CLIENT_SECRET,
    redirect_uri=OIDC_REDIRECT_URI,
    scope="openid profile email",
)

# Load data from CSV
def load_data():
    if os.path.exists(DOWNLOAD_PATH):
        return pd.read_csv(DOWNLOAD_PATH, index_col=0)
    else:
        return pd.DataFrame(columns=["Name", "Email", "Age", "last_updated", "active"])

# Save data to CSV
def save_data(data):
    data.to_csv(DOWNLOAD_PATH)

# Identify inserted, updated, and deleted records
def identify_changes(original_df, updated_df):
    original_df = original_df.sort_index()
    updated_df = updated_df.sort_index()

    # Inserted records
    inserted_records = updated_df[~updated_df.index.isin(original_df.index)]

    # Deleted records
    deleted_records = original_df[~original_df.index.isin(updated_df.index)]

    # Updated records
    common_indices = original_df.index.intersection(updated_df.index)
    updated_records = updated_df.loc[common_indices][
        (original_df.loc[common_indices] != updated_df.loc[common_indices]).any(axis=1)
    ]

    return {
        "inserted": inserted_records,
        "updated": updated_records,
        "deleted": deleted_records
    }

# Handle OIDC authentication
def oidc_auth_app():
    st.title("OIDC Authentication Streamlit App")

    if "token" not in st.session_state:
        st.session_state.token = None

    # Start login flow
    if st.session_state.token is None:
        st.write("You are not logged in.")
        login_button = st.button("Login")

        if login_button:
            authorization_url, state = oauth_client.create_authorization_url(OIDC_AUTH_URL)
            st.session_state.state = state
            st.markdown(f"[Click here to authenticate]({authorization_url})")
    else:
        try:
            token = st.session_state.token
            headers = {"Authorization": f"Bearer {token['access_token']}"}
            response = requests.get(OIDC_USER_INFO_URL, headers=headers)

            if response.status_code == 200:
                user_info = response.json()
                st.write(f"Welcome, {user_info.get('name', 'User')}!")
                table_page()
            else:
                st.error("Failed to fetch user information. Please log in again.")
        except Exception as e:
            st.error(f"Authentication error: {e}")

    if st.button("Logout"):
        st.session_state.token = None
        st.write("Logged out successfully.")

# Data management page
def table_page():
    st.subheader("Data Management")

    # Load original data
    original_data = load_data()

    # Ensure required columns exist
    if "last_updated" not in original_data.columns:
        original_data["last_updated"] = None
    if "active" not in original_data.columns:
        original_data["active"] = True

    # Use Streamlit data editor with num_rows="dynamic" for row management
    st.write("### Editable Table")
    updated_data = st.data_editor(
        original_data,
        num_rows="dynamic",
        key="data_editor",
        use_container_width=True
    )

    # Identify changes (inserted, updated, and deleted rows)
    changes = identify_changes(original_data, updated_data)

    # Save changes
    if st.button("Save Changes"):
        # Update timestamps for inserted and updated records
        if not changes["inserted"].empty:
            changes["inserted"]["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if not changes["updated"].empty:
            changes["updated"]["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Save updated data
        save_data(updated_data)

        # Display changes to the user
        st.success("Changes saved successfully!")
        st.write("### Inserted Records")
        st.dataframe(changes["inserted"])
        st.write("### Updated Records")
        st.dataframe(changes["updated"])
        st.write("### Deleted Records")
        st.dataframe(changes["deleted"])

# Main function
def main():
    # Handle OIDC callback
    if st.query_params.get("code"):
        try:
            # Exchange the authorization code for a token
            code = st.query_params["code"]
            token = oauth_client.fetch_token(OIDC_TOKEN_URL, code=code, redirect_uri=OIDC_REDIRECT_URI)
            st.session_state.token = token
            
            # Clear authorization code from memory after token exchange
            st.session_state.code = None

        except Exception as e:
            st.error(f"Token exchange failed: {e}")
            # st.write("Debugging Info:", {"code": code, "redirect_uri": OIDC_REDIRECT_URI})

    oidc_auth_app()

if __name__ == "__main__":
    main()
