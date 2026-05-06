---
aid: amazon-signer
name: Amazon Signer
description: AWS Signer is a fully managed code-signing service to ensure the trust and integrity of your code. It manages the code-signing certificate public and private keys and enables central management and deployment of code signing certificates for Lambda functions and IoT devices.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Code Signing
  - IoT
  - Lambda
  - Security
url: https://raw.githubusercontent.com/api-evangelist/amazon-signer/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-signer:aws-signer-api
    name: AWS Signer API
    description: The AWS Signer API provides programmatic access to create and manage signing profiles, signing jobs, and signing platform permissions for code signing of Lambda functions and IoT device software.
    humanURL: https://aws.amazon.com/signer/
    baseURL: https://signer.amazonaws.com
    tags:
      - Code Signing
      - Lambda
      - Security
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/signer/latest/api/Welcome.html
      - type: OpenAPI
        url: openapi/amazon-signer.yaml
      - type: GettingStarted
        url: https://aws.amazon.com/signer/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/signer/pricing/
      - type: FAQ
        url: https://aws.amazon.com/signer/faqs/
common:
  - type: Portal
    url: https://aws.amazon.com/signer/
  - type: Documentation
    url: https://docs.aws.amazon.com/signer/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/compute/tag/aws-signer/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/signer/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-signer-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-signer-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/shared/amazon-signer.yaml
  - type: Features
    data:
      - name: Centralized Code Signing
        description: Security administrators define signing policies and which IAM roles can sign code.
      - name: Certificate Management
        description: Automatically manages code-signing certificate public and private keys.
      - name: Lifecycle Management
        description: Central management and deployment of code-signing certificates.
      - name: Compliance Tracking
        description: Integration with AWS CloudTrail tracks who generates signatures for compliance.
      - name: Fully Managed
        description: No infrastructure to maintain — fully managed code signing service.
      - name: Signature Revocation
        description: Revoke signing profiles and individual signatures with effective timestamps.
  - type: UseCases
    data:
      - name: Lambda Code Signing
        description: Sign Lambda deployment packages to ensure only trusted code is deployed.
      - name: IoT Firmware Signing
        description: Sign firmware images for microcontrollers and over-the-air (OTA) updates via Amazon FreeRTOS.
      - name: Container Image Signing
        description: Sign container images using Notation CLI with Amazon ECR and verify at EKS deployment.
      - name: Audit and Compliance
        description: Track all signing operations via CloudTrail for audit and compliance requirements.
  - type: Integrations
    data:
      - name: AWS Lambda
        description: Sign Lambda deployment packages; Lambda verifies signatures at deployment.
      - name: Amazon FreeRTOS
        description: Sign firmware images for IoT microcontrollers and OTA updates.
      - name: Amazon ECR
        description: Sign container images using Notation CLI stored in ECR registry.
      - name: Amazon EKS
        description: Verify image ownership and integrity at Kubernetes deployment time.
      - name: AWS Certificate Manager
        description: Create or import SSL/TLS certificates used for code signing.
      - name: AWS CloudTrail
        description: Record and audit all API calls to AWS Signer for compliance.
      - name: AWS IoT Device Management
        description: Sign code for IoT devices managed by AWS IoT Device Management.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
x-type: company
---
