---
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 11.4
  scored_at: '2026-09-24'
api_count: 1
apis:
- description: Token-authenticated REST and WebSocket API for real-time and historical financial market data across crypto, forex, indices, stock, future, and fund product lines.
  name: iTick Market Data API
  slug: itick-market-data-api
artifact_total: 7
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/itick/refs/heads/main/security/itick-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/itick-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://itick.org/en
- group: start
  title: ''
  type: DeveloperPortal
  url: https://itick.org/en
- group: docs
  title: ''
  type: Documentation
  url: https://docs.itick.org/en
- group: docs
  title: ''
  type: APIReference
  url: https://docs.itick.org/en/api-url
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.itick.org/en/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://itick.org/en/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.itick.org
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/itick-org
- group: company
  title: ''
  type: Blog
  url: https://itick.org/en/blog
- group: start
  title: ''
  type: SignUp
  url: https://itick.org/en/dashboard
- group: operate
  title: ''
  type: Support
  url: https://itick.org/en/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://itick.org/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://itick.org/en/privacy
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/itick/refs/heads/main/packages/itick-packages.yml
  title: ''
  type: Packages
  url: packages/itick-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/itick/refs/heads/main/packages/itick-packages.yml
  title: ''
  type: SDKs
  url: packages/itick-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/itick/refs/heads/main/components/itick-components.yml
  title: ''
  type: Components
  url: components/itick-components.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/itick/refs/heads/main/plans/itick-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/itick-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/itick/refs/heads/main/lifecycle/itick-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/itick-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/itick/refs/heads/main/conformance/itick-conformance.yml
  title: ''
  type: Conformance
  url: conformance/itick-conformance.yml
created: '2026-09-16'
description: Real-time and historical financial market data across stocks, forex, indices, crypto, futures, and funds, delivered via REST, WebSocket, and FIX interfaces, plus a hosted MCP server and embeddable AI agent chat.
layout: provider
mcp_servers:
- description: ''
  name: iTick MCP Server
  slug: itick-mcp-server
- description: Official iTick MCP server exposing the REST market-data API as MCP tools for basics, stocks, indices, futures, funds, forex and crypto. WebSocket and FIX surfaces are explicitly NOT implemented by the
  name: iTick MCP Server
  slug: itick-mcp-server-2
modified: '2026-09-16'
name: iTick
nav: Providers
network: true
overview: 'iTick publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Data, Market Data, Stocks, Forex, and Crypto.


  iTick''s developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, signup flow, support, and 13 more developer resources.'
plans:
- name: Itick Plans Pricing
  plan_count: 4
  slug: itick-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 4
  name: Itick Rate Limits
  slug: itick-rate-limits
score:
  band: developing
  composite: 40.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 59.0
    catalog_earned_first_party: 24.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 72.2
    operational_transparency: 50.0
  previous_composite: 40.0
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 51.7
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Itick Authentication
  slug: itick-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Itick Domain Security
  slug: itick-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: itick
tags:
- Financial Data
- Market Data
- Stocks
- Forex
- Crypto
- Indices
- Futures
- Fund
- Real-Time Data
- WebSocket
- FIX Protocol
- Fintech
- Quantitative Trading
- MCP Server
website: https://itick.org/en
---
