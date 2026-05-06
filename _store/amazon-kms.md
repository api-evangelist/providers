---
name: Amazon KMS
segments:
  - Security
  - Encryption
description: AWS Key Management Service (KMS) is a managed service that makes it easy to create and control the cryptographic keys used to protect your data, integrated with other AWS services to simplify encryption of data stored and managed in those services.
url: https://aws.amazon.com/kms/
type: Index
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
tags:
  - AWS
  - Cryptography
  - Data Protection
  - Encryption
  - Key Management
  - Security
created: '2024-01-15'
modified: '2026-04-19'
apis:
  - name: Amazon KMS API
    description: The AWS Key Management Service API provides programmatic access to create and manage cryptographic keys, encrypt and decrypt data, generate data keys, and manage key policies and grants for controlling access to encryption operations.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://aws.amazon.com/kms/
    baseURL: https://kms.amazonaws.com
    tags:
      - Cryptography
      - Encryption
      - Key Management
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/kms/latest/developerguide/overview.html
      - type: OpenAPI
        url: https://api.apis.guru/v2/specs/amazonaws.com/kms/2014-11-01/openapi.yaml
      - type: Pricing
        url: https://aws.amazon.com/kms/pricing/
      - type: GettingStarted
        url: https://aws.amazon.com/kms/getting-started/
      - type: FAQ
        url: https://aws.amazon.com/kms/faqs/
      - type: Features
        url: https://aws.amazon.com/kms/features/
      - type: Documentation
        url: https://docs.aws.amazon.com/kms/latest/developerguide/overview.html
      - type: APIReference
        url: https://docs.aws.amazon.com/kms/latest/APIReference/Welcome.html
      - type: OpenAPI
        url: openapi/amazon-kms-openapi.yml
      - type: JSONLD
        url: json-ld/amazon-kms-context.jsonld
      - type: JSONSchema
        url: json-schema/amazon-kms-key-schema.json
common:
  - type: Blog
    url: https://aws.amazon.com/blogs/security/category/security-identity-compliance/aws-key-management-service/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Console
    url: https://console.aws.amazon.com/kms/home
  - type: CLI
    url: https://docs.aws.amazon.com/cli/latest/reference/kms/
  - type: SDK
    url: https://aws.amazon.com/tools/
  - type: StatusPage
    url: https://status.aws.amazon.com/
  - type: Compliance
    url: https://aws.amazon.com/compliance/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: Portal
    url: https://aws.amazon.com/kms/
  - type: Documentation
    url: https://docs.aws.amazon.com/kms/
  - type: Pricing
    url: https://aws.amazon.com/kms/pricing/
  - type: GettingStarted
    url: https://aws.amazon.com/kms/getting-started/
  - type: FAQ
    url: https://aws.amazon.com/kms/faqs/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Features
    data:
      - name: Centralized Key Management
        description: Create, import, rotate, disable, delete, and audit usage of cryptographic keys from a central location.
      - name: Hardware Security Modules
        description: Keys are protected by FIPS 140-2 validated hardware security modules (HSMs).
      - name: Automatic Key Rotation
        description: Enable automatic annual rotation of KMS keys without changing key ARNs.
      - name: Multi-Region Keys
        description: Create multi-Region keys that can be replicated into multiple AWS Regions.
      - name: Asymmetric Key Support
        description: Generate and use asymmetric RSA and ECC key pairs for encryption and signing.
      - name: CloudTrail Integration
        description: Every KMS API call is logged to AWS CloudTrail for auditing and compliance.
  - type: UseCases
    data:
      - name: Data at Rest Encryption
        description: Encrypt data stored in S3, RDS, EBS, and other AWS services using KMS keys.
      - name: Envelope Encryption
        description: Use KMS to generate data encryption keys for envelope encryption patterns.
      - name: Digital Signatures
        description: Use asymmetric KMS keys to sign and verify digital signatures.
      - name: BYOK (Bring Your Own Key)
        description: Import your own cryptographic key material into AWS KMS for compliance requirements.
  - type: Integrations
    data:
      - name: Amazon S3
        description: Encrypt S3 objects at rest using SSE-KMS with customer managed keys.
      - name: Amazon RDS
        description: Encrypt RDS database instances and automated backups with KMS keys.
      - name: AWS CloudTrail
        description: All KMS API usage is automatically logged for audit and compliance.
      - name: AWS Secrets Manager
        description: Encrypt secrets stored in Secrets Manager with KMS keys.
      - name: AWS Lambda
        description: Encrypt Lambda environment variables with KMS customer managed keys.
  - type: SpectralRules
    url: rules/amazon-kms-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/amazon-kms-workflow.yaml
  - type: Vocabulary
    url: vocabulary/amazon-kms-vocabulary.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
include: []
---
