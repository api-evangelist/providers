---
aid: google-cloud
name: Google Cloud Platform
description: Google Cloud Platform provides a comprehensive suite of cloud computing services including compute, storage, databases, machine learning, and networking capabilities.
url: https://cloud.google.com/
type: Index
specificationVersion: '0.19'
created: '2024-01-01'
modified: '2026-05-04'
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
common:
  - type: Portal
    url: https://console.cloud.google.com
  - type: Documentation
    url: https://cloud.google.com/docs
  - type: Getting Started
    url: https://cloud.google.com/docs/get-started
  - type: Authentication
    url: https://cloud.google.com/docs/authentication
  - type: SDKs
    url: https://cloud.google.com/sdk
  - type: Status
    url: https://status.cloud.google.com
  - type: Support
    url: https://cloud.google.com/support
  - type: Pricing
    url: https://cloud.google.com/pricing
  - type: Blog
    url: https://cloud.google.com/blog
  - type: Terms of Service
    url: https://cloud.google.com/terms
  - type: Privacy Policy
    url: https://policies.google.com/privacy
  - type: Sign Up
    url: https://console.cloud.google.com/freetrial
  - type: Login
    url: https://console.cloud.google.com/
  - type: Features
    data:
      - 'Google Cloud: hundreds of services across Cloud Infrastructure'
      - 'Detailed pricing: see https://cloud.google.com/pricing'
      - 'Service: Compute Engine'
      - 'Service: Cloud Storage'
      - 'Service: Cloud SQL'
      - 'Service: Spanner'
      - 'Service: Firestore'
      - 'Service: BigQuery'
      - 'Service: Bigtable'
      - 'Service: Cloud Functions (Gen 2)'
      - 'Service: Cloud Run'
      - 'Service: GKE (Kubernetes)'
      - 'Service: Cloud Load Balancing'
      - 'Service: Cloud CDN'
      - 'Service: Cloud DNS'
      - 'Service: VPC'
      - 'Service: IAM'
      - 'Service: Cloud KMS'
      - 'Service: Secret Manager'
      - 'Service: Cloud Monitoring'
      - 'Service: Cloud Logging'
      - 'Service: Cloud Trace'
      - 'Service: Vertex AI / Gemini API'
      - 'Service: Cloud Translation'
      - 'Service: Speech-to-Text'
      - 'Service: Text-to-Speech'
      - 'Service: Vision AI'
      - 'Service: Natural Language AI'
      - 'Service: Document AI'
      - 'Service: Maps Platform'
      - 'Service: Apigee (API management)'
      - 'Service: Pub/Sub'
      - 'Service: Dataflow'
      - 'Service: Dataproc'
      - 'Service: Composer (Airflow)'
      - 'Service: Looker (BI)'
      - 'Service: Cloud Build'
      - 'Service: Artifact Registry'
    sources:
      - https://cloud.google.com/pricing
      - https://focus.finops.org/
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
tags:
  - Cloud Computing
  - Data Analytics
  - Infrastructure
  - Machine Learning
  - Platform as a Service
---
