---
aid: amazon-payment-cryptography
name: Amazon Payment Cryptography
description: AWS Payment Cryptography is a managed service that makes it easy to build and maintain payment processing applications by providing cloud-based cryptographic capabilities. It enables you to perform cryptographic operations required by payment card industry standards without managing hardware security modules.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Cryptography
  - Financial Services
  - Payment Processing
  - PCI
url: https://raw.githubusercontent.com/api-evangelist/amazon-payment-cryptography/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-payment-cryptography:aws-payment-cryptography-api
    name: AWS Payment Cryptography API
    description: The AWS Payment Cryptography API provides programmatic access to manage keys, aliases, and perform cryptographic operations for payment processing applications that require PCI-compliant security.
    humanURL: https://aws.amazon.com/payment-cryptography/
    baseURL: https://controlplane.payment-cryptography.amazonaws.com
    tags:
      - Cryptography
      - Financial Services
      - Payment Processing
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/Welcome.html
      - type: OpenAPI
        url: openapi/amazon-payment-cryptography-openapi.yml
      - type: Getting Started
        url: https://aws.amazon.com/payment-cryptography/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/payment-cryptography/pricing/
      - type: FAQ
        url: https://aws.amazon.com/payment-cryptography/faqs/
common:
  - type: Portal
    url: https://aws.amazon.com/payment-cryptography/
  - type: Website
    url: https://aws.amazon.com/payment-cryptography/
  - type: Documentation
    url: https://docs.aws.amazon.com/payment-cryptography/
  - type: Terms of Service
    url: https://aws.amazon.com/service-terms/
  - type: Privacy Policy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/industries/financial-services/
  - type: GitHub Organization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/payment-cryptography/
  - type: Sign Up
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: Status
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-payment-cryptography-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-payment-cryptography-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/amazon-payment-cryptography-workflow.yaml
  - type: JSON-LD
    url: json-ld/amazon-payment-cryptography-openapi-context.jsonld
  - type: JSONSchema
    url: json-schema/openapi-access-denied-exception-schema.json
    title: Openapi Access Denied Exception
  - type: JSONSchema
    url: json-schema/openapi-alias-name-schema.json
    title: Openapi Alias Name
  - type: JSONSchema
    url: json-schema/openapi-alias-schema.json
    title: Openapi Alias
  - type: JSONSchema
    url: json-schema/openapi-aliases-schema.json
    title: Openapi Aliases
  - type: JSONSchema
    url: json-schema/openapi-boolean-schema.json
    title: Openapi Boolean
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
