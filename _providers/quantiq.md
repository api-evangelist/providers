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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: QuantiQ provides a comprehensive REST API for real-time and historical financial market data, including stock quotes, company profiles, earnings, and congressional trades.
  name: QuantiQ API
  slug: quantiq-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/quantiq/hosts/quantiq-hosts.yml
  title: ''
  type: Hosts
  url: hosts/quantiq-hosts.yml
- group: other
  href: https://artifacts.apis.io/quantiq/vendors/quantiq-vendors.yml
  title: ''
  type: Vendors
  url: vendors/quantiq-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.quantiq.live/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/laurentiugabriel
- group: auth
  href: https://artifacts.apis.io/quantiq/security/quantiq-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/quantiq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://quantiq.live/
coverage:
  checked: '2026-10-18'
  detail: Documentation pages render only via JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://www.quantiq.live/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-18'
description: QuantiQ delivers a developer‑first financial data API providing public company fundamentals, historical market data, and congressional trading disclosures. The platform offers easy REST endpoints for income statements, balance sheets, cash flow, and more, enabling developers to embed reliable financial intelligence into apps, analytics, and trading tools.
layout: provider
modified: '2026-10-18'
name: QuantiQ
nav: Providers
network: true
overview: QuantiQ is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial Data, Developer-First, and Market Data.
random_paper: 3
score:
  band: minimal
  composite: 5.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 9.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Quantiq Domain Security
  slug: quantiq-domain-security
  summary_line: TLSv1.3 · HSTS
slug: quantiq
tags:
- Company
- Financial Data
- Developer-First
- Market Data
website: https://quantiq.live/
---
