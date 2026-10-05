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
- description: API documentation for Atlas Magnetics products and services.
  name: Atlas Magnetics API
  slug: atlas-magnetics-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/atlasmagnetics/refs/heads/main/hosts/atlasmagnetics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atlasmagnetics-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/atlasmagnetics/refs/heads/main/vendors/atlasmagnetics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/atlasmagnetics-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://atlasmagnetics.com/news/am1u1412-goes-to-mass-production
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/atlasmagnetics/refs/heads/main/security/atlasmagnetics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atlasmagnetics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://atlasmagnetics.com
- group: docs
  title: ''
  type: Documentation
  url: https://atlasmagnetics.com/resources
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://atlasmagnetics.com/page/privacy-policy
coverage:
  checked: 2026-09-26
  detail: Documentation pages are rendered via JavaScript, preventing machine‑readable contract discovery.
  evidence:
  - status: 200
    url: https://atlasmagnetics.com/resources
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: Atlas Magnetics is a Southern California based manufacturer of custom solenoids, magnetic components, μASICs, DC/DC converters and load switches. It serves aerospace, defense and industrial customers, offering standard components with full datasheets and evaluation boards available in‑stock through distribution partners. The company provides engineering resources, design services and rapid prototyping to accelerate product development.
image: https://atlasmagnetics.com/images/am-building.webp
layout: provider
modified: '2026-09-26'
name: Atlasmagnetics
nav: Providers
network: true
overview: 'Atlasmagnetics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Manufacturing, Magnetic Components, Aerospace, and Defense.


  Atlasmagnetics'' developer surface includes documentation and 6 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 9.0
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
  provenance:
    mcp: unknown
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
  name: Atlasmagnetics Domain Security
  slug: atlasmagnetics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: atlasmagnetics
tags:
- Company
- Manufacturing
- Magnetic Components
- Aerospace
- Defense
website: https://atlasmagnetics.com
---
