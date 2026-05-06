---
name: Amazon S3
description: Amazon Simple Storage Service (S3) is an object storage service offering industry-leading scalability, data availability, security, and performance.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
url: https://aws.amazon.com/s3/
created: '2024-01-15'
modified: '2026-04-18'
apis:
  - name: Amazon S3 REST API
    description: RESTful API for Amazon S3 storage operations including bucket management, object operations, and access control.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://aws.amazon.com/s3/
    baseURL: https://s3.amazonaws.com
    tags:
      - AWS
      - Cloud Storage
      - Object Storage
      - Storage
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/AmazonS3/latest/API/
      - type: OpenAPI
        url: openapi/amazon-s3-rest-api-openapi.yml
      - type: OpenAPI
        url: https://api.apis.guru/v2/specs/amazonaws.com/s3/2006-03-01/openapi.yaml
      - type: JSONSchema
        url: json-schema/amazon-s3-bucket-schema.json
      - type: JSONSchema
        url: json-schema/amazon-s3-object-schema.json
      - type: JSONLD
        url: json-ld/amazon-s3-context.jsonld
      - type: Pricing
        url: https://aws.amazon.com/s3/pricing/
      - type: GettingStarted
        url: https://aws.amazon.com/s3/getting-started/
      - type: Authentication
        url: https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html
      - type: SDK
        url: https://aws.amazon.com/tools/
      - type: StatusPage
        url: https://status.aws.amazon.com/
      - type: BestPractices
        url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/best-practices.html
      - type: FAQ
        url: https://aws.amazon.com/s3/faqs/
      - type: APIReference
        url: https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html
      - type: ChangeLog
        url: https://docs.aws.amazon.com/AmazonS3/latest/API/WhatsNew.html
      - type: CodeExamples
        url: https://docs.aws.amazon.com/AmazonS3/latest/API/service_code_examples.html
      - type: Security
        url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/security.html
  - name: Amazon S3 Control API
    description: Amazon S3 Control provides API operations for managing S3 account-level settings, access points, Batch Operations jobs, S3 Access Grants, Multi-Region Access Points, and Storage Lens configurations.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://docs.aws.amazon.com/AmazonS3/latest/API/API_Types_AWS_S3_Control.html
    baseURL: https://s3-control.amazonaws.com
    tags:
      - Access Control
      - AWS
      - Batch Operations
      - Storage
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_Types_AWS_S3_Control.html
      - type: OpenAPI
        url: openapi/amazon-s3-control-api-openapi.yml
      - type: OpenAPI
        url: https://api.apis.guru/v2/specs/amazonaws.com/s3control/2018-08-20/openapi.yaml
      - type: JSONLD
        url: json-ld/amazon-s3-context.jsonld
      - type: Pricing
        url: https://aws.amazon.com/s3/pricing/
      - type: GettingStarted
        url: https://aws.amazon.com/s3/getting-started/
      - type: Authentication
        url: https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html
      - type: SDK
        url: https://aws.amazon.com/tools/
      - type: FAQ
        url: https://aws.amazon.com/s3/faqs/
      - type: ChangeLog
        url: https://docs.aws.amazon.com/AmazonS3/latest/API/WhatsNew.html
  - name: Amazon S3 Tables API
    description: Amazon S3 Tables API provides operations for managing table buckets and tables stored in Apache Iceberg format, enabling structured tabular data storage in Apache Parquet format within Amazon S3.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://docs.aws.amazon.com/AmazonS3/latest/API/API_Operations_Amazon_S3_Tables.html
    baseURL: https://s3tables.amazonaws.com
    tags:
      - Apache Iceberg
      - AWS
      - Data Lake
      - Storage
      - Tables
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_Operations_Amazon_S3_Tables.html
      - type: OpenAPI
        url: openapi/amazon-s3-tables-api-openapi.yml
      - type: JSONLD
        url: json-ld/amazon-s3-context.jsonld
      - type: APIReference
        url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_Operations_Amazon_S3_Tables.html
      - type: Pricing
        url: https://aws.amazon.com/s3/pricing/
      - type: GettingStarted
        url: https://aws.amazon.com/s3/getting-started/
      - type: Authentication
        url: https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html
      - type: SDK
        url: https://aws.amazon.com/tools/
      - type: FAQ
        url: https://aws.amazon.com/s3/faqs/
common:
  - type: Portal
    url: https://aws.amazon.com/
  - type: Documentation
    url: https://docs.aws.amazon.com/s3/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/storage/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/s3/
  - type: SignUp
    url: https://signin.aws.amazon.com/signup?request_type=register
  - type: Login
    url: https://aws.amazon.com/console/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: KnowledgeCenter
    url: https://repost.aws/knowledge-center
  - type: YouTube
    url: https://www.youtube.com/user/AmazonWebServices
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/amazon-s3
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: Security
    url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/security.html
  - type: Compliance
    url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-compliance.html
  - type: ChangeLog
    url: https://docs.aws.amazon.com/AmazonS3/latest/API/WhatsNew.html
  - type: Features
    data:
      - Industry-leading scalability and 99.999999999% durability
      - Multiple storage classes for cost optimization
      - Object versioning and lifecycle management
      - Server-side encryption and access control
      - S3 Object Lock for WORM compliance
      - Cross-region and same-region replication
      - S3 Tables for Apache Iceberg tabular data
      - S3 Access Grants for identity-based access
      - Storage Lens analytics and insights
      - Batch Operations for large-scale object processing
  - type: UseCases
    data:
      - Storing and serving static website content
      - Data lake foundation for analytics workloads
      - Backup and disaster recovery storage
      - Archive storage with Glacier integration
      - Hosting machine learning training datasets
      - Storing application logs and audit trails
  - type: Integrations
    data:
      - AWS Lambda
      - Amazon CloudFront
      - Amazon Athena
      - AWS Glue
      - Amazon EMR
      - Amazon Redshift
      - AWS CloudTrail
      - Amazon EventBridge
properties:
  - type: Capabilities
    url: capabilities/storage-management.yaml
    title: Storage Management Capability
  - type: Capabilities
    url: capabilities/shared/s3-rest.yaml
    title: S3 REST API Shared Definition
  - type: Capabilities
    url: capabilities/shared/s3-control.yaml
    title: S3 Control API Shared Definition
  - type: Capabilities
    url: capabilities/shared/s3-tables.yaml
    title: S3 Tables API Shared Definition
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
tags:
  - Archive
  - AWS
  - Backup
  - Cloud Storage
  - Data Storage
  - Object Storage
  - Scalable Storage
---
