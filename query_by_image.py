import weaviate
import json

from PIL import Image
from io import BytesIO
import base64

client = weaviate.Client(
    url="http://localhost:8080"
)

nearImage = {"image": "./query_images/henning-witzel-ukvgqriuOgo-unsplash.jpg"}

response = (
    client.query
    .get("MySchemaName", ["name", "image"])
    .with_near_image(nearImage, encode=True)
    .with_limit(2)
    .do()
)

print(json.dumps(response, indent=4))
