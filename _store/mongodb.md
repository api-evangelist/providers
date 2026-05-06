---
aid: mongodb
name: MongoDB
description: MongoDB is a source-available cross-platform document-oriented database program. Classified as a NoSQL database, MongoDB uses JSON-like documents with optional schemas.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Database
  - Database
  - Document Database
  - NoSQL
created: '2024'
modified: '2026-05-04'
url: https://www.mongodb.com
specificationVersion: '0.19'
apis:
  - name: MongoDB Atlas Administration API
    description: The MongoDB Atlas Administration API allows you to programmatically manage your MongoDB Atlas clusters, projects, organizations, users, and other resources.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.mongodb.com/docs/atlas/api/
    baseURL: https://cloud.mongodb.com/api/atlas/v2
    tags:
      - Cloud
      - Clusters
      - Database Management
      - Atlas
    properties:
      - type: Documentation
        url: https://www.mongodb.com/docs/atlas/api/atlas-admin-api-ref/
      - type: OpenAPI
        url: openapi/mongodb-atlas-openapi.yaml
      - type: Authentication
        url: https://www.mongodb.com/docs/atlas/api/api-authentication/
      - type: RateLimits
        url: https://www.mongodb.com/docs/atlas/api/api-rate-limit/
      - type: Versioning
        url: https://www.mongodb.com/docs/atlas/api/versioned-api-overview/
      - type: Changelog
        url: https://www.mongodb.com/docs/atlas/reference/api-resources-spec/changelog/
  - name: MongoDB Atlas Data API
    description: The Atlas Data API lets you read and write data in MongoDB Atlas with standard HTTPS requests, without the need for a MongoDB driver.
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
      - type: Examples
        url: https://www.mongodb.com/docs/atlas/app-services/data-api/examples/
  - name: MongoDB Atlas App Services Admin API
    description: Admin API for MongoDB Atlas App Services (formerly Realm), used to manage applications, services, functions, and triggers.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.mongodb.com/docs/atlas/app-services/admin/api/v3/
    baseURL: https://realm.mongodb.com/api/admin/v3.0
    tags:
      - App Services
      - Mobile
      - Serverless
      - Realm
    properties:
      - type: Documentation
        url: https://www.mongodb.com/docs/atlas/app-services/admin/api/v3/
common:
  - type: Website
    url: https://www.mongodb.com
  - type: Getting Started
    url: https://www.mongodb.com/docs/atlas/getting-started/
  - type: Blog
    url: https://www.mongodb.com/blog
  - type: Support
    url: https://www.mongodb.com/support
  - type: Community
    url: https://www.mongodb.com/community
  - type: Portal
    url: https://www.mongodb.com/developer/
  - type: Status
    url: https://status.mongodb.com/
  - type: Terms of Service
    url: https://www.mongodb.com/legal/terms-of-use
  - type: Privacy Policy
    url: https://www.mongodb.com/legal/privacy-policy
  - type: GitHub Organization
    url: https://github.com/mongodb
  - type: Features
    data:
      - Atlas M0 Free shared cluster (512 MB, 100 ops/sec)
      - Atlas Flex with $8-$30/month capped pricing
      - Atlas Dedicated M10+ from ~$0.08/hr ($57/month)
      - 'Atlas Serverless: $0.10/M reads, $1.00/M writes, $0.025/GB-month storage'
      - Atlas Search and Atlas Vector Search
      - Atlas Stream Processing
      - Atlas Data Federation across S3 and Atlas
      - Atlas Data API and GraphQL API
      - Atlas App Services (formerly Realm)
      - Atlas Admin API for programmatic cluster management
      - Multi-cloud across AWS, Azure, GCP
      - Multi-region clusters with global write zones
      - BI Connector for SQL access
      - Online archive for cold data tiering
      - Backups with point-in-time restore
      - VPC Peering and Private Endpoints
      - LDAP, X.509, and AWS IAM authentication
    sources:
      - https://www.mongodb.com/pricing
      - https://www.mongodb.com/pricing/calculator
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
