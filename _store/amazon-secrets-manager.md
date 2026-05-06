---
name: Amazon Secrets Manager
description: Amazon Secrets Manager helps you manage, retrieve, and rotate database credentials, API keys, and other secrets throughout their lifecycle. It provides centralized secrets management with built-in integration for Amazon RDS, Amazon Redshift, and Amazon DocumentDB, enabling automatic rotation of secrets without requiring application changes.
url: https://aws.amazon.com/secrets-manager/
baseURL: https://secretsmanager.amazonaws.com
x-type: company
created: '2024-01-01'
modified: '2026-04-19'
tags:
  - AWS
  - Configuration
  - Credentials
  - Rotation
  - Secrets
  - Security
apis:
  - name: Amazon Secrets Manager API
    description: The Amazon Secrets Manager API for creating, managing, retrieving, and rotating secrets including database credentials, API keys, and other sensitive configuration.
    humanURL: https://docs.aws.amazon.com/secretsmanager/latest/apireference/
    baseURL: https://secretsmanager.{region}.amazonaws.com
    tags:
      - Security
      - Secrets
      - Credentials
      - Rotation
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/secretsmanager/latest/apireference/
      - type: OpenAPI
        url: openapi/amazon-secrets-manager-openapi.yml
      - type: JSONSchema
        url: json-schema/amazon-secrets-manager-secret-schema.json
      - type: JSONSchema
        url: json-schema/amazon-secrets-manager-secret-value-schema.json
      - type: JSONSchema
        url: json-schema/amazon-secrets-manager-rotation-rules-schema.json
common:
  - type: Portal
    url: https://aws.amazon.com/
  - type: GettingStarted
    url: https://aws.amazon.com/secrets-manager/getting-started/
  - type: Documentation
    url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/
  - type: APIReference
    url: https://docs.aws.amazon.com/secretsmanager/latest/apireference/
  - type: Console
    url: https://console.aws.amazon.com/secretsmanager/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Pricing
    url: https://aws.amazon.com/secrets-manager/pricing/
  - type: FAQ
    url: https://aws.amazon.com/secrets-manager/faqs/
  - type: Blog
    url: https://aws.amazon.com/blogs/security/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Support
    url: https://aws.amazon.com/support/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Security
    url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/security.html
  - type: Compliance
    url: https://aws.amazon.com/compliance/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: YouTube
    url: https://www.youtube.com/user/AmazonWebServices
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/aws-secrets-manager
  - type: KnowledgeCenter
    url: https://repost.aws/knowledge-center
  - type: CLI
    url: https://docs.aws.amazon.com/cli/latest/reference/secretsmanager/
  - type: SpectralRules
    url: rules/amazon-secrets-manager-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-secrets-manager-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/secrets-management.yaml
  - type: Features
    data:
      - name: Automatic Secret Rotation
        description: Automatically rotate secrets on a schedule using AWS Lambda rotation functions without changing application code.
      - name: Centralized Secret Storage
        description: Store and manage all secrets in a single, centralized location with fine-grained access controls.
      - name: Native Database Integration
        description: Built-in integration with Amazon RDS, Aurora, Redshift, and DocumentDB for automatic credential rotation.
      - name: Secret Versioning
        description: Maintain multiple versions of a secret simultaneously to support zero-downtime rotation.
      - name: Audit and Compliance
        description: Log all secret access and management actions via AWS CloudTrail for compliance and audit purposes.
      - name: Cross-Account Access
        description: Share secrets across AWS accounts using resource-based policies.
      - name: Encryption at Rest
        description: All secrets are encrypted at rest using AWS KMS keys you control.
      - name: Random Password Generation
        description: Generate cryptographically secure random passwords with configurable complexity requirements.
  - type: UseCases
    data:
      - name: Database Credential Management
        description: Automatically rotate and manage database credentials for RDS, Aurora, and other databases.
      - name: API Key Storage
        description: Securely store and retrieve API keys, OAuth tokens, and other third-party service credentials.
      - name: Application Configuration
        description: Centralize sensitive application configuration such as connection strings and encryption keys.
      - name: Cross-Service Credentials
        description: Share service-to-service credentials securely across microservices without embedding in code.
      - name: Compliance Secret Rotation
        description: Meet compliance requirements like PCI DSS and SOC 2 by enforcing regular credential rotation.
      - name: Secrets Lifecycle Governance
        description: Enforce organizational policies on secret creation, rotation schedules, and access patterns.
  - type: Integrations
    data:
      - name: Amazon RDS
        description: Native integration for automatic rotation of RDS database credentials.
      - name: Amazon Aurora
        description: Built-in support for rotating Aurora database master user passwords.
      - name: Amazon Redshift
        description: Automatic rotation of Redshift cluster credentials.
      - name: Amazon DocumentDB
        description: Native rotation support for DocumentDB user credentials.
      - name: AWS Lambda
        description: Lambda-powered custom rotation functions for any secret type.
      - name: AWS CloudTrail
        description: Audit logging of all Secrets Manager API calls via CloudTrail.
      - name: AWS KMS
        description: Encryption of secrets at rest using customer-managed KMS keys.
      - name: AWS IAM
        description: Fine-grained access control for secrets using IAM policies and resource-based policies.
      - name: AWS CloudFormation
        description: Provision and manage secrets as part of CloudFormation stacks.
  - type: JSON-LD
    url: json-ld/amazon-secrets-manager-context.jsonld
  - type: JSONSchema
    url: json-schema/amazon-secrets-manager-get-random-password-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-secrets-manager-list-secrets-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-secrets-manager-tag-schema.json
  - type: JSONStructure
    url: json-structure/amazon-secrets-manager-get-random-password-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-secrets-manager-list-secrets-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-secrets-manager-rotation-rules-structure.json
  - type: JSONStructure
    url: json-structure/amazon-secrets-manager-secret-structure.json
  - type: JSONStructure
    url: json-structure/amazon-secrets-manager-secret-value-structure.json
  - type: JSONStructure
    url: json-structure/amazon-secrets-manager-tag-structure.json
  - type: Example
    url: examples/amazon-secrets-manager-get-random-password-response-example.json
  - type: Example
    url: examples/amazon-secrets-manager-list-secrets-response-example.json
  - type: Example
    url: examples/amazon-secrets-manager-rotation-rules-example.json
  - type: Example
    url: examples/amazon-secrets-manager-secret-example.json
  - type: Example
    url: examples/amazon-secrets-manager-secret-value-example.json
  - type: Example
    url: examples/amazon-secrets-manager-tag-example.json
  - type: NaftikoCapability
    url: capabilities/shared/amazon-secrets-manager.yaml
maintainer: Kin Lane
---
