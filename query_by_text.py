import weaviate
import json

from PIL import Image
from io import BytesIO
import base64

client = weaviate.Client(
    url="http://localhost:8080"
)

nearText = {
  "concepts": ["city"],
  "certainty": 0.6,
  "moveAwayFrom": {
    "concepts": ["bread"],
    "force": 0.45
  },
  "moveTo": {
    "concepts": ["landscape"],
    "force": 0.85
  }
}

response = (
    client.query
    .get("MySchemaName", ["name", "image"])
    .with_near_text(nearText)
    .with_limit(2)
    .do()
)
#  print(json.dumps(response, indent=4))

base64_img = response.get("data").get("Get").get("MySchemaName")[0].get("image")

im = Image.open(BytesIO(base64.b64decode(base64_img)))
im.show()
