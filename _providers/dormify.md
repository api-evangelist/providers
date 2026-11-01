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
- group: other
  href: https://artifacts.apis.io/dormify/hosts/dormify-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dormify-hosts.yml
- group: other
  href: https://artifacts.apis.io/dormify/vendors/dormify-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dormify-vendors.yml
- group: auth
  href: https://artifacts.apis.io/dormify/security/dormify-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dormify-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dormify.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.dormify.com
  - status: 403
    url: https://equityzen.com/company/dormify
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: Dormify is an internet-first home‑goods brand owned by Williams‑Sonoma, offering stylish, space‑saving bedding, furniture and décor for college dorm rooms and small living spaces. Founded in 2011, the company curates a range of products designed for functionality and modern aesthetics, targeting students and young adults looking to personalize their living environments. Dormify operates primarily through its e‑commerce site, providing a curated shopping experience with a focus on quality, design, and convenience.
layout: provider
modified: '2026-10-24'
name: Dormify
nav: Providers
network: true
overview: Dormify is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Home Goods, E-commerce, Dorm Decor, Furniture, and Bedding.
random_paper: 18
score:
  band: minimal
  composite: 3.1
  coverage:
    artifact_dirs: 6
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
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dormify Domain Security
  slug: dormify-domain-security
  summary_line: TLSv1.3
slug: dormify
tags:
- Home Goods
- E-commerce
- Dorm Decor
- Furniture
- Bedding
website: https://www.dormify.com
---
