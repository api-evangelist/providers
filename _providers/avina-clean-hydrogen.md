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
- description: API information is referenced on the pricing page of Avina Clean Hydrogen website.
  name: Avina Clean Hydrogen API
  slug: avina-clean-hydrogen-api
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/avina-clean-hydrogen/refs/heads/main/plans/avina-clean-hydrogen-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/avina-clean-hydrogen-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avina-clean-hydrogen/refs/heads/main/hosts/avina-clean-hydrogen-hosts.yml
  title: ''
  type: Hosts
  url: hosts/avina-clean-hydrogen-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avina-clean-hydrogen/refs/heads/main/vendors/avina-clean-hydrogen-vendors.yml
  title: ''
  type: Vendors
  url: vendors/avina-clean-hydrogen-vendors.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://avinah2.com/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://avinah2.com/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avina-clean-hydrogen/refs/heads/main/security/avina-clean-hydrogen-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avina-clean-hydrogen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://avinah2.com/
coverage:
  checked: 2026-09-27
  detail: No OpenAPI or other machine‑readable contract was found at the API host.
  evidence:
  - status: 0
    url: https://api.avinah2.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-27'
description: Avina Clean Hydrogen, part of Avina Inc., develops and delivers cutting‑edge clean energy solutions, focusing on low‑carbon ammonia, synthetic aviation fuel, and especially clean hydrogen produced via renewable electrolysis. The company aims to accelerate the global transition to clean fuels for heavy transport, shipping, steel and chemicals, with commercial plants slated for operation from 2025. Avina’s mission is to provide affordable, reliable clean energy, scaling next‑generation fuels worldwide.
layout: provider
modified: '2026-09-27'
name: Avina Clean Hydrogen
nav: Providers
network: true
overview: 'Avina Clean Hydrogen publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Clean Energy, Hydrogen, Synthetic Fuels, and Renewables.


  Avina Clean Hydrogen''s developer surface includes pricing and 6 more developer resources.'
plans:
- name: Avina Clean Hydrogen Plans Pricing
  plan_count: 3
  slug: avina-clean-hydrogen-plans-pricing
random_paper: 16
score:
  band: emerging
  composite: 12.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 42.0
    catalog_earned_first_party: 12.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 4.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Avina Clean Hydrogen Domain Security
  slug: avina-clean-hydrogen-domain-security
  summary_line: TLSv1.3
slug: avina-clean-hydrogen
tags:
- Company
- Clean Energy
- Hydrogen
- Synthetic Fuels
- Renewables
website: https://avinah2.com/
---
