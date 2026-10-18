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
  href: https://raw.githubusercontent.com/api-evangelist/cellcentric/refs/heads/main/hosts/cellcentric-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cellcentric-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cellcentric/refs/heads/main/vendors/cellcentric-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cellcentric-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cellcentric.net/en-us/legal-notice
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cellcentric.net/en-us/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.cellcentric.net/en-us/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cellcentric/refs/heads/main/security/cellcentric-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cellcentric-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cellcentric.net/en-us
coverage:
  checked: '2026-10-07'
  detail: Cellcentric's website provides no developer program or API documentation, and no machine-readable contracts were discovered.
  evidence:
  - status: 0
    url: https://api.cellcentric.net/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-07'
description: Cellcentric is a joint venture between Daimler Truck AG and Volvo Group, founded in 2021 to develop, produce, and commercialize hydrogen fuel cell systems for heavy‑duty vehicles. The company supplies Tier‑1 fuel cell modules, aiming for climate‑neutral transport by 2050, and operates globally with sites in Germany, Canada, and beyond. It offers advanced fuel cell products such as the BZA375, supports OEMs and fleet operators, and maintains a strong portfolio of patents and partnerships across the hydrogen ecosystem.
image: https://images.prismic.io/cellcentric/ZemRSHUurf2G3Luo_cellcentric-ogImage.jpg?auto=format,compress&rect=0,18,960,504&w=2400&h=1260
layout: provider
modified: '2026-10-07'
name: Cellcentric
nav: Providers
network: true
overview: Cellcentric is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fuel Cells, Heavy‑Duty Trucks, Hydrogen Powertrain, OEMs, and Fleet Operators.
random_paper: 16
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 11.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cellcentric Domain Security
  slug: cellcentric-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cellcentric
tags:
- Fuel Cells
- Heavy‑Duty Trucks
- Hydrogen Powertrain
- OEMs
- Fleet Operators
- Stationary Power
website: https://www.cellcentric.net/en-us
---
