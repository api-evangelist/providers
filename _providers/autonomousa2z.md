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
api_count: 1
apis:
- description: Autonomousa2z offers autonomous vehicle and mobility services; API details are not publicly machine‑readable.
  name: Autonomousa2z API
  slug: autonomousa2z-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/autonomousa2z/refs/heads/main/hosts/autonomousa2z-hosts.yml
  title: ''
  type: Hosts
  url: hosts/autonomousa2z-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/autonomousa2z/refs/heads/main/vendors/autonomousa2z-vendors.yml
  title: ''
  type: Vendors
  url: vendors/autonomousa2z-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.autoa2z.ai/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.autoa2z.ai/News
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/autonomousa2z/refs/heads/main/security/autonomousa2z-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/autonomousa2z-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.autoa2z.ai
- group: docs
  title: ''
  type: Documentation
  url: https://www.autoa2z.ai/company
- group: operate
  title: ''
  type: Contact
  url: https://www.autoa2z.ai/Contact
coverage:
  checked: 2026-09-26
  detail: Company docs are rendered via JavaScript and no machine‑readable spec was found.
  evidence:
  - status: 200
    url: https://www.autoa2z.ai/company
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: Autonomous A2Z is an autonomous driving solution provider focused on enabling future mobility through advanced AI, LiDAR, and safety systems. The company offers a suite of services including autonomous shuttles, delivery robots, and smart city integration, with operations in Korea and expanding globally. Their mission is to create safe, reliable, and scalable autonomous transportation for all.
image: https://cdn.imweb.me/upload/S202309086909876845cbd/e570b54cfe754.png
layout: provider
modified: '2026-09-26'
name: Autonomousa2z
nav: Providers
network: true
overview: 'Autonomousa2z publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Autonomous Vehicles, Artificial Intelligence, Mobility, and South Korea.


  Autonomousa2z''s developer surface includes documentation and 7 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 8.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 58.9
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - south-korea
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Autonomousa2Z Domain Security
  slug: autonomousa2z-domain-security
  summary_line: TLSv1.3
slug: autonomousa2z
tags:
- Company
- Autonomous Vehicles
- Artificial Intelligence
- Mobility
- South Korea
website: https://www.autoa2z.ai
---
