from google.oauth2 import service_account
import googleapiclient.discovery

SCOPES = ['https://www.googleapis.com/auth/cloud-identity.groups']
SERVICE_ACCOUNT_FILE = 'groups.json'

def create_service():
  credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
  delegated_credentials = credentials.with_subject('yancymelany@support-domain29.xyz')

  service_name = 'cloudidentity'
  api_version = 'v1'
  
  service = googleapiclient.discovery.build(
    service_name,
    api_version,
    credentials=delegated credentials)

  return service