---
name: Amazon EFS
description: Amazon Elastic File System (EFS) provides a simple, serverless, set-and-forget elastic file system for use with AWS cloud services and on-premises resources. EFS is built to scale on demand to petabytes without disrupting applications, growing and shrinking automatically as you add and remove files.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
url: https://aws.amazon.com/efs/
created: '2024-01-15'
modified: '2026-04-19'
tags:
  - Amazon Web Services
  - AWS
  - EFS
  - Elastic File System
  - File Storage
  - NFS
  - Serverless
  - Storage
apis:
  - name: Amazon EFS API
    description: API for managing Amazon EFS file systems, mount targets, and related resources.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    url: https://aws.amazon.com/efs/
    baseURL: https://elasticfilesystem.amazonaws.com
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/efs/latest/ug/
      - type: OpenAPI
        url: openapi/amazon-efs-openapi.yml
      - type: OpenAPI
        url: https://api.apis.guru/v2/specs/amazonaws.com/elasticfilesystem/2015-02-01/openapi.yaml
      - type: JSONSchema
        url: json-schema/amazon-efs-filesystem-schema.json
      - type: JSONLD
        url: json-ld/amazon-efs-context.jsonld
      - type: Pricing
        url: https://aws.amazon.com/efs/pricing/
      - type: GettingStarted
        url: https://aws.amazon.com/efs/getting-started/
      - type: FAQ
        url: https://aws.amazon.com/efs/faqs/
      - type: Documentation
        url: https://docs.aws.amazon.com/efs/latest/ug/
      - type: APIReference
        url: https://docs.aws.amazon.com/efs/latest/ug/API_Reference.html
      - type: Documentation
        url: https://docs.aws.amazon.com/cli/latest/reference/efs/
      - type: Security
        url: https://docs.aws.amazon.com/efs/latest/ug/security.html
      - type: JSONStructure
        url: json-structure/amazon-efs-filesystem-structure.json
      - type: Example
        url: examples/amazon-efs-filesystem-example.json
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
      - name: Elastic Scalability
        description: Automatically grows and shrinks as you add and remove files with no provisioning required.
      - name: Multiple Storage Classes
        description: Standard, Infrequent Access, and Archive storage classes with automatic lifecycle management.
      - name: Multi-AZ Replication
        description: Data automatically replicated across multiple Availability Zones for 99.999999999% durability.
      - name: Concurrent Access
        description: Thousands of EC2 instances and Lambda functions can access the same file system simultaneously.
      - name: EFS Access Points
        description: Application-specific entry points with customized directory access and POSIX permissions.
      - name: AWS Backup Integration
        description: Centralized backup management for EFS file systems with policy-based retention.
  - type: UseCases
    data:
      - name: Containerized Application Storage
        description: Persistent shared storage for containerized applications running on ECS or EKS.
      - name: Machine Learning
        description: Shared training data storage accessible simultaneously by multiple compute instances.
      - name: Content Management
        description: Shared file storage for web servers and CMS platforms requiring concurrent file access.
      - name: DevOps and Code Sharing
        description: Centralized code and configuration storage accessible by development teams and CI/CD pipelines.
      - name: Big Data Analytics
        description: High-throughput shared storage for analytics workloads requiring parallel data access.
  - type: Integrations
    data:
      - name: Amazon EC2
        description: Mount EFS file systems on EC2 instances using the NFS protocol.
      - name: Amazon ECS
        description: Provide persistent shared storage for ECS tasks with EFS volume drivers.
      - name: Amazon EKS
        description: Use the Amazon EFS CSI driver to mount EFS file systems as Kubernetes persistent volumes.
      - name: AWS Lambda
        description: Access EFS file systems from Lambda functions for shared data storage and large model loading.
      - name: AWS Backup
        description: Automated backup of EFS file systems with centralized policy management.
  - type: SpectralRules
    url: rules/amazon-efs-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-efs-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/efs-management.yaml
maintainer:
  name: Kin Lane
  email: kin@apievangelist.com
---
