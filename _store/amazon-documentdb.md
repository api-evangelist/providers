---
name: Amazon DocumentDB
description: Amazon DocumentDB is a fully managed, MongoDB-compatible document database service that makes it easy to set up, operate, and scale MongoDB-compatible databases in the cloud. DocumentDB is designed from the ground up to give you the performance, scalability, and availability you need when operating mission-critical MongoDB workloads at scale.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
url: https://aws.amazon.com/documentdb/
created: '2024-01-15'
modified: '2026-04-19'
tags:
  - Amazon Web Services
  - AWS
  - Database
  - Document Database
  - DocumentDB
  - Managed Database
  - MongoDB
  - NoSQL
apis:
  - name: Amazon DocumentDB API
    description: API for managing Amazon DocumentDB clusters, instances, parameter groups, subnet groups, snapshots, and related resources.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://aws.amazon.com/documentdb/
    baseURL: https://rds.amazonaws.com
    tags:
      - AWS
      - Database
      - Document Database
      - MongoDB
      - NoSQL
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/documentdb/latest/developerguide/
      - type: OpenAPI
        url: openapi/amazon-documentdb-openapi.yml
      - type: OpenAPI
        url: https://api.apis.guru/v2/specs/amazonaws.com/docdb/2014-10-31/openapi.yaml
      - type: JSONSchema
        url: json-schema/amazon-documentdb-dbcluster-schema.json
      - type: JSONLD
        url: json-ld/amazon-documentdb-context.jsonld
      - type: Pricing
        url: https://aws.amazon.com/documentdb/pricing/
      - type: GettingStarted
        url: https://aws.amazon.com/documentdb/getting-started/
      - type: FAQ
        url: https://aws.amazon.com/documentdb/faqs/
      - type: APIReference
        url: https://docs.aws.amazon.com/documentdb/latest/developerguide/API_Reference.html
      - type: Authentication
        url: https://docs.aws.amazon.com/documentdb/latest/developerguide/security.html
      - type: RateLimits
        url: https://docs.aws.amazon.com/documentdb/latest/developerguide/limits.html
      - type: JSONStructure
        url: json-structure/amazon-documentdb-dbcluster-structure.json
      - type: Example
        url: examples/amazon-documentdb-dbcluster-example.json
common:
  - type: Portal
    url: https://aws.amazon.com/
  - type: DeveloperPortal
    url: https://aws.amazon.com/developer/
  - type: Documentation
    url: https://docs.aws.amazon.com/documentdb/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/support/
  - type: Blog
    url: https://aws.amazon.com/blogs/database/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/docdb/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: KnowledgeCenter
    url: https://repost.aws/knowledge-center
  - type: YouTube
    url: https://www.youtube.com/user/AmazonWebServices
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/amazon-documentdb
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: Security
    url: https://aws.amazon.com/security/
  - type: Compliance
    url: https://aws.amazon.com/compliance/
  - type: Features
    data:
      - name: Serverless Architecture
        description: Automatically scales capacity up or down in fine-grained increments based on application demand, with up to 90% cost savings versus peak provisioning.
      - name: MongoDB Compatibility
        description: Migrate applications typically without code changes or downtime using existing MongoDB drivers and tools.
      - name: Global Clusters
        description: Automatically replicates data across up to 10 AWS Regions for low-latency reads and disaster recovery.
      - name: Fully Managed
        description: Eliminates database patching, backups, and monitoring overhead so you can focus on application development.
      - name: I/O-Optimized Storage
        description: Provides up to 40% cost savings for I/O-intensive workloads with predictable pricing.
      - name: Memory-Optimized Instances
        description: Offers memory-optimized instance types with up to 43% cost savings for large workloads.
      - name: Automated Backups
        description: Continuous backups to Amazon S3 and point-in-time recovery within the backup retention window.
      - name: Encryption at Rest and in Transit
        description: Data is encrypted using AES-256, with support for AWS KMS customer-managed keys.
  - type: UseCases
    data:
      - name: Content Management Systems
        description: Store and retrieve flexible JSON-structured content with rich query capabilities for CMS platforms.
      - name: E-Commerce Platforms
        description: Manage product catalogs, user profiles, and order data with scalable document storage.
      - name: Mobile and Web Applications
        description: Power real-time application backends with low-latency, scalable document storage.
      - name: Generative AI Applications
        description: Store and retrieve context, embeddings, and conversational history for AI-powered agentic applications.
      - name: Gaming Applications
        description: Handle player profiles, leaderboards, and game state with flexible schema and high throughput.
  - type: Integrations
    data:
      - name: Amazon CloudWatch
        description: Monitor DocumentDB cluster metrics, set alarms, and view performance data through CloudWatch dashboards.
      - name: AWS IAM
        description: Control access to DocumentDB resources and operations using IAM policies and roles.
      - name: AWS Backup
        description: Centrally manage and automate backups of DocumentDB clusters using AWS Backup policies.
      - name: Amazon OpenSearch Service
        description: Zero-ETL integration to replicate DocumentDB data to OpenSearch for full-text search and analytics.
      - name: AWS CloudTrail
        description: Log all DocumentDB API calls for auditing, compliance, and security analysis.
      - name: AWS Key Management Service
        description: Manage encryption keys for DocumentDB clusters using KMS customer-managed keys.
  - type: SpectralRules
    url: rules/amazon-documentdb-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-documentdb-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/documentdb-management.yaml
maintainer:
  name: Kin Lane
  email: kin@apievangelist.com
---
