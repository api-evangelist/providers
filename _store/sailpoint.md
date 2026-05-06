---
aid: sailpoint
name: SailPoint
description: Enterprise identity security and governance platform providing identity management, access governance, and compliance solutions for workforce and non-employee identities. SailPoint delivers cloud-native IAM, certification automation, role mining, AI-driven recommendations, and developer-friendly APIs for integrating identity into any workflow.
type: Index
x-type: company
position: Consumer
access: 3rd-Party
image: https://www.sailpoint.com/wp-content/uploads/2021/02/sailpoint-logo.svg
tags:
  - Access Governance
  - Compliance
  - IAM
  - Identity Management
  - Identity Security
  - Security
created: '2025-02-17'
modified: '2026-05-02'
url: https://raw.githubusercontent.com/api-evangelist/sailpoint/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: sailpoint:sailpoint
    name: SailPoint
    description: The SailPoint Developer Forums are a great place to find solutions to common development problems.
    humanURL: ' https://developer.sailpoint.com/'
    tags: []
    properties:
      - type: Documentation
        url: ' https://developer.sailpoint.com/'
  - aid: sailpoint:identity-security-cloud-v3-api
    name: SailPoint Identity Security Cloud V3 API
    description: The V3 APIs provide core endpoints to interact with the SailPoint Identity Security Cloud platform, covering access profiles, certifications, identities, roles, search, sources, transforms, workflows, and more.
    humanURL: https://developer.sailpoint.com/docs/api/v3/
    tags:
      - Access Governance
      - IAM
      - Identity Security
    properties:
      - type: Documentation
        url: https://developer.sailpoint.com/docs/api/v3/
      - type: OpenAPI
        url: https://developer.sailpoint.com/docs/api/v3/identity-security-cloud-v-3-api/
      - type: OpenAPI
        url: openapi/identity-security-cloud-v3.yml
      - type: JSONSchema
        url: json-schema/sailpoint-identity-schema.json
      - type: JSONLD
        url: json-ld/sailpoint-context.jsonld
      - type: SpectralRules
        url: rules/sailpoint-rules.yml
      - type: Capabilities
        url: capabilities/identity-governance.yaml
      - type: Vocabulary
        url: vocabulary/sailpoint-vocabulary.yml
  - aid: sailpoint:identity-security-cloud-v2024-api
    name: SailPoint Identity Security Cloud V2024 API
    description: The V2024 APIs provide annual-release endpoints to interact with the Identity Security Cloud platform, including advanced features like machine identities, connector customizers, IAI recommendations, role mining, and multi-host integration.
    humanURL: https://developer.sailpoint.com/docs/api/v2024/
    tags:
      - Access Governance
      - IAM
      - Identity Security
    properties:
      - type: Documentation
        url: https://developer.sailpoint.com/docs/api/v2024/
      - type: OpenAPI
        url: https://developer.sailpoint.com/docs/api/v2024/identity-security-cloud-v-2024-api/
  - aid: sailpoint:identity-security-cloud-v2025-api
    name: SailPoint Identity Security Cloud V2025 API
    description: The V2025 APIs are the latest annual-release endpoints for the Identity Security Cloud platform, introducing new capabilities such as data access security, role propagation, and transitioning key APIs from experimental to public production status.
    humanURL: https://developer.sailpoint.com/docs/api/v2025/
    tags:
      - Access Governance
      - IAM
      - Identity Security
    properties:
      - type: Documentation
        url: https://developer.sailpoint.com/docs/api/v2025/
      - type: OpenAPI
        url: https://developer.sailpoint.com/docs/api/v2025/identity-security-cloud-v-2025-api/
  - aid: sailpoint:identity-security-cloud-beta-api
    name: SailPoint Identity Security Cloud Beta API
    description: The Beta APIs provide early access to new and experimental endpoints for the Identity Security Cloud platform, including triggers, notifications, custom forms, identity history, entitlements, and AI-driven recommendations.
    humanURL: https://developer.sailpoint.com/docs/api/beta/
    tags:
      - Beta
      - Identity Security
    properties:
      - type: Documentation
        url: https://developer.sailpoint.com/docs/api/beta/
      - type: OpenAPI
        url: https://developer.sailpoint.com/docs/api/beta/identity-security-cloud-beta-api/
  - aid: sailpoint:identityiq-scim-api
    name: SailPoint IdentityIQ SCIM API
    description: The IdentityIQ SCIM API provides RESTful SCIM 2.0 endpoints for SailPoint's on-premise IdentityIQ service, covering accounts, users, roles, entitlements, applications, workflows, policy violations, and task results.
    humanURL: https://developer.sailpoint.com/docs/api/iiq/
    tags:
      - Identity Governance
      - On-Premise
      - SCIM
    properties:
      - type: Documentation
        url: https://developer.sailpoint.com/docs/api/iiq/
      - type: OpenAPI
        url: https://developer.sailpoint.com/docs/api/iiq/identityiq-scim-rest-api/
  - aid: sailpoint:nerm-v1-api
    name: SailPoint Non-Employee Risk Management V1 API
    description: The NERM V1 API provides endpoints for managing non-employee lifecycle, profiles, risk levels, risk scores, workflows, delegations, forms, roles, and user management within the Non-Employee Risk Management platform.
    humanURL: https://developer.sailpoint.com/docs/api/nerm/v1/
    tags:
      - Identity Security
      - Non-Employee
      - Risk Management
    properties:
      - type: Documentation
        url: https://developer.sailpoint.com/docs/api/nerm/v1/
  - aid: sailpoint:nerm-v2025-api
    name: SailPoint Non-Employee Risk Management V2025 API
    description: The NERM V2025 API provides the latest annual-release endpoints for the Non-Employee Risk Management platform, supporting application integrations and programmatic management of non-employee profiles and delegations.
    humanURL: https://developer.sailpoint.com/docs/api/nerm/v2025/
    tags:
      - Identity Security
      - Non-Employee
      - Risk Management
    properties:
      - type: Documentation
        url: https://developer.sailpoint.com/docs/api/nerm/v2025/
  - aid: sailpoint:identity-security-cloud-v2026-api
    name: SailPoint Identity Security Cloud V2026 API
    description: The V2026 APIs provide experimental annual-release endpoints for the Identity Security Cloud platform, introducing upcoming capabilities such as account deletion requests, entitlement management, human and machine account deletion approval configuration, machine subtype approval configuration, and task management.
    humanURL: https://developer.sailpoint.com/docs/api/v2026/
    tags:
      - Access Governance
      - Experimental
      - IAM
      - Identity Security
    properties:
      - type: Documentation
        url: https://developer.sailpoint.com/docs/api/v2026/
      - type: OpenAPI
        url: https://developer.sailpoint.com/docs/api/v2026/identity-security-cloud-v-2026-api/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
  - name: SailPoint Technologies
    email: developer@sailpoint.com
    url: https://developer.sailpoint.com
