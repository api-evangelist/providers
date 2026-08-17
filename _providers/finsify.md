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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: RESTful bank-aggregation API for accessing consumer banking data — accounts, balances, and categorized transaction history — plus customer, connection token, and login lifecycle management, with webho
  name: Finsify Hub API
  slug: finsify-hub-api
artifact_total: 5
asyncapis:
- description: ''
  name: Finsify Webhooks
  slug: finsify-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://hub.finsify.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://hub.finsify.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.finsify.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.finsify.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/finsify-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/finsify-error-codes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/finsify-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/finsify-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/finsify-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/finsify-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/finsify-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/finsify-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/finsify-domain-security.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/finsify-service-catalog.json
created: '2026-07-17'
description: Finsify is a Southeast Asian bank-data aggregation company whose Finsify Hub service exposes a RESTful API for accessing end-user banking data — account balances and status, and categorized transaction history — across 50+ bank and statement services in 15 countries. The API handles customer creation, short-lived connection tokens that drive the end-user bank-login flow, account retrieval, transaction history filtered by date range, and login lifecycle management (activate, deactivate, refresh, reconnect), with machine-learning transaction categorization and webhook notifications for new transactions and login-status changes. Finsify is a 500 Global portfolio company and powers fintech products including Money Lover, Money Paper, Ngan Luong, and Bao Kim.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/finsify.png
layout: provider
mcp_servers:
- description: ''
  name: finsify-mcp.yml
  slug: finsify-mcpyml
modified: '2026-07-19'
name: Finsify
nav: Providers
network: true
overview: 'Finsify publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial Services, Open Banking, Bank Aggregation, and Financial Data.


  The Finsify catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Finsify''s developer surface includes documentation, API reference, authentication, and 11 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 26.9
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 51.6
    developer_ergonomics: 37.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 26.9
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 15.2
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/finsify/refs/heads/main/screenshots/finsify-2026-07-25T214546.png
security:
- kind: authentication
  name: Finsify Authentication
  slug: finsify-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Finsify Domain Security
  slug: finsify-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: finsify
tags:
- Company
- Financial Services
- Open Banking
- Bank Aggregation
- Financial Data
- Transactions
- Fintech
- Southeast Asia
website: https://hub.finsify.com
---
