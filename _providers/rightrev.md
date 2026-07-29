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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.3
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: RightRev's REST (and GraphQL) API for revenue recognition — transaction ingestion (orders, invoices, events, bulk uploads), policy-set and company configuration, Revenue Desk 360 contract search and d
  name: RightRev REST API
  slug: rightrev-rest-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://rightrev.com
- group: docs
  title: ''
  type: Documentation
  url: https://apis.rightrev.com/
- group: docs
  title: ''
  type: APIReference
  url: https://apis.rightrev.com/rightrev-rest-api.md
- group: start
  title: ''
  type: GettingStarted
  url: https://apis.rightrev.com/getting-started.md
- group: operate
  title: ''
  type: Support
  url: https://www.rightrev.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rightrev.com/terms-of-use/
- group: auth
  title: ''
  type: Authentication
  url: authentication/rightrev-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/rightrev-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rightrev-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/rightrev-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rightrev-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rightrev-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/rightrev-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/rightrev-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rightrev-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rightrev-domain-security.yml
created: '2026-07-17'
description: RightRev is an AI-powered revenue recognition platform that automates ASC 606 and IFRS 15 compliant accounting for subscription, usage-based, and hybrid revenue models. Its API-first architecture ingests orders, invoices, and usage events, applies configurable Standalone Selling Price (SSP) and revenue policies, and produces revenue contracts, revenue and cost schedules, journal entries, and period-close outputs. RightRev exposes REST and GraphQL APIs secured with OAuth 2.0 / OpenID Connect, alongside a Salesforce-native application and ERP integrations for finance teams.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rightrev.png
layout: provider
mcp_servers:
- description: ''
  name: rightrev-mcp.yml
  slug: rightrev-mcpyml
modified: '2026-07-21'
name: Rightrev
nav: Providers
network: true
overview: 'Rightrev publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Revenue Recognition, Accounting, Finance, and Billing.


  Rightrev''s developer surface includes documentation, API reference, getting-started guide, support, authentication, and 11 more developer resources.'
random_paper: 28
scopes:
- name: Rightrev Scopes
  scope_count: 2
  slug: rightrev-scopes
  summary_line: 2 scopes
score:
  band: emerging
  composite: 19.9
  delta: -1.5
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 43.5
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 21.4
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Rightrev Authentication
  slug: rightrev-authentication
  summary_line: oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Rightrev Domain Security
  slug: rightrev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rightrev
tags:
- Company
- Revenue Recognition
- Accounting
- Finance
- Billing
- ASC 606
- IFRS 15
- Revenue
- SaaS Metrics
website: https://rightrev.com
---
