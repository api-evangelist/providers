---
aid: amazon-s3-glacier
url: https://raw.githubusercontent.com/api-evangelist/amazon-s3-glacier/refs/heads/main/apis.yml
apis:
- name: Amazon S3 Glacier API
  description: The Amazon S3 Glacier API provides programmatic access to manage long-term archive storage. It enables developers to create and manage vaults, upload and retrieve archives, configure vault notifications and access policies, initiate inventory retrieval jobs, and manage data lifecycle for cost- effective archival storage.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/s3/storage-classes/glacier/
  baseURL: https://glacier.amazonaws.com
  tags:
  - Archive
  - AWS
  - Backup
  - Storage
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/amazonglacier/
  - type: OpenAPI
    url: openapi/amazon-s3-glacier-openapi.yml
  - type: Pricing
    url: https://aws.amazon.com/s3/pricing/
  - type: Getting Started
    url: https://aws.amazon.com/s3/getting-started/
  - type: FAQ
    url: https://aws.amazon.com/s3/faqs/
name: Amazon S3 Glacier
tags:
- Archive
- AWS
- Backup
- Storage
type: Contract
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Amazon S3 Glacier is a secure, durable, and extremely low-cost Amazon S3 storage class purpose-built for long-term data archiving and digital preservation. It provides comprehensive security and compliance capabilities that can help meet even the most stringent regulatory requirements, with retrieval options ranging from minutes to hours depending on your access needs.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

