---
aid: torii
url: https://raw.githubusercontent.com/api-evangelist/torii/refs/heads/main/apis.yml
apis:
  - aid: torii:torii
    name: Torii SaaS Management API
    tags:
      - Apps
      - Audit
      - Contracts
      - Files
      - Metadata
      - Parsings
      - SaaS Management
      - SCIM
      - Users
    humanURL: https://developers.toriihq.com/reference/introduction-1
    properties:
      - url: https://developers.toriihq.com/reference/introduction-1
        type: Documentation
      - url: https://www.toriihq.com/
        type: Website
      - url: openapi/torii-torii-openapi.yml
        type: OpenAPI
      - url: rules/torii-rules.yml
        type: SpectralRules
      - url: capabilities/shared/torii-saas-management.yaml
        type: NaftikoCapability
      - url: json-schema/app.json
        type: JSONSchema
      - url: json-schema/user.json
        type: JSONSchema
      - url: json-schema/contract.json
        type: JSONSchema
      - url: json-schema/audit-log-entry.json
        type: JSONSchema
      - url: json-schema/field-metadata.json
        type: JSONSchema
      - url: json-schema/parsing-request.json
        type: JSONSchema
      - url: json-schema/scim-user.json
        type: JSONSchema
      - url: json-ld/torii-context.jsonld
        type: JSONLD
    description: The Torii API provides programmatic access to the Torii SaaS Management Platform. It allows IT, Finance, and Security teams to manage apps, users, contracts, licenses, audit logs, and file uploads. Supports custom integration data sync, workflow execution monitoring, and SCIM 2.0 user provisioning. The API closely follows REST semantics, uses JSON to encode objects, cursor-based pagination, and relies on standard HTTP codes to signal operation outcomes. Authentication uses Bearer API keys generated in Torii Settings.
name: Torii
tags:
  - Apps
  - Compliance
  - Cost Optimization
  - Governance
  - IT Management
  - SaaS Management
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-07-15'
modified: '2026-05-03'
position: Consuming
description: Torii is the market leading SaaS Management Platform built to bring all your software into one place. Discover shadow IT, enforce governance, cut costs, and operationalize every app. Torii integrates with 180+ SaaS applications to provide license and usage data, automate user onboarding and offboarding workflows, manage SaaS contracts and renewals, and maintain compliance audit trails.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
common:
  - name: LinkedIn
    url: https://www.linkedin.com/company/toriihq/
    type: LinkedIn
  - name: Torii Website
    url: https://www.toriihq.com/
    type: Website
  - name: Torii Developer Documentation
    url: https://developers.toriihq.com
    type: Documentation
  - name: About Torii
    url: https://www.toriihq.com/about
    type: About
  - name: Integrations
    url: https://www.toriihq.com/integration/page/14
    type: Integrations
  - name: Pricing
    url: https://www.toriihq.com/pricing
    type: Pricing
  - name: Terms of Service
    url: https://www.toriihq.com/terms
    type: TermsOfService
  - name: Security
    url: https://www.toriihq.com/security
    type: PrivacyPolicy
  - name: Customers
    url: https://www.toriihq.com/customers
    type: Customers
  - name: Partners
    url: https://www.toriihq.com/partners
    type: Partners
  - name: Brand Guidelines
    url: https://www.toriihq.com/brand-guidelines
    type: Branding
  - name: Torii Login
    url: https://app.toriihq.com/login
    type: Login
  - name: Torii JSON-LD Context
    url: json-ld/torii-context.jsonld
    type: JSON-LD
    description: JSON-LD context for Torii SaaS Management domain vocabulary.
  - name: Torii App JSON Structure
    url: json-structure/torii-app-structure.json
    type: JSONStructure
    description: Structured documentation of the Torii App, User, Contract, and Audit objects.
  - name: Torii Spectral Rules
    url: rules/torii-rules.yml
    type: SpectralRules
    description: Spectral ruleset for Torii API conventions.
  - name: Torii SaaS Governance Capability
    url: capabilities/saas-governance.yaml
    type: NaftikoCapability
    description: Naftiko workflow capability for SaaS governance (REST + MCP, 14 tools).
  - name: Torii Vocabulary
    url: vocabulary/torii-vocabulary.yml
    type: Vocabulary
    description: Domain vocabulary for the Torii SaaS Management Platform.
  - name: Features
    type: Features
    data:
      - name: SaaS Management Platform
      - name: Shadow IT Discovery
      - name: App Lifecycle Management
      - name: License Optimization
      - name: Contract and Renewal Management
      - name: Workflow Automation
      - name: User Onboarding and Offboarding
      - name: SCIM 2.0 Provisioning
      - name: Compliance Audit Logs
      - name: Custom Integrations
      - name: Browser Extension
      - name: 180+ Native Integrations
  - name: Use Cases
    type: UseCases
    data:
      - name: Shadow IT Discovery
      - name: Onboarding and Offboarding Automation
      - name: SaaS Spend Management
      - name: SaaS Vendor and Renewal Management
      - name: Compliance and Governance
      - name: Open Platform Integration
      - name: AI Powered SaaS Management
  - name: Integrations
    type: Integrations
    data:
      - name: Okta
      - name: Microsoft Entra ID
      - name: Google Workspace
      - name: Slack
      - name: Salesforce
      - name: Jira Cloud
      - name: GitHub Enterprise
      - name: Azure DevOps
      - name: Zoom
      - name: Microsoft Teams
      - name: Datadog
      - name: ServiceNow
      - name: BambooHR
      - name: Workday HCM
      - name: Rippling
      - name: HubSpot
      - name: Zendesk
      - name: PagerDuty
      - name: Confluence
      - name: Notion
---
