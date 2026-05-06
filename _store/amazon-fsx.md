---
name: Amazon FSx
description: Amazon FSx provides fully managed file systems with the native compatibility and feature sets for workloads that require shared file storage. FSx supports four widely-used file systems including NetApp ONTAP, OpenZFS, Windows File Server, and Lustre, delivering high performance and low latency access to data.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
url: https://aws.amazon.com/fsx/
type: Index
created: '2024-01-15'
modified: '2026-04-19'
tags:
  - AWS
  - File Systems
  - Lustre
  - NetApp
  - OpenZFS
  - Storage
  - Windows
apis:
  - name: Amazon FSx API
    description: The Amazon FSx API enables programmatic access to create, manage, and monitor fully managed file systems. You can create file systems, manage backups, configure data repositories, create snapshots, and manage storage virtual machines across multiple file system types.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://aws.amazon.com/fsx/
    baseURL: https://fsx.amazonaws.com
    tags:
      - File Systems
      - High Performance
      - Managed Services
      - Storage
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/fsx/latest/APIReference/Welcome.html
      - type: OpenAPI
        url: openapi/amazon-fsx-openapi.yml
      - type: JSONSchema
        url: json-schema/amazon-fsx-file-system-schema.json
      - type: JSONSchema
        url: json-schema/amazon-fsx-backup-schema.json
      - type: JSONSchema
        url: json-schema/amazon-fsx-snapshot-schema.json
      - type: JSONSchema
        url: json-schema/amazon-fsx-storage-virtual-machine-schema.json
      - type: JSONSchema
        url: json-schema/amazon-fsx-tag-schema.json
      - type: JSONStructure
        url: json-structure/amazon-fsx-file-system-structure.json
      - type: JSONStructure
        url: json-structure/amazon-fsx-backup-structure.json
      - type: JSONStructure
        url: json-structure/amazon-fsx-snapshot-structure.json
      - type: JSONStructure
        url: json-structure/amazon-fsx-storage-virtual-machine-structure.json
      - type: JSONStructure
        url: json-structure/amazon-fsx-tag-structure.json
      - type: Example
        url: examples/amazon-fsx-file-system-example.json
      - type: Example
        url: examples/amazon-fsx-backup-example.json
      - type: Example
        url: examples/amazon-fsx-snapshot-example.json
      - type: Example
        url: examples/amazon-fsx-storage-virtual-machine-example.json
      - type: Example
        url: examples/amazon-fsx-tag-example.json
      - type: GettingStarted
        url: https://aws.amazon.com/fsx/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/fsx/pricing/
      - type: FAQ
        url: https://aws.amazon.com/fsx/faqs/
      - type: APIReference
        url: https://docs.aws.amazon.com/fsx/latest/APIReference/Welcome.html
    aid: amazon-fsx:amazon-fsx-api
common:
  - type: Portal
    url: https://aws.amazon.com/fsx/
  - type: Website
    url: https://aws.amazon.com/fsx/
  - type: Documentation
    url: https://docs.aws.amazon.com/fsx/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/storage/category/storage/amazon-fsx/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/fsx/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: YouTube
    url: https://www.youtube.com/user/AmazonWebServices
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/amazon-fsx
  - type: SpectralRules
    url: rules/amazon-fsx-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/shared/fsx.yaml
  - type: NaftikoCapability
    url: capabilities/amazon-fsx-file-system-management.yaml
  - type: Vocabulary
    url: vocabulary/amazon-fsx-vocabulary.yaml
  - type: JSON-LD
    url: json-ld/amazon-fsx-context.jsonld
  - type: Features
    data:
      - name: Multiple File System Types
        description: Choose from Lustre, Windows File Server, NetApp ONTAP, and OpenZFS based on workload requirements.
      - name: High Performance
        description: FSx for Lustre delivers hundreds of GB/s throughput and millions of IOPS for HPC and ML workloads.
      - name: Native Compatibility
        description: Fully compatible with each file system protocol — SMB for Windows, NFS for Linux, POSIX for Lustre.
      - name: Automatic Backups
        description: Daily automatic backups stored in Amazon S3 with user-initiated backup support for disaster recovery.
      - name: Multi-AZ Deployment
        description: FSx for Windows File Server and ONTAP support Multi-AZ configurations for high availability.
      - name: Data Repository Integration
        description: FSx for Lustre integrates natively with Amazon S3 for transparent data import, export, and auto-release.
      - name: Encryption at Rest
        description: All file systems are encrypted at rest using AWS KMS with customer-managed key support.
  - type: UseCases
    data:
      - name: HPC and ML Training
        description: Use FSx for Lustre for fast scratch storage in high-performance computing and distributed ML training jobs.
      - name: Windows Workloads
        description: Migrate on-premises Windows file shares to FSx for Windows File Server with Active Directory integration.
      - name: Enterprise NAS
        description: Use FSx for NetApp ONTAP for enterprise NAS with SnapMirror replication, FlexClone, and multi-protocol access.
      - name: DevOps and CI/CD
        description: Use FSx for OpenZFS for fast NFS shared storage in development, testing, and containerized workflows.
      - name: Media Processing
        description: Process high-resolution video and media assets using FSx for Lustre with S3 data repository tiering.
      - name: Database Backup Storage
        description: Use FSx for Windows File Server or ONTAP as high-performance backup targets for Oracle, SQL Server, and SAP.
  - type: Integrations
    data:
      - name: Amazon S3
        description: FSx for Lustre integrates with S3 as a data repository for transparent file import and export.
      - name: AWS Batch
        description: Use FSx for Lustre as shared scratch storage for parallel AWS Batch compute jobs.
      - name: Amazon SageMaker
        description: Mount FSx for Lustre directly to SageMaker training instances for fast ML dataset access.
      - name: Amazon ECS and EKS
        description: Mount FSx volumes as persistent volumes in containerized workloads.
      - name: AWS Directory Service
        description: Integrate FSx for Windows File Server and ONTAP with Active Directory for user authentication.
      - name: AWS Backup
        description: Centrally manage FSx backup policies across file systems using AWS Backup.
      - name: AWS KMS
        description: Encrypt all FSx file systems with customer-managed keys stored in AWS KMS.
      - name: Amazon CloudWatch
        description: Monitor FSx throughput, IOPS, and latency metrics with CloudWatch dashboards and alarms.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
aid: amazon-fsx
specificationVersion: '0.19'
---
