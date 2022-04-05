from google.oauth2 import service_account
import googleapiclient.discovery

# Scopes required by this endpoint ->  https://developers.google.com/admin-sdk/directory/reference/rest/v1/groups/list
SCOPES = [
    'https://apps-apis.google.com/a/feeds/groups/',
    'https://www.googleapis.com/auth/admin.directory.group',
    'https://www.googleapis.com/auth/admin.directory.group.readonly']

# Service Account Credentials to be used. How to create at https://developers.google.com/workspace/guides/create-credentials#service-account
SERVICE_ACCOUNT_FILE = 'groups.json'

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
delegated_credentials = credentials.with_subject(
    'SuperAdmin@YourDomain.xyz') # Super Admin account to be impersonated by the Service account created

service = googleapiclient.discovery.build(
    'admin', 'directory_v1', credentials=delegated_credentials)

def groupList():
    pageToken = None
    while True:
        response = service.groups().list(
            customer='my_customer',
            maxResults=25,
            pageToken=pageToken).execute()
        for group in response.get('groups', []):
            print(group['name'], group['email'])
        pageToken = response.get('nextPageToken', None)
        if not pageToken:
            break

groupList()
