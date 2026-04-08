---
aid: mongodb
url: https://raw.githubusercontent.com/api-evangelist/mongodb/refs/heads/main/apis.yml
apis:
- name: MongoDB Atlas API
  description: The MongoDB Atlas API allows you to programmatically manage your MongoDB Atlas clusters, projects, and users.
  image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://www.mongodb.com/docs/atlas/api/
  baseURL: https://cloud.mongodb.com/api/atlas/v2
  tags:
  - Cloud
  - Clusters
  - Database Management
  properties:
  - type: Documentation
    url: https://www.mongodb.com/docs/atlas/api/atlas-admin-api/
  - type: Authentication
    url: https://www.mongodb.com/docs/atlas/configure-api-access/
- name: MongoDB Data API
  description: The Atlas Data API lets you read and write data in Atlas with standard HTTPS requests.
  image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://www.mongodb.com/docs/atlas/app-services/data-api/
  baseURL: https://data.mongodb-api.com/app
  tags:
  - Data Access
  - HTTPS
  - REST API
  properties:
  - type: Documentation
    url: https://www.mongodb.com/docs/atlas/app-services/data-api/
- name: MongoDB Realm API
  description: Admin API for MongoDB Atlas App Services (formerly Realm).
  image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://www.mongodb.com/docs/atlas/app-services/admin/api/v3/
  baseURL: https://realm.mongodb.com/api/admin/v3.0
  tags:
  - App Services
  - Mobile
  - Serverless
  properties:
  - type: Documentation
    url: https://www.mongodb.com/docs/atlas/app-services/admin/api/v3/
name: MongoDB
tags:
- Cloud Database
- Database
- Document Database
- NoSQL
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: MongoDB is a source-available cross-platform document-oriented database program. Classified as a NoSQL database, MongoDB uses JSON-like documents with optional schemas.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

