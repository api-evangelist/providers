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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/baraja/refs/heads/main/conformance/baraja-conformance.yml
  title: ''
  type: Conformance
  url: conformance/baraja-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/baraja/refs/heads/main/hosts/baraja-hosts.yml
  title: ''
  type: Hosts
  url: hosts/baraja-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/baraja/refs/heads/main/vendors/baraja-vendors.yml
  title: ''
  type: Vendors
  url: vendors/baraja-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.baraja.com/en/media
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/baraja/refs/heads/main/security/baraja-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/baraja-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.baraja.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.baraja.com/en/technology/white-paper
- group: company
  title: ''
  type: Blog
  url: https://www.baraja.com/en/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.baraja.com/en/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.baraja.com/en/terms-and-conditions
coverage:
  detail: Baraja provides no public developer program or API documentation.
  evidence:
  - status: 200
    url: https://www.baraja.com/en
  reason: no-developer-program
  state: none
created: '2026-09-27'
description: Baraja is a deep‑technology company that has reinvented LiDAR for self‑driving vehicles. Their Spectrum‑Scan™ platform delivers unprecedented range, precision and reliability, enabling high‑quality point‑cloud data for autonomous automotive applications. Founded in 2015 in Sydney, Australia, Baraja operates globally with offices in China and the USA, focusing on single‑chip LiDAR designs and scalable manufacturing.
image: https://cdn.sanity.io/images/vpc9c65d/production/10d33da50f646e098491588caf45aa832533b52f-1200x630.jpg?w=1200&h=630
layout: provider
modified: '2026-09-27'
name: Baraja
nav: Providers
network: true
overview: 'Baraja is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, LiDAR, Autonomous Vehicles, Deep Tech, and AustralianStartup.


  Baraja''s developer surface includes documentation, engineering blog, and 8 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 14.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Baraja Domain Security
  slug: baraja-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: baraja
tags:
- Company
- LiDAR
- Autonomous Vehicles
- Deep Tech
- AustralianStartup
website: https://www.baraja.com
---
