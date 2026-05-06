---
aid: aws-s3
name: Amazon S3 API
description: Amazon Simple Storage Service (S3) is an object storage service offering industry-leading scalability, data availability, security, and performance for storing and retrieving any amount of data.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Cloud Storage
  - Object Storage
  - Storage
url: https://raw.githubusercontent.com/api-evangelist/aws-s3/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: aws-s3:amazon-s3-rest-api
    name: Amazon S3 REST API
    description: RESTful API for Amazon S3 object storage operations including bucket management, object CRUD, access control, versioning, lifecycle policies, and multipart uploads.
    humanURL: https://aws.amazon.com/s3/
    baseURL: https://s3.amazonaws.com
    tags:
      - Buckets
      - Objects
      - REST
      - Storage
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html
      - type: OpenAPI
        url: openapi/aws-s3-openapi.yaml
      - type: Authentication
        url: https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html
      - type: GettingStarted
        url: https://aws.amazon.com/s3/getting-started/
      - type: SDK
        url: https://aws.amazon.com/tools/
        title: AWS SDKs
common:
  - type: Website
    url: https://aws.amazon.com/s3/
  - type: Blog
    url: https://aws.amazon.com/blogs/storage/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Console
    url: https://console.aws.amazon.com/s3/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Pricing
    url: https://aws.amazon.com/s3/pricing/
  - type: ChangeLog
    url: https://aws.amazon.com/releasenotes/Amazon-S3/
  - type: Documentation
    url: https://docs.aws.amazon.com/s3/
  - type: SpectralRules
    url: rules/aws-s3-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/aws-s3-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/object-storage-workflow.yaml
  - type: Features
    data:
      - name: Scalable Object Storage
        description: Store and retrieve any amount of data, at any time, from anywhere.
      - name: Versioning
        description: Keep multiple variants of an object in the same bucket to recover from unintended actions.
      - name: Lifecycle Policies
        description: Automatically transition objects to cheaper storage classes or expire them after a defined period.
      - name: Cross-Region Replication
        description: Automatically replicate objects across AWS Regions for compliance and disaster recovery.
      - name: Server-Side Encryption
        description: Encrypt objects at rest using SSE-S3, SSE-KMS, or SSE-C managed keys.
      - name: Access Control
        description: Fine-grained access via bucket policies, ACLs, and IAM policies.
      - name: Event Notifications
        description: Trigger Lambda functions, SQS messages, or SNS topics on bucket events.
      - name: S3 Select
        description: Retrieve a subset of data from an object using SQL expressions.
      - name: Transfer Acceleration
        description: Speed up uploads using CloudFront's globally distributed edge locations.
      - name: Intelligent-Tiering
        description: Automatically move objects to the most cost-effective access tier based on usage patterns.
  - type: UseCases
    data:
      - name: Data Lake Storage
        description: Store raw data for analytics pipelines using AWS Glue, Athena, and Redshift Spectrum.
      - name: Static Website Hosting
        description: Host static websites and single-page applications directly from S3.
      - name: Backup and Archive
        description: Store backups and archives with lifecycle policies to move data to Glacier for long-term retention.
      - name: Media Storage and Distribution
        description: Store and serve images, videos, and documents globally via CloudFront CDN.
      - name: Application Data Storage
        description: Store user-generated content, application logs, and configuration files.
  - type: Integrations
    data:
      - name: AWS Lambda
        description: Trigger serverless functions on S3 object events.
      - name: Amazon CloudFront
        description: Distribute S3 content globally with low-latency delivery.
      - name: AWS Glue
        description: Catalog and ETL data in S3 for analytics workflows.
      - name: Amazon Athena
        description: Query data stored in S3 using standard SQL without loading.
      - name: Amazon Redshift Spectrum
        description: Query S3 data lake files from Redshift without data movement.
      - name: Amazon EventBridge
        description: Route S3 events to downstream AWS services using EventBridge rules.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
