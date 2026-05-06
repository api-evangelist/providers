---
aid: amazon-inspector
name: Amazon Inspector
description: Amazon Inspector is an automated vulnerability management service that continually scans AWS workloads for software vulnerabilities and unintended network exposure, providing detailed findings and prioritized remediation guidance.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Compliance
  - Container Security
  - EC2
  - Lambda
  - Security
  - Vulnerability Scanning
url: https://raw.githubusercontent.com/api-evangelist/amazon-inspector/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-inspector:aws-inspector-api
    name: AWS Amazon Inspector API
    description: The Amazon Inspector API provides programmatic access to vulnerability management for scanning EC2 instances, container images, and Lambda functions for software vulnerabilities and network exposure.
    humanURL: https://aws.amazon.com/inspector/
    baseURL: https://inspector2.amazonaws.com
    tags:
      - Compliance
      - Security
      - Vulnerability Scanning
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html
      - type: OpenAPI
        url: openapi/amazon-inspector-openapi-original.yml
      - type: GettingStarted
        url: https://aws.amazon.com/inspector/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/inspector/pricing/
      - type: FAQ
        url: https://aws.amazon.com/inspector/faqs/
common:
  - type: Portal
    url: https://aws.amazon.com/inspector/
  - type: Website
    url: https://aws.amazon.com/inspector/
  - type: Documentation
    url: https://docs.aws.amazon.com/inspector/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/security/category/security-identity-compliance/amazon-inspector/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/inspector/v2/home
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-inspector-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/shared/inspector.yaml
  - type: NaftikoCapability
    url: capabilities/security-vulnerability-management.yaml
  - type: Vocabulary
    url: vocabulary/amazon-inspector-vocabulary.yaml
  - type: JSONLD
    url: json-ld/amazon-inspector-context.jsonld
  - type: Features
    data:
      - name: Automated Vulnerability Scanning
        description: Continuously scans EC2, container images, and Lambda functions for software vulnerabilities.
      - name: Risk Scoring
        description: Ranks vulnerabilities by exploitability and impact to prioritize remediation.
      - name: SBOM Export
        description: Generates software bill of materials for scanned workloads.
      - name: Multi-Account Support
        description: Manages vulnerability scanning across all accounts in an AWS Organization.
  - type: UseCases
    data:
      - name: CI/CD Security Scanning
        description: Automatically scan container images in ECR during build pipelines.
      - name: Compliance Reporting
        description: Generate vulnerability reports for SOC 2, PCI DSS compliance.
      - name: Patch Prioritization
        description: Prioritize OS patches based on exploitability scores.
  - type: Integrations
    data:
      - name: Amazon ECR
        description: Automatically scans container images stored in Elastic Container Registry.
      - name: AWS Security Hub
        description: Sends all findings to Security Hub for centralized visibility.
      - name: AWS Organizations
        description: Manages Inspector across all organizational accounts.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
