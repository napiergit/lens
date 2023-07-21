import weaviate
import json

from PIL import Image
from io import BytesIO
import base64

client = weaviate.Client(
    url="http://localhost:8080"
)

nearImage = {"image": "./query_images/lily.jpg"}

response = (
    client.query
    .get("MySchemaName", ["name", "image"])
    .with_near_image(nearImage, encode=True)
    .with_limit(2)
    .do()
)

#  print(json.dumps(response, indent=4))
base64_img = response.get("data").get("Get").get("MySchemaName")[0].get("image")

im = Image.open(BytesIO(base64.b64decode(base64_img)))
im.show()
