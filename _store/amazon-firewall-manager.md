---
aid: amazon-firewall-manager
name: Amazon Firewall Manager
description: AWS Firewall Manager is a security management service that allows you to centrally configure and manage firewall rules across your accounts and applications in AWS Organizations. It makes it easier to bring new applications and resources into compliance with security policies.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Compliance
  - Firewall
  - Network Security
  - Security
url: https://raw.githubusercontent.com/api-evangelist/amazon-firewall-manager/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-firewall-manager:aws-firewall-manager-api
    name: AWS Firewall Manager API
    description: The AWS Firewall Manager API provides programmatic access to create and manage security policies, compliance status, and protection configurations for AWS WAF, Shield, and VPC security groups across your organization.
    humanURL: https://aws.amazon.com/firewall-manager/
    baseURL: https://fms.amazonaws.com
    tags:
      - Firewall Management
      - Network Security
      - Security
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/fms/latest/APIReference/Welcome.html
      - type: OpenAPI
        url: openapi/amazon-firewall-manager-openapi.yml
      - type: JSONSchema
        url: json-schema/amazon-firewall-manager-policy-schema.json
      - type: JSONSchema
        url: json-schema/amazon-firewall-manager-compliance-violator-schema.json
      - type: JSONSchema
        url: json-schema/amazon-firewall-manager-resource-set-schema.json
      - type: JSONSchema
        url: json-schema/amazon-firewall-manager-security-service-policy-data-schema.json
      - type: JSONSchema
        url: json-schema/amazon-firewall-manager-tag-schema.json
      - type: JSONStructure
        url: json-structure/amazon-firewall-manager-policy-structure.json
      - type: JSONStructure
        url: json-structure/amazon-firewall-manager-compliance-violator-structure.json
      - type: JSONStructure
        url: json-structure/amazon-firewall-manager-resource-set-structure.json
      - type: JSONStructure
        url: json-structure/amazon-firewall-manager-security-service-policy-data-structure.json
      - type: JSONStructure
        url: json-structure/amazon-firewall-manager-tag-structure.json
      - type: Example
        url: examples/amazon-firewall-manager-policy-example.json
      - type: Example
        url: examples/amazon-firewall-manager-compliance-violator-example.json
      - type: Example
        url: examples/amazon-firewall-manager-resource-set-example.json
      - type: Example
        url: examples/amazon-firewall-manager-security-service-policy-data-example.json
      - type: Example
        url: examples/amazon-firewall-manager-tag-example.json
      - type: GettingStarted
        url: https://aws.amazon.com/firewall-manager/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/firewall-manager/pricing/
      - type: FAQ
        url: https://aws.amazon.com/firewall-manager/faqs/
      - type: APIReference
        url: https://docs.aws.amazon.com/fms/latest/APIReference/Welcome.html
common:
  - type: Portal
    url: https://aws.amazon.com/firewall-manager/
  - type: Website
    url: https://aws.amazon.com/firewall-manager/
  - type: Documentation
    url: https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/security/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/wafv2/fmsv2/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: YouTube
    url: https://www.youtube.com/user/AmazonWebServices
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/aws-firewall-manager
  - type: SpectralRules
    url: rules/amazon-firewall-manager-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/shared/firewall-manager.yaml
  - type: NaftikoCapability
    url: capabilities/amazon-firewall-manager-security-governance.yaml
  - type: Vocabulary
    url: vocabulary/amazon-firewall-manager-vocabulary.yaml
  - type: JSON-LD
    url: json-ld/amazon-firewall-manager-context.jsonld
  - type: Features
    data:
      - name: Centralized Policy Management
        description: Define and enforce WAF, Shield Advanced, Network Firewall, and security group policies from a single pane of glass across all AWS accounts.
      - name: Automatic Remediation
        description: Automatically remediate non-compliant resources so that new accounts and resources are always protected.
      - name: Multi-Account Support
        description: Manage security policies across hundreds of AWS accounts within an AWS Organization.
      - name: Compliance Visibility
        description: View policy compliance status per account and resource with detailed violation reports.
      - name: Resource Sets
        description: Group AWS resources by type for targeted policy application and management.
      - name: Tag-Based Targeting
        description: Apply policies to resources based on AWS resource tags for fine-grained scope control.
      - name: Third-Party Firewall Support
        description: Deploy and manage third-party firewall appliances through AWS Marketplace with Firewall Manager.
  - type: UseCases
    data:
      - name: WAF Rule Standardization
        description: Enforce standard WAF rule sets across all CloudFront distributions and ALBs organization-wide.
      - name: DDoS Protection Baseline
        description: Mandate Shield Advanced protection for all internet-facing resources across accounts.
      - name: Security Group Governance
        description: Audit and remediate overly permissive security group rules across EC2 and VPC resources.
      - name: Network Firewall Deployment
        description: Deploy and manage AWS Network Firewall across VPCs in multiple accounts from a central policy.
      - name: Compliance Reporting
        description: Monitor and report on firewall policy compliance for SOC 2, PCI DSS, and regulatory requirements.
      - name: New Account Onboarding
        description: Automatically apply security policies to new AWS accounts as they join the organization.
  - type: Integrations
    data:
      - name: AWS Organizations
        description: Manage Firewall Manager policies across all accounts in the organization hierarchy.
      - name: AWS WAF
        description: Centrally create and deploy WAF rule groups and web ACLs across accounts.
      - name: AWS Shield Advanced
        description: Enable and manage Shield Advanced protection for all DDoS-sensitive resources.
      - name: AWS Network Firewall
        description: Deploy centrally managed network firewall policies across VPCs.
      - name: Amazon Route 53 Resolver
        description: Manage DNS Firewall rule groups for Route 53 Resolver across accounts.
      - name: Amazon CloudWatch
        description: Monitor compliance metrics and set alarms for non-compliant resources.
      - name: AWS Security Hub
        description: Send Firewall Manager compliance findings to Security Hub for centralized security posture management.
      - name: AWS IAM
        description: Control who can create, modify, and view Firewall Manager policies using IAM permissions.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
