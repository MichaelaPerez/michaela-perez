from google.oauth2 import service_account
from googleapiclient.discovery import build

# Replace 'path/to/your/credentials.json' with the path to your credentials JSON file
credentials = service_account.Credentials.from_service_account_file(
    'path/to/your/credentials.json',
    scopes=['https://www.googleapis.com/auth/documents.readonly']
)

# Replace 'your-document-id' with the ID of your Google Docs document
document_id = 'your-document-id'

# Create the Google Docs API service
service = build('docs', 'v1', credentials=credentials)

# Retrieve the document content
document = service.documents().get(documentId=document_id).execute()
content = document['body']['content']

# Extract text content from the document
text_content = ''
for element in content:
    if 'paragraph' in element:
        for run in element['paragraph']['elements']:
            text_content += run.get('text', '')

print("Contents of the document as plain text:")
print(text_content)
