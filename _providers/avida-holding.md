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
  href: https://raw.githubusercontent.com/api-evangelist/avida-holding/refs/heads/main/hosts/avida-holding-hosts.yml
  title: ''
  type: Hosts
  url: hosts/avida-holding-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avida-holding/refs/heads/main/security/avida-holding-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avida-holding-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://avida.ae
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-developer-program
  state: none
created: '2026-09-26'
description: Avida Holding AB operates as a holding company providing financial services including corporate and consumer lending solutions across Sweden, Norway, and Finland. Through its subsidiaries it offers mortgage loans, invoice factoring, and other credit products, aiming to enable customers to access easy financing and improve financial wellbeing. The company is backed by investors such as KKR and focuses on growth through customer‑centric, solution‑oriented culture.
image: https://avida-ae-350686.hostingersite.com/wp-content/uploads/2025/09/Website-images-1-1024x724.png
layout: provider
modified: '2026-09-26'
name: Avida Holding
nav: Providers
network: true
overview: Avida Holding is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Lending, Sweden, and Norway.
random_paper: 5
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - finland
    - norway
    - sweden
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Avida Holding Domain Security
  slug: avida-holding-domain-security
  summary_line: TLSv1.3 · DMARC
slug: avida-holding
tags:
- Company
- Finance
- Lending
- Sweden
- Norway
- Finland
website: https://avida.ae
---
