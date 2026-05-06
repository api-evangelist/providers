---
aid: saasment
name: Saasment
description: Saasment is an AI-powered SaaS security posture management (SSPM) and cloud cost optimization platform that detects misconfigurations, compliance gaps, and cost inefficiencies across cloud applications. It provides continuous monitoring, automated breach and attack simulation, privileged access management, and seamless integrations with identity management systems and other security tools.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - SaaS Security
  - SSPM
  - Cloud Security
  - Cost Optimization
  - Compliance
  - Misconfigurations
url: https://raw.githubusercontent.com/api-evangelist/saasment/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: saasment:saasment
    name: Saasment API
    description: The Saasment API provides programmatic access to SaaS security posture management capabilities including configuration scanning, compliance assessment, misconfigurations detection, cost optimization recommendations, and integration with cloud identity systems to secure SaaS estates.
    humanURL: https://www.saasment.com
    tags:
      - SaaS Security
      - SSPM
      - Cloud Security
      - Compliance
      - Cost Optimization
    properties:
      - type: Documentation
        url: https://www.saasment.com/resources
      - type: Website
        url: https://www.saasment.com
      - type: OpenAPI
        url: openapi/saasment-openapi.yml
common:
  - type: Website
    url: https://www.saasment.com
  - type: Documentation
    url: https://www.saasment.com/resources
  - type: Blog
    url: https://www.saasment.com/blog
  - type: OpenAPI
    url: openapi/saasment-openapi.yml
  - type: SpectralRules
    url: rules/saasment-rules.yml
  - type: JSONSchema
    url: json-schema/saasment-misconfiguration-schema.json
  - type: JSONSchema
    url: json-schema/saasment-application-schema.json
  - type: JSONStructure
    url: json-structure/saasment-misconfiguration-structure.json
  - type: JSONStructure
    url: json-structure/saasment-application-structure.json
  - type: JSONLDContext
    url: json-ld/saasment-context.jsonld
  - type: Vocabulary
    url: vocabulary/saasment-vocabulary.yml
  - type: Capabilities
    url: capabilities/saas-security-posture.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
