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
    agent_skills: true
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 46.2
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: JSON REST API for authentication, users/KYC, balances, beneficiaries, collections, collection requests, conversions, currencies, deductions, funding, internal transfers, payments, and webhook notifica
  name: Wallex Partner API
  slug: wallex-partner-api
artifact_total: 6
asyncapis:
- description: ''
  name: Wallex Webhooks
  slug: wallex-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://wallex.asia
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.wallex.asia/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.wallex.asia/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.wallex.asia/docs/api/authentication/authenticate
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.wallex.asia/docs/send-first-payment
- group: operate
  title: ''
  type: Support
  url: https://help.wallex.asia/
- group: auth
  title: ''
  type: Authentication
  url: authentication/wallex-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wallex-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/wallex-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wallex-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wallex-conformance.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wallex-rate-limits.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/wallex-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/wallex-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/wallex-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/wallex-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wallex-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wallex-llms.txt
created: '2026-07-17'
description: Wallex is a Singapore-headquartered cross-border payments and business banking platform for businesses across Southeast Asia and Greater China. Its Partner API is a JSON REST API that lets platforms embed multi-currency wallets, issue virtual collection accounts, run FX conversions, send cross-border payments to beneficiaries, and onboard and KYC their own members. The API is organised around a hierarchical account model (Standard and Partner accounts, Individual and Company entities, Regular and Lite KYC) and covers authentication, balances, beneficiaries, collections, collection requests, conversions, currencies, deductions, funding, internal transfers, payments, users, and webhooks. Wallex is a portfolio company of 500 Global.
image: https://docs.wallex.asia/img/wallex-icon.png
layout: provider
mcp_servers:
- description: ''
  name: wallex-mcp.yml
  slug: wallex-mcpyml
modified: '2026-07-21'
name: Wallex
nav: Providers
network: true
overview: 'Wallex publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Cross-Border Payments, Foreign Exchange, and Fintech.


  The Wallex catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Wallex''s developer surface includes documentation, API reference, getting-started guide, support, authentication, sandbox, and 13 more developer resources.'
random_paper: 41
rate_limits:
- limit_count: 0
  name: Wallex Rate Limits
  slug: wallex-rate-limits
score:
  band: thin
  composite: 31.3
  delta: 1.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 22.6
    developer_ergonomics: 71.7
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 30.3
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 37.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Wallex Authentication
  slug: wallex-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Wallex Domain Security
  slug: wallex-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: wallex
tags:
- Company
- Payments
- Cross-Border Payments
- Foreign Exchange
- Fintech
- Collections
- B2B Payments
- Embedded Finance
- Southeast Asia
website: https://wallex.asia
---
