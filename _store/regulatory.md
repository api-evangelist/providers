---
aid: regulatory
name: Regulatory
description: The regulatory domain encompasses compliance requirements, regulatory reporting, and governance frameworks that organizations must adhere to across industries. APIs in this space enable businesses to automate compliance workflows, track regulatory changes, submit required filings, and manage risk. Key sectors include financial services (SEC, FINRA, CFTC), healthcare (FDA, CMS), telecommunications (FCC), and environmental regulation (EPA).
type: Index
url: https://raw.githubusercontent.com/api-evangelist/regulatory/refs/heads/main/apis.yml
tags:
  - Compliance
  - Financial Services
  - Governance
  - Healthcare Regulation
  - Regulatory Reporting
  - Risk Management
  - RegTech
created: '2025-01-01'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: regulatory:finra
    name: FINRA Developer Center API
    description: FINRA (Financial Industry Regulatory Authority) provides APIs to support automation goals for member firms and the broader financial services industry. APIs provide access to market data, compliance tools, regulatory filings, and risk management resources.
    humanURL: https://developer.finra.org/
    baseURL: https://api.finra.org
    tags:
      - Financial Regulation
      - FINRA
      - Market Data
      - Regulatory Compliance
    properties:
      - type: Documentation
        url: https://developer.finra.org/
  - aid: regulatory:compliance-ai
    name: Compliance.ai API
    description: Compliance.ai automatically aggregates regulatory data from Federal and State agencies, enforcement actions, regulatory publications, and millions of rules, providing an API for financial institutions and GRC platforms to stay current on regulatory changes.
    humanURL: https://www.compliance.ai/api/
    baseURL: https://api.compliance.ai
    tags:
      - Financial Services
      - Regulatory Change Management
      - RegTech
    properties:
      - type: Documentation
        url: https://www.compliance.ai/api/
  - aid: regulatory:regology
    name: Regology API
    description: Regology is an AI-powered global regulatory compliance platform providing APIs for regulatory research, change management, and compliance workflows. Aggregates and organizes regulatory content from thousands of global sources.
    humanURL: https://regology.com/
    baseURL: https://api.regology.com/v1
    tags:
      - AI
      - Compliance
      - Global Regulation
      - Regulatory Research
    properties:
      - type: Documentation
        url: https://regology.com/platform
  - aid: regulatory:lseg-regulatory
    name: LSEG Risk and Regulatory Compliance API
    description: London Stock Exchange Group (LSEG) offers a developer portal with APIs for risk and regulatory compliance including sanctions screening, KYC/AML checks, and regulatory reporting tools used by financial institutions globally.
    humanURL: https://developers.lseg.com/en/use-cases-catalog/risk-regulatory-compliance
    baseURL: https://api.refinitiv.com
    tags:
      - AML
      - Financial Services
      - KYC
      - Regulatory Reporting
      - Sanctions Screening
    properties:
      - type: Documentation
        url: https://developers.lseg.com/en/use-cases-catalog/risk-regulatory-compliance
common:
  - type: Website
    url: https://developer.finra.org/
    name: FINRA Developer Center
  - type: Website
    url: https://www.compliance.ai/api/
    name: Compliance.ai Developer Program
  - type: Website
    url: https://regology.com/
    name: Regology AI Regulatory Compliance Platform
  - type: Website
    url: https://developers.lseg.com/en/use-cases-catalog/risk-regulatory-compliance
    name: LSEG Risk and Regulatory Compliance Developer Portal
  - type: Website
    url: https://www.regulativ.ai/
    name: Regulativ AI Compliance Platform
  - type: Website
    url: https://nordicapis.com/10-data-regulations-all-api-developers-should-know-about/
    name: 10 Data Regulations All API Developers Should Know
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/regulatory/refs/heads/main/json-schema/regulatory-compliance-check-schema.json
    name: Regulatory Compliance Check JSON Schema
  - type: JSONStructure
    url: https://raw.githubusercontent.com/api-evangelist/regulatory/refs/heads/main/json-structure/regulatory-compliance-check-structure.json
    name: Regulatory Compliance Check JSON Structure
  - type: JSONLD
    url: https://raw.githubusercontent.com/api-evangelist/regulatory/refs/heads/main/json-ld/regulatory-context.jsonld
    name: Regulatory JSON-LD Context
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/regulatory/refs/heads/main/vocabulary/regulatory-vocabulary.yml
    name: Regulatory Vocabulary
  - type: Examples
    url: https://raw.githubusercontent.com/api-evangelist/regulatory/refs/heads/main/examples/regulatory-compliance-check-finra-example.json
    name: FINRA Compliance Check Example
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
