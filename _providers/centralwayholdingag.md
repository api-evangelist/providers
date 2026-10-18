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
  href: https://raw.githubusercontent.com/api-evangelist/centralwayholdingag/refs/heads/main/hosts/centralwayholdingag-hosts.yml
  title: ''
  type: Hosts
  url: hosts/centralwayholdingag-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/centralwayholdingag/refs/heads/main/vendors/centralwayholdingag-vendors.yml
  title: ''
  type: Vendors
  url: vendors/centralwayholdingag-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/centralwayholdingag/refs/heads/main/security/centralwayholdingag-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/centralwayholdingag-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://centralwaygroup.com
coverage:
  checked: '2026-10-07'
  detail: The company website returns a JavaScript shell with no machine‑readable documentation.
  evidence:
  - status: 200
    url: https://centralwaygroup.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-07'
description: Centralwayholdingag is a Swiss holding company listed on the SIX Swiss Exchange. It operates as a diversified investment group with interests in various sectors including real estate, financial services, and industrial holdings. The company provides strategic oversight and capital allocation across its portfolio, aiming to generate sustainable growth and shareholder value.
layout: provider
modified: '2026-10-07'
name: Centralwayholdingag
nav: Providers
network: true
overview: Centralwayholdingag is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Holding, Investment, Swiss, and Finance.
random_paper: 21
score:
  band: minimal
  composite: 3.1
  coverage:
    artifact_dirs: 4
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Centralwayholdingag Domain Security
  slug: centralwayholdingag-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: centralwayholdingag
tags:
- Company
- Holding
- Investment
- Swiss
- Finance
website: https://centralwaygroup.com
---
