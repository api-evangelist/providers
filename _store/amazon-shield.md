---
name: Amazon Shield
description: AWS Shield is a managed Distributed Denial of Service (DDoS) protection service that safeguards applications running on AWS. It provides always-on detection and automatic inline mitigations that minimize application downtime and latency, with two tiers of protection - Shield Standard for automatic defense against common attacks and Shield Advanced for enhanced detection and 24/7 access to the DDoS Response Team.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
url: https://raw.githubusercontent.com/api-evangelist/amazon-shield/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-19'
apis:
  - name: AWS Shield API
    description: The AWS Shield API provides programmatic access to manage DDoS protection for your AWS resources. It enables developers to create and manage protections, subscribe to Shield Advanced, configure emergency contacts, view attack details and statistics, and manage protection groups for coordinated defense across multiple resources.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://aws.amazon.com/shield/
    baseURL: https://shield.amazonaws.com
    tags:
      - AWS
      - DDoS Protection
      - Networking
      - Security
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html
      - type: OpenAPI
        url: openapi/amazon-shield-openapi.yml
      - type: Pricing
        url: https://aws.amazon.com/shield/pricing/
      - type: GettingStarted
        url: https://aws.amazon.com/shield/getting-started/
      - type: FAQ
        url: https://aws.amazon.com/shield/faqs/
common:
  - type: Portal
    url: https://aws.amazon.com/
  - type: Portal
    url: https://aws.amazon.com/shield/
  - type: Documentation
    url: https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Portal
    url: https://console.aws.amazon.com/wafv2/shieldv2
  - type: SignUp
    url: https://signin.aws.amazon.com/signup?request_type=register
  - type: Login
    url: https://aws.amazon.com/console/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: JSON-LD
    url: json-ld/amazon-shield-context-context.jsonld
  - type: JSON-LD
    url: json-ld/amazon-shield-context.jsonld
  - type: JSONSchema
    url: json-schema/amazon-shield-api-attack-detail-schema.json
  - type: JSONSchema
    url: json-schema/amazon-shield-api-create-protection-group-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-shield-api-create-protection-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-shield-api-create-protection-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-shield-api-describe-attack-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-shield-api-describe-attack-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-shield-api-describe-protection-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-shield-api-describe-protection-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-shield-api-list-protections-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-shield-api-list-protections-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-shield-api-mitigation-schema.json
  - type: JSONSchema
    url: json-schema/amazon-shield-api-protection-schema.json
  - type: JSONSchema
    url: json-schema/amazon-shield-api-summarized-counter-schema.json
  - type: JSONSchema
    url: json-schema/amazon-shield-api-tag-schema.json
  - type: JSONSchema
    url: json-schema/amazon-shield-protection-schema.json
  - type: JSONStructure
    url: json-structure/amazon-shield-api-attack-detail-structure.json
  - type: JSONStructure
    url: json-structure/amazon-shield-api-create-protection-group-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-shield-api-create-protection-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-shield-api-create-protection-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-shield-api-describe-attack-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-shield-api-describe-attack-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-shield-api-describe-protection-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-shield-api-describe-protection-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-shield-api-list-protections-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-shield-api-list-protections-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-shield-api-mitigation-structure.json
  - type: JSONStructure
    url: json-structure/amazon-shield-api-protection-structure.json
  - type: JSONStructure
    url: json-structure/amazon-shield-api-summarized-counter-structure.json
  - type: JSONStructure
    url: json-structure/amazon-shield-api-tag-structure.json
  - type: JSONStructure
    url: json-structure/amazon-shield-protection-structure.json
  - type: Example
    url: examples/amazon-shield-api-attack-detail-example.json
  - type: Example
    url: examples/amazon-shield-api-create-protection-group-request-example.json
  - type: Example
    url: examples/amazon-shield-api-create-protection-request-example.json
  - type: Example
    url: examples/amazon-shield-api-create-protection-response-example.json
  - type: Example
    url: examples/amazon-shield-api-describe-attack-request-example.json
  - type: Example
    url: examples/amazon-shield-api-describe-attack-response-example.json
  - type: Example
    url: examples/amazon-shield-api-describe-protection-request-example.json
  - type: Example
    url: examples/amazon-shield-api-describe-protection-response-example.json
  - type: Example
    url: examples/amazon-shield-api-list-protections-request-example.json
  - type: Example
    url: examples/amazon-shield-api-list-protections-response-example.json
  - type: Example
    url: examples/amazon-shield-api-mitigation-example.json
  - type: Example
    url: examples/amazon-shield-api-protection-example.json
  - type: Example
    url: examples/amazon-shield-api-summarized-counter-example.json
  - type: Example
    url: examples/amazon-shield-api-tag-example.json
  - type: Example
    url: examples/amazon-shield-protection-example.json
  - type: NaftikoCapability
    url: capabilities/amazon-shield.yaml
  - type: NaftikoCapability
    url: capabilities/shared/amazon-shield.yaml
  - type: SpectralRules
    url: rules/amazon-shield-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-shield-vocabulary.yaml
  - type: OpenAPI
    url: openapi/amazon-shield-api-openapi.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
tags:
  - AWS
  - DDoS Protection
  - Networking
  - Security
---
