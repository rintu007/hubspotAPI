"""
Use this script to connect to HubSpot via the Single-Send Transactional API

Notes:
    - Uses OAuth 2 authentication. Read here: https://developers.hubspot.com/docs/methods/oauth2/oauth2-overview
    - Requires the client_id and client_secret from an app you create in your HubSpot Developer Account
    - Generates code and access token. Use the access_token to generate refresh_token
    - Send email using the transaction id (for the template email in HubSpot), email address, and first name
    - Add other properties as set in HubSpot

"""

import requests


# Hubspot Transactional Emails
def hubspot_trans(tId, cust_email, fname, headers):

    pURL = 'https://api.hubapi.com/email/public/v1/singleEmail/send'
    payload = {'emailId': tId, 'message': {'to': cust_email}, "contactProperties": [{"name": "firstname", "value": fname}]}

    r = requests.post(pURL, json=payload, headers=headers)


# Set up parameters for Hubspot Transactional API

# Get application code

client_id = 'xxxxxxxxx'
client_secret = 'xxxxxxxxxx'
redirect_uri = 'https://www.example.com/'

# Get access_token
payload = {
    'grant_type': 'authorization_code',
    'client_id': client_id,
    'client_secret': client_secret,
    'redirect_uri': redirect_uri,
    'code': 'xxxxxxxxxxx'
}

r = requests.post('https://api.hubapi.com/oauth/v1/token', data=payload)

# Refresh Tokens
refresh_payload = {
    'grant_type': 'refresh_token',
    'client_id': client_id,
    'client_secret': client_secret,
    'refresh_token': 'xxxxxxxxx'
}

if r.reason == 'Bad Request':
    rFresh = requests.post('https://api.hubapi.com/oauth/v1/token', data=refresh_payload)

responseDict = rFresh.json()

headers = {'Authorization': 'Bearer ' + str(responseDict['access_token']), 'Content-Type': 'application/json'}

# Send Email
tId = 12345678
cust_email = 'maxdog@dogs.com'
fname = 'Max'
hubspot_trans(tId, cust_email, fname, headers)