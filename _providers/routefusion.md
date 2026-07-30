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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 41.7
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'Routefusion''s global payments GraphQL API: users, entities, wallets, virtual accounts, beneficiaries, transfers, quotes/rates, incoming transfers, and webhooks for cross-border payouts over SWIFT, loc'
  name: Routefusion GraphQL API
  slug: routefusion-graphql-api
artifact_total: 5
asyncapis:
- description: ''
  name: Routefusion Webhooks
  slug: routefusion-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://routefusion.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.routefusion.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.routefusion.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.routefusion.com/reference/getting-started-with-your-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.routefusion.com/docs/send-your-first-payment-v2
- group: company
  title: ''
  type: Blog
  url: https://routefusion.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/routefusion
- group: operate
  title: ''
  type: StatusPage
  url: https://status.routefusion.com
- group: operate
  title: ''
  type: Support
  url: https://routefusion.com/contact
- group: start
  title: ''
  type: Login
  url: https://accounts.routefusion.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://routefusion.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://routefusion.com/legal/privacy
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/2597780/TzCV3Q8u
- group: build
  title: ''
  type: SDKs
  url: packages/routefusion-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/routefusion-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/routefusion-webhooks.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/routefusion-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/routefusion-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/routefusion-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/routefusion-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/routefusion-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/routefusion-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/routefusion-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/routefusion-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/routefusion-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/routefusion-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/routefusion-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/routefusion-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Routefusion is a global payments infrastructure platform that lets platforms, fintechs, and marketplaces move money across borders through a single GraphQL API. It supports payouts to 180+ countries over SWIFT, local rails, and stablecoin (USDC), non-resident and FDIC/virtual accounts in multiple currencies, multi-currency wallets, FX rate locking and quotes, beneficiary and entity onboarding with compliance review, incoming-transfer reconciliation, and Ed25519-signed webhooks. The API is GraphQL over HTTPS with bearer-token authentication and a full sandbox environment. This profile was added to the API Evangelist network as a portfolio company of Initialized Capital and enriched from Routefusion's public developer documentation.
image: https://routefusion.com/images/routefusion-logo.png
layout: provider
mcp_servers:
- description: ''
  name: routefusion-mcp.yml
  slug: routefusion-mcpyml
modified: '2026-07-21'
name: Routefusion
nav: Providers
network: true
overview: 'Routefusion publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Payments, Cross-Border Payments, and Global Payments.


  The Routefusion catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Routefusion''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, sandbox, and 22 more developer resources.'
random_paper: 71
score:
  band: developing
  composite: 46.9
  delta: 1.8
  facets:
    commercial_clarity: 34.2
    contract_quality: 51.6
    developer_ergonomics: 73.4
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 36.8
  previous_composite: 45.1
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Routefusion Authentication
  slug: routefusion-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Routefusion Domain Security
  slug: routefusion-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: routefusion
tags:
- Company
- Fintech
- Payments
- Cross-Border Payments
- Global Payments
- FX
- Wallets
- GraphQL
- Stablecoin
website: https://routefusion.com/
---
