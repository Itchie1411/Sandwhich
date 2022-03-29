import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPTED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPTED_CREDS)
SHEET = GSPREAD_CLIENT.open('sandwiches')


def get_sales_data():
    """
    get sales figures"""

    print('please enter sales data from last market')
    print('data should be siz nunmbers, seperated by comma')
    print('example: 20, 15, 16, ... etc\n')

    data_str = input('Enter data here: ')

    sales_data = data_str.split(',')

    validate_data(sales_data)


def validate_data(values):
    try:
       if len(values) != 6:
           raise ValueError(
               f'Exactly 6 values required, you provided {len(values)}'
           )
    except ValueError as e:
        print(f'invalid data {e}, please try again')







get_sales_data()