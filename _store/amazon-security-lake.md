---
name: Amazon Security Lake
description: Amazon Security Lake is a service that automatically centralizes an organization's security data from cloud, on-premises, and custom sources into a purpose-built data lake stored in your own Amazon S3. It manages the data lifecycle to help you optimize storage and supports OCSF (Open Cybersecurity Schema Framework) for normalized security data analysis.
url: https://aws.amazon.com/security-lake/
baseURL: https://securitylake.amazonaws.com
x-type: company
created: '2026-03-16'
modified: '2026-04-19'
tags:
  - AWS
  - Data Lake
  - Security
  - SIEM
  - Threat Detection
apis:
  - name: Amazon Security Lake API
    description: The Amazon Security Lake API provides programmatic access to create and manage data lakes, data sources, subscribers, and log sources for centralizing and analyzing security data across your organization using the OCSF (Open Cybersecurity Schema Framework).
    humanURL: https://docs.aws.amazon.com/security-lake/latest/APIReference/Welcome.html
    baseURL: https://securitylake.{region}.amazonaws.com
    tags:
      - Data Lake
      - Security
      - Threat Detection
      - OCSF
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/security-lake/latest/APIReference/Welcome.html
      - type: OpenAPI
        url: openapi/amazon-security-lake-openapi.yml
      - type: JSONSchema
        url: json-schema/amazon-security-lake-data-lake-schema.json
      - type: JSONSchema
        url: json-schema/amazon-security-lake-log-source-schema.json
      - type: JSONSchema
        url: json-schema/amazon-security-lake-subscriber-schema.json
common:
  - type: Portal
    url: https://aws.amazon.com/security-lake/
  - type: GettingStarted
    url: https://aws.amazon.com/security-lake/getting-started/
  - type: Documentation
    url: https://docs.aws.amazon.com/security-lake/
  - type: APIReference
    url: https://docs.aws.amazon.com/security-lake/latest/APIReference/
  - type: Console
    url: https://console.aws.amazon.com/securitylake/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Pricing
    url: https://aws.amazon.com/security-lake/pricing/
  - type: FAQ
    url: https://aws.amazon.com/security-lake/faqs/
  - type: Blog
    url: https://aws.amazon.com/blogs/security/tag/amazon-security-lake/
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
    url: https://stackoverflow.com/questions/tagged/amazon-security-lake
  - type: KnowledgeCenter
    url: https://repost.aws/knowledge-center
  - type: SpectralRules
    url: rules/amazon-security-lake-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-security-lake-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/security-data-lake.yaml
  - type: Features
    data:
      - name: Automatic Data Centralization
        description: Automatically centralizes security data from AWS services, third-party tools, and custom sources into a single data lake.
      - name: OCSF Normalization
        description: Converts security data to the Open Cybersecurity Schema Framework (OCSF) for standardized analysis across tools.
      - name: Apache Parquet Format
        description: Stores all security data in Apache Parquet format optimized for analytical query performance.
      - name: Multi-Account Support
        description: Centralizes security data across an entire AWS Organization from all accounts and regions.
      - name: Lifecycle Management
        description: Automatically manages storage lifecycle with configurable retention and tiering policies.
      - name: Subscriber Access
        description: Grant third-party SIEMs and analytics tools direct query access to your security data lake.
      - name: Native AWS Integration
        description: Native connectors for CloudTrail, VPC Flow Logs, Route 53, Security Hub, and EKS audit logs.
      - name: Custom Log Sources
        description: Ingest custom and third-party security data sources in OCSF format.
  - type: UseCases
    data:
      - name: Security Data Centralization
        description: Aggregate all security data from across a multi-account AWS environment into one queryable data lake.
      - name: SIEM Integration
        description: Provide SIEM platforms like Splunk, Sumo Logic, and Microsoft Sentinel direct access to normalized security data.
      - name: Threat Hunting
        description: Enable security analysts to query normalized OCSF data for threat hunting and forensic investigation.
      - name: Compliance Data Retention
        description: Retain security logs in a cost-optimized data lake for compliance audit requirements.
      - name: Security Analytics
        description: Run advanced analytics and ML models against normalized security data for anomaly detection.
      - name: Multi-Cloud Security Data
        description: Centralize security data from on-premises and other cloud providers alongside AWS security data.
  - type: Integrations
    data:
      - name: AWS CloudTrail
        description: Native connector for management event and data event logs from CloudTrail.
      - name: Amazon VPC Flow Logs
        description: Ingest VPC network flow logs for network traffic analysis.
      - name: Amazon Route 53
        description: Collect DNS query logs for domain analysis and threat detection.
      - name: AWS Security Hub
        description: Aggregate Security Hub findings into the security data lake.
      - name: Amazon EKS
        description: Ingest Kubernetes audit logs from Amazon EKS clusters.
      - name: Amazon S3
        description: All security data is stored in S3 buckets within your own AWS account.
      - name: AWS Lake Formation
        description: Control fine-grained subscriber access using AWS Lake Formation permissions.
      - name: Splunk
        description: SIEM subscriber integration for Splunk to query Security Lake data directly.
      - name: Microsoft Sentinel
        description: Connect Microsoft Sentinel as a subscriber to consume OCSF-normalized data.
      - name: CrowdStrike
        description: Ingest CrowdStrike endpoint detection findings as a custom log source.
  - type: JSON-LD
    url: json-ld/amazon-security-lake-context.jsonld
  - type: JSONStructure
    url: json-structure/amazon-security-lake-data-lake-structure.json
  - type: JSONStructure
    url: json-structure/amazon-security-lake-log-source-structure.json
  - type: JSONStructure
    url: json-structure/amazon-security-lake-subscriber-structure.json
  - type: Example
    url: examples/amazon-security-lake-data-lake-example.json
  - type: Example
    url: examples/amazon-security-lake-log-source-example.json
  - type: Example
    url: examples/amazon-security-lake-subscriber-example.json
  - type: NaftikoCapability
    url: capabilities/shared/amazon-security-lake.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
