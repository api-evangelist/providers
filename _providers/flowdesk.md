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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Flowdesk Platform Connect is the developer API for programmatic OTC spot trading. It offers a REST interface for quoting and trading OTC spot orders and a WebSocket channel for real-time streaming, au
  name: Flowdesk Platform Connect
  slug: flowdesk-platform-connect
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flowdesk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.flowdesk.co
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.flowdesk.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.flowdesk.co
- group: docs
  title: ''
  type: APIReference
  url: https://docs.flowdesk.co/reference/otc-spot
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.flowdesk.co/getting-started/intro
- group: auth
  title: ''
  type: Authentication
  url: authentication/flowdesk-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/flowdesk-conventions.yml
- group: company
  title: ''
  type: Blog
  url: https://www.flowdesk.co/insights
- group: operate
  title: ''
  type: Support
  url: https://www.flowdesk.co/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.flowdesk.co/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.flowdesk.co/legal/privacy-notice
- group: auth
  title: ''
  type: TrustCenter
  url: security/flowdesk-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.flowdesk.co
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/flowdesk-llms.txt
created: '2026-07-17'
description: Flowdesk is a full-service digital-asset trading and technology firm that delivers liquidity, execution, and market infrastructure to token issuers, exchanges, and institutions. It is a regulated Crypto-Asset Service Provider registered with France's AMF and licensed by Dubai's Virtual Assets Regulatory Authority (VARA). Products span liquidity solutions (token, stablecoin, exchange, and DeFi), OTC trading (spot, derivatives, and credit) across 150+ venues and 1,000+ asset pairs, tokenized-market infrastructure, and ventures. Flowdesk exposes a developer-facing "Platform Connect" API for programmatic OTC spot trading over REST with a companion WebSocket streaming channel, authenticated with OAuth 2.0 JWT bearer tokens issued through its Auth0 tenant.
image: https://www.flowdesk.co/favicon.ico
layout: provider
modified: '2026-07-19'
name: Flowdesk
nav: Providers
network: true
overview: 'Flowdesk publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Crypto, Digital Assets, and Trading.


  Flowdesk''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, support, and 9 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 17.3
  coverage:
    artifact_dirs: 6
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 17.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 41.7
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flowdesk/refs/heads/main/screenshots/flowdesk-2026-07-25T214834.png
security:
- kind: authentication
  name: Flowdesk Authentication
  slug: flowdesk-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Flowdesk Domain Security
  slug: flowdesk-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Flowdesk Trust Center
  slug: flowdesk-trust-center
  summary_line: trust center published
slug: flowdesk
tags:
- Company
- Fintech
- Crypto
- Digital Assets
- Trading
- Liquidity
- Market Maker
- OTC
- WebSocket
website: https://www.flowdesk.co
---
