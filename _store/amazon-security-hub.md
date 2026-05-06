---
name: Amazon Security Hub
description: AWS Security Hub is a cloud security posture management service that provides a comprehensive view of your security state across AWS accounts. It aggregates, organizes, and prioritizes security findings from multiple AWS services and third-party tools, enabling centralized security monitoring, compliance checking, and automated remediation workflows.
url: https://aws.amazon.com/security-hub/
baseURL: https://securityhub.amazonaws.com
x-type: company
created: '2024-01-15'
modified: '2026-04-19'
tags:
  - AWS
  - Compliance
  - Monitoring
  - Security
apis:
  - name: AWS Security Hub API
    description: The AWS Security Hub API provides programmatic access to manage centralized security findings across your AWS environment. It enables developers to import and manage security findings, configure security standards and controls, manage integrations with other AWS services and third-party tools, and automate security workflows.
    humanURL: https://docs.aws.amazon.com/securityhub/latest/APIReference/
    baseURL: https://securityhub.{region}.amazonaws.com
    tags:
      - AWS
      - Compliance
      - Monitoring
      - Security
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/securityhub/latest/APIReference/
      - type: OpenAPI
        url: openapi/amazon-security-hub-openapi.yml
      - type: JSONSchema
        url: json-schema/amazon-security-hub-finding-schema.json
common:
  - type: Portal
    url: https://aws.amazon.com/
  - type: GettingStarted
    url: https://aws.amazon.com/security-hub/getting-started/
  - type: Documentation
    url: https://docs.aws.amazon.com/securityhub/
  - type: APIReference
    url: https://docs.aws.amazon.com/securityhub/latest/APIReference/
  - type: Console
    url: https://console.aws.amazon.com/securityhub/
  - type: SignUp
    url: https://signin.aws.amazon.com/signup?request_type=register
  - type: Pricing
    url: https://aws.amazon.com/security-hub/pricing/
  - type: FAQ
    url: https://aws.amazon.com/security-hub/faqs/
  - type: Blog
    url: https://aws.amazon.com/blogs/security/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Compliance
    url: https://aws.amazon.com/compliance/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: YouTube
    url: https://www.youtube.com/user/AmazonWebServices
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/aws-security-hub
  - type: KnowledgeCenter
    url: https://repost.aws/knowledge-center
  - type: SpectralRules
    url: rules/amazon-security-hub-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-security-hub-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/cloud-security-posture.yaml
  - type: Features
    data:
      - name: Multi-Account Findings Aggregation
        description: Aggregate security findings from across multiple AWS accounts and regions into a single pane of glass.
      - name: AWS Security Finding Format (ASFF)
        description: Standardized JSON format for all security findings enabling consistent analysis and automation.
      - name: Built-in Compliance Standards
        description: Automated compliance checks against CIS AWS Foundations, PCI DSS, NIST, SOC 2, and AWS Foundational Security Best Practices.
      - name: Third-Party Integrations
        description: Ingest findings from 80+ third-party security partners including CrowdStrike, Palo Alto Networks, and Splunk.
      - name: Automated Remediation
        description: Trigger automated remediation via Amazon EventBridge and AWS Security Hub automated response and remediation.
      - name: Security Insights
        description: Correlated views of security findings to highlight areas needing attention.
      - name: Custom Actions
        description: Create custom actions to send findings to ticketing, chat, and SOAR platforms.
      - name: Cross-Region Aggregation
        description: Aggregate findings across multiple AWS regions into a designated aggregation region.
  - type: UseCases
    data:
      - name: Cloud Security Posture Management
        description: Continuously monitor your AWS environment for security misconfigurations and compliance gaps.
      - name: Compliance Reporting
        description: Automate compliance checks and generate reports for CIS, PCI DSS, NIST, and other frameworks.
      - name: Multi-Account Security Operations
        description: Centralize security monitoring across dozens or hundreds of AWS accounts in an organization.
      - name: Threat Detection Aggregation
        description: Aggregate findings from GuardDuty, Inspector, Macie, and third-party tools in one place.
      - name: Automated Incident Response
        description: Trigger automated remediation workflows when critical findings are detected.
      - name: Security Tool Consolidation
        description: Replace multiple point solutions with centralized finding aggregation and normalized data.
  - type: Integrations
    data:
      - name: Amazon GuardDuty
        description: Native integration to ingest GuardDuty threat detection findings.
      - name: Amazon Inspector
        description: Aggregate Inspector vulnerability assessment findings.
      - name: Amazon Macie
        description: Ingest Macie sensitive data discovery findings.
      - name: AWS Config
        description: Integration with Config rules for configuration compliance findings.
      - name: Amazon EventBridge
        description: Trigger automated remediation and notification workflows based on findings.
      - name: AWS Lambda
        description: Execute custom remediation actions in response to security findings.
      - name: AWS Organizations
        description: Enable Security Hub across all accounts in an AWS Organization.
      - name: CrowdStrike
        description: Third-party integration for endpoint detection and response findings.
      - name: Splunk
        description: Export Security Hub findings to Splunk SIEM for advanced analysis.
      - name: Palo Alto Networks
        description: Ingest Prisma Cloud and other Palo Alto findings via Security Hub integration.
  - type: JSON-LD
    url: json-ld/amazon-security-hub-context.jsonld
  - type: JSONStructure
    url: json-structure/amazon-security-hub-finding-structure.json
  - type: Example
    url: examples/amazon-security-hub-finding-example.json
  - type: NaftikoCapability
    url: capabilities/shared/amazon-security-hub.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
