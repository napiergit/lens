#!/bin/bash

curl \
    -X DELETE \
    -H "Content-Type: application/json" \
    http://localhost:8080/v1/schema/MySchemaName
