09.27.19
Srikant Sarangi

Use this script to connect to HubSpot via the Single-Send Transactional API

Notes:
    - Uses OAuth 2 authentication. Read here: https://developers.hubspot.com/docs/methods/oauth2/oauth2-overview
    - Requires the client_id and client_secret from an app you create in your HubSpot Developer Account
    - Generates code and access token. Use the access_token to generate refresh_token
    - Send email using the transaction id (for the template email in HubSpot), email address, and first name
    - Add other properties as set in HubSpot
