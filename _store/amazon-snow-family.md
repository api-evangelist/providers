---
aid: amazon-snow-family
name: Amazon Snow Family
description: AWS Snow Family is a collection of physical devices and capacity points that help customers with data transfers in and out of AWS when network capacity is limited or unavailable. It includes Snowcone, Snowball, and Snowmobile devices for edge computing and offline data migration.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Data Migration
  - Edge Computing
  - Offline Transfer
  - Physical Appliance
url: https://raw.githubusercontent.com/api-evangelist/amazon-snow-family/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-snow-family:aws-snow-device-management-api
    name: AWS Snow Device Management API
    description: The AWS Snow Device Management API provides programmatic access to manage Snow device jobs, tasks, device resources, and network configurations for edge computing and data transfer operations.
    humanURL: https://aws.amazon.com/snow/
    baseURL: https://snow-device-management.amazonaws.com
    tags:
      - Data Migration
      - Edge Computing
      - Physical Appliance
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/snowball/latest/developer-guide/api-reference.html
      - type: OpenAPI
        url: openapi/amazon-snow-family.yaml
      - type: GettingStarted
        url: https://aws.amazon.com/snowball/
      - type: Pricing
        url: https://aws.amazon.com/snowball/pricing/
      - type: FAQ
        url: https://aws.amazon.com/snowball/faqs/
common:
  - type: Portal
    url: https://aws.amazon.com/snowball/
  - type: Documentation
    url: https://docs.aws.amazon.com/snowball/latest/developer-guide/api-reference.html
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
    url: https://console.aws.amazon.com/snowball/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-snow-family-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-snow-family-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/shared/amazon-snow-family.yaml
  - type: Features
    data:
      - name: Petabyte-scale Data Transfer
        description: Transfer large datasets to AWS using physical devices.
      - name: Edge Computing
        description: Run compute workloads at the edge with Snowball Edge and Snowcone.
      - name: Cluster Mode
        description: Use multiple Snow Family devices as a cluster for more storage and compute.
      - name: Encryption
        description: All data is automatically encrypted with 256-bit encryption.
  - type: UseCases
    data:
      - name: Large Data Migration
        description: Migrate terabytes to petabytes of data to AWS.
      - name: Disconnected Edge Computing
        description: Run AWS compute in environments with no internet connectivity.
      - name: Disaster Recovery
        description: Collect and transfer disaster recovery data to AWS.
  - type: Integrations
    data:
      - name: Amazon S3
        description: Transfer data directly to S3 buckets using Snow devices.
      - name: AWS IoT Greengrass
        description: Run IoT Greengrass on Snowball Edge for edge IoT workloads.
      - name: Amazon EC2
        description: Run EC2 compute instances on Snowball Edge devices.
      - name: AWS DataSync
        description: Use DataSync with Snow Family for accelerated data transfer.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
x-type: company
---
