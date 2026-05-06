---
aid: amazon-mainframe-modernization
name: Amazon Mainframe Modernization
description: AWS Mainframe Modernization provides tools and resources to help you plan and implement migration and modernization of your mainframe applications to AWS. It supports automated refactoring and replatforming of COBOL applications to run natively on AWS with managed runtime environments, deployment pipelines, and batch job execution capabilities.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - COBOL
  - Mainframe
  - Migration
  - Modernization
  - Batch Processing
url: https://raw.githubusercontent.com/api-evangelist/amazon-mainframe-modernization/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-mainframe-modernization:aws-mainframe-modernization-api
    name: AWS Mainframe Modernization API
    description: The AWS Mainframe Modernization API provides programmatic access to create and manage applications, environments, deployments, and batch job executions for mainframe application modernization on AWS. Covers 25 paths and 33 operations for the full modernization lifecycle.
    humanURL: https://aws.amazon.com/mainframe-modernization/
    baseURL: https://m2.amazonaws.com
    tags:
      - Mainframe
      - Migration
      - Modernization
      - COBOL
      - Batch Processing
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/m2/latest/APIReference/Welcome.html
      - type: OpenAPI
        url: openapi/amazon-mainframe-modernization-openapi-original.yaml
      - type: GettingStarted
        url: https://aws.amazon.com/mainframe-modernization/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/mainframe-modernization/pricing/
      - type: FAQ
        url: https://aws.amazon.com/mainframe-modernization/faqs/
      - type: JSONSchema
        url: json-schema/amazon-mainframe-modernization-application-summary-schema.json
      - type: JSONStructure
        url: json-structure/amazon-mainframe-modernization-application-summary-structure.json
      - type: JSON-LD
        url: json-ld/amazon-mainframe-modernization-context.jsonld
common:
  - type: Portal
    url: https://aws.amazon.com/mainframe-modernization/
  - type: Documentation
    url: https://docs.aws.amazon.com/m2/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/modernizing-with-aws/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/m2/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-mainframe-modernization-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-mainframe-modernization-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/modernization-workflow.yaml
  - type: Features
    data:
      - name: Automated Refactoring
        description: Automatically refactor COBOL mainframe applications to run natively on AWS.
      - name: Managed Runtime Environments
        description: Create and manage runtime environments using Micro Focus or Blue Age engines on AWS.
      - name: Application Deployment
        description: Deploy and manage versions of modernized mainframe applications.
      - name: Batch Job Execution
        description: Execute batch jobs migrated from mainframe in managed AWS environments.
      - name: Data Set Management
        description: Import and manage mainframe data sets for use by modernized applications.
  - type: UseCases
    data:
      - name: COBOL Modernization
        description: Refactor legacy COBOL applications to Java or other modern languages running on AWS.
      - name: Mainframe Replatforming
        description: Replatform mainframe workloads to AWS-managed environments without code changes.
      - name: Batch Job Migration
        description: Migrate batch processing workloads from mainframe to AWS for cost savings and scalability.
      - name: Mainframe Retirement
        description: Decommission on-premises mainframe hardware by migrating all workloads to AWS.
  - type: Integrations
    data:
      - name: Micro Focus Runtime
        description: Use Micro Focus Enterprise Server as the runtime engine for replatformed applications.
      - name: Blue Age Runtime
        description: Use Blue Age as the runtime engine for refactored applications.
      - name: Amazon EFS
        description: Store application artifacts and data sets in Elastic File System.
      - name: AWS CloudWatch
        description: Monitor application and batch job metrics through CloudWatch.
      - name: AWS VPC
        description: Deploy environments within a Virtual Private Cloud for network isolation.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
