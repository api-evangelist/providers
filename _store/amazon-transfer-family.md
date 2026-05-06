---
aid: amazon-transfer-family
name: Amazon Transfer Family
description: AWS Transfer Family is a secure transfer service that enables you to transfer files into and out of AWS storage services. It supports SFTP, FTPS, and FTP protocols, providing a fully managed file transfer service with native integration to Amazon S3 and Amazon EFS.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - File Transfer
  - FTP
  - SFTP
url: https://raw.githubusercontent.com/api-evangelist/amazon-transfer-family/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-transfer-family:amazon-transfer-family-api
    name: AWS Transfer Family API
    description: The AWS Transfer Family API provides programmatic access to create and manage SFTP, FTPS, and FTP file transfer servers. It enables managing users, SSH public keys, roles, and server configurations for secure file transfer workflows integrated with Amazon S3 and EFS.
    humanURL: https://aws.amazon.com/aws-transfer-family/
    baseURL: https://transfer.amazonaws.com
    tags:
      - AWS
      - File Transfer
      - SFTP
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/transfer/latest/userguide/
      - type: APIReference
        url: https://docs.aws.amazon.com/transfer/latest/userguide/API_Operations.html
      - type: GettingStarted
        url: https://docs.aws.amazon.com/transfer/latest/userguide/getting-started.html
      - type: Pricing
        url: https://aws.amazon.com/aws-transfer-family/pricing/
      - type: FAQ
        url: https://aws.amazon.com/aws-transfer-family/faqs/
common:
  - type: Portal
    url: https://aws.amazon.com/
  - type: Website
    url: https://aws.amazon.com/aws-transfer-family/
  - type: Documentation
    url: https://docs.aws.amazon.com/transfer/latest/userguide/
  - type: Console
    url: https://console.aws.amazon.com/transfer/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: SignUp
    url: https://signin.aws.amazon.com/signup?request_type=register
  - type: Login
    url: https://aws.amazon.com/console/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/amazon-transfer-family/refs/heads/main/rules/amazon-transfer-family-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/amazon-transfer-family/refs/heads/main/vocabulary/amazon-transfer-family-vocabulary.yaml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/amazon-transfer-family/refs/heads/main/capabilities/amazon-transfer-family-capability.yaml
  - type: Features
    data:
      - name: Automation
        description: Automate operational tasks with Amazon Transfer Family.
      - name: API Access
        description: Programmatic access to Amazon Transfer Family resources.
  - type: UseCases
    data:
      - name: Cloud Operations
        description: Use Amazon Transfer Family to manage and automate cloud operations.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
