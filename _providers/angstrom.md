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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/angstrom/refs/heads/main/hosts/angstrom-hosts.yml
  title: ''
  type: Hosts
  url: hosts/angstrom-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://angstromsports.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://angstromsports.com/privacy/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/angstrom/refs/heads/main/security/angstrom-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/angstrom-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://angstromsports.com/
created: '2026-09-24'
description: Angstrom Sports provides advanced sports forecasting and data analytics solutions for the US betting industry. Leveraging over 50 years of combined experience in bookmaking, modelling, proprietary trading, risk management, and service delivery, the company offers Monte‑Carlo simulations, granular play‑by‑play data, and neural‑network driven player valuation. Their platform delivers real‑time insights and predictive analytics to help clients make informed betting decisions.
layout: provider
modified: '2026-09-24'
name: Angstrom
nav: Providers
network: true
overview: Angstrom is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Sports, Analytics, Forecasting, Betting, and Data.
random_paper: 17
score:
  band: minimal
  composite: 8.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Angstrom Domain Security
  slug: angstrom-domain-security
  summary_line: TLSv1.2
slug: angstrom
tags:
- Sports
- Analytics
- Forecasting
- Betting
- Data
website: https://angstromsports.com/
---
