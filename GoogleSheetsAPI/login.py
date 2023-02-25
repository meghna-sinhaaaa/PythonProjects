import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials


def login(file_path):
    gc = gspread.service_account(filename=file_path)
    print(gc)

    return gc

