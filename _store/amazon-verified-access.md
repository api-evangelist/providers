---
aid: amazon-verified-access
name: Amazon Verified Access
description: AWS Verified Access provides secure access to corporate applications without requiring a VPN. It evaluates each application request in real time using security signals like identity, device posture, and contextual data to grant granular access only to users who meet the specified requirements.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Access Management
  - AWS
  - Security
  - Zero Trust
url: https://raw.githubusercontent.com/api-evangelist/amazon-verified-access/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-verified-access:amazon-verified-access-api
    name: AWS Verified Access API
    description: The AWS Verified Access API provides programmatic access to create and manage Verified Access instances, groups, endpoints, and trust providers. It enables configuring zero-trust network access policies that evaluate user identity and device security posture for each application request.
    humanURL: https://aws.amazon.com/verified-access/
    baseURL: https://ec2.amazonaws.com
    tags:
      - Access Management
      - AWS
      - Security
      - Zero Trust
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/verified-access/latest/ug/
      - type: APIReference
        url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/OperationList-query-verified-access.html
      - type: GettingStarted
        url: https://docs.aws.amazon.com/verified-access/latest/ug/getting-started.html
      - type: Pricing
        url: https://aws.amazon.com/verified-access/pricing/
      - type: FAQ
        url: https://aws.amazon.com/verified-access/faqs/
common:
  - type: Portal
    url: https://aws.amazon.com/
  - type: Website
    url: https://aws.amazon.com/verified-access/
  - type: Documentation
    url: https://docs.aws.amazon.com/verified-access/latest/ug/
  - type: Console
    url: https://console.aws.amazon.com/verified-access/
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
    url: https://raw.githubusercontent.com/api-evangelist/amazon-verified-access/refs/heads/main/rules/amazon-verified-access-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/amazon-verified-access/refs/heads/main/vocabulary/amazon-verified-access-vocabulary.yaml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/amazon-verified-access/refs/heads/main/capabilities/amazon-verified-access-capability.yaml
  - type: Features
    data:
      - name: Automation
        description: Automate operational tasks with Amazon Verified Access.
      - name: API Access
        description: Programmatic access to Amazon Verified Access resources.
  - type: UseCases
    data:
      - name: Cloud Operations
        description: Use Amazon Verified Access to manage and automate cloud operations.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
