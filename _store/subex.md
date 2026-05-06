---
aid: subex
url: https://raw.githubusercontent.com/api-evangelist/subex/refs/heads/main/apis.yml
apis:
  - aid: subex:subex-revenue-assurance-api
    name: Subex Revenue Assurance & Fraud Management API
    tags:
      - Revenue Assurance
      - Fraud Management
      - CDR Reconciliation
      - Analytics
      - Telecom
    humanURL: https://www.subex.com/roc/
    properties:
      - url: https://www.subex.com/roc/
        type: Documentation
      - url: https://www.subex.com/contact-us/
        type: Contact
      - url: openapi/subex-revenue-assurance-openapi.yml
        type: OpenAPI
    description: Subex ROC (Revenue Operations Center) API for telecom operators. Provides revenue leakage detection and management, fraud case investigation, subscriber risk scoring, CDR reconciliation, and analytics across voice, data, roaming, and digital services.
name: Subex
tags:
  - Telecom
  - Revenue Assurance
  - Fraud Management
  - Analytics
  - BSS/OSS
type: Contract
access: 3rd-Party
created: '2026-03-18'
modified: '2026-05-02'
position: Consuming
description: Subex is a telecom analytics company providing revenue assurance, fraud management, and network analytics solutions through its ROC (Revenue Operations Center) platform. Subex helps telecom operators detect and prevent revenue leakage, manage telecom fraud (SIM swap, IRSF, bypass fraud, roaming fraud), reconcile CDR data, and gain analytics insights across their business support systems.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
common:
  - url: https://www.subex.com
    type: Website
  - url: https://www.subex.com/roc/
    type: Portal
  - url: https://www.subex.com/blog/
    type: Blog
  - url: https://www.subex.com/contact-us/
    type: Support
  - url: https://www.subex.com/privacy-policy/
    type: Privacy Policy
  - url: https://www.subex.com/newsroom/
    type: Change Log
  - url: rules/subex-rules.yml
    type: Spectral Rules
  - url: capabilities/revenue-operations-center.yaml
    type: Naftiko Capability
  - url: vocabulary/subex-vocabulary.yml
    type: Vocabulary
  - url: json-schema/subex-fraud-case-schema.json
    type: JSON Schema
  - url: json-structure/subex-leakage-alert-structure.json
    type: JSON Structure
  - url: json-ld/subex-context.jsonld
    type: JSON-LD Context
  - url: examples/subex-list-fraud-cases-example.json
    type: Example
  - url: examples/subex-get-subscriber-risk-score-example.json
    type: Example
---
