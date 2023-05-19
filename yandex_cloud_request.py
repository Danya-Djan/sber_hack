import requests
import time
name_list = ['mvd.mp3', 'Nout_f_4.mp3', 'out_a_1.mp3', 'out_a_2.mp3', 'out_a_2.mp3', 'Nout_a_1.mp3', 'Nout_a_2.mp3', 'Nout_a_4.mp3', 'Nout_a_9.mp3', 'Nout_a_10.mp3']

for FILE_NAME in name_list:
    url = 'https://transcribe.api.cloud.yandex.net/speech/stt/v2/longRunningRecognize'
    headers = {"Authorization": "Bearer t1.9euelZrHmZHOksebnY-UlI6Sy5aZie3rnpWax4_JzpmMjIqdlYmMyozKnZLl8_c6PGBc-e8pWkFa_t3z93pqXVz57ylaQVr-zef1656VmsbKiZnMi5aWmomal8-MzJXI7_0.E3DgsuZZkwMBrwvgIcFpVMf2JjJvGpCu8dBfaIT5wvhzVFW-9VvVMe3h8dwj8zjYBcXQbsp-Hj3CC7rJRflrCg"}
    myobj = {"config": {"specification": {"audioEncoding": "MP3"},},"audio": {"uri": "https://storage.yandexcloud.net/kaifyoucaught/" + FILE_NAME},}
    x = requests.post(url, headers=headers, json=myobj)
    operationID = x.json()["id"]
    time.sleep(25)
    response = requests.get('https://operation.api.cloud.yandex.net/operations/' + operationID, headers=headers)
    response = response.json()['response']
    final_text = ""
    for i in response['chunks']:
        final_text += i['alternatives'][0]['text'] + "."
    with open(FILE_NAME[:-4] + "_out.txt", "w", encoding="utf-8") as f:
        f.write(final_text)
