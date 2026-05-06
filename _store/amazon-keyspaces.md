---
name: Amazon Keyspaces
segments:
  - Databases
  - NoSQL
description: Amazon Keyspaces (for Apache Cassandra) is a scalable, highly available, and managed Apache Cassandra-compatible database service that lets you run Cassandra workloads on AWS without managing servers or software.
url: https://aws.amazon.com/keyspaces/
type: Index
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
tags:
  - AWS
  - Cassandra
  - Database
  - Managed Database
  - NoSQL
  - Wide Column
created: '2024-01-15'
modified: '2026-04-19'
apis:
  - name: Amazon Keyspaces API
    description: The Amazon Keyspaces API provides programmatic access to manage Cassandra-compatible keyspaces and tables, configure capacity modes, encryption, and point-in-time recovery for serverless Cassandra workloads.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://aws.amazon.com/keyspaces/
    baseURL: https://cassandra.amazonaws.com
    tags:
      - Cassandra
      - NoSQL Database
      - Serverless
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/keyspaces/latest/devguide/what-is-keyspaces.html
      - type: OpenAPI
        url: https://api.apis.guru/v2/specs/amazonaws.com/keyspaces/2022-02-10/openapi.yaml
      - type: Pricing
        url: https://aws.amazon.com/keyspaces/pricing/
      - type: GettingStarted
        url: https://aws.amazon.com/keyspaces/getting-started/
      - type: FAQ
        url: https://aws.amazon.com/keyspaces/faqs/
      - type: Features
        url: https://aws.amazon.com/keyspaces/features/
      - type: Documentation
        url: https://docs.aws.amazon.com/keyspaces/latest/devguide/what-is-keyspaces.html
      - type: APIReference
        url: https://docs.aws.amazon.com/keyspaces/latest/APIReference/Welcome.html
      - type: OpenAPI
        url: openapi/amazon-keyspaces-openapi.yml
      - type: JSONLD
        url: json-ld/amazon-keyspaces-context.jsonld
      - type: JSONSchema
        url: json-schema/amazon-keyspaces-keyspace-schema.json
      - type: JSONSchema
        url: json-schema/amazon-keyspaces-table-schema.json
common:
  - type: Blog
    url: https://aws.amazon.com/blogs/database/category/database/amazon-keyspaces/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Console
    url: https://console.aws.amazon.com/keyspaces/home
  - type: CLI
    url: https://docs.aws.amazon.com/cli/latest/reference/keyspaces/
  - type: SDK
    url: https://aws.amazon.com/tools/
  - type: StatusPage
    url: https://status.aws.amazon.com/
  - type: Compliance
    url: https://aws.amazon.com/compliance/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: Portal
    url: https://aws.amazon.com/keyspaces/
  - type: Documentation
    url: https://docs.aws.amazon.com/keyspaces/
  - type: Pricing
    url: https://aws.amazon.com/keyspaces/pricing/
  - type: GettingStarted
    url: https://aws.amazon.com/keyspaces/getting-started/
  - type: FAQ
    url: https://aws.amazon.com/keyspaces/faqs/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Features
    data:
      - name: Cassandra Compatibility
        description: Fully compatible with Apache Cassandra drivers, tools, and applications with no code changes required.
      - name: Serverless Scaling
        description: Automatically scales table throughput and storage up and down based on application traffic.
      - name: Point-in-Time Recovery
        description: Continuous backup with PITR enables restoration of tables to any second within the last 35 days.
      - name: Encryption at Rest
        description: Data is encrypted at rest by default using AWS managed keys or customer-managed keys via AWS KMS.
      - name: Virtual Private Cloud (VPC) Support
        description: Access Amazon Keyspaces from within VPCs using VPC endpoints for enhanced network security.
      - name: Capacity Modes
        description: Choose on-demand or provisioned capacity mode with auto scaling for predictable workloads.
  - type: UseCases
    data:
      - name: IoT Data Storage
        description: Store high-volume sensor data and telemetry from IoT devices with wide-column schema.
      - name: User Activity Tracking
        description: Track user events, clickstreams, and behavioral data at massive scale.
      - name: Time-Series Data
        description: Manage time-series data for monitoring, metrics, and log aggregation.
      - name: Migrate Cassandra Workloads
        description: Lift and shift existing Cassandra applications to a fully managed cloud service.
  - type: Integrations
    data:
      - name: AWS KMS
        description: Use customer-managed keys for encryption with AWS Key Management Service.
      - name: AWS CloudTrail
        description: Audit all API calls to Amazon Keyspaces for security and compliance.
      - name: Amazon VPC
        description: Access Keyspaces securely from within your VPC using VPC endpoints.
      - name: AWS Identity and Access Management
        description: Control access to Keyspaces resources using IAM policies and roles.
  - type: SpectralRules
    url: rules/amazon-keyspaces-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/amazon-keyspaces-workflow.yaml
  - type: Vocabulary
    url: vocabulary/amazon-keyspaces-vocabulary.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
include: []
---
