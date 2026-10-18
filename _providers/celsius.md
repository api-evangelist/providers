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
api_count: 1
apis:
- description: Celsius provides a cryptocurrency lending and mining platform; no public developer API documentation was found.
  name: Celsius API
  slug: celsius-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/celsius/refs/heads/main/hosts/celsius-hosts.yml
  title: ''
  type: Hosts
  url: hosts/celsius-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/celsius/refs/heads/main/vendors/celsius-vendors.yml
  title: ''
  type: Vendors
  url: vendors/celsius-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://celsius.network/static/privacy-policy.pdf
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/celsius/refs/heads/main/security/celsius-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/celsius-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://celsius.network/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://api.celsius.network/mcp
  - status: 200
    url: https://celsius.network/
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-developer-program
  state: none
created: '2026-10-07'
description: Celsius Network is a cryptocurrency lending and mining platform that filed for Chapter 11 bankruptcy in early 2024 and is currently in the process of winding down its operations. The company provides services for earning interest on crypto assets, borrowing against holdings, and operates a mining business. Following reorganization, creditors receive distributions in cryptocurrency, USD, or equity in the successor entity Ionic Digital LLC. The platform’s website offers detailed information on claims, distribution processes, and corporate updates.
layout: provider
modified: '2026-10-07'
name: Celsius
nav: Providers
network: true
overview: Celsius is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cryptocurrency, Lending, Mining, and Bankruptcy.
random_paper: 12
score:
  band: minimal
  composite: 6.7
  coverage:
    artifact_dirs: 5
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Celsius Domain Security
  slug: celsius-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: celsius
tags:
- Company
- Cryptocurrency
- Lending
- Mining
- Bankruptcy
website: https://celsius.network/
---
