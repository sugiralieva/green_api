import requests


def get_settings(apiurl, idinstance, apitokeninstance):
    url = f"{apiurl}/waInstance{idinstance}/getSettings/{apitokeninstance}"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text.encode("utf-8")


def get_state_instance(apiurl, idinstance, apitokeninstance):
    url = f"{apiurl}/waInstance{idinstance}/getStateInstance/{apitokeninstance}"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text.encode('utf8')


def send_message(apiurl, idinstance, apitokeninstance, number, message_text):

    url = f"{apiurl}/waInstance{idinstance}/sendMessage/{apitokeninstance}"

    payload = f"""{{
        "chatId": "{number}@c.us",
        "message": "{message_text}"
    }}"""

    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)

    return response.text.encode('utf8')


def send_file_by_url(apiurl, idinstance, apitokeninstance, number, file_url):
    url = f"{apiurl}/waInstance{idinstance}/sendFileByUrl/{apitokeninstance}"

    payload = f'{{\n   "chatId": "{number}@c.us",\n   "urlFile": "{file_url}",\n   "fileName": "{file_url.split("/")[-1]}",\n   "caption": "{file_url.split("/")[-1].split(".")[0]}"\n}}'

    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)

    return response.text.encode('utf8')
