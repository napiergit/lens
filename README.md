# Setup
### 1. Install the Weaviate python client
```pip install weaviate-client```

### 2. Run weaviate with clip module in docker
```docker-compose up -d```

### 3. Create the schema
```python create_schema.py```

### 4. Download your dataset images into dataset_images folder
This is a manual step

### 5. Insert the images into Weaviate
```./import_images.sh```


# Run
### Query by text
Edit query_by_text.py with your desired text and then run:
```python query_by_text.py```

### Query by image 
Add an image to query_images folder, and point to the image in query_by_image.py, then run:
```python query_by_image.py```


# You can also drop the schema to start again
```./drop_schema.sh```
