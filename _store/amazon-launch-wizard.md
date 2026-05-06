---
aid: amazon-launch-wizard
name: Amazon Launch Wizard
description: AWS Launch Wizard is a service that guides you through the sizing, configuration, and deployment of enterprise applications on AWS, such as Microsoft SQL Server Always On and HANA-based SAP systems, without the need to manually identify and provision individual AWS resources.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Deployment
  - Enterprise Applications
  - SAP
  - SQL Server
url: https://raw.githubusercontent.com/api-evangelist/amazon-launch-wizard/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-launch-wizard:aws-launch-wizard-api
    name: AWS Launch Wizard API
    description: The AWS Launch Wizard API provides programmatic access to manage deployments, workload specs, and deployment events for guided enterprise application deployments on AWS.
    humanURL: https://aws.amazon.com/launchwizard/
    baseURL: https://launchwizard.amazonaws.com
    tags:
      - Automation
      - Deployment
      - Enterprise Applications
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/launchwizard/latest/APIReference/Welcome.html
      - type: OpenAPI
        url: https://api.apis.guru/v2/specs/amazonaws.com/launchwizard/2018-05-10/openapi.yaml
      - type: GettingStarted
        url: https://aws.amazon.com/launchwizard/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/launchwizard/pricing/
      - type: FAQ
        url: https://aws.amazon.com/launchwizard/faqs/
      - type: JSONSchema
        url: json-schema/amazon-launch-wizard-deployment-schema.json
      - type: JSONLD
        url: json-ld/amazon-launch-wizard-context.jsonld
common:
  - type: Portal
    url: https://aws.amazon.com/launchwizard/
  - type: Portal
    url: https://aws.amazon.com/launchwizard/
  - type: Documentation
    url: https://docs.aws.amazon.com/launchwizard/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/apn/tag/aws-launch-wizard/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/launchwizard/
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
      - name: Guided Deployment
        description: Step-by-step guidance to size, configure, and deploy enterprise applications on AWS.
      - name: SAP Support
        description: Deploy SAP HANA and SAP NetWeaver on AWS with automated infrastructure sizing and setup.
      - name: SQL Server Support
        description: Deploy Microsoft SQL Server on AWS with Always On availability groups and best practices.
      - name: Active Directory Support
        description: Deploy Microsoft Active Directory on AWS with recommended configurations.
      - name: Cost Estimation
        description: Estimate the cost of your deployment before provisioning resources.
  - type: UseCases
    data:
      - name: SAP Migration
        description: Migrate SAP workloads to AWS with guided deployment and AWS best practices.
      - name: SQL Server HA
        description: Deploy highly available SQL Server with Always On availability groups.
      - name: Active Directory Setup
        description: Deploy and configure Active Directory on AWS for enterprise identity management.
  - type: Integrations
    data:
      - name: AWS CloudFormation
        description: Launch Wizard generates CloudFormation templates for repeatable infrastructure deployments.
      - name: Amazon EC2
        description: Provisions and configures EC2 instances with recommended sizes for enterprise workloads.
      - name: Amazon EBS
        description: Attaches appropriately sized EBS volumes optimized for enterprise application performance.
      - name: AWS Systems Manager
        description: Uses Systems Manager for configuration management and post-deployment tasks.
  - type: SpectralRules
    url: rules/amazon-launch-wizard-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/amazon-launch-wizard-workflow.yaml
  - type: Vocabulary
    url: vocabulary/amazon-launch-wizard-vocabulary.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
