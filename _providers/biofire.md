---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/biofire/refs/heads/main/well-known/biofire-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/biofire-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/biofire/refs/heads/main/hosts/biofire-hosts.yml
  title: ''
  type: Hosts
  url: hosts/biofire-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/biofire/refs/heads/main/security/biofire-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/biofire-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://biofire.com
- group: operate
  title: ''
  type: Contact
  url: https://biofire.com/kontakt/
- group: company
  title: ''
  type: Impressum
  url: https://biofire.com/impressum/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://equityzen.com/company/biofire
  reason: no-developer-program
  state: none
created: '2026-09-28'
description: Biofire manufactures handcrafted ceramic storage stoves and fireplaces in Germany, offering custom designs and high-quality heating solutions. With over 40 years of experience, the company provides personalized service, from planning to on‑site installation, emphasizing durability, efficiency, and timeless design. Their product range includes various stove models, accessories, and consulting services for optimal home heating.
image: https://biofire.com/wp-content/uploads/2025/04/modernes_wohnzimmer.jpg
layout: provider
modified: '2026-09-28'
name: Biofire
nav: Providers
network: true
overview: Biofire is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Heating, Ceramics, CustomDesign, and GermanManufacturing.
random_paper: 10
score:
  band: minimal
  composite: 4.3
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
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Biofire Domain Security
  slug: biofire-domain-security
  summary_line: TLSv1.3
slug: biofire
tags:
- Company
- Heating
- Ceramics
- CustomDesign
- GermanManufacturing
website: https://biofire.com
---
