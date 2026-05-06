---
aid: amazon-verified-permissions
name: Amazon Verified Permissions
description: Amazon Verified Permissions is a scalable, fine-grained permissions management and authorization service for the applications you build. Using Cedar, an expressive and analyzable open-source policy language, it helps developers build secure applications faster by externalizing authorization and centralizing policy management.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Authorization
  - AWS
  - Permissions
  - Security
url: https://raw.githubusercontent.com/api-evangelist/amazon-verified-permissions/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-verified-permissions:amazon-verified-permissions-api
    name: Amazon Verified Permissions API
    description: The Amazon Verified Permissions API provides programmatic access to manage policy stores, policies, policy templates, identity sources, and schemas. It enables fine-grained authorization using the Cedar policy language, supporting real-time authorization decisions for application resources.
    humanURL: https://aws.amazon.com/verified-permissions/
    baseURL: https://verifiedpermissions.amazonaws.com
    tags:
      - Authorization
      - AWS
      - Cedar
      - Permissions
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/
      - type: APIReference
        url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/
      - type: GettingStarted
        url: https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/getting-started.html
      - type: Pricing
        url: https://aws.amazon.com/verified-permissions/pricing/
      - type: FAQ
        url: https://aws.amazon.com/verified-permissions/faqs/
common:
  - type: Portal
    url: https://aws.amazon.com/
  - type: Website
    url: https://aws.amazon.com/verified-permissions/
  - type: Documentation
    url: https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/
  - type: Console
    url: https://console.aws.amazon.com/verifiedpermissions/
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
    url: https://raw.githubusercontent.com/api-evangelist/amazon-verified-permissions/refs/heads/main/rules/amazon-verified-permissions-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/amazon-verified-permissions/refs/heads/main/vocabulary/amazon-verified-permissions-vocabulary.yaml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/amazon-verified-permissions/refs/heads/main/capabilities/amazon-verified-permissions-capability.yaml
  - type: Features
    data:
      - name: Automation
        description: Automate operational tasks with Amazon Verified Permissions.
      - name: API Access
        description: Programmatic access to Amazon Verified Permissions resources.
  - type: UseCases
    data:
      - name: Cloud Operations
        description: Use Amazon Verified Permissions to manage and automate cloud operations.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
