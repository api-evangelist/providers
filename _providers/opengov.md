---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 66.0
  scored_at: '2026-08-06'
api_count: 10
apis:
- description: 'The Permitting & Licensing (PLC) public API v2 provides programmatic access to permitting, licensing and code enforcement workflows for a community: records, record types, workflow steps (approval, do'
  name: OpenGov Permitting & Licensing API v2
  slug: permitting-licensing-v2
- description: The v1 Permitting, Licensing & Code Enforcement API covering records, record form fields, record contacts, record locations, workflow steps and step comments. Superseded by v2 for new integrations.
  name: OpenGov Permitting & Licensing API v1
  slug: permitting-licensing-v1
- description: The Budgeting & Performance API exposes budget data and the chart of accounts for an OpenGov budgeting entity, authenticated with an X-API-KEY header key generated in the product Control Panel or a be
  name: OpenGov Budgeting & Performance API
  slug: budgeting-performance
- description: The Procurement & Contract Management API v2 covers contracts, contract categories, tags and procurement datasets for an OpenGov procurement entity.
  name: OpenGov Procurement & Contract Management API v2
  slug: procurement-v2
- description: The v1 Procurement & Contract Management API covering contracts, categories, tags and datasets. Superseded by v2.
  name: OpenGov Procurement & Contract Management API v1
  slug: procurement-v1
- description: 'The Purchase Order API is the largest surface in the OpenGov catalog: purchase orders and purchase order types, line items, change orders, terms and terms attachments, comments, attachments and attach'
  name: OpenGov Purchase Order API
  slug: purchase-order
- description: The Receipt API manages goods and services receipts against purchase orders, including receipt attachments, comments, activity and surface versions.
  name: OpenGov Receipt API
  slug: receipt
- description: The Vendor Management API manages the vendor lifecycle end to end — vendor CRUD, search and export, submission and promotion workflows, taskmaster approval actions, contacts, addresses, payment method
  name: OpenGov Vendor Management API
  slug: vendor-management
- description: 'The Enterprise Asset Management (EAM, formerly Cartegraph) REST API provides generic business-object CRUD over classes (assets, work orders, requests, resources), class metadata and layouts, targeted '
  name: OpenGov Enterprise Asset Management API
  slug: enterprise-asset-management
- description: OpenGov Open Data portals expose the CKAN Action API (v2.9) at /api/3/action — package, resource, organization, group, tag and system actions for publishing and querying open government datasets. Each
  name: OpenGov Open Data CKAN Action API
  slug: open-data
artifact_total: 18
asyncapis:
- description: ''
  name: Opengov Permitting Licensing Webhooks
  slug: opengov-permitting-licensing-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/opengov-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opengov-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/opengov-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://opengov.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.opengov.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.opengov.com/docs/overview
- group: docs
  title: ''
  type: APIReference
  url: https://developer.opengov.com/catalog
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.opengov.com/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://support.opengov.com
- group: company
  title: ''
  type: Blog
  url: https://opengov.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/opengov
- group: start
  title: ''
  type: SignUp
  url: https://developer.opengov.com/applications
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.opengov.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://opengov.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.opengov.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.opengov.com/
- group: auth
  title: ''
  type: Security
  url: https://opengov.com/security/
- group: start
  title: ''
  type: Sandbox
  url: sandbox/opengov-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/opengov-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/opengov-permitting-licensing-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/opengov-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/opengov-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/opengov-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/opengov-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/opengov-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/opengov-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/opengov-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/opengov-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/opengov-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/opengov-conventions.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/opengov-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/opengov-scopes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/opengov-rate-limits.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/opengov-openid-configuration.json
created: '2026-08-04'
description: OpenGov builds cloud enterprise resource planning and public service software for state and local government, serving more than 2,000 communities across budgeting and performance, financial management, procurement and contract management, vendor management, permitting and licensing, enterprise asset management, tax and revenue, utility billing, grants management, 311 request management and open data. The OpenGov Public Service Platform exposes a public developer portal at developer.opengov.com with a catalog of ten OpenAPI 3.x definitions covering roughly 358 operations, an integration/app model with scoped permissions and per-integration API keys, a JSON:API-shaped Permitting & Licensing API, a webhook event catalog of 31 Permitting & Licensing events, SCIM 2.0 identity provisioning, and an in-browser API test console.
image: https://opengov.com/wp-content/uploads/2025/02/opengov-2025.svg
layout: provider
mcp_servers:
- description: ''
  name: opengov-mcp.yml
  slug: opengov-mcpyml
modified: '2026-08-04'
name: OpenGov
nav: Providers
network: true
overview: 'OpenGov publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Permitting & Licensing API v2, Permitting & Licensing API v1, Budgeting & Performance API, and 7 more. Tagged areas include Government, GovTech, Public Sector, Permitting, and Licensing.


  The OpenGov catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  OpenGov''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 28 more developer resources.'
random_paper: 88
rate_limits:
- limit_count: 0
  name: Opengov Rate Limits
  slug: opengov-rate-limits
scopes:
- name: Opengov Scopes
  scope_count: 0
  slug: opengov-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 60.9
  delta: -2.1
  facets:
    commercial_clarity: 50.0
    contract_quality: 68.7
    developer_ergonomics: 62.5
    discoverability: 83.3
    governance: 11.5
    operational_transparency: 55.3
  previous_composite: 63.0
  provenance:
    conformance: derived
    contracts:
      callable: 90.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 85.2
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Opengov Authentication
  slug: opengov-authentication
  summary_line: apiKey/http/openIdConnect · 6 schemes
- kind: domain-security
  name: Opengov Domain Security
  slug: opengov-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Opengov Vulnerability Disclosure
  slug: opengov-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Opengov Trust Center
  slug: opengov-trust-center
  summary_line: SOC 2 Type 2, SOC 3, TX-RAMP, AZ RAMP, GovRAMP, GDPR, CCPA, CPRA, VPAT
slug: opengov
tags:
- Government
- GovTech
- Public Sector
- Permitting
- Licensing
- Procurement
- Budgeting
- Asset Management
- Vendor Management
- Open Data
- ERP
- Local Government
website: https://opengov.com
---
