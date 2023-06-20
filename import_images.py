import os, glob
import weaviate
import base64
import time

client = weaviate.Client(
    url="http://localhost:8080",
)


def add_object(filename, contents) -> None:
    global counter
    properties = {
      "name": filename,
      "image": contents,
    }

    client.batch.add_data_object(
      properties,
      "MySchemaName",
    )


client.batch.configure(batch_size=10)

for filename in glob.glob('dataset_images/*.JPG'):
    with open(os.path.join(os.getcwd(), filename), 'rb') as f:
        contents = base64.b64encode(f.read()).decode('utf-8')
        add_object(filename, contents)
        print(filename)
        time.sleep(1)

client.batch.flush()
