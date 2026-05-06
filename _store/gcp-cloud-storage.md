---
name: Google Cloud Storage
description: Object storage service offering high durability, availability, and scalability for storing and accessing data on Google Cloud Platform.
image: https://cloud.google.com/images/social-icon-google-cloud-1200-630.png
url: https://cloud.google.com/storage
created: '2024-01-01'
modified: '2026-04-18'
tags:
  - Archival
  - Backup
  - Blob Storage
  - Cloud Storage
  - Data
  - File Storage
  - Google Cloud
  - Object Storage
  - Storage
apis:
  - name: Google Cloud Storage JSON API
    description: RESTful API for interacting with Google Cloud Storage buckets and objects.
    image: https://cloud.google.com/images/storage/storage-icon.svg
    humanURL: https://cloud.google.com/storage/docs/json_api
    baseURL: https://storage.googleapis.com/storage/v1
    tags:
      - Buckets
      - Objects
      - Access Control
      - IAM
      - Storage
    properties:
      - type: Documentation
        url: https://cloud.google.com/storage/docs/json_api
      - type: OpenAPI
        url: https://storage.googleapis.com/$discovery/rest?version=v1
      - type: OpenAPI
        url: openapi/gcp-cloud-storage-json-api-openapi.yml
      - type: Authentication
        url: https://cloud.google.com/storage/docs/authentication
      - type: Pricing
        url: https://cloud.google.com/storage/pricing
      - type: RateLimits
        url: https://cloud.google.com/storage/quotas
      - type: StatusPage
        url: https://status.cloud.google.com/
      - type: TermsOfService
        url: https://cloud.google.com/terms
      - type: APIReference
        url: https://cloud.google.com/storage/docs/json_api/v1
      - type: JSONSchema
        url: json-schema/gcp-cloud-storage-bucket-schema.json
      - type: JSONSchema
        url: json-schema/gcp-cloud-storage-json-bucket-schema.json
      - type: JSONSchema
        url: json-schema/gcp-cloud-storage-json-bucket-access-control-schema.json
      - type: JSONSchema
        url: json-schema/gcp-cloud-storage-json-bucket-list-schema.json
      - type: JSONSchema
        url: json-schema/gcp-cloud-storage-json-channel-schema.json
      - type: JSONSchema
        url: json-schema/gcp-cloud-storage-json-compose-request-schema.json
      - type: JSONSchema
        url: json-schema/gcp-cloud-storage-json-error-schema.json
      - type: JSONSchema
        url: json-schema/gcp-cloud-storage-json-object-access-control-schema.json
      - type: JSONSchema
        url: json-schema/gcp-cloud-storage-json-object-list-schema.json
      - type: JSONSchema
        url: json-schema/gcp-cloud-storage-json-object-schema.json
      - type: JSONSchema
        url: json-schema/gcp-cloud-storage-json-policy-schema.json
      - type: JSONSchema
        url: json-schema/gcp-cloud-storage-json-rewrite-response-schema.json
      - type: JSONLD
        url: json-ld/gcp-cloud-storage-context.jsonld
      - type: JSONLD
        url: json-ld/gcp-cloud-storage-json-context.jsonld
    contact:
      - type: Support
        url: https://cloud.google.com/storage/docs/getting-support
  - name: Google Cloud Storage XML API
    description: Amazon S3-compatible XML API for Google Cloud Storage.
    image: https://cloud.google.com/images/storage/storage-icon.svg
    humanURL: https://cloud.google.com/storage/docs/xml-api
    baseURL: https://storage.googleapis.com
    tags:
      - S3 Compatible
      - XML
      - Interoperability
    properties:
      - type: Documentation
        url: https://cloud.google.com/storage/docs/xml-api/overview
      - type: Authentication
        url: https://cloud.google.com/storage/docs/authentication/hmackeys
      - type: APIReference
        url: https://cloud.google.com/storage/docs/xml-api/reference-methods
      - type: Pricing
        url: https://cloud.google.com/storage/pricing
      - type: RateLimits
        url: https://cloud.google.com/storage/quotas
      - type: TermsOfService
        url: https://cloud.google.com/terms
    contact:
      - type: Support
        url: https://cloud.google.com/storage/docs/getting-support
common:
  - type: GettingStarted
    url: https://cloud.google.com/storage/docs/quickstarts
  - type: SDK
    url: https://cloud.google.com/storage/docs/reference/libraries
  - type: Console
    url: https://console.cloud.google.com/storage
  - type: Blog
    url: https://cloud.google.com/blog/products/storage-data-transfer
  - type: ChangeLog
    url: https://cloud.google.com/storage/docs/release-notes
  - type: BestPractices
    url: https://cloud.google.com/storage/docs/best-practices
  - type: Security
    url: https://cloud.google.com/storage/docs/security
  - type: Compliance
    url: https://cloud.google.com/security/compliance
  - type: APIReference
    url: https://cloud.google.com/storage/docs/apis
  - type: CLI
    url: https://cloud.google.com/storage/docs/discover-object-storage-gsutil
  - type: SpectralRules
    url: rules/gcp-cloud-storage-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/gcp-cloud-storage-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/cloud-storage.yaml
  - type: Features
    data:
      - name: Multi-Regional Storage
        description: Store data across multiple regions for high availability and low-latency access worldwide.
      - name: Object Lifecycle Management
        description: Automatically transition objects between storage classes or delete them based on configurable rules.
      - name: Versioning
        description: Maintain multiple versions of objects for data protection and recovery.
      - name: Fine-Grained Access Control
        description: Control access using IAM policies, ACLs, and signed URLs for secure data sharing.
      - name: Object Composition
        description: Compose multiple objects into a single object without downloading and re-uploading data.
      - name: Change Notifications
        description: Watch for changes to objects in a bucket and receive push notifications.
      - name: Retention Policies
        description: Lock retention policies to prevent object deletion for regulatory compliance.
  - type: UseCases
    data:
      - name: Data Lake Storage
        description: Store structured and unstructured data at scale for analytics and machine learning pipelines.
      - name: Backup and Disaster Recovery
        description: Store backups with configurable retention and cross-region replication for business continuity.
      - name: Static Website Hosting
        description: Serve static web content directly from Cloud Storage buckets with custom domains.
      - name: Media Content Delivery
        description: Store and serve media assets with CDN integration for low-latency content delivery.
  - type: Integrations
    data:
      - name: BigQuery
        description: Load data directly from Cloud Storage into BigQuery for analytics and data warehousing.
      - name: Cloud Functions
        description: Trigger serverless functions on object creation, deletion, or metadata changes.
      - name: Dataflow
        description: Process data stored in Cloud Storage using Apache Beam pipelines.
      - name: Transfer Service
        description: Transfer data between on-premises storage, other clouds, and Cloud Storage.
      - name: Cloud CDN
        description: Cache and serve Cloud Storage content through Google's global edge network.
maintainers:
  - name: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
