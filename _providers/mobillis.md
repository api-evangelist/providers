---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 17.3
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: Partner-facing REST API for distributing prepaid vehicle access. Documented resources include wallet creation and management, PSP-orchestrated top-ups, ledger / transaction history, and webhook regist
  name: Mobillis Open API
  slug: mobillis-open-api
artifact_total: 4
asyncapis:
- description: ''
  name: Mobillis Webhooks
  slug: mobillis-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mobillis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mobillis.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://auth.mobillis.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://auth.mobillis.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://auth.mobillis.com/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mobillis-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/mobillis-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mobillis-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mobillis-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mobillis-llms.txt
created: '2026-07-17'
description: Mobillis, operated by Reflex Mobility, Inc., is a fintech mobility platform that turns vehicle fleet inventory into a prepaid billing and access product. It sits as an overlay on top of legacy rental and fleet systems rather than replacing them, letting fleet operators collect payment upfront and reach new "everyday driver" segments, while non-fleet distribution partners resell vehicle access through referral links, a white-label front end, or the Mobillis Open APIs. The documented API surface covers wallet creation and management, PSP-orchestrated top-ups, ledger and transaction-history access, and webhook events for low-balance alerts and billing triggers. Mobillis operates from Johannesburg and New York.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mobillis.png
layout: provider
mcp_servers:
- description: ''
  name: mobillis-mcp.yml
  slug: mobillis-mcpyml
modified: '2026-07-20'
name: Mobillis
nav: Providers
network: true
overview: 'Mobillis publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Mobility, Payments, and Wallets.


  The Mobillis catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Mobillis'' developer surface includes signup flow and 9 more developer resources.'
random_paper: 43
score:
  band: emerging
  composite: 24.3
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 22.6
    developer_ergonomics: 8.7
    discoverability: 80.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 24.3
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 30.4
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: domain-security
  name: Mobillis Domain Security
  slug: mobillis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mobillis
tags:
- Company
- Fintech
- Mobility
- Payments
- Wallets
- Fleet Management
- Prepaid
- Webhooks
- Ledger
website: https://mobillis.com/
---
