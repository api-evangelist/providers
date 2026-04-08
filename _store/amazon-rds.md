---
aid: amazon-rds
url: https://raw.githubusercontent.com/api-evangelist/amazon-rds/refs/heads/main/apis.yml
apis:
- name: Amazon RDS API
  description: Core API for managing Amazon RDS database instances, clusters, snapshots, parameter groups, subnet groups, and other relational database resources across multiple database engines including MySQL, PostgreSQL, MariaDB, Oracle, SQL Server, and Amazon Aurora.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/rds/
  baseURL: https://rds.amazonaws.com
  tags:
  - AWS
  - Cloud Databases
  - Databases
  - Managed Databases
  - Relational Databases
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/Welcome.html
  - type: OpenAPI
    url: openapi/amazon-rds-openapi.yml
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/rds/2014-10-31/openapi.yaml
  - type: JSONSchema
    url: json-schema/amazon-rds-instance-schema.json
  - type: JSONLD
    url: json-ld/amazon-rds-context.jsonld
  - type: Pricing
    url: https://aws.amazon.com/rds/pricing/
  - type: Getting Started
    url: https://aws.amazon.com/rds/getting-started/
  - type: FAQ
    url: https://aws.amazon.com/rds/faqs/
  - type: Service Level Agreement
    url: https://aws.amazon.com/rds/sla/
  - type: User Guide
    url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/
  - type: API Reference
    url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/
  - type: CLI Reference
    url: https://docs.aws.amazon.com/cli/latest/reference/rds/
  - type: Security
    url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.html
name: Amazon RDS
tags:
- AWS
- Cloud Databases
- Database Service
- DBaaS
- Managed Databases
- Relational Databases
type: Contract
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Amazon Relational Database Service (RDS) makes it easy to set up, operate, and scale a relational database in the cloud, providing cost-efficient and resizable capacity while automating time-consuming administration tasks such as hardware provisioning, database setup, patching, and backups.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

