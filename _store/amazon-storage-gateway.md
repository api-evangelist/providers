---
name: Amazon Storage Gateway
description: AWS Storage Gateway is a hybrid cloud storage service that provides on-premises access to virtually unlimited cloud storage. It seamlessly connects on-premises environments to AWS cloud storage, providing low-latency data access with local caching.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
url: https://aws.amazon.com/storagegateway/
created: '2024-01-15'
modified: '2026-04-19'
apis:
  - name: Amazon Storage Gateway REST API
    description: RESTful API for AWS Storage Gateway enabling management of gateways, volumes, tapes, file shares, and cached storage for hybrid cloud storage architectures.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://aws.amazon.com/storagegateway/
    baseURL: https://storagegateway.amazonaws.com
    tags:
      - AWS
      - Gateway
      - Hybrid Cloud
      - Storage
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/storagegateway/latest/APIReference/Welcome.html
      - type: OpenAPI
        url: openapi/amazon-storage-gateway.yaml
      - type: GettingStarted
        url: https://aws.amazon.com/storagegateway/
      - type: Pricing
        url: https://aws.amazon.com/storagegateway/pricing/
      - type: FAQ
        url: https://aws.amazon.com/storagegateway/faqs/
common:
  - type: Portal
    url: https://aws.amazon.com/storagegateway/
  - type: Documentation
    url: https://docs.aws.amazon.com/storagegateway/latest/APIReference/Welcome.html
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
    url: https://console.aws.amazon.com/storagegateway/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-storage-gateway-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-storage-gateway-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/shared/amazon-storage-gateway.yaml
  - type: Features
    data:
      - name: File Gateway
        description: Provides NFS and SMB access to objects stored in Amazon S3.
      - name: Volume Gateway
        description: Provides iSCSI block storage backed by Amazon S3 and Glacier.
      - name: Tape Gateway
        description: Virtual tape library backed by S3 and Glacier for backup.
      - name: Hybrid Storage
        description: Seamlessly integrate on-premises environments with AWS storage.
      - name: Local Caching
        description: Cache frequently accessed data locally for low-latency access.
  - type: UseCases
    data:
      - name: Cloud Backup
        description: Back up on-premises data to AWS using existing backup workflows.
      - name: Disaster Recovery
        description: Store data in AWS for disaster recovery with low RTO.
      - name: Data Archiving
        description: Archive cold data to Amazon Glacier through virtual tape library.
      - name: Hybrid File Storage
        description: Share files between on-premises and cloud with NFS/SMB access.
  - type: Integrations
    data:
      - name: Amazon S3
        description: Store all gateway data in S3 with intelligent tiering.
      - name: Amazon Glacier
        description: Archive tape data to Glacier for long-term retention.
      - name: AWS Backup
        description: Centralized backup of Storage Gateway volumes and file shares.
      - name: Amazon CloudWatch
        description: Monitor gateway metrics and set alarms via CloudWatch.
      - name: AWS CloudTrail
        description: Audit all Storage Gateway API calls for compliance.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
tags:
  - AWS
  - Backup
  - File Storage
  - Gateway
  - Hybrid Cloud
  - Storage
x-type: company
---
