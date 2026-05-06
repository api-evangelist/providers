---
aid: amazon-directory-service
name: Amazon Directory Service
description: AWS Directory Service for Microsoft Active Directory, also known as AWS Managed Microsoft AD, enables your directory-aware workloads and AWS resources to use managed Active Directory in AWS. It provides a fully managed, highly available Microsoft Active Directory in the AWS Cloud, with features including trust relationships, domain controllers, LDAPS, and multi-account sharing.
type: Index
x-type: company
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Active Directory
  - Authentication
  - AWS
  - Directory Services
  - Identity Management
url: https://raw.githubusercontent.com/api-evangelist/amazon-directory-service/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-directory-service:aws-directory-service-api
    name: AWS Directory Service API
    description: The AWS Directory Service API provides programmatic access to create and manage directories, trusts, snapshots, and domain controllers for Microsoft Active Directory in the AWS Cloud.
    humanURL: https://aws.amazon.com/directoryservice/
    baseURL: https://ds.amazonaws.com
    tags:
      - Active Directory
      - Directory Services
      - Identity Management
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/directoryservice/latest/devguide/what_is.html
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/amazon-directory-service/refs/heads/main/openapi/amazon-directory-service-openapi.yaml
      - type: GettingStarted
        url: https://aws.amazon.com/directoryservice/getting-started/
common:
  - type: Portal
    url: https://aws.amazon.com/directoryservice/
  - type: Website
    url: https://aws.amazon.com/directoryservice/
  - type: Documentation
    url: https://docs.aws.amazon.com/directoryservice/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/security/tag/aws-directory-service/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/directoryservicev2/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/amazon-directory-service/refs/heads/main/rules/amazon-directory-service-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/amazon-directory-service/refs/heads/main/vocabulary/amazon-directory-service-vocabulary.yaml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/amazon-directory-service/refs/heads/main/capabilities/active-directory-management.yaml
  - type: Features
    data:
      - name: Managed Microsoft AD
        description: Fully managed AWS Managed Microsoft Active Directory with automatic patching and monitoring
      - name: Simple AD
        description: Standalone managed directory powered by Samba 4 for basic AD functionality
      - name: AD Connector
        description: Proxy service for connecting AWS applications to existing on-premises AD
      - name: Trust Relationships
        description: One-way and two-way trust relationships between AWS and on-premises directories
      - name: Multi-Region Replication
        description: Replicate your AWS Managed Microsoft AD across multiple AWS Regions
      - name: Directory Sharing
        description: Share a single directory across multiple AWS accounts and VPCs
  - type: UseCases
    data:
      - name: Hybrid Identity
        description: Extend on-premises Active Directory into AWS for unified identity management
      - name: Workload Authentication
        description: Enable Windows and Linux workloads to join and authenticate against managed AD
      - name: AWS Application Integration
        description: Use managed AD for AWS WorkSpaces, RDS, and other AD-aware services
      - name: LDAPS Encryption
        description: Secure LDAP communications with certificates for compliance requirements
      - name: Disaster Recovery
        description: Use directory snapshots for point-in-time recovery of directory data
  - type: Integrations
    data:
      - name: Amazon WorkSpaces
        description: Join WorkSpaces desktops to managed AD for enterprise desktop management
      - name: Amazon RDS
        description: Enable Windows Authentication for SQL Server RDS instances via managed AD
      - name: AWS IAM Identity Center
        description: Use managed AD as identity source for centralized access management
      - name: AWS CloudTrail
        description: Audit all Directory Service API calls for compliance and security monitoring
      - name: Amazon SNS
        description: Receive directory event notifications via SNS topic subscriptions
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
