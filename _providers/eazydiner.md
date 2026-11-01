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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/eazydiner/llms/eazydiner-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/eazydiner-llms.txt
- group: other
  href: https://artifacts.apis.io/eazydiner/hosts/eazydiner-hosts.yml
  title: ''
  type: Hosts
  url: hosts/eazydiner-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.eazydiner.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.eazydiner.com/privacy-policy
- group: auth
  href: https://artifacts.apis.io/eazydiner/security/eazydiner-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/eazydiner-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.eazydiner.com
coverage:
  checked: '2026-10-25'
  detail: The public website renders content via JavaScript and provides no machine‑readable API specifications.
  evidence:
  - status: 200
    url: https://www.eazydiner.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-24'
description: Eazydiner is an Indian restaurant discovery and reservation platform offering deals and discounts across major cities in India and the UAE. It aggregates over 40,000 restaurants, provides real‑time table booking, loyalty rewards, and a mobile app for seamless dining experiences. The service targets food enthusiasts seeking convenient reservations, special offers, and curated dining recommendations.
layout: provider
modified: '2026-10-24'
name: Eazydiner
nav: Providers
network: true
overview: Eazydiner is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Restaurant, Reservation, Deals, and India.
random_paper: 11
score:
  band: minimal
  composite: 8.5
  coverage:
    artifact_dirs: 7
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
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Eazydiner Domain Security
  slug: eazydiner-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: eazydiner
tags:
- Company
- Restaurant
- Reservation
- Deals
- India
website: https://www.eazydiner.com
---
