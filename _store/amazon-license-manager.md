---
aid: amazon-license-manager
name: Amazon License Manager
description: AWS License Manager makes it easier to manage licenses in AWS and on-premises servers from software vendors such as Microsoft, SAP, Oracle, and IBM. It helps you control your licensing costs by letting you create rules that emulate the terms of your licensing agreements.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Compliance
  - Cost Management
  - License Management
  - Software Licensing
url: https://raw.githubusercontent.com/api-evangelist/amazon-license-manager/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-license-manager:aws-license-manager-api
    name: AWS License Manager API
    description: The AWS License Manager API provides programmatic access to create and manage license configurations, license associations, grants, tokens, and license reports for managing software licenses across AWS.
    humanURL: https://aws.amazon.com/license-manager/
    baseURL: https://license-manager.amazonaws.com
    tags:
      - Compliance
      - License Management
      - Software Licensing
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/license-manager/latest/APIReference/Welcome.html
      - type: OpenAPI
        url: https://api.apis.guru/v2/specs/amazonaws.com/license-manager/2018-08-01/openapi.yaml
      - type: GettingStarted
        url: https://aws.amazon.com/license-manager/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/license-manager/pricing/
      - type: FAQ
        url: https://aws.amazon.com/license-manager/faqs/
      - type: JSONSchema
        url: json-schema/amazon-license-manager-license-configuration-schema.json
      - type: JSONLD
        url: json-ld/amazon-license-manager-context.jsonld
common:
  - type: Portal
    url: https://aws.amazon.com/license-manager/
  - type: Portal
    url: https://aws.amazon.com/license-manager/
  - type: Documentation
    url: https://docs.aws.amazon.com/license-manager/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/mt/tag/aws-license-manager/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/license-manager/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: Status
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: Features
    data:
      - name: License Rule Enforcement
        description: Define licensing rules based on software attributes and enforce them during instance launches.
      - name: License Tracking
        description: Track license usage across AWS and on-premises environments from a central dashboard.
      - name: Cross-Account Discovery
        description: Discover software inventory across multiple AWS accounts in an AWS Organization.
      - name: Automated Compliance Reports
        description: Generate license compliance reports for auditors and software vendors.
      - name: Bring Your Own License (BYOL)
        description: Use existing on-premises software licenses on EC2 with BYOL programs.
  - type: UseCases
    data:
      - name: License Compliance
        description: Ensure software deployments comply with license agreements across your AWS estate.
      - name: Cost Optimization
        description: Track license usage to identify unused licenses and optimize software spend.
      - name: Vendor Audit Preparation
        description: Generate detailed license reports for software vendor audits.
  - type: Integrations
    data:
      - name: AWS Systems Manager
        description: Discover software inventory on EC2 instances using Systems Manager inventory.
      - name: AWS Organizations
        description: Manage licenses across all accounts in an AWS Organization from a single pane.
      - name: AWS Marketplace
        description: Access software licenses purchased through AWS Marketplace.
  - type: SpectralRules
    url: rules/amazon-license-manager-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/amazon-license-manager-workflow.yaml
  - type: Vocabulary
    url: vocabulary/amazon-license-manager-vocabulary.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
