from login import *

if __name__ == "__main__":
    credential_file = os.getcwd()+"/resources/credentials.json"
    gc = login(credential_file)
    file_url = input("Enter google sheet url: ")
    # file_url = "https://docs.google.com/spreadsheets/d/1Jt31sT87_yoKuOQkasf71tCUZnBRz88_3kcAc7ojQco/"
    gsheet = gc.open_by_url(file_url)
    print(gsheet.title)
    stop = False
    i = 0
    spreadsheets = []
    while not stop:
        try:
            worksheet = gsheet.get_worksheet(i)
            spreadsheets.append(worksheet.get_all_records())
            i += 1
        except:
            stop = True

    print("Spreadsheets data: \n {}".format(spreadsheets))

