---
aid: sandbox-banking
name: Sandbox Banking
description: Sandbox Banking (now nCino Integration Gateway) is an Integration Platform as a Service (iPaaS) purpose-built for financial institutions. The platform enables banks and credit unions to connect core banking systems (Fiserv, Jack Henry, FIS, and 14+ other cores) with fintech applications, loan origination systems, CRMs, KYC/AML providers, and 50+ financial services solutions. Glyue, the core integration framework, provides low-code workflow automation with Python extensibility, audit trails, role-based access control, and regulatory compliance features aligned with CFPB Section 1033, GLBA, and FFIEC guidelines.
url: https://glyue.docs.sandboxbanking.com/
tags:
  - API Integration
  - Banking
  - Core Banking
  - Credit Unions
  - Financial Services
  - Fintech
  - Integration Platform
  - iPaaS
  - Open Banking
created: '2024-12-25'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: sandbox-banking:glyue
    name: Glyue Integration Gateway API
    description: The Glyue Integration Gateway API provides programmatic access to the Sandbox Banking integration platform for building, managing, and monitoring banking integrations. The API supports creating and executing integration workflows, managing service request adapters, configuring field mappings, value mappings, validation rules, and accessing run history audit logs.
    humanURL: https://glyue.docs.sandboxbanking.com/
    baseURL: https://{tenant}.sandboxbanking.com/api
    tags:
      - Audit
      - Banking Integration
      - Core Banking
      - Field Mapping
      - Glyue
      - Integration
      - iPaaS
      - Workflow
    properties:
      - type: Documentation
        url: https://glyue.docs.sandboxbanking.com/
      - type: Documentation
        url: https://glyue.docs.sandboxbanking.com/reference/integration_anatomy
      - type: OpenAPI
        url: openapi/sandbox-banking-glyue-openapi.yml
  - aid: sandbox-banking:mockbank
    name: Mock Bank API
    description: The Mock Bank API provides a sandbox environment for testing and developing banking integrations without connecting to production core banking systems. It simulates standard banking operations including account management, transactions, and customer data in a controlled test environment.
    humanURL: https://mockbank.docs.sandboxbanking.com/
    tags:
      - Banking
      - Mock API
      - Sandbox
      - Testing
    properties:
      - type: Documentation
        url: https://mockbank.docs.sandboxbanking.com/reference/introduction
common:
  - type: Documentation
    url: https://glyue.docs.sandboxbanking.com/
    title: Glyue Integration Gateway Documentation
  - type: Documentation
    url: https://www.ncino.com/solutions/integrations
    title: nCino Integration Gateway
  - type: Documentation
    url: https://mockbank.docs.sandboxbanking.com/
    title: Mock Bank API Documentation
  - type: Website
    url: https://sandboxbanking.com/
    title: Sandbox Banking Website
  - type: SpectralRules
    url: rules/sandbox-banking-rules.yml
    title: Sandbox Banking API Spectral Rules
  - type: NaftikoCapability
    url: capabilities/banking-integration-management.yaml
    title: Sandbox Banking Integration Management Capability
  - type: JSONSchema
    url: json-schema/sandbox-banking-integration-schema.json
    title: Sandbox Banking Integration Schema
  - type: JSONStructure
    url: json-structure/sandbox-banking-integration-structure.json
    title: Sandbox Banking Integration Structure
  - type: JSONLDContext
    url: json-ld/sandbox-banking-context.jsonld
    title: Sandbox Banking JSON-LD Context
  - type: Example
    url: examples/sandbox-banking-list-integrations-example.json
    title: Sandbox Banking List Integrations Example
  - type: Example
    url: examples/sandbox-banking-run-integration-example.json
    title: Sandbox Banking Run Integration Example
  - type: Vocabulary
    url: vocabulary/sandbox-banking-vocabulary.yml
    title: Sandbox Banking Vocabulary
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
