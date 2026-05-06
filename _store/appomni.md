---
aid: appomni
name: AppOmni
description: AppOmni is a SaaS security management platform providing continuous monitoring, threat detection, and compliance for enterprise SaaS applications.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - SaaS Security
  - Compliance
  - Threat Detection
  - CASB
  - Zero Trust
url: https://raw.githubusercontent.com/api-evangelist/appomni/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: appomni:appomni-api
    name: AppOmni API
    tags:
      - SaaS Security
      - Compliance
      - Threat Detection
      - Policies
    humanURL: https://www.appomni.com
    properties:
      - url: https://www.appomni.com
        type: Website
      - url: https://www.appomni.com/resources
        type: Documentation
      - url: openapi/appomni-openapi.yaml
        type: OpenAPI
      - url: json-schema/security-event-schema.json
        type: JSONSchema
      - url: json-structure/security-event-structure.json
        type: JSONStructure
      - url: examples/security-event-example.json
        type: Example
      - url: json-ld/appomni-context.jsonld
        type: JSONLD
      - url: rules/appomni-spectral-rules.yml
        type: SpectralRules
      - url: capabilities/shared/appomni-api.yaml
        type: NaftikoCapability
      - url: capabilities/saas-security-monitoring.yaml
        type: NaftikoCapability
      - url: vocabulary/appomni-vocabulary.yaml
        type: Vocabulary
    description: API for the AppOmni SaaS security management platform providing security event monitoring, policy management, and compliance reporting across enterprise SaaS applications.
common:
  - type: Website
    url: https://www.appomni.com
  - type: Documentation
    url: https://www.appomni.com/resources
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
