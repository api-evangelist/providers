---
aid: apishare
url: https://raw.githubusercontent.com/api-evangelist/apishare/refs/heads/main/apis.yml
name: ApiShare
tags:
  - API Governance
  - API Lifecycle
  - API Management
  - Catalog
  - Governance
  - Internal Developer Platform
  - Platform
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-01-08'
modified: '2026-04-19'
position: Consumer
description: ApiShare is an API governance platform that provides a unified operational model for API lifecycle management, access control, catalog management, and asset reuse across organizations. It operates as a native component of an Internal Developer Platform, enabling self-service, standardized, and secure API governance without replacing existing systems.
apis:
  - aid: apishare:apishare
    name: ApiShare
    tags:
      - API Governance
      - API Lifecycle
      - Catalog
      - Governance
      - Internal Developer Platform
    humanURL: https://www.apishare.cloud/
    properties:
      - url: https://www.apishare.cloud/documentation-1.12
        type: Documentation
      - url: https://www.apishare.cloud/documentation-1.12
        type: GettingStarted
      - url: https://www.apishare.cloud/pricing
        type: Pricing
    description: ApiShare provides a unified catalog of APIs, applications, assets, MCP servers, and AI agents with role-based visibility, configurable lifecycle workflows, subscription management, and built-in auditability. It integrates with API gateways (Boomi, Red Hat 3scale, Azure, Kong) and identity providers (Azure Entra ID, KeyCloak, Oracle Access Management) without replacing existing systems.
common:
  - type: Documentation
    url: https://www.apishare.cloud/documentation-1.12
  - type: Pricing
    url: https://www.apishare.cloud/pricing
  - type: Blog
    url: https://www.apishare.cloud/blog
  - type: ReleaseNotes
    url: https://www.apishare.cloud/release-note
  - type: Contact
    url: https://www.apishare.cloud/contacts
  - type: Features
    data:
      - name: Unified API Catalog
        description: Active catalog of APIs, applications, assets, MCP servers, and AI agents with role-based visibility.
      - name: Lifecycle Management
        description: Full digital product lifecycle governance from design through retirement with version control.
      - name: Workflow Orchestration
        description: Configurable workflows for product lifecycle, usage approvals, and ownership management.
      - name: Subscription Management
        description: Structured request approval workflows with automated keyset management, key rotation, grace periods, and revocation.
      - name: Access Control
        description: Role-based permissions and catalog visibility controls defining who can view digital products.
      - name: Traceability and Audit
        description: Built-in auditability and evidence collection by design.
      - name: AI-Ready Architecture
        description: Exposes digital products in governed, structured format for AI agent consumption.
      - name: Live API Testing
        description: Interactive API testing directly from the portal with live documentation.
      - name: AI-Powered Agent Design Expert
        description: AI-powered assistant for creating OpenAPI specifications.
      - name: Public Marketplace Showcase
        description: Public API discovery and showcase functionality for external consumers.
  - type: UseCases
    data:
      - name: API Governance at Scale
        description: Enforce API policies, track lifecycle changes, and ensure compliance without slowing down development teams.
      - name: Internal Developer Platform Integration
        description: Operate as a native governance component within an existing Internal Developer Platform.
      - name: AI Agent Governance
        description: Apply governance to non-human users including AI agents consuming APIs and MCP servers.
      - name: Multi-Domain Governance
        description: Govern APIs and digital products across multiple organizational domains with consistent policies.
      - name: API Access Management
        description: Manage consumer subscriptions, approvals, and keyset lifecycle for API access control.
  - type: Integrations
    data:
      - name: Boomi API Management
        description: Connector for governing APIs managed through the Boomi API Management gateway.
      - name: Red Hat 3scale
        description: Connector for governing APIs managed through the Red Hat 3scale API gateway.
      - name: Microsoft Azure API Management
        description: Integration with Microsoft Azure API Gateway for unified governance.
      - name: Kong
        description: Connector for governing APIs managed through the Kong API gateway.
      - name: Microsoft Azure Entra ID
        description: Identity provider integration for authentication and authorization.
      - name: KeyCloak
        description: Open-source identity provider integration for authentication.
      - name: Oracle Access Management
        description: Enterprise identity provider integration for access management.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
specificationVersion: '0.19'
---
