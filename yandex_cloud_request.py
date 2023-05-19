import requests
import time
import boto3

ACCESS_KEY_UPLOAD = 'YCAJEslrAKKbLge1bCCRQfrkY'
SECRET_KEY_UPLOAD = 'YCMFVTBsh5Oc8X3pi0J_BWOVHV6dIobigKS9rB1R'
YANDEX_URL = 'https://storage.yandexcloud.net/'
REGION = 'ru-central1'
BEST_TEAM_EVER = 'kaifyoucaught'
FILE_NAME = "senya.mp3"
API_KEY = "t1.9euelZrHmZHOksebnY-UlI6Sy5aZie3rnpWax4_JzpmMjIqdlYmMyozKnZLl8_c6PGBc-e8pWkFa_t3z93pqXVz57ylaQVr-zef1656VmsbKiZnMi5aWmomal8-MzJXI7_0.E3DgsuZZkwMBrwvgIcFpVMf2JjJvGpCu8dBfaIT5wvhzVFW-9VvVMe3h8dwj8zjYBcXQbsp-Hj3CC7rJRflrCg"

#uploading file to yandex cloud service
s3_client = boto3.client(
    's3',
    aws_access_key_id=ACCESS_KEY_UPLOAD,
    aws_secret_access_key=SECRET_KEY_UPLOAD,
    endpoint_url=YANDEX_URL,
    region_name=REGION
)
s3_client.upload_file(FILE_NAME, BEST_TEAM_EVER, FILE_NAME)
time.sleep(5)
#sending file to be analyzed
url = 'https://transcribe.api.cloud.yandex.net/speech/stt/v2/longRunningRecognize'
headers = {"Authorization": "Bearer " + API_KEY}
myobj = {"config": {"specification": {"audioEncoding": "MP3"}, }, "audio": {"uri": YANDEX_URL + BEST_TEAM_EVER + "/" + FILE_NAME}}
x = requests.post(url, headers=headers, json=myobj)
operationID = x.json()["id"]

#waiting for response
time.sleep(25)
if requests.get('https://operation.api.cloud.yandex.net/operations/' + operationID, headers=headers).json()["done"] == "false":
    time.sleep(25)
    if requests.get('https://operation.api.cloud.yandex.net/operations/' + operationID, headers=headers).json()[
        "done"] == "false":
        time.sleep(25)

#saving file as txt
response = requests.get('https://operation.api.cloud.yandex.net/operations/' + operationID, headers=headers)
response = response.json()['response']
final_text = ""
for i in response['chunks']:
    final_text += i['alternatives'][0]['text'] + "."
with open(FILE_NAME[:-4] + "_out.txt", "w", encoding="utf-8") as f:
    f.write(final_text)
