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
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: REST and SOAP object API (v1) for reading and writing Impartner platform records (accounts, partners, deals, and tenant-defined custom objects) using the THQL query language with skip/take paging, fie
  name: Impartner Objects API
  slug: impartner-objects-api
artifact_total: 6
asyncapis:
- description: ''
  name: Impartner Webhooks
  slug: impartner-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.impartner.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.impartner.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.impartner.com
- group: docs
  title: ''
  type: APIReference
  url: https://prod.impartner.live/swagger/ui/index
- group: start
  title: ''
  type: Login
  url: https://login.impartner.com
- group: commercial
  title: ''
  type: Pricing
  url: https://impartner.com/request-prm-pricing/
- group: company
  title: ''
  type: Blog
  url: https://impartner.com/blog
- group: operate
  title: ''
  type: Support
  url: https://impartner.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://impartner.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.impartner.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/impartner-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/impartner-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/impartner-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/impartner-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/impartner-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/impartner-cli.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/impartner-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/impartner-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/impartner-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/impartner-webhooks.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/impartner-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/impartner-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/impartner-llms.txt
created: '2026-07-17'
description: Impartner is a SaaS-based Partner Relationship Management (PRM) and partner revenue orchestration platform, founded in 1997 and headquartered in South Jordan, Utah, and backed by Emergence Capital. It helps enterprises manage the full indirect-channel lifecycle - partner recruitment, onboarding, deal registration, co-selling, through-channel marketing automation (TCMA), and performance measurement - from a single connected system. For developers and integrators, Impartner exposes an Objects API (version 1) over both REST and SOAP, queried with THQL (The Impartner Query Language), secured by an Auth0-based OAuth2 / OpenID Connect identity layer plus per-tenant API keys, and extended through workflow-engine webhooks and a family of first-party @impartner npm packages, design system, and CLI for building applications on Impartner Orchestration Studio.
image: https://impartner.com/wp-content/uploads/2023/01/impartner-logo.png
layout: provider
mcp_servers:
- description: ''
  name: impartner-mcp.yml
  slug: impartner-mcpyml
modified: '2026-07-19'
name: Impartner
nav: Providers
network: true
overview: 'Impartner publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, SaaS, Partner Relationship Management, PRM, and Channel Management.


  The Impartner catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Impartner''s developer surface includes documentation, API reference, pricing, engineering blog, support, authentication, CLI, and 16 more developer resources.'
random_paper: 30
scopes:
- name: Impartner Scopes
  scope_count: 14
  slug: impartner-scopes
  summary_line: 14 scopes
score:
  band: developing
  composite: 44.3
  delta: 6.9
  facets:
    commercial_clarity: 34.2
    contract_quality: 51.6
    developer_ergonomics: 56.5
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 23.7
  previous_composite: 37.4
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/impartner/refs/heads/main/screenshots/impartner-2026-07-25T222146.png
security:
- kind: authentication
  name: Impartner Authentication
  slug: impartner-authentication
  summary_line: oauth2/openIdConnect/apiKey · 3 schemes
- kind: domain-security
  name: Impartner Domain Security
  slug: impartner-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: impartner
tags:
- Company
- SaaS
- Partner Relationship Management
- PRM
- Channel Management
- Partner Ecosystem
- Through-Channel Marketing
- Sales
- CRM
website: https://www.impartner.com
---