common:
  - url: https://developer.sailpoint.com
    type: Developer Portal
  - url: https://developer.sailpoint.com/idn/api/getting-started
    type: Getting Started
  - url: https://developer.sailpoint.com/idn/tools/sdk
    type: SDKs
  - url: https://developer.sailpoint.com/discuss
    type: Community
  - url: https://www.sailpoint.com/blog
    type: Blog
  - url: https://www.sailpoint.com/support
    type: Support
  - url: https://status.sailpoint.com
    type: Status Page
  - url: https://www.sailpoint.com/legal/terms-of-use
    type: Terms of Service
  - url: https://www.sailpoint.com/legal/privacy
    type: Privacy Policy
  - url: https://developer.sailpoint.com/docs/api/authentication/
    type: Authentication
  - url: https://developer.sailpoint.com/docs/api/postman-collections/
    type: Postman Collection
  - url: https://developer.sailpoint.com/docs/api/getting-started/
    type: GettingStarted
  - url: https://developer.sailpoint.com/docs/api/api-versioning-strategy/
    type: API Versioning
  - url: https://github.com/sailpoint-oss/api-specs
    type: OpenAPI Source
  - url: https://github.com/sailpoint-oss
    type: GitHub Organization
  - url: https://developer.sailpoint.com/docs/tools/sdk/python/
    type: Python SDK
  - url: https://developer.sailpoint.com/docs/tools/sdk/typescript/
    type: TypeScript SDK
  - url: https://developer.sailpoint.com/docs/tools/sdk/go/
    type: Go SDK
  - url: https://developer.sailpoint.com/docs/tools/sdk/powershell/
    type: PowerShell SDK
  - url: https://developer.sailpoint.com/docs/tools/cli/
    type: CLI
  - url: https://developer.sailpoint.com/docs/extensibility/event-triggers/
    type: Event Triggers
  - url: https://developer.sailpoint.com/docs/extensibility/transforms/
    type: Transforms
  - url: https://developer.sailpoint.com/docs/extensibility/rules/
    type: Rules
  - url: https://developer.sailpoint.com/docs/connectivity/saas-connectivity/
    type: SaaS Connectivity
  - url: https://developer.sailpoint.com/blog/
    type: Developer Blog
  - url: https://developer.sailpoint.com/discuss/c/announcements/product-news/65
    type: Product News
  - url: https://documentation.sailpoint.com/
    type: Product Documentation
  - url: https://community.sailpoint.com
    type: Compass Community
  - url: https://www.postman.com/sailpoint
    type: Postman Workspace
  - url: https://developer.sailpoint.com/discuss/c/colab/59
    type: CoLab
  - url: https://sailpoint-oss.github.io/sailpoint-api-guidelines/
    type: API Guidelines
  - url: https://developer.sailpoint.com/docs/tools/
    type: Tools
  - url: https://developer.sailpoint.com/docs/tools/rule-development-kit/
    type: Rule Development Kit
  - url: https://developer.sailpoint.com/docs/tools/ui-development-kit/
    type: UI Development Kit
  - url: https://developer.sailpoint.com/docs/extensibility/
    type: Extensibility
  - url: https://developer.sailpoint.com/docs/extensibility/mcp-getting-started/
    type: MCP Server
  - url: https://developer.sailpoint.com/docs/extensibility/configuration-management/
    type: Configuration Management
  - url: https://developer.sailpoint.com/docs/connectivity/
    type: Connectivity
  - url: https://developer.sailpoint.com/docs/guides/
    type: Guides
  - url: https://developer.sailpoint.com/docs/extensibility/rules/java-docs/
    type: Java Docs
  - url: https://developer.sailpoint.com/docs/
    type: Identity Security Cloud Documentation
---
