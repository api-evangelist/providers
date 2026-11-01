---
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Provides on‑chain and market data endpoints for developers to retrieve blockchain statistics, transaction volumes, and price information.
  name: CryptoKeyhole API
  slug: cryptokeyhole-api
artifact_total: 6
common:
- group: operate
  href: https://artifacts.apis.io/cryptokeyhole/rate-limits/cryptokeyhole-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cryptokeyhole-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/cryptokeyhole/plans/cryptokeyhole-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cryptokeyhole-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/cryptokeyhole/llms/cryptokeyhole-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cryptokeyhole-llms.txt
- group: other
  href: https://artifacts.apis.io/cryptokeyhole/hosts/cryptokeyhole-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cryptokeyhole-hosts.yml
- group: other
  href: https://artifacts.apis.io/cryptokeyhole/vendors/cryptokeyhole-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cryptokeyhole-vendors.yml
- group: auth
  href: https://artifacts.apis.io/cryptokeyhole/security/cryptokeyhole-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cryptokeyhole-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cryptokeyhole.com
- group: docs
  title: ''
  type: Documentation
  url: https://cryptokeyhole.com/about/
- group: commercial
  title: ''
  type: Pricing
  url: https://cryptokeyhole.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cryptokeyhole.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cryptokeyhole.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://cryptokeyhole.com/contact/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cryptokeyhole
coverage:
  checked: '2026-10-30'
  detail: The site is a JavaScript‑rendered SPA with no machine‑readable API specification publicly available.
  evidence:
  - status: 200
    url: https://cryptokeyhole.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-30'
description: CryptoKeyhole provides on‑chain and market data visualizations for Bitcoin, Ethereum and over 60 other cryptocurrencies. The platform runs its own full nodes, aggregates blockchain metrics and market prices, and offers real‑time charts, historical data, and API endpoints for developers to retrieve blockchain statistics, transaction volumes, and price information. By combining on‑chain analytics with market data, CryptoKeyhole enables traders, researchers, and applications to gain insight into cryptocurrency performance.
image: https://cryptokeyhole.com/assets/brand/cryptokeyhole-logo-1980d65a5c1f.png
layout: provider
modified: '2026-10-30'
name: CryptoKeyhole
nav: Providers
network: true
overview: 'CryptoKeyhole is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include cryptocurrency, blockchain, analytics, data, and charts.


  CryptoKeyhole''s developer surface includes documentation, pricing, support, and 10 more developer resources.'
plans:
- name: Cryptokeyhole Plans Pricing
  plan_count: 7
  slug: cryptokeyhole-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: Cryptokeyhole Rate Limits
  slug: cryptokeyhole-rate-limits
scopes:
- name: Cryptokeyhole Scopes
  scope_count: 0
  slug: cryptokeyhole-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 25.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 50.0
    catalog_earned_first_party: 0.0
    catalog_gap: 65.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 57.1
    operational_transparency: 24.2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Cryptokeyhole Authentication
  slug: cryptokeyhole-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Cryptokeyhole Domain Security
  slug: cryptokeyhole-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cryptokeyhole
tags:
- cryptocurrency
- blockchain
- analytics
- data
- charts
website: https://cryptokeyhole.com
---
