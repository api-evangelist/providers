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
api_count: 0
artifact_total: 4
common:
- group: other
  href: https://artifacts.apis.io/arda/hosts/arda-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arda-hosts.yml
- group: auth
  href: https://artifacts.apis.io/arda/security/arda-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arda-domain-security.yml
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://arda.finance/
  reason: no-developer-program
  state: none
created: '2026-10-20'
description: Arda is a financial technology company offering a suite of APIs for digital asset management, portfolio tracking, and automated trading. The platform provides developers with access to real-time market data, transaction execution, and account management capabilities, enabling integration of advanced financial services into applications. Arda focuses on security, scalability, and compliance, supporting both retail and institutional clients.
layout: provider
modified: '2026-10-20'
name: Arda
nav: Providers
network: true
overview: Arda is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, FinTech, API, DigitalAssets, and Trading.
plans:
- name: Arda Plans Pricing
  plan_count: 4
  slug: arda-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Arda Rate Limits
  slug: arda-rate-limits
score:
  band: minimal
  composite: 9.4
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 12.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 11.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Arda Authentication
  slug: arda-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Arda Domain Security
  slug: arda-domain-security
  summary_line: DNSSEC · DMARC
slug: arda
tags:
- Company
- FinTech
- API
- DigitalAssets
- Trading
---
