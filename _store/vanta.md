---
aid: vanta
url: https://raw.githubusercontent.com/api-evangelist/vanta/refs/heads/main/apis.yml
name: Vanta
tags:
  - Cybersecurity
  - Compliance
  - Security
  - Governance
  - Risk Management
type: company
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-11-14'
modified: '2026-05-03'
description: Vanta is a trust management platform that automates security compliance for frameworks including SOC 2, ISO 27001, HIPAA, PCI DSS, and GDPR. The Vanta API enables organizations to programmatically manage their compliance posture, automate security monitoring, manage vulnerabilities, track controls, manage vendors, and integrate with existing tools and workflows.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
apis:
  - aid: vanta:vanta-api
    name: Vanta API
    tags:
      - Cybersecurity
      - Compliance
      - Security
      - Governance
      - Risk Management
    humanURL: https://developer.vanta.com/docs/vanta-api-overview
    baseURL: https://api.vanta.com
    properties:
      - url: https://developer.vanta.com/docs/vanta-api-overview
        type: Documentation
      - url: https://developer.vanta.com/docs/api-access-setup
        type: Authentication
      - url: https://developer.vanta.com/docs/faq
        type: FAQ
      - url: https://raw.githubusercontent.com/api-evangelist/vanta/refs/heads/main/openapi/vanta-openapi.yml
        type: OpenAPI
    description: The Vanta REST API enables programmatic access to compliance, security monitoring, vulnerability management, personnel management, vendor management, and custom integration capabilities. The API uses OAuth 2.0 authentication and returns JSON responses. Rate limits range from 5 to 250 requests per minute depending on endpoint category.
  - aid: vanta:vanta-auditor-api
    name: Vanta Auditor API
    tags:
      - Cybersecurity
      - Compliance
      - Audit
      - Security
    humanURL: https://developer.vanta.com/docs/vanta-api-overview
    baseURL: https://api.vanta.com
    properties:
      - url: https://developer.vanta.com/docs/vanta-api-overview
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/vanta/refs/heads/main/openapi/vanta-auditor-openapi.yml
        type: OpenAPI
    description: The Vanta Auditor API provides external audit firms programmatic access to customer compliance data. Auditors can query audits, vendors, monitored computers, people, vulnerabilities, evidence, controls, and comments during audit engagements.
common:
  - name: Developer Portal
    url: https://developer.vanta.com/docs/vanta-api-overview
    type: Portal
  - name: Authentication Guide
    url: https://developer.vanta.com/docs/api-access-setup
    type: Authentication
  - name: Getting Started
    url: https://developer.vanta.com/docs/vanta-first-api-request
    type: GettingStarted
  - name: Postman Collection
    url: https://developer.vanta.com/docs/vanta-postman-setup
    type: PostmanCollection
  - name: FAQ
    url: https://developer.vanta.com/docs/faq
    type: FAQ
  - name: Build Integrations
    url: https://developer.vanta.com/docs/build-integrations
    type: Documentation
  - name: Manage Vendors
    url: https://developer.vanta.com/docs/manage-vendors
    type: Documentation
  - name: Connectors API Blog
    url: https://www.vanta.com/resources/introducing-vantas-connectors-api
    type: Blog
  - name: API Product Overview
    url: https://www.vanta.com/products/vanta-api
    type: Product
  - name: Auditor SDK TypeScript
    url: https://github.com/VantaInc/vanta-auditor-api-sdk-typescript
    type: SDK
  - name: Auditor SDK Java
    url: https://github.com/VantaInc/vanta-auditor-api-sdk-java
    type: SDK
  - name: MCP Server
    url: https://github.com/VantaInc/vanta-mcp-server
    type: SDK
  - name: ESLint Plugin
    url: https://github.com/VantaInc/eslint-plugin-vanta
    type: SDK
  - name: Control Set
    url: https://github.com/VantaInc/vanta-control-set
    type: Schema
  - name: GitHub Integration
    url: https://www.vanta.com/integrations/github
    type: Integration
  - name: April 2026 Updates
    url: https://www.vanta.com/resources/new-in-vanta-april-2026
    type: ChangeLog
  - name: OpenAPI Spec
    url: https://raw.githubusercontent.com/api-evangelist/vanta/refs/heads/main/openapi/vanta-openapi.yml
    type: OpenAPI
  - name: Auditor OpenAPI Spec
    url: https://raw.githubusercontent.com/api-evangelist/vanta/refs/heads/main/openapi/vanta-auditor-openapi.yml
    type: OpenAPI
---
