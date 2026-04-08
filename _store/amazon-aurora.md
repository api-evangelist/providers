---
aid: amazon-aurora
url: https://raw.githubusercontent.com/api-evangelist/amazon-aurora/refs/heads/main/apis.yml
apis:
- name: Amazon Aurora API
  description: The Amazon Aurora API is accessed through the Amazon RDS API and enables programmatic management of Aurora DB clusters, instances, snapshots, parameter groups, and other database resources for both MySQL and PostgreSQL compatible editions.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/rds/aurora/
  baseURL: https://rds.amazonaws.com
  tags:
  - Database
  - MySQL
  - PostgreSQL
  - Relational
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html
  - type: OpenAPI
    url: openapi/amazon-aurora-openapi.yml
  - type: JSON Schema
    url: json-schema/amazon-aurora-schema.json
  - type: JSON-LD
    url: json-ld/amazon-aurora-context.jsonld
  - type: Pricing
    url: https://aws.amazon.com/rds/aurora/pricing/
  - type: Getting Started
    url: https://aws.amazon.com/rds/aurora/getting-started/
  - type: FAQ
    url: https://aws.amazon.com/rds/aurora/faqs/
  - type: User Guide
    url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html
  - type: API Reference
    url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/Welcome.html
  - type: CLI Reference
    url: https://docs.aws.amazon.com/cli/latest/reference/rds/
  - type: Security
    url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.html
name: Amazon Aurora
tags:
- AWS
- Cloud Database
- Database
- MySQL
- PostgreSQL
- RDS
- Relational Database
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Amazon Aurora is a MySQL and PostgreSQL-compatible relational database built for the cloud that combines the performance and availability of traditional enterprise databases with the simplicity and cost-effectiveness of open source databases.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

