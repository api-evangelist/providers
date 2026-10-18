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
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bitooda/refs/heads/main/hosts/bitooda-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bitooda-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bitooda/refs/heads/main/vendors/bitooda-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bitooda-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://www.bitooda.io/leadership/tom-nath
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bitooda/refs/heads/main/security/bitooda-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bitooda-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bitooda.io
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bitooda.io/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bitooda.io/terms-of-use
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bitooda
coverage:
  checked: '2026-10-14'
  detail: bitooda.io is an institutional compute/commodities brokerage marketing site whose only call to action is an Inquire form; api.bitooda.io, docs.bitooda.io and developer.bitooda.io do not resolve and contract discovery found no spec.
  evidence:
  - status: 200
    url: https://www.bitooda.io
  - status: 0
    url: https://api.bitooda.io
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: BitOoda is an institutional, AI-native brokerage and market infrastructure firm that builds markets around compute, power, infrastructure and capital, covering GPU rental rate and memory futures, energy and metals hedging, origination, structuring and price discovery for institutional clients. It publishes no public developer program or API.
layout: provider
modified: '2026-10-14'
name: BitOoda
nav: Providers
network: true
overview: BitOoda is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Brokerage, Financial Services, Commodities, and Compute Markets.
random_paper: 12
score:
  band: minimal
  composite: 7.7
  coverage:
    artifact_dirs: 5
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
    discoverability: 46.4
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 13.0
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bitooda Domain Security
  slug: bitooda-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bitooda
tags:
- Company
- Brokerage
- Financial Services
- Commodities
- Compute Markets
- Cryptocurrency
website: https://www.bitooda.io
---
