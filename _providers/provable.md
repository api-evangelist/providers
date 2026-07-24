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
    agent_skills: true
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 35.6
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: The Aurora Connect (Buf) API for the SEC-registered securities-finance ATS — authentication, company/instrument reference, order management (OMS), venue order book, contract requests, contract lifecyc
  name: Aurora API
  slug: aurora-api
artifact_total: 5
asyncapis:
- description: ''
  name: Provable Events Webhooks
  slug: provable-events-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/provable-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.provablemarkets.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.provablemarkets.com/workflows
- group: docs
  title: ''
  type: APIReference
  url: https://developer.provablemarkets.com/api/connectapi
- group: operate
  title: ''
  type: Support
  url: https://provablemarkets.com/contact
- group: company
  title: ''
  type: Blog
  url: https://provablemarkets.com/news-insights
- group: commercial
  title: ''
  type: TermsOfService
  url: https://provablemarkets.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://provablemarkets.com/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://provablemarkets.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/provable-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/provable-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/provable-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/provable-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/provable-events-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/provable-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/provable-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/provable-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/provable-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/provable-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Provable Markets is a New York and Amsterdam based financial technology firm operating Aurora, the first new SEC-registered Alternative Trading System (ATS) for securities finance in over a decade. Through Aurora Marketplace and Aurora Trade Manager, Provable delivers front-, middle-, and back-office technology for the securities lending market: automated trade matching, contract lifecycle management (returns, recalls, marks, rate changes), and CCP connectivity via NSCC. Its cloud-native platform exposes open APIs — a Connect/gRPC Aurora API, FIX specifications, and WebSocket/webhook event streams — and it is a FINRA member registered as an SEC ATS with SOC 2 and ISO 27001 certifications.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/provable.png
layout: provider
mcp_servers:
- description: ''
  name: provable-mcp.yml
  slug: provable-mcpyml
modified: '2026-07-20'
name: Provable
nav: Providers
network: true
overview: 'Provable publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Securities Lending, Capital Markets, Fintech, and Trading.


  The Provable catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Provable''s developer surface includes documentation, API reference, support, engineering blog, authentication, changelog, and 14 more developer resources.'
random_paper: 43
score:
  band: thin
  composite: 39.6
  delta: 4.5
  facets:
    commercial_clarity: 28.9
    contract_quality: 22.6
    developer_ergonomics: 56.5
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 35.1
  regulatory:
    applies: true
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 65.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Provable Authentication
  slug: provable-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Provable Domain Security
  slug: provable-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: provable
tags:
- Company
- Securities Lending
- Capital Markets
- Fintech
- Trading
- Alternative Trading System
- Post-Trade
- gRPC
- FIX
website: https://developer.provablemarkets.com
---
