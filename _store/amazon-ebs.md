---
name: Amazon EBS
description: Amazon Elastic Block Store (EBS) provides persistent block storage volumes for use with Amazon EC2 instances. EBS volumes are highly available and reliable storage volumes that can be attached to any running instance in the same Availability Zone, offering consistent and low-latency performance for workloads that require persistent storage.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
url: https://aws.amazon.com/ebs/
created: '2024-01-15'
modified: '2026-04-19'
tags:
  - Amazon Web Services
  - AWS
  - Block Storage
  - EBS
  - EC2
  - Snapshots
  - Storage
  - Volumes
apis:
  - name: Amazon EBS API
    description: API for managing Amazon EBS volumes, snapshots, and related resources through the EC2 API.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    url: https://aws.amazon.com/ebs/
    baseURL: https://ec2.amazonaws.com
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/ebs/latest/userguide/
      - type: OpenAPI
        url: openapi/amazon-ebs-openapi.yml
      - type: JSONSchema
        url: json-schema/amazon-ebs-volume-schema.json
      - type: JSONLD
        url: json-ld/amazon-ebs-context.jsonld
      - type: Pricing
        url: https://aws.amazon.com/ebs/pricing/
      - type: GettingStarted
        url: https://aws.amazon.com/ebs/getting-started/
      - type: FAQ
        url: https://aws.amazon.com/ebs/faqs/
      - type: Documentation
        url: https://docs.aws.amazon.com/ebs/latest/userguide/
      - type: APIReference
        url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/
      - type: Documentation
        url: https://docs.aws.amazon.com/cli/latest/reference/ec2/
      - type: Security
        url: https://docs.aws.amazon.com/ebs/latest/userguide/security.html
      - type: JSONStructure
        url: json-structure/amazon-ebs-volume-structure.json
      - type: Example
        url: examples/amazon-ebs-volume-example.json
common:
  - type: Portal
    url: https://aws.amazon.com/
  - type: DeveloperPortal
    url: https://aws.amazon.com/
  - type: Documentation
    url: https://docs.aws.amazon.com/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/support/
  - type: Blog
    url: https://aws.amazon.com/blogs/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://status.aws.amazon.com/
  - type: KnowledgeCenter
    url: https://repost.aws/knowledge-center
  - type: YouTube
    url: https://www.youtube.com/user/AmazonWebServices
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/amazon-web-services
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: Security
    url: https://aws.amazon.com/security/
  - type: Compliance
    url: https://aws.amazon.com/compliance/
  - type: Features
    data:
      - name: Multiple Volume Types
        description: Choose from gp3, gp2, io2, io1, st1, sc1, and io2 Block Express volumes optimized for different workloads.
      - name: EBS Snapshots
        description: Point-in-time backups stored in Amazon S3 for disaster recovery, migration, and data sharing.
      - name: Encryption
        description: AES-256 encryption at rest and in transit using AWS KMS customer-managed or AWS-managed keys.
      - name: Elastic Volumes
        description: Dynamically modify volume size, performance, and type without detaching from instances.
      - name: Data Lifecycle Manager
        description: Automate snapshot creation, retention, deletion, and cross-account sharing with policy-based management.
      - name: Multi-Attach
        description: Attach a single io2 volume to up to 16 EC2 instances simultaneously for high availability.
  - type: UseCases
    data:
      - name: Relational Databases
        description: High-performance persistent storage for MySQL, PostgreSQL, Oracle, and SQL Server databases.
      - name: NoSQL Databases
        description: Low-latency block storage for MongoDB, Cassandra, and other NoSQL workloads.
      - name: Enterprise Applications
        description: SAN workload migration for I/O-intensive SAP, Oracle, and other enterprise applications.
      - name: Big Data Analytics
        description: Resizable storage for Hadoop, Spark, and other big data cluster deployments.
      - name: Boot Volumes
        description: OS and application boot volumes for all EC2 instance types.
  - type: Integrations
    data:
      - name: Amazon EC2
        description: Attach EBS volumes to EC2 instances in the same Availability Zone for persistent storage.
      - name: Amazon Data Lifecycle Manager
        description: Automate snapshot management and cross-account data sharing policies.
      - name: AWS Backup
        description: Centralized backup management for EBS volumes with configurable retention and compliance.
      - name: AWS Key Management Service
        description: Manage encryption keys for EBS volumes and snapshots.
      - name: Amazon CloudWatch
        description: Monitor EBS volume performance metrics including IOPS, throughput, and latency.
  - type: SpectralRules
    url: rules/amazon-ebs-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-ebs-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/ebs-management.yaml
maintainer:
  name: Kin Lane
  email: kin@apievangelist.com
---
