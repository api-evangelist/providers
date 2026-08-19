---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.2
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: 'REST API for Perk travel, expense, invoice, trip, cost-center, event, and card data. Authenticate with an account API key (customers) or OAuth 2.0 (partners); send Api-Version: 1.'
  name: Perk Travel & Spend API
  slug: perk-travel-spend-api
- description: SCIM 2.0 user-provisioning API for creating, updating, and deactivating Perk users from identity providers (Okta, Microsoft Entra ID), including an expense extension schema.
  name: Perk SCIM API
  slug: perk-scim-api
artifact_total: 8
asyncapis:
- description: ''
  name: Perk Webhooks
  slug: perk-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.perk.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.perk.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developers.perk.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.perk.com/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://support.perk.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.perk.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.perk.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.perk.com/docs/travelperk-marketplace-and-api-terms-of-use
- group: build
  title: ''
  type: Postman
  url: https://app.getpostman.com/run-collection/26205026-08341f0b-356a-460b-b386-54f8c30b9bad
- group: operate
  title: ''
  type: StatusPage
  url: https://status.perk.com
- group: agent
  title: ''
  type: MCPServer
  url: mcp/perk-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/perk-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/perk-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/perk-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/perk-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/perk-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/perk-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/perk-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/perk-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/perk-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/perk-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/perk-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/perk-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/perk-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/perk-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/perk-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/perk-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/perk-vulnerability-disclosure.yml
created: '2026-07-17'
description: Perk (formerly TravelPerk) is the intelligent platform for corporate travel and spend management, combining travel booking with expense, invoice, and card controls for finance teams. Founded in Barcelona in 2015, Perk serves thousands of global teams and is backed by General Catalyst, SoftBank Vision Fund, Speedinvest and others. Its developer platform exposes a Travel & Spend REST API, a SCIM 2.0 user-provisioning API, webhooks, a sandbox, a public Postman collection, and an official hosted Model Context Protocol (MCP) server for AI clients.
image: https://d2balr5nj4353r.cloudfront.net/favicon-192x192.png
layout: provider
mcp_servers:
- description: ''
  name: perk-mcp.yml
  slug: perk-mcpyml
modified: '2026-07-20'
name: Perk
nav: Providers
network: true
overview: 'Perk publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Corporate Travel, Expense Management, Spend Management, and Travel.


  The Perk catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Perk''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, authentication, and 22 more developer resources.'
random_paper: 136
scopes:
- name: Perk Scopes
  scope_count: 0
  slug: perk-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 44.2
  delta: -6.4
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 45.1
    developer_ergonomics: 49.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 57.9
  previous_composite: 50.6
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/perk/refs/heads/main/screenshots/perk-2026-08-17T081158.png
security:
- kind: authentication
  name: Perk Authentication
  slug: perk-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Perk Domain Security
  slug: perk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Perk Vulnerability Disclosure
  slug: perk-vulnerability-disclosure
  summary_line: Intigriti · security.txt · contact published
slug: perk
tags:
- Company
- Corporate Travel
- Expense Management
- Spend Management
- Travel
- Invoices
- Fintech
- SaaS
website: https://developers.perk.com
---
