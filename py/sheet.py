import gspread
from google.oauth2 import service_account
import json
# Set up credentials
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
# credentials = service_account.Credentials.from_service_account_file("google-oauth-secret.json").with_scopes(scope)
# gc = gspread.authorize(credentials)
gc = gspread.oauth(
    credentials_filename='google-oauth-secret.json',
    authorized_user_filename="authed-users.json"
)


# Open the Google Sheets spreadsheet using its title or URL
# Replace 'Your Spreadsheet Title' with the title of your spreadsheet
# or replace 'Your Spreadsheet URL' with the URL of your spreadsheet
# spreadsheet = gc.open("Your Spreadsheet Title")  # or gc.open_by_url("Your Spreadsheet URL")
spreadsheet = gc.open_by_url("https://docs.google.com/spreadsheets/d/17stqNpvbFzflmh11bq779kbpxerlaq0Ne73s9HSLQRQ/edit#gid=0")

# Select the worksheet by title
# Replace 'Your Worksheet Title' with the title of your worksheet
worksheet = spreadsheet.worksheet("Sheet1")

# Specify the cell you want to retrieve (e.g., A1, B2, etc.)
cell = worksheet.get_all_records()

# Get the value of the cell
#print(cell)
with open("poem-sheet.json", 'w') as jfp:
    json.dump(cell, jfp)