---
aid: amazon-backup
url: https://raw.githubusercontent.com/api-evangelist/amazon-backup/refs/heads/main/apis.yml
apis:
- name: Amazon Backup API
  description: API for centrally managing and automating backups across AWS services including Amazon EBS, Amazon RDS, Amazon DynamoDB, Amazon EFS, Amazon FSx, Amazon EC2, and AWS Storage Gateway. Supports creating backup plans, managing backup vaults, starting and monitoring backup jobs, and restoring resources.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/backup/
  baseURL: https://backup.amazonaws.com
  tags:
  - AWS
  - Backup
  - Data Protection
  - Disaster Recovery
  - Storage
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/aws-backup/latest/devguide/
  - type: OpenAPI
    url: openapi/amazon-backup-openapi.yml
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/backup/2018-11-15/openapi.yaml
  - type: JSONSchema
    url: json-schema/amazon-backup-plan-schema.json
  - type: JSONLD
    url: json-ld/amazon-backup-context.jsonld
  - type: Pricing
    url: https://aws.amazon.com/backup/pricing/
  - type: Getting Started
    url: https://aws.amazon.com/backup/getting-started/
  - type: FAQ
    url: https://aws.amazon.com/backup/faqs/
  - type: User Guide
    url: https://docs.aws.amazon.com/aws-backup/latest/devguide/
  - type: API Reference
    url: https://docs.aws.amazon.com/aws-backup/latest/devguide/API_Reference.html
  - type: CLI Reference
    url: https://docs.aws.amazon.com/cli/latest/reference/backup/
  - type: Security
    url: https://docs.aws.amazon.com/aws-backup/latest/devguide/security.html
name: Amazon Backup
tags:
- AWS
- Backup
- Data Protection
- Disaster Recovery
- Storage
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: AWS Backup is a fully managed backup service that centralizes and automates the backup of data across AWS services, enabling you to configure backup policies, monitor backup activity, and restore resources with a single, unified console and API.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

