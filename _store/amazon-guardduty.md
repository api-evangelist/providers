---
aid: amazon-guardduty
name: Amazon GuardDuty
description: Amazon GuardDuty is an intelligent threat detection service that continuously monitors your AWS accounts, workloads, and data for malicious activity. It uses machine learning, anomaly detection, and integrated threat intelligence to identify and prioritize potential threats to your AWS environment.
type: Index
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
url: https://raw.githubusercontent.com/api-evangelist/amazon-guardduty/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-19'
specificationVersion: '0.19'
tags:
  - Anomaly Detection
  - AWS
  - Compliance
  - Machine Learning
  - Monitoring
  - Security
  - Threat Detection
apis:
  - aid: amazon-guardduty:amazon-guardduty-api
    name: Amazon GuardDuty API
    description: The Amazon GuardDuty API provides programmatic access to manage detectors, findings, filters, trusted IP sets, and threat intelligence for continuous threat detection across AWS accounts and workloads.
    humanURL: https://aws.amazon.com/guardduty/
    baseURL: https://guardduty.amazonaws.com
    tags:
      - Security
      - Threat Detection
      - Machine Learning
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/guardduty/latest/APIReference/Welcome.html
      - type: OpenAPI
        url: openapi/amazon-guardduty-openapi.yml
      - type: GettingStarted
        url: https://aws.amazon.com/guardduty/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/guardduty/pricing/
      - type: FAQ
        url: https://aws.amazon.com/guardduty/faqs/
      - type: APIReference
        url: https://docs.aws.amazon.com/guardduty/latest/APIReference/Welcome.html
      - type: Authentication
        url: https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html
      - type: JSONSchema
        url: json-schema/guardduty-finding-schema.json
      - type: JSONLD
        url: json-ld/amazon-guardduty-context.jsonld
common:
  - type: Portal
    url: https://aws.amazon.com/guardduty/
  - type: Documentation
    url: https://docs.aws.amazon.com/guardduty/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/security/tag/amazon-guardduty/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/guardduty/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-guardduty-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-guardduty-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/amazon-guardduty-threat-detection.yaml
  - type: Features
    data:
      - name: Intelligent Threat Detection
        description: Uses ML and anomaly detection to identify threats without manual configuration or rule management.
      - name: Integrated Threat Intelligence
        description: Incorporates curated threat intelligence feeds from AWS, CrowdStrike, and Proofpoint for enhanced detection.
      - name: Multi-Account Support
        description: Monitor all accounts in an AWS Organization from a central administrator account.
      - name: Continuous Monitoring
        description: Analyzes CloudTrail, VPC Flow Logs, DNS logs, and S3 access logs 24/7 without performance impact.
      - name: Finding Prioritization
        description: Automatically prioritizes findings by severity (Low, Medium, High) for efficient response.
      - name: Malware Protection
        description: Scans EC2 instance volumes and S3 objects for malware and known threats.
  - type: UseCases
    data:
      - name: Account Compromise Detection
        description: Detect compromised AWS credentials and unauthorized API calls using ML-based anomaly detection.
      - name: Insider Threat Monitoring
        description: Identify suspicious behavior from privileged users or compromised internal accounts.
      - name: Cryptocurrency Mining Detection
        description: Detect and alert on unauthorized cryptocurrency mining using EC2 or Lambda resources.
      - name: Malware Detection
        description: Scan workloads and data for malware and ransomware threats.
      - name: Data Exfiltration Prevention
        description: Identify unusual data access patterns and potential exfiltration from S3 buckets.
  - type: Integrations
    data:
      - name: AWS Security Hub
        description: Automatically send GuardDuty findings to Security Hub for centralized security management.
      - name: Amazon EventBridge
        description: Trigger automated responses to findings using EventBridge rules and Lambda functions.
      - name: AWS Organizations
        description: Enable GuardDuty organization-wide for centralized multi-account threat monitoring.
      - name: Amazon Detective
        description: Investigate GuardDuty findings in depth using Detective for root cause analysis.
      - name: Amazon Macie
        description: Combine with Macie for comprehensive data security and threat detection.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
