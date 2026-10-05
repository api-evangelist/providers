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
  href: https://raw.githubusercontent.com/api-evangelist/axton/refs/heads/main/hosts/axton-hosts.yml
  title: ''
  type: Hosts
  url: hosts/axton-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://axton.ca/privacy-policy/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/axton/refs/heads/main/security/axton-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/axton-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://axton.ca
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://equityzen.com/company/axton
  reason: no-developer-program
  state: none
created: '2026-09-27'
description: Axton Inc. is a custom equipment manufacturing company based in Delta, British Columbia, Canada. Founded in 1976, it serves heavy industries such as petro‑chemical, oil & gas, pulp & paper, mining, and environmental sectors. The firm designs, engineers, fabricates and assembles pressure vessels, heat exchangers, tanks, rotating equipment, and complex mechanical systems, offering end‑to‑end solutions from concept through delivery.
image: https://axton.ca/wp-content/uploads/2021/07/Axton-Home-Capabilities-Cooler-Condenser-1024x685.jpg
layout: provider
modified: '2026-09-27'
name: Axton
nav: Providers
network: true
overview: Axton is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Manufacturing, Metal Fabrication, Industrial Equipment, Canada, and Engineering.
random_paper: 4
score:
  band: minimal
  composite: 6.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Axton Domain Security
  slug: axton-domain-security
  summary_line: TLSv1.3 · DMARC
slug: axton
tags:
- Manufacturing
- Metal Fabrication
- Industrial Equipment
- Canada
- Engineering
website: https://axton.ca
---
