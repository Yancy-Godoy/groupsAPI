from distutils.command.build import build
from pprint import pprint
from tokenize import group
from google.oauth2 import service_account
import googleapiclient.discovery

# Scopes required by this endpoint ->  https://developers.google.com/admin-sdk/directory/reference/rest/v1/groups/insert
SCOPES = [
    'https://apps-apis.google.com/a/feeds/groups/',
    'https://www.googleapis.com/auth/admin.directory.group',
    'https://www.googleapis.com/auth/admin.directory.group.readonly']

# Service Account Credentials to be used. How to create at https://developers.google.com/workspace/guides/create-credentials#service-account
SERVICE_ACCOUNT_FILE = 'groups.json'


credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
delegated_credentials = credentials.with_subject('SuperAdmin@YourDomain.xyz') # Super Admin account to be impersonated by the Service account created

service = googleapiclient.discovery.build('admin', 'directory_v1', credentials=delegated_credentials)

mydomain = '@YourDomain.xyz' #This, in case you have different domains and you want to create a group for one in specific.
group_name = 'creating a group using APIs'
group_email = 'usernameGroup'+ '@'+ mydomain
group_description = 'This is a test group created using APIs'

def create_group(group_name, group_email, group_description):
    body = {
        'email': group_email,
        'name': group_name,
        'description': group_description
    }
    return service.groups().insert(body=body).execute()

results = create_group(group_name, group_email, group_description)

pprint(results)
