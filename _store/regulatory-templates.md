---
aid: regulatory-templates
name: Regulatory Templates
description: Pre-built templates, frameworks, and policy libraries for meeting regulatory compliance requirements across industries and jurisdictions including GDPR, HIPAA, SOC 2, ISO 27001, PCI DSS, and more. Compliance platforms and API governance tools provide template-driven approaches to accelerate audit readiness, evidence collection, and risk management workflows.
type: Index
url: https://raw.githubusercontent.com/api-evangelist/regulatory-templates/refs/heads/main/apis.yml
tags:
  - Compliance
  - Governance
  - GDPR
  - HIPAA
  - ISO 27001
  - PCI DSS
  - Policy Templates
  - Regulatory
  - SOC 2
  - Templates
created: '2025-01-01'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: regulatory-templates:onetrust
    name: OneTrust API
    description: OneTrust provides a privacy, security, and data governance platform with APIs for automating compliance with GDPR, CCPA, HIPAA, and 50+ regulatory frameworks. Offers pre-built templates for consent management, data subject requests, and risk assessments.
    humanURL: https://developer.onetrust.com/
    baseURL: https://app.onetrust.com/api/v2
    tags:
      - Compliance Automation
      - GDPR
      - Privacy
      - Risk Management
    properties:
      - type: Documentation
        url: https://developer.onetrust.com/
  - aid: regulatory-templates:vanta
    name: Vanta API
    description: Vanta automates security compliance for SOC 2, ISO 27001, HIPAA, PCI DSS, and GDPR. The API enables programmatic access to compliance monitoring, evidence collection, and audit preparation workflows with pre-built control templates.
    humanURL: https://developer.vanta.com/
    baseURL: https://api.vanta.com/v1
    tags:
      - Audit Automation
      - Compliance
      - SOC 2
      - Security
    properties:
      - type: Documentation
        url: https://developer.vanta.com/
  - aid: regulatory-templates:drata
    name: Drata API
    description: Drata is a security and compliance automation platform providing pre-built control frameworks and policy templates for SOC 2, ISO 27001, HIPAA, GDPR, and PCI DSS. The API supports continuous compliance monitoring and evidence collection automation.
    humanURL: https://drata.com/
    baseURL: https://api.drata.com/v1
    tags:
      - Compliance
      - Control Frameworks
      - ISO 27001
      - SOC 2
    properties:
      - type: Documentation
        url: https://drata.com/
  - aid: regulatory-templates:scrut-automation
    name: Scrut Automation API
    description: Scrut Automation provides a compliance platform supporting 50+ frameworks including SOC 2, ISO 27001, HIPAA, GDPR, and PCI DSS, with built-in integrations and automated evidence collection through API-driven workflows.
    humanURL: https://www.scrut.io/
    baseURL: https://api.scrut.io/v1
    tags:
      - Compliance
      - Evidence Collection
      - Framework Automation
      - Security
    properties:
      - type: Documentation
        url: https://www.scrut.io/
common:
  - type: Website
    url: https://usercentrics.com/knowledge-hub/regulatory-compliance-platform/
    name: Best Regulatory Compliance Platforms 2026
  - type: Website
    url: https://www.vero-ai.com/blog/regulatory-compliance-software-vendors
    name: Regulatory Compliance Software Vendors Compared
  - type: Website
    url: https://riskonnect.com/solutions/regulatory-compliance-software/
    name: Riskonnect Regulatory Compliance Software
  - type: Website
    url: https://www.speakeasy.com/api-design/api-compliance
    name: API Compliance Best Practices - Speakeasy
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/regulatory-templates/refs/heads/main/json-schema/regulatory-templates-control-schema.json
    name: Compliance Control JSON Schema
  - type: JSONStructure
    url: https://raw.githubusercontent.com/api-evangelist/regulatory-templates/refs/heads/main/json-structure/regulatory-templates-control-structure.json
    name: Compliance Control JSON Structure
  - type: JSONLD
    url: https://raw.githubusercontent.com/api-evangelist/regulatory-templates/refs/heads/main/json-ld/regulatory-templates-context.jsonld
    name: Regulatory Templates JSON-LD Context
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/regulatory-templates/refs/heads/main/vocabulary/regulatory-templates-vocabulary.yml
    name: Regulatory Templates Vocabulary
  - type: Examples
    url: https://raw.githubusercontent.com/api-evangelist/regulatory-templates/refs/heads/main/examples/regulatory-templates-soc2-control-example.json
    name: SOC 2 Compliance Control Example
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
