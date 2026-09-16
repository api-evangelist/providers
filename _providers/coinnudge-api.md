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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.9
  scored_at: '2026-09-15'
api_count: 1
apis:
- description: REST HTTP API returning JSON/CSV for crypto market datasets. Includes a free Research scope (no paid key required) and a paid Market Events v1 scope with versioned releases, schema, manifest, and chec
  name: CoinNudge Data API
  slug: coinnudge-data-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://coinnudge.site/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coinnudge-api/refs/heads/main/security/coinnudge-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coinnudge-api-domain-security.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/coinnudge-api/refs/heads/main/plans/coinnudge-api-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/coinnudge-api-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/coinnudge-api/refs/heads/main/conformance/coinnudge-api-conformance.yml
  title: ''
  type: Conformance
  url: conformance/coinnudge-api-conformance.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://coinnudge.site/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://coinnudge.site/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://coinnudge.site/privacy
- group: operate
  title: ''
  type: Support
  url: https://coinnudge.site/about
created: '2026-09-13'
description: CoinNudge Data provides a REST HTTP API returning JSON/CSV for cryptocurrency market data, including a free Research API with current derived datasets (market breadth, dominance, funding/OI, liquidations, volatility, listings) and a paid Market Events v1 product with versioned event/control study data for major Binance Spot pairs. Operated by LUMOS AI TECHNOLOGY CO LTD.
layout: provider
mcp_servers:
- description: No official hosted or local MCP server was found for CoinNudge (no /mcp endpoint, no npm/PyPI package, no mention in docs or llms.txt). This is a DERIVED candidate tool list mapped from the documented
  name: CoinNudge Data API MCP (candidate)
  slug: coinnudge-data-api-mcp-candidate
modified: '2026-09-13'
name: CoinNudge API
nav: Providers
network: true
overview: 'CoinNudge API publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cryptocurrency, Market Data, Trading, Quantitative Finance, and Research.


  CoinNudge API''s developer surface includes pricing, support, and 6 more developer resources.'
plans:
- name: Coinnudge Api Plans Pricing
  plan_count: 5
  slug: coinnudge-api-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 3
  name: Coinnudge Api Rate Limits
  slug: coinnudge-api-rate-limits
score:
  band: thin
  composite: 32.2
  coverage:
    artifact_dirs: 12
    catalog_earned: 59.0
    catalog_earned_first_party: 24.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 63.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 72.2
    operational_transparency: 31.6
  previous_composite: 32.2
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 51.7
  schema_version: 0.22.0
  scored_at: '2026-09-15'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Coinnudge Api Authentication
  slug: coinnudge-api-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Coinnudge Api Domain Security
  slug: coinnudge-api-domain-security
  summary_line: TLSv1.3 · HSTS
slug: coinnudge-api
tags:
- Cryptocurrency
- Market Data
- Trading
- Quantitative Finance
- Research
- Derivatives
- Financial Data
- Datasets
website: https://coinnudge.site/
---
