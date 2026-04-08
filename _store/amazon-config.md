---
aid: amazon-config
url: https://raw.githubusercontent.com/api-evangelist/amazon-config/refs/heads/main/apis.yml
apis:
- name: Amazon Config API
  description: The AWS Config API provides programmatic access to manage configuration recording, evaluate resource compliance against rules, query resource configurations, and track configuration changes across your AWS infrastructure.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  url: https://aws.amazon.com/config/
  baseURL: https://config.amazonaws.com
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/config/latest/APIReference/
  - type: OpenAPI
    url: openapi/amazon-config-openapi.yml
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/config/2014-11-12/openapi.yaml
  - type: JSONSchema
    url: json-schema/amazon-config-rule-schema.json
  - type: JSONLD
    url: json-ld/amazon-config-context.jsonld
  - type: Pricing
    url: https://aws.amazon.com/config/pricing/
  - type: Getting Started
    url: https://aws.amazon.com/config/getting-started/
  - type: FAQ
    url: https://aws.amazon.com/config/faq/
  - type: User Guide
    url: https://docs.aws.amazon.com/config/latest/developerguide/
  - type: API Reference
    url: https://docs.aws.amazon.com/config/latest/APIReference/
  - type: CLI Reference
    url: https://docs.aws.amazon.com/cli/latest/reference/configservice/
  - type: Security
    url: https://docs.aws.amazon.com/config/latest/developerguide/security.html
name: Amazon Config
tags:
- Auditing
- AWS
- Compliance
- Configuration
- Governance
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: AWS Config provides a detailed view of the configuration of AWS resources in your AWS account. This includes how the resources are related to one another and how they were configured in the past, enabling assessment, auditing, and evaluation of configurations for compliance and security governance.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

