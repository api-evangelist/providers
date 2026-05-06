---
aid: amazon-datasync
name: Amazon DataSync
description: AWS DataSync is an online data transfer service that simplifies, automates, and accelerates moving data between on-premises storage systems, AWS storage services, and other cloud storage. DataSync can transfer data at speeds up to 10 times faster than open-source tools by using purpose-built network protocol and parallel multi-threaded architecture. It supports NFS, SMB, HDFS, S3, EFS, FSx, and more as transfer endpoints.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Data Transfer
  - Migration
  - Storage
  - Automation
  - Hybrid Cloud
url: https://raw.githubusercontent.com/api-evangelist/amazon-datasync/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-datasync:amazon-datasync-api
    name: Amazon DataSync REST API
    description: RESTful API for AWS DataSync enabling management of data transfer tasks, locations, agents, and task executions for automated data movement between on-premises storage systems and AWS cloud storage. Supports NFS, SMB, S3, EFS, FSx, and HDFS as transfer endpoints.
    humanURL: https://aws.amazon.com/datasync/
    baseURL: https://datasync.amazonaws.com
    tags:
      - Data Transfer
      - Migration
      - Storage
      - Automation
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/datasync/latest/userguide/API_Reference.html
      - type: OpenAPI
        url: openapi/amazon-datasync-api-openapi.yml
      - type: OpenAPI
        url: https://api.apis.guru/v2/specs/amazonaws.com/datasync/2018-11-09/openapi.yaml
      - type: GettingStarted
        url: https://aws.amazon.com/datasync/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/datasync/pricing/
      - type: FAQ
        url: https://aws.amazon.com/datasync/faqs/
      - type: APIReference
        url: https://docs.aws.amazon.com/datasync/latest/userguide/API_Reference.html
      - type: Authentication
        url: https://docs.aws.amazon.com/datasync/latest/userguide/security.html
      - type: JSONSchema
        url: json-schema/task-schema.json
      - type: JSONSchema
        url: json-schema/location-schema.json
      - type: JSONSchema
        url: json-schema/agent-schema.json
      - type: JSONSchema
        url: json-schema/task-execution-schema.json
      - type: JSONLD
        url: json-ld/amazon-datasync-context.jsonld
common:
  - type: Portal
    url: https://aws.amazon.com/datasync/
  - type: DeveloperPortal
    url: https://aws.amazon.com/datasync/
  - type: Documentation
    url: https://docs.aws.amazon.com/datasync/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/storage/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/datasync/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: YouTube
    url: https://www.youtube.com/user/AmazonWebServices
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/aws-datasync
  - type: SpectralRules
    url: rules/amazon-datasync-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-datasync-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/data-transfer-operations.yaml
  - type: NaftikoCapability
    url: capabilities/shared/datasync.yaml
  - type: Features
    data:
      - name: High-Speed Data Transfer
        description: Transfer data at speeds up to 10 times faster than open-source tools using purpose-built multi-threaded network protocol over TLS.
      - name: Multi-Protocol Support
        description: Connect to NFS, SMB, HDFS, Amazon S3, Amazon EFS, FSx for Windows, FSx for Lustre, and FSx for NetApp ONTAP as transfer endpoints.
      - name: Automated Data Validation
        description: Automatically verify data integrity using checksums at both source and destination to ensure byte-for-byte data consistency after transfer.
      - name: Scheduled Transfers
        description: Configure recurring scheduled transfers on hourly, daily, or weekly cadences for ongoing data synchronization between systems.
      - name: On-Premises Agent
        description: Deploy the DataSync agent VM on-premises to connect local NFS and SMB storage to AWS without opening inbound firewall ports.
      - name: Bandwidth Throttling
        description: Control the network bandwidth consumed by DataSync transfers to minimize impact on production workloads during business hours.
      - name: CloudWatch Integration
        description: Monitor transfer metrics, task execution history, and set up alarms for failed transfers using Amazon CloudWatch.
  - type: UseCases
    data:
      - name: Data Center Migration
        description: Migrate petabytes of data from on-premises NAS and SAN systems to Amazon S3 or EFS during cloud adoption and data center exit projects.
      - name: Ongoing Hybrid Synchronization
        description: Keep on-premises and cloud storage in sync on a scheduled basis for hybrid cloud architectures and distributed workloads.
      - name: Backup and Archive to Cloud
        description: Transfer on-premises file data to Amazon S3 Glacier for cost-effective long-term archival and backup storage.
      - name: Data Distribution
        description: Transfer datasets between AWS Regions or across AWS accounts for data sharing, disaster recovery, or multi-region analytics.
      - name: HPC Data Staging
        description: Stage large datasets from S3 or on-premises storage to FSx for Lustre for high-performance computing workloads on AWS.
  - type: Integrations
    data:
      - name: Amazon S3
        description: Primary cloud storage destination supporting all S3 storage classes including Glacier for cost-effective data archival.
      - name: Amazon EFS
        description: Transfer data to and from Amazon Elastic File System for shared file storage accessible from multiple EC2 instances.
      - name: Amazon FSx
        description: Integrate with FSx for Windows, FSx for Lustre, and FSx for NetApp ONTAP as high-performance managed file system destinations.
      - name: Amazon CloudWatch
        description: Receive DataSync task execution metrics, transfer rates, and error alerts in CloudWatch for monitoring and incident response.
      - name: AWS Snowball
        description: Use Snowball for initial bulk data transfer followed by DataSync for ongoing incremental synchronization after migration.
      - name: AWS Storage Gateway
        description: Combine Storage Gateway for cache-based hybrid access with DataSync for bulk data movement between on-premises and cloud.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
