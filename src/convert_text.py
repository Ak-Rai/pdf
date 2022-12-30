import requests
import json
from decouple import config
import PyPDF2


# API_KEY = config('API_KEY')

def readPdf(path):
    reader = PyPDF2.PdfReader(path)
    pages = len(reader.pages)
    text = ''
    for x in range(0, pages):
        dt = reader.pages[x].extract_text()
        txt = dt.split('\n')[9:-1]
        if (x == pages - 1):
            txt = txt[:-11]
        t = " ".join(txt)
        text = text + t
    return text


def img_text(path):
    try:
        url = "https://app.nanonets.com/api/v2/OCR/FullText"
        files = [('file', ('xyz', open(path, 'rb'), 'application/pdf'))]
        headers = {}
        response = requests.request("POST", url, headers=headers, files=files,
                                    auth=requests.auth.HTTPBasicAuth(API_KEY, ''))
        print("OCR Response - ", response.status_code)
        json_response = json.loads(response.text)
        text = json_response["results"][0]['page_data'][0]["raw_text"]
        return text
    except:
        print('Something went wrong while getting TRF from OCR.')

