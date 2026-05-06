---
aid: amazon-dms
name: Amazon DMS
description: AWS Database Migration Service (AWS DMS) helps you migrate databases to AWS quickly and securely. The source database remains fully operational during the migration, minimizing downtime to applications that rely on the database. AWS DMS can migrate your data to and from the most widely used commercial and open-source databases, supporting homogeneous and heterogeneous migrations with continuous data replication.
type: Index
x-type: company
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Data Replication
  - Database
  - Database Migration
  - Migration
url: https://raw.githubusercontent.com/api-evangelist/amazon-dms/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-dms:amazon-dms-api
    name: Amazon DMS API
    description: The AWS Database Migration Service API provides programmatic access to create and manage replication instances, endpoints, replication tasks, and monitor migration progress for database migrations to AWS.
    humanURL: https://aws.amazon.com/dms/
    baseURL: https://dms.amazonaws.com
    tags:
      - Database Migration
      - Data Replication
      - AWS
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/dms/latest/APIReference/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/amazon-dms/refs/heads/main/openapi/amazon-dms-openapi.yaml
      - type: GettingStarted
        url: https://aws.amazon.com/dms/getting-started/
common:
  - type: Portal
    url: https://aws.amazon.com/dms/
  - type: Website
    url: https://aws.amazon.com/dms/
  - type: Documentation
    url: https://docs.aws.amazon.com/dms/
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
  - type: Console
    url: https://console.aws.amazon.com/dms/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/amazon-dms/refs/heads/main/rules/amazon-dms-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/amazon-dms/refs/heads/main/vocabulary/amazon-dms-vocabulary.yaml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/amazon-dms/refs/heads/main/capabilities/database-migration-management.yaml
  - type: Features
    data:
      - name: Homogeneous Migration
        description: Migrate between databases of the same engine type with minimal conversion
      - name: Heterogeneous Migration
        description: Migrate between different database engines using Schema Conversion Tool
      - name: Continuous Data Replication
        description: Continuously replicate data changes using change data capture (CDC)
      - name: Minimal Downtime Migration
        description: Keep source database operational during migration for high availability
      - name: Multi-AZ Replication
        description: Provision replication instances across multiple Availability Zones for resilience
      - name: Premigration Assessment
        description: Run automated assessments to identify migration issues before starting
  - type: UseCases
    data:
      - name: Database Consolidation
        description: Consolidate multiple databases into a single AWS-managed database
      - name: Cross-Engine Migration
        description: Migrate from Oracle or SQL Server to open-source Aurora or PostgreSQL
      - name: Development and Testing
        description: Continuously replicate production data to development environments
      - name: Active-Active Replication
        description: Maintain synchronized database replicas across regions for failover
      - name: Analytics Migration
        description: Migrate transactional databases to analytical data warehouses like Redshift
  - type: Integrations
    data:
      - name: Amazon Aurora
        description: Target Aurora MySQL and Aurora PostgreSQL for cost-efficient managed databases
      - name: Amazon RDS
        description: Migrate to RDS instances for fully managed relational database hosting
      - name: Amazon Redshift
        description: Migrate data warehouses or replicate transactional data for analytics
      - name: AWS Schema Conversion Tool
        description: Convert database schemas for heterogeneous migrations between engine types
      - name: Amazon S3
        description: Stream migration data to S3 for archival or downstream processing
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
