---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/coinroutes/refs/heads/main/llms/coinroutes-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/coinroutes-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coinroutes/refs/heads/main/hosts/coinroutes-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coinroutes-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coinroutes/refs/heads/main/vendors/coinroutes-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coinroutes-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://coinroutes.com/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://coinroutes.com/insights/news/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CoinRoutes
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coinroutes/refs/heads/main/security/coinroutes-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coinroutes-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://coinroutes.com/
coverage:
  checked: '2026-10-09'
  detail: No OpenAPI, AsyncAPI, GraphQL or other machine-readable contract found on discovered hosts.
  evidence:
  - status: 0
    url: https://api.coinroutes.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-09'
description: CoinRoutes provides an institutional algorithmic crypto trading platform offering portfolio management, risk solutions, and execution across multiple digital asset exchanges. The company delivers award‑winning algorithms, real‑time market data, advanced charting, and order management tools for asset managers, prop traders, and prime brokers.
image: https://coinroutes.com/og-image.png
layout: provider
modified: '2026-10-09'
name: CoinRoutes
nav: Providers
network: true
overview: CoinRoutes is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Algorithmic Trading, Cryptocurrency, Institutional Trading, Portfolio Management, and Risk Management.
random_paper: 21
score:
  band: minimal
  composite: 6.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 9.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Coinroutes Domain Security
  slug: coinroutes-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: coinroutes
tags:
- Algorithmic Trading
- Cryptocurrency
- Institutional Trading
- Portfolio Management
- Risk Management
- Execution Services
website: https://coinroutes.com/
---
