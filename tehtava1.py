
from google.cloud import storage
import requests

def tiedoston_kirjoitus():
    sr = requests.get('https://2ri98gd9i4.execute-api.us-east-1.amazonaws.com/dev/academy-checkpoint2-json')
    data = sr.json()
    tiedosto = open("C:/Users/creep/desktop/checkpoint-3/vko3-1/checkpoint.txt", "w")
    parametrit = []

    for i in sorted(data['items'], key=lambda x: x['number']):
        parametrit.append(f"{i['parameter']}")

    for nimi in parametrit:    
        tiedosto.write(nimi)
        tiedosto.write("\n")
    
def bucketti_create():
    storage_client = storage.Client()
    bucket_name = "elinan-checkpoint3-bucketti"

    bucket = storage_client.create_bucket(bucket_name)

def buckettiin_upload():
    storage_client = storage.Client()
    bucket_name = "elinan-checkpoint3-bucketti"
    file_name = "C:/Users/creep/desktop/checkpoint-3/vko3-1/checkpoint.txt"
    blob_name = "checkpoint1"

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(file_name)

if __name__ == "__main__":
    tiedoston_kirjoitus()
    bucketti_create()
    buckettiin_upload()

#juukeli