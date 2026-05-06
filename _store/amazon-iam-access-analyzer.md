---
aid: amazon-iam-access-analyzer
name: Amazon IAM Access Analyzer
description: AWS IAM Access Analyzer helps you set, verify, and refine your IAM policies by providing a suite of capabilities including findings for external, internal, and unused access, basic and custom policy checks for validating policies, and policy generation to generate fine-grained policies. It uses automated reasoning to identify resources shared with external entities and helps implement least privilege access across your AWS environment.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Access Control
  - AWS
  - Compliance
  - IAM
  - Policy Management
  - Security
url: https://raw.githubusercontent.com/api-evangelist/amazon-iam-access-analyzer/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-iam-access-analyzer:aws-access-analyzer-api
    name: AWS IAM Access Analyzer API
    description: The AWS IAM Access Analyzer API provides programmatic access to create and manage analyzers, findings, archive rules, and policy validations to identify and remediate unintended resource access across AWS accounts and organizations.
    humanURL: https://aws.amazon.com/iam/features/analyze-access/
    baseURL: https://access-analyzer.amazonaws.com
    tags:
      - Access Control
      - IAM
      - Policy Management
      - Security
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/Welcome.html
      - type: OpenAPI
        url: openapi/amazon-iam-access-analyzer-openapi-original.yml
      - type: GettingStarted
        url: https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html
      - type: Pricing
        url: https://aws.amazon.com/iam/pricing/
      - type: FAQ
        url: https://aws.amazon.com/iam/faqs/
      - type: JSONSchema
        url: json-schema/iam-access-analyzer-analyzer-schema.json
      - type: JSONStructure
        url: json-structure/iam-access-analyzer-analyzer-structure.json
      - type: Example
        url: examples/iam-access-analyzer-analyzer-example.json
common:
  - type: Portal
    url: https://aws.amazon.com/iam/features/analyze-access/
  - type: Website
    url: https://aws.amazon.com/iam/
  - type: Documentation
    url: https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/security/tag/iam-access-analyzer/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/access-analyzer/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-iam-access-analyzer-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/shared/iam-access-analyzer.yaml
  - type: NaftikoCapability
    url: capabilities/access-security-management.yaml
  - type: Vocabulary
    url: vocabulary/amazon-iam-access-analyzer-vocabulary.yaml
  - type: JSONLD
    url: json-ld/amazon-iam-access-analyzer-context.jsonld
  - type: Features
    data:
      - name: External Access Analysis
        description: Identifies resources shared with external entities outside your AWS organization using automated reasoning.
      - name: Internal Access Analysis
        description: Identifies which principals within your organization have access to selected resources.
      - name: Unused Access Analysis
        description: Identifies unused IAM roles, access keys, console passwords, and unused service permissions.
      - name: Policy Validation
        description: Validates IAM policies against best practices and custom security standards before deployment.
      - name: Policy Generation
        description: Generates fine-grained IAM policies based on actual access activity logged in AWS CloudTrail.
      - name: Access Preview
        description: Preview public and cross-account access to resources before deploying permission changes.
      - name: Archive Rules
        description: Automatically archive findings that match specified criteria to reduce noise.
  - type: UseCases
    data:
      - name: Least Privilege Enforcement
        description: Analyze actual API activity to generate minimal permission policies that implement least privilege access.
      - name: Security Compliance Auditing
        description: Continuously monitor for unintended external access to sensitive resources like S3 buckets and IAM roles.
      - name: CI/CD Policy Validation
        description: Integrate policy checks into deployment pipelines to catch overpermissive policies before they reach production.
      - name: Access Governance
        description: Identify and remediate unused access across IAM users, roles, and service accounts organization-wide.
      - name: Cross-Account Access Review
        description: Identify all resources shared across AWS accounts and validate the intent of each cross-account permission.
  - type: Integrations
    data:
      - name: AWS CloudTrail
        description: Uses CloudTrail activity logs to generate least-privilege IAM policies based on actual usage.
      - name: AWS Security Hub
        description: Publishes Access Analyzer findings to Security Hub for centralized security monitoring.
      - name: AWS Organizations
        description: Analyzes access across all accounts in an AWS Organization for comprehensive governance.
      - name: AWS Config
        description: Triggers re-scanning of resources when configuration changes are detected.
      - name: Amazon EventBridge
        description: Publishes finding events to EventBridge for automated security workflow responses.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
