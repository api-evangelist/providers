---
aid: amazon-dms
url: https://raw.githubusercontent.com/api-evangelist/amazon-dms/refs/heads/main/apis.yml
apis:
- name: Amazon DMS API
  description: The AWS Database Migration Service API provides programmatic access to create and manage replication instances, endpoints, replication tasks, and monitor migration progress for database migrations to AWS.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  url: https://aws.amazon.com/dms/
  baseURL: https://dms.amazonaws.com
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/dms/latest/APIReference/
  - type: OpenAPI
    url: openapi/amazon-dms-openapi.yml
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/dms/2016-01-01/openapi.yaml
  - type: JSONSchema
    url: json-schema/amazon-dms-replication-task-schema.json
  - type: JSONLD
    url: json-ld/amazon-dms-context.jsonld
  - type: Pricing
    url: https://aws.amazon.com/dms/pricing/
  - type: Getting Started
    url: https://aws.amazon.com/dms/getting-started/
  - type: FAQ
    url: https://aws.amazon.com/dms/faqs/
  - type: User Guide
    url: https://docs.aws.amazon.com/dms/latest/userguide/
  - type: API Reference
    url: https://docs.aws.amazon.com/dms/latest/APIReference/
  - type: CLI Reference
    url: https://docs.aws.amazon.com/cli/latest/reference/dms/
  - type: Security
    url: https://docs.aws.amazon.com/dms/latest/userguide/security.html
name: Amazon DMS
tags:
- AWS
- Data Replication
- Database
- Database Migration
- Migration
type: Contract
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: AWS Database Migration Service (AWS DMS) helps you migrate databases to AWS quickly and securely. The source database remains fully operational during the migration, minimizing downtime to applications that rely on the database. AWS DMS can migrate your data to and from the most widely used commercial and open-source databases, supporting homogeneous and heterogeneous migrations.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

