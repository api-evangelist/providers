---
name: Amazon S3 Glacier
description: Amazon S3 Glacier is a secure, durable, and extremely low-cost Amazon S3 storage class purpose-built for long-term data archiving and digital preservation. It provides comprehensive security and compliance capabilities that can help meet even the most stringent regulatory requirements, with retrieval options ranging from minutes to hours depending on your access needs.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
url: https://raw.githubusercontent.com/api-evangelist/amazon-s3-glacier/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-19'
apis:
  - name: Amazon S3 Glacier API
    description: The Amazon S3 Glacier API provides programmatic access to manage long-term archive storage. It enables developers to create and manage vaults, upload and retrieve archives, configure vault notifications and access policies, initiate inventory retrieval jobs, and manage data lifecycle for cost- effective archival storage.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://aws.amazon.com/s3/storage-classes/glacier/
    baseURL: https://glacier.amazonaws.com
    tags:
      - Archive
      - AWS
      - Backup
      - Storage
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/amazonglacier/
      - type: OpenAPI
        url: openapi/amazon-s3-glacier-openapi.yml
      - type: Pricing
        url: https://aws.amazon.com/s3/pricing/
      - type: GettingStarted
        url: https://aws.amazon.com/s3/getting-started/
      - type: FAQ
        url: https://aws.amazon.com/s3/faqs/
common:
  - type: Portal
    url: https://aws.amazon.com/
  - type: Portal
    url: https://aws.amazon.com/s3/storage-classes/glacier/
  - type: Documentation
    url: https://docs.aws.amazon.com/amazonglacier/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Portal
    url: https://console.aws.amazon.com/glacier/
  - type: SignUp
    url: https://signin.aws.amazon.com/signup?request_type=register
  - type: Login
    url: https://aws.amazon.com/console/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: JSON-LD
    url: json-ld/amazon-s3-glacier-api-describe-vault-context.jsonld
  - type: JSON-LD
    url: json-ld/amazon-s3-glacier-api-job-parameters-context.jsonld
  - type: JSON-LD
    url: json-ld/amazon-s3-glacier-api-list-vaults-context.jsonld
  - type: JSON-LD
    url: json-ld/amazon-s3-glacier-context.jsonld
  - type: JSON-LD
    url: json-ld/amazon-s3-glacier-vault-context.jsonld
  - type: JSONSchema
    url: json-schema/amazon-s3-glacier-api-describe-vault-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-s3-glacier-api-job-parameters-schema.json
  - type: JSONSchema
    url: json-schema/amazon-s3-glacier-api-list-vaults-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-s3-glacier-vault-schema.json
  - type: JSONStructure
    url: json-structure/amazon-s3-glacier-api-describe-vault-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-s3-glacier-api-job-parameters-structure.json
  - type: JSONStructure
    url: json-structure/amazon-s3-glacier-api-list-vaults-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-s3-glacier-vault-structure.json
  - type: Example
    url: examples/amazon-s3-glacier-api-describe-vault-output-example.json
  - type: Example
    url: examples/amazon-s3-glacier-api-job-parameters-example.json
  - type: Example
    url: examples/amazon-s3-glacier-api-list-vaults-output-example.json
  - type: Example
    url: examples/amazon-s3-glacier-vault-example.json
  - type: NaftikoCapability
    url: capabilities/amazon-s3-glacier.yaml
  - type: NaftikoCapability
    url: capabilities/shared/amazon-s3-glacier.yaml
  - type: SpectralRules
    url: rules/amazon-s3-glacier-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-s3-glacier-vocabulary.yaml
  - type: OpenAPI
    url: openapi/amazon-s3-glacier-api-openapi.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
tags:
  - Archive
  - AWS
  - Backup
  - Storage
---
