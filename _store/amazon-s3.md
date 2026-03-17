---
name: Amazon S3
description: Amazon Simple Storage Service (S3) is an object storage service offering industry-leading scalability, data availability, security, and performance.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
url: https://aws.amazon.com/s3/
created: '2024-01-15'
modified: '2026-03-16'
apis:
- name: Amazon S3 REST API
  description: RESTful API for Amazon S3 storage operations including bucket management, object operations, and access control
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/s3/
  baseURL: https://s3.amazonaws.com
  tags:
  - Storage
  - Cloud Storage
  - Object Storage
  - AWS
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
  - type: Getting Started
    url: https://aws.amazon.com/s3/getting-started/
  - type: Authentication
    url: https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html
  - type: SDKs
    url: https://aws.amazon.com/tools/
  - type: Status
    url: https://status.aws.amazon.com/
  - type: Best Practices
    url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/best-practices.html
  - type: FAQ
    url: https://aws.amazon.com/s3/faqs/
  - type: Service Level Agreement
    url: https://aws.amazon.com/s3/sla/
  - type: User Guide
    url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html
  - type: API Reference
    url: https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html
  - type: Change Log
    url: https://docs.aws.amazon.com/AmazonS3/latest/API/WhatsNew.html
  - type: Code Examples
    url: https://docs.aws.amazon.com/AmazonS3/latest/API/service_code_examples.html
  - type: Security
    url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/security.html
  - type: Videos
    url: https://aws.amazon.com/s3/videos/
- name: Amazon S3 Control API
  description: Amazon S3 Control provides API operations for managing S3 account-level settings, access points, Batch Operations jobs, S3 Access Grants, Multi-Region Access Points, and Storage Lens configurations.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://docs.aws.amazon.com/AmazonS3/latest/API/API_Types_AWS_S3_Control.html
  baseURL: https://s3-control.amazonaws.com
  tags:
  - Storage
  - Access Control
  - Batch Operations
  - AWS
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_Types_AWS_S3_Control.html
  - type: OpenAPI
    url: openapi/amazon-s3-control-api-openapi.yml
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/s3control/2018-08-20/openapi.yaml
  - type: JSONLD
    url: json-ld/amazon-s3-context.jsonld
  - type: User Guide
    url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html
  - type: Pricing
    url: https://aws.amazon.com/s3/pricing/
  - type: Getting Started
    url: https://aws.amazon.com/s3/getting-started/
  - type: Authentication
    url: https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html
  - type: SDKs
    url: https://aws.amazon.com/tools/
  - type: Endpoints
    url: https://docs.aws.amazon.com/general/latest/gr/s3.html
  - type: Batch Operations
    url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops.html
  - type: Access Grants
    url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants.html
  - type: FAQ
    url: https://aws.amazon.com/s3/faqs/
  - type: Change Log
    url: https://docs.aws.amazon.com/AmazonS3/latest/API/WhatsNew.html
- name: Amazon S3 Tables API
  description: Amazon S3 Tables API provides operations for managing table buckets and tables stored in Apache Iceberg format, enabling structured tabular data storage in Apache Parquet format within Amazon S3.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://docs.aws.amazon.com/AmazonS3/latest/API/API_Operations_Amazon_S3_Tables.html
  baseURL: https://s3tables.amazonaws.com
  tags:
  - Storage
  - Tables
  - Apache Iceberg
  - Data Lake
  - AWS
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_Operations_Amazon_S3_Tables.html
  - type: OpenAPI
    url: openapi/amazon-s3-tables-api-openapi.yml
  - type: JSONLD
    url: json-ld/amazon-s3-context.jsonld
  - type: API Reference
    url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_Operations_Amazon_S3_Tables.html
  - type: Pricing
    url: https://aws.amazon.com/s3/pricing/
  - type: Getting Started
    url: https://aws.amazon.com/s3/getting-started/
  - type: Authentication
    url: https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html
  - type: SDKs
    url: https://aws.amazon.com/tools/
  - type: FAQ
    url: https://aws.amazon.com/s3/faqs/
common:
- type: Portal
  url: https://aws.amazon.com/
- type: Website
  url: https://aws.amazon.com/s3/
- type: Documentation
  url: https://docs.aws.amazon.com/s3/
- type: Terms of Service
  url: https://aws.amazon.com/service-terms/
- type: Privacy Policy
  url: https://aws.amazon.com/privacy/
- type: Support
  url: https://aws.amazon.com/premiumsupport/
- type: Blog
  url: https://aws.amazon.com/blogs/storage/
- type: GitHub Organization
  url: https://github.com/aws
- type: Console
  url: https://console.aws.amazon.com/s3/
- type: Sign Up
  url: https://signin.aws.amazon.com/signup?request_type=register
- type: Login
  url: https://aws.amazon.com/console/
- type: Status
  url: https://health.aws.amazon.com/health/status
- type: Knowledge Center
  url: https://repost.aws/knowledge-center
- type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- type: Stack Overflow
  url: https://stackoverflow.com/questions/tagged/amazon-s3
- type: Contact
  url: https://aws.amazon.com/contact-us/
- type: Security
  url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/security.html
- type: Compliance
  url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-compliance.html
- type: Change Log
  url: https://docs.aws.amazon.com/AmazonS3/latest/API/WhatsNew.html
maintainers:
- FN: Kin Lane
  email: kin@apievangelist.com
  url: https://apievangelist.com
tags:
- Cloud Storage
- Object Storage
- Data Storage
- AWS
- Scalable Storage
- Backup
- Archive
---