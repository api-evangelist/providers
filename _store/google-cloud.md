---
aid: google-cloud
url: https://raw.githubusercontent.com/api-evangelist/google-cloud/refs/heads/main/apis.yml
apis:
- name: Google Compute Engine API
  description: Create and manage virtual machines on Google's infrastructure.
  image: https://cloud.google.com/images/social-icon-google-cloud-1200-630.png
  humanURL: https://cloud.google.com/compute
  baseURL: https://compute.googleapis.com
  tags:
  - Compute
  - IaaS
  - Infrastructure
  - Virtual Machines
  properties:
  - type: Documentation
    url: https://cloud.google.com/compute/docs/reference/rest/v1
  - type: OpenAPI
    url: https://compute.googleapis.com/$discovery/rest?version=v1
  - type: Authentication
    url: https://cloud.google.com/compute/docs/authentication
  - type: Pricing
    url: https://cloud.google.com/compute/pricing
  - type: Console
    url: https://console.cloud.google.com/compute
- name: Google Cloud Storage API
  description: Object storage service for storing and accessing data on Google Cloud Platform.
  image: https://cloud.google.com/images/social-icon-google-cloud-1200-630.png
  humanURL: https://cloud.google.com/storage
  baseURL: https://storage.googleapis.com
  tags:
  - Buckets
  - Files
  - Object Storage
  - Storage
  properties:
  - type: Documentation
    url: https://cloud.google.com/storage/docs/json_api
  - type: OpenAPI
    url: https://storage.googleapis.com/$discovery/rest?version=v1
  - type: Authentication
    url: https://cloud.google.com/storage/docs/authentication
  - type: Pricing
    url: https://cloud.google.com/storage/pricing
  - type: Console
    url: https://console.cloud.google.com/storage
- name: Google Kubernetes Engine API
  description: Deploy, manage, and scale containerized applications using Kubernetes.
  image: https://cloud.google.com/images/social-icon-google-cloud-1200-630.png
  humanURL: https://cloud.google.com/kubernetes-engine
  baseURL: https://container.googleapis.com
  tags:
  - Containers
  - Docker
  - Kubernetes
  - Orchestration
  properties:
  - type: Documentation
    url: https://cloud.google.com/kubernetes-engine/docs/reference/rest
  - type: OpenAPI
    url: https://container.googleapis.com/$discovery/rest?version=v1
  - type: Authentication
    url: https://cloud.google.com/kubernetes-engine/docs/how-to/api-server-authentication
  - type: Pricing
    url: https://cloud.google.com/kubernetes-engine/pricing
  - type: Console
    url: https://console.cloud.google.com/kubernetes
- name: Google Cloud Functions API
  description: Event-driven serverless compute platform for building and connecting cloud services.
  image: https://cloud.google.com/images/social-icon-google-cloud-1200-630.png
  humanURL: https://cloud.google.com/functions
  baseURL: https://cloudfunctions.googleapis.com
  tags:
  - Event-Driven
  - FaaS
  - Functions
  - Serverless
  properties:
  - type: Documentation
    url: https://cloud.google.com/functions/docs/reference/rest
  - type: OpenAPI
    url: https://cloudfunctions.googleapis.com/$discovery/rest?version=v1
  - type: Authentication
    url: https://cloud.google.com/functions/docs/securing
  - type: Pricing
    url: https://cloud.google.com/functions/pricing
  - type: Console
    url: https://console.cloud.google.com/functions
- name: Google BigQuery API
  description: Serverless, highly scalable, and cost-effective data warehouse for analytics.
  image: https://cloud.google.com/images/social-icon-google-cloud-1200-630.png
  humanURL: https://cloud.google.com/bigquery
  baseURL: https://bigquery.googleapis.com
  tags:
  - Analytics
  - Big Data
  - Data Warehouse
  - SQL
  properties:
  - type: Documentation
    url: https://cloud.google.com/bigquery/docs/reference/rest
  - type: OpenAPI
    url: https://bigquery.googleapis.com/$discovery/rest?version=v2
  - type: Authentication
    url: https://cloud.google.com/bigquery/docs/authentication
  - type: Pricing
    url: https://cloud.google.com/bigquery/pricing
  - type: Console
    url: https://console.cloud.google.com/bigquery
- name: Google Cloud Pub/Sub API
  description: Messaging and ingestion service for event-driven systems and streaming analytics.
  image: https://cloud.google.com/images/social-icon-google-cloud-1200-630.png
  humanURL: https://cloud.google.com/pubsub
  baseURL: https://pubsub.googleapis.com
  tags:
  - Event Streaming
  - Messaging
  - Pub/Sub
  - Queue
  properties:
  - type: Documentation
    url: https://cloud.google.com/pubsub/docs/reference/rest
  - type: OpenAPI
    url: https://pubsub.googleapis.com/$discovery/rest?version=v1
  - type: Authentication
    url: https://cloud.google.com/pubsub/docs/authentication
  - type: Pricing
    url: https://cloud.google.com/pubsub/pricing
  - type: Console
    url: https://console.cloud.google.com/cloudpubsub
- name: Google Cloud Vision API
  description: Derive insights from images with machine learning.
  image: https://cloud.google.com/images/social-icon-google-cloud-1200-630.png
  humanURL: https://cloud.google.com/vision
  baseURL: https://vision.googleapis.com
  tags:
  - AI
  - Computer Vision
  - Image Analysis
  - Machine Learning
  properties:
  - type: Documentation
    url: https://cloud.google.com/vision/docs/reference/rest
  - type: OpenAPI
    url: https://vision.googleapis.com/$discovery/rest?version=v1
  - type: Authentication
    url: https://cloud.google.com/vision/docs/authentication
  - type: Pricing
    url: https://cloud.google.com/vision/pricing
  - type: Console
    url: https://console.cloud.google.com/apis/library/vision.googleapis.com
- name: Google Cloud SQL Admin API
  description: Manage Cloud SQL instances for MySQL, PostgreSQL, and SQL Server.
  image: https://cloud.google.com/images/social-icon-google-cloud-1200-630.png
  humanURL: https://cloud.google.com/sql
  baseURL: https://sqladmin.googleapis.com
  tags:
  - Database
  - MySQL
  - PostgreSQL
  - SQL
  properties:
  - type: Documentation
    url: https://cloud.google.com/sql/docs/mysql/admin-api
  - type: OpenAPI
    url: https://sqladmin.googleapis.com/$discovery/rest?version=v1
  - type: Authentication
    url: https://cloud.google.com/sql/docs/mysql/authentication
  - type: Pricing
    url: https://cloud.google.com/sql/pricing
  - type: Console
    url: https://console.cloud.google.com/sql
name: Google Cloud Platform
tags:
- Cloud Computing
- Data Analytics
- Infrastructure
- Machine Learning
- Platform as a Service
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Google Cloud Platform provides a comprehensive suite of cloud computing services including compute, storage, databases, machine learning, and networking capabilities.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

