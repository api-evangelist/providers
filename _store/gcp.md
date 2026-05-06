---
aid: gcp
name: Google Cloud Platform APIs
description: Comprehensive collection of Google Cloud Platform APIs for cloud computing, storage, machine learning, and infrastructure management.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-01-01'
modified: '2026-04-28'
position: Consumer
url: https://raw.githubusercontent.com/api-evangelist/gcp/refs/heads/main/apis.yml
specificationVersion: '0.19'
tags:
  - Cloud Computing
  - Databases
  - Infrastructure
  - Machine Learning
  - Networking
  - Security
  - Serverless
  - Storage
apis:
  - aid: gcp:compute-engine
    name: Compute Engine API
    description: Create and manage virtual machines on Google's infrastructure.
    humanURL: https://cloud.google.com/compute
    baseURL: https://compute.googleapis.com
    tags:
      - Compute
      - IaaS
      - Virtual Machines
    properties:
      - type: Documentation
        url: https://cloud.google.com/compute/docs/reference/rest/v1
      - type: OpenAPI
        url: https://compute.googleapis.com/$discovery/rest?version=v1
      - type: Console
        url: https://console.cloud.google.com/compute
  - aid: gcp:cloud-storage
    name: Cloud Storage API
    description: Object storage service for storing and accessing data on Google Cloud Platform.
    humanURL: https://cloud.google.com/storage
    baseURL: https://storage.googleapis.com
    tags:
      - Data
      - Object Storage
      - Storage
    properties:
      - type: Documentation
        url: https://cloud.google.com/storage/docs/json_api
      - type: OpenAPI
        url: https://storage.googleapis.com/$discovery/rest?version=v1
      - type: Console
        url: https://console.cloud.google.com/storage
  - aid: gcp:cloud-functions
    name: Cloud Functions API
    description: Event-driven serverless compute platform for building and connecting cloud services.
    humanURL: https://cloud.google.com/functions
    baseURL: https://cloudfunctions.googleapis.com
    tags:
      - FaaS
      - Functions
      - Serverless
    properties:
      - type: Documentation
        url: https://cloud.google.com/functions/docs/reference/rest
      - type: OpenAPI
        url: https://cloudfunctions.googleapis.com/$discovery/rest?version=v1
      - type: Console
        url: https://console.cloud.google.com/functions
  - aid: gcp:cloud-pubsub
    name: Cloud Pub/Sub API
    description: Messaging and ingestion service for event-driven systems and streaming analytics.
    humanURL: https://cloud.google.com/pubsub
    baseURL: https://pubsub.googleapis.com
    tags:
      - Events
      - Messaging
      - Streaming
    properties:
      - type: Documentation
        url: https://cloud.google.com/pubsub/docs/reference/rest
      - type: OpenAPI
        url: https://pubsub.googleapis.com/$discovery/rest?version=v1
      - type: Console
        url: https://console.cloud.google.com/cloudpubsub
  - aid: gcp:bigquery
    name: BigQuery API
    description: Serverless, highly scalable data warehouse for analytics.
    humanURL: https://cloud.google.com/bigquery
    baseURL: https://bigquery.googleapis.com
    tags:
      - Analytics
      - Big Data
      - Data Warehouse
    properties:
      - type: Documentation
        url: https://cloud.google.com/bigquery/docs/reference/rest
      - type: OpenAPI
        url: https://bigquery.googleapis.com/$discovery/rest?version=v2
      - type: Console
        url: https://console.cloud.google.com/bigquery
  - aid: gcp:cloud-vision
    name: Cloud Vision API
    description: Image analysis and machine learning for detecting objects, faces, and text.
    humanURL: https://cloud.google.com/vision
    baseURL: https://vision.googleapis.com
    tags:
      - AI
      - Computer Vision
      - Machine Learning
    properties:
      - type: Documentation
        url: https://cloud.google.com/vision/docs/reference/rest
      - type: OpenAPI
        url: https://vision.googleapis.com/$discovery/rest?version=v1
      - type: Console
        url: https://console.cloud.google.com/apis/library/vision.googleapis.com
  - aid: gcp:cloud-natural-language
    name: Cloud Natural Language API
    description: Natural language understanding and sentiment analysis.
    humanURL: https://cloud.google.com/natural-language
    baseURL: https://language.googleapis.com
    tags:
      - AI
      - Machine Learning
      - NLP
    properties:
      - type: Documentation
        url: https://cloud.google.com/natural-language/docs/reference/rest
      - type: OpenAPI
        url: https://language.googleapis.com/$discovery/rest?version=v1
      - type: Console
        url: https://console.cloud.google.com/apis/library/language.googleapis.com
  - aid: gcp:kubernetes-engine
    name: Kubernetes Engine API
    description: Managed Kubernetes service for deploying containerized applications.
    humanURL: https://cloud.google.com/kubernetes-engine
    baseURL: https://container.googleapis.com
    tags:
      - Containers
      - Kubernetes
      - Orchestration
    properties:
      - type: Documentation
        url: https://cloud.google.com/kubernetes-engine/docs/reference/rest
      - type: OpenAPI
        url: https://container.googleapis.com/$discovery/rest?version=v1
      - type: Console
        url: https://console.cloud.google.com/kubernetes
  - aid: gcp:cloud-sql
    name: Cloud SQL Admin API
    description: Managed MySQL, PostgreSQL, and SQL Server databases.
    humanURL: https://cloud.google.com/sql
    baseURL: https://sqladmin.googleapis.com
    tags:
      - Database
      - Managed Service
      - SQL
    properties:
      - type: Documentation
        url: https://cloud.google.com/sql/docs/mysql/admin-api
      - type: OpenAPI
        url: https://sqladmin.googleapis.com/$discovery/rest?version=v1
      - type: Console
        url: https://console.cloud.google.com/sql
  - aid: gcp:cloud-firestore
    name: Cloud Firestore API
    description: NoSQL document database for mobile, web, and server development.
    humanURL: https://cloud.google.com/firestore
    baseURL: https://firestore.googleapis.com
    tags:
      - Database
      - NoSQL
      - Real-Time
    properties:
      - type: Documentation
        url: https://cloud.google.com/firestore/docs/reference/rest
      - type: OpenAPI
        url: https://firestore.googleapis.com/$discovery/rest?version=v1
      - type: Console
        url: https://console.cloud.google.com/firestore
common:
  - type: Authentication
    url: https://cloud.google.com/docs/authentication
  - type: Console
    url: https://console.cloud.google.com
  - type: Status
    url: https://status.cloud.google.com
  - type: Support
    url: https://cloud.google.com/support
  - type: Getting Started
    url: https://cloud.google.com/docs
  - type: SDKs
    url: https://cloud.google.com/sdk
  - type: Blog
    url: https://cloud.google.com/blog
  - type: Terms of Service
    url: https://cloud.google.com/terms
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
