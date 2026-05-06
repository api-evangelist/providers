---
name: Amazon Detective
description: Amazon Detective is a security investigation service that makes it easy to analyze, investigate, and quickly identify the root cause of potential security issues or suspicious activities. It automatically collects log data from your AWS resources and uses machine learning, statistical analysis, and graph theory to build interactive visualizations that help you conduct faster and more efficient security investigations.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
url: https://aws.amazon.com/detective/
created: '2024-01-15'
modified: '2026-04-19'
apis:
  - name: Amazon Detective API
    description: The Amazon Detective API provides programmatic access to manage security investigation workflows. It enables developers to create and manage behavior graphs, invite and manage member accounts, start and manage investigations, list indicators of compromise, manage data source packages, and configure AWS Organizations integration for multi-account security management.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://aws.amazon.com/detective/
    baseURL: https://api.detective.amazonaws.com
    tags:
      - AWS
      - Forensics
      - Investigation
      - Security
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/detective/
      - type: OpenAPI
        url: openapi/amazon-detective-openapi.yml
      - type: Pricing
        url: https://aws.amazon.com/detective/pricing/
      - type: GettingStarted
        url: https://aws.amazon.com/detective/getting-started/
      - type: FAQ
        url: https://aws.amazon.com/detective/faqs/
      - type: JSONSchema
        url: json-schema/amazon-detective-graph-schema.json
      - type: JSONSchema
        url: json-schema/amazon-detective-member-detail-schema.json
      - type: JSONSchema
        url: json-schema/amazon-detective-investigation-detail-schema.json
      - type: JSONSchema
        url: json-schema/amazon-detective-indicator-schema.json
      - type: JSONSchema
        url: json-schema/amazon-detective-administrator-schema.json
      - type: JSONStructure
        url: json-structure/amazon-detective-graph-structure.json
      - type: JSONStructure
        url: json-structure/amazon-detective-member-detail-structure.json
      - type: JSONStructure
        url: json-structure/amazon-detective-investigation-detail-structure.json
      - type: JSON-LD
        url: json-ld/amazon-detective-context.jsonld
      - type: Example
        url: examples/amazon-detective-graph-example.json
      - type: Example
        url: examples/amazon-detective-member-detail-example.json
      - type: Example
        url: examples/amazon-detective-investigation-detail-example.json
common:
  - type: Portal
    url: https://aws.amazon.com/
  - type: Website
    url: https://aws.amazon.com/detective/
  - type: Documentation
    url: https://docs.aws.amazon.com/detective/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/detective/
  - type: SignUp
    url: https://signin.aws.amazon.com/signup?request_type=register
  - type: Login
    url: https://aws.amazon.com/console/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: Blog
    url: https://aws.amazon.com/blogs/security/tag/amazon-detective/
  - type: ReleaseNotes
    url: https://docs.aws.amazon.com/detective/latest/userguide/release-notes.html
  - type: SpectralRules
    url: rules/amazon-detective-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-detective-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/security-investigation.yaml
  - type: Features
    data:
      - name: Behavior Graph Analysis
        description: Automatically builds a behavior graph from log data using machine learning and graph theory to visualize security issues.
      - name: Security Investigations
        description: Start and manage structured investigations on IAM users and roles with scoped time ranges and severity scoring.
      - name: Indicators of Compromise
        description: Automatically identifies indicators including impossible travel, flagged IP addresses, new geolocations, new user agents, and TTP observations.
      - name: Multi-Account Support
        description: Aggregate security data from multiple AWS accounts using an administrator account and member account model.
      - name: AWS Organizations Integration
        description: Automatically enable new organization accounts as member accounts in the organization behavior graph.
      - name: Data Source Packages
        description: Ingest security telemetry from CloudTrail, VPC Flow Logs, GuardDuty findings, EKS audit logs, and Active Directory audit logs.
      - name: Interactive Visualizations
        description: Provides interactive graph visualizations in the AWS console to explore entity relationships and security events.
      - name: Investigation Severity Scoring
        description: Assigns severity levels (Informational, Low, Medium, High, Critical) based on likelihood and impact of compromise indicators.
  - type: UseCases
    data:
      - name: Security Incident Investigation
        description: Rapidly investigate security incidents by analyzing entity behavior, network activity, and API call patterns across your AWS environment.
      - name: Threat Hunting
        description: Proactively search for suspicious activity and potential threats using behavior analysis and machine learning across your AWS accounts.
      - name: Root Cause Analysis
        description: Identify the root cause of security issues by exploring the relationships between resources, users, and events in a behavior graph.
      - name: Compliance Forensics
        description: Collect and preserve forensic evidence for compliance investigations using structured investigations with defined scope and time ranges.
      - name: Multi-Account Security Operations
        description: Centrally manage security investigations across an AWS Organization from a single administrator account.
  - type: Integrations
    data:
      - name: Amazon GuardDuty
        description: Automatically ingests GuardDuty findings into the behavior graph for deeper investigation context.
      - name: AWS CloudTrail
        description: Ingests CloudTrail API call logs to track user and service activity across your AWS environment.
      - name: Amazon VPC Flow Logs
        description: Analyzes VPC flow logs to identify network communication patterns and anomalies.
      - name: Amazon EKS
        description: Optionally ingests EKS audit logs to monitor Kubernetes API server activity.
      - name: AWS Organizations
        description: Integrates with AWS Organizations to manage multi-account behavior graphs and auto-enable new accounts.
      - name: AWS Security Hub
        description: Surfaces Detective investigation context within Security Hub for consolidated security findings.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
tags:
  - AWS
  - Forensics
  - Investigation
  - Security
---
