---
aid: amazon-control-tower
name: Amazon Control Tower
description: AWS Control Tower provides the easiest way to set up and govern a secure, multi-account AWS environment based on best practices. It establishes a landing zone with pre-configured governance and guardrails, enabling organizations to maintain compliance and manage accounts at scale. With over 750 preconfigured controls, it automates account creation, OU registration, and compliance enforcement across the entire AWS organization.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Compliance
  - Governance
  - Landing Zone
  - Multi-Account
  - Security
  - Controls
url: https://raw.githubusercontent.com/api-evangelist/amazon-control-tower/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-control-tower:aws-control-tower-api
    name: AWS Control Tower API
    description: The AWS Control Tower API provides programmatic access to manage landing zones, organizational units, accounts, controls (guardrails), and baselines within your AWS environment, enabling automated governance at scale. Supports operations for landing zone lifecycle, control enablement/disablement, and OU baseline registration.
    humanURL: https://docs.aws.amazon.com/controltower/latest/APIReference/Welcome.html
    baseURL: https://controltower.amazonaws.com
    tags:
      - Governance
      - Landing Zone
      - Multi-Account
      - Controls
      - Baselines
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/controltower/latest/APIReference/Welcome.html
      - type: OpenAPI
        url: openapi/amazon-control-tower-openapi.yml
      - type: OpenAPI
        url: https://api.apis.guru/v2/specs/amazonaws.com/controltower/2018-11-28/openapi.yaml
      - type: GettingStarted
        url: https://aws.amazon.com/controltower/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/controltower/pricing/
      - type: FAQ
        url: https://aws.amazon.com/controltower/faqs/
      - type: APIReference
        url: https://docs.aws.amazon.com/controltower/latest/APIReference/API_Operations.html
      - type: Documentation
        url: https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html
      - type: JSONSchema
        url: json-schema/landing-zone-schema.json
      - type: JSONSchema
        url: json-schema/enabled-control-schema.json
      - type: JSONSchema
        url: json-schema/enabled-baseline-schema.json
      - type: JSONLD
        url: json-ld/amazon-control-tower-context.jsonld
common:
  - type: Portal
    url: https://aws.amazon.com/controltower/
  - type: DeveloperPortal
    url: https://aws.amazon.com/controltower/
  - type: Documentation
    url: https://docs.aws.amazon.com/controltower/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/mt/category/management-tools/aws-control-tower/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/controltower/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: Pricing
    url: https://aws.amazon.com/controltower/pricing/
  - type: SpectralRules
    url: rules/amazon-control-tower-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-control-tower-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/governance-operations.yaml
  - type: NaftikoCapability
    url: capabilities/shared/control-tower.yaml
  - type: Features
    data:
      - name: Landing Zone Management
        description: Create, configure, update, reset, and delete AWS Control Tower landing zones programmatically via API, automating multi-account environment setup.
      - name: Controls (Guardrails) Library
        description: Over 750 preconfigured controls (guardrails) covering security, operations, and compliance. Enable or disable controls on organizational units via API.
      - name: Baseline Registration
        description: Apply and manage baselines on organizational units (OUs) to register them with AWS Control Tower and enforce standard configurations programmatically.
      - name: Multi-Account Governance
        description: Automate creation of AWS accounts with built-in governance, policies, and security controls through integration with AWS Organizations.
      - name: Compliance Enforcement
        description: Deploy preventive, detective, and proactive controls to enforce compliance standards including CIS, NIST, PCI-DSS, HIPAA, and SOC 2.
      - name: Audit and Logging
        description: Centralized audit logging to Amazon S3 and AWS CloudTrail integration for full visibility into API calls and governance actions.
      - name: Third-Party Integrations
        description: Seamlessly integrate third-party security, compliance, and ITSM tools at scale to enhance your AWS multi-account environment.
  - type: UseCases
    data:
      - name: Multi-Account Environment Setup
        description: Quickly set up a secure, well-architected multi-account AWS environment with landing zone configuration completed in under 30 minutes.
      - name: Compliance Automation
        description: Deploy preconfigured controls to enforce regulatory compliance standards such as PCI-DSS, HIPAA, NIST, and SOC 2 across all accounts.
      - name: Account Vending
        description: Automate provisioning of new AWS accounts with built-in security policies, IAM roles, and governance configurations using Account Factory.
      - name: OU Governance
        description: Programmatically register organizational units with Control Tower baselines and apply targeted controls for department-specific governance.
      - name: Risk and Posture Management
        description: Continuously monitor compliance posture across all accounts and receive alerts when controls are violated or drift is detected.
  - type: Integrations
    data:
      - name: AWS Organizations
        description: Native integration with AWS Organizations for multi-account structure, OU management, and account creation within a Control Tower landing zone.
      - name: AWS Service Catalog
        description: Account Factory integration through AWS Service Catalog for self-service account provisioning with pre-approved configurations.
      - name: AWS CloudTrail
        description: All Control Tower API calls are logged to AWS CloudTrail for audit trails, security investigations, and compliance reporting.
      - name: AWS Config
        description: Detective controls are implemented using AWS Config rules to continuously evaluate resource compliance within managed accounts.
      - name: AWS Security Hub
        description: Integrate Control Tower findings with AWS Security Hub for centralized security posture management and cross-account visibility.
      - name: AWS CloudFormation
        description: Launch landing zones and enable controls using CloudFormation templates and resource providers for infrastructure-as-code governance.
      - name: Terraform
        description: Community-supported Terraform providers for managing Control Tower landing zones, controls, and account factory configurations.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
