---
name: Amazon RDS
description: Amazon Relational Database Service (RDS) makes it easy to set up, operate, and scale a relational database in the cloud, providing cost-efficient and resizable capacity while automating time-consuming administration tasks such as hardware provisioning, database setup, patching, and backups.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
url: https://raw.githubusercontent.com/api-evangelist/amazon-rds/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-19'
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
      - type: GettingStarted
        url: https://aws.amazon.com/rds/getting-started/
      - type: FAQ
        url: https://aws.amazon.com/rds/faqs/
      - type: Service Level Agreement
        url: https://aws.amazon.com/rds/sla/
      - type: User Guide
        url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/
      - type: APIReference
        url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/
      - type: CLI
        url: https://docs.aws.amazon.com/cli/latest/reference/rds/
      - type: Security
        url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.html
common:
  - type: Portal
    url: https://aws.amazon.com/
  - type: Portal
    url: https://aws.amazon.com/rds/
  - type: Documentation
    url: https://docs.aws.amazon.com/rds/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/database/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Portal
    url: https://console.aws.amazon.com/rds/
  - type: SignUp
    url: https://signin.aws.amazon.com/signup?request_type=register
  - type: Login
    url: https://aws.amazon.com/console/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Knowledge Center
    url: https://repost.aws/knowledge-center
  - type: YouTube
    url: https://www.youtube.com/user/AmazonWebServices
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/amazon-rds
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: Security
    url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.html
  - type: Compliance
    url: https://aws.amazon.com/compliance/
  - type: JSON-LD
    url: json-ld/amazon-rds-context-context.jsonld
  - type: JSONSchema
    url: json-schema/amazon-rds-openapi-create-db-cluster-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-rds-openapi-create-db-instance-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-rds-openapi-create-db-snapshot-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-rds-openapi-db-cluster-schema.json
  - type: JSONSchema
    url: json-schema/amazon-rds-openapi-db-instance-schema.json
  - type: JSONSchema
    url: json-schema/amazon-rds-openapi-db-snapshot-schema.json
  - type: JSONSchema
    url: json-schema/amazon-rds-openapi-describe-db-clusters-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-rds-openapi-describe-db-instances-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-rds-openapi-describe-db-snapshots-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-rds-openapi-modify-db-instance-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-rds-openapi-tag-schema.json
  - type: JSONStructure
    url: json-structure/amazon-rds-instance-structure.json
  - type: JSONStructure
    url: json-structure/amazon-rds-openapi-create-db-cluster-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-rds-openapi-create-db-instance-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-rds-openapi-create-db-snapshot-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-rds-openapi-db-cluster-structure.json
  - type: JSONStructure
    url: json-structure/amazon-rds-openapi-db-instance-structure.json
  - type: JSONStructure
    url: json-structure/amazon-rds-openapi-db-snapshot-structure.json
  - type: JSONStructure
    url: json-structure/amazon-rds-openapi-describe-db-clusters-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-rds-openapi-describe-db-instances-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-rds-openapi-describe-db-snapshots-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-rds-openapi-modify-db-instance-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-rds-openapi-tag-structure.json
  - type: Example
    url: examples/amazon-rds-instance-example.json
  - type: Example
    url: examples/amazon-rds-openapi-create-db-cluster-response-example.json
  - type: Example
    url: examples/amazon-rds-openapi-create-db-instance-response-example.json
  - type: Example
    url: examples/amazon-rds-openapi-create-db-snapshot-response-example.json
  - type: Example
    url: examples/amazon-rds-openapi-db-cluster-example.json
  - type: Example
    url: examples/amazon-rds-openapi-db-instance-example.json
  - type: Example
    url: examples/amazon-rds-openapi-db-snapshot-example.json
  - type: Example
    url: examples/amazon-rds-openapi-describe-db-clusters-response-example.json
  - type: Example
    url: examples/amazon-rds-openapi-describe-db-instances-response-example.json
  - type: Example
    url: examples/amazon-rds-openapi-describe-db-snapshots-response-example.json
  - type: Example
    url: examples/amazon-rds-openapi-modify-db-instance-response-example.json
  - type: Example
    url: examples/amazon-rds-openapi-tag-example.json
  - type: NaftikoCapability
    url: capabilities/amazon-rds.yaml
  - type: NaftikoCapability
    url: capabilities/shared/amazon-rds.yaml
  - type: SpectralRules
    url: rules/amazon-rds-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-rds-vocabulary.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
tags:
  - AWS
  - Cloud Databases
  - Database Service
  - DBaaS
  - Managed Databases
  - Relational Databases
---
