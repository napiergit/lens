# Install the Weaviate python client
```pip install weaviate-client```

# Run weaviate with clip module in docker
```docker-compose up -d```

# Create the schema
```python create_schema.py```

# Insert the images into Weaviate
```./import_images.sh```

python query.py


# You can also drop the schema to start again
```./drop_schema.sh```
