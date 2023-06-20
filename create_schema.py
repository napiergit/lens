import weaviate

client = weaviate.Client(
    url="http://localhost:8080",
)

class_obj = {
    "class": "MySchemaName",
    "moduleConfig": {
      "multi2vec-clip": {
        "imageFields": [
          "image"
        ],
        "textFields": [
          "name"
        ],
        "weights": {
          "textFields": [0.2],
          "imageFields": [0.8]
        }
      }
    },
    "properties": [
      {
        "dataType": [
          "text"
        ],
        "name": "name"
      },
      {
        "dataType": [
          "blob"
        ],
        "name": "image"
      }
    ],
    "vectorIndexType": "hnsw",
    "vectorizer": "multi2vec-clip"
}


client.schema.create_class(class_obj)
