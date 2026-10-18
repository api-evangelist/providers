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
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API for California Catalysts platform (no public developer program discovered).
  name: California Catalysts API
  slug: california-catalysts-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/california-catalysts/refs/heads/main/well-known/california-catalysts-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/california-catalysts-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/california-catalysts/refs/heads/main/hosts/california-catalysts-hosts.yml
  title: ''
  type: Hosts
  url: hosts/california-catalysts-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/california-catalysts/refs/heads/main/vendors/california-catalysts-vendors.yml
  title: ''
  type: Vendors
  url: vendors/california-catalysts-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://calicat.com/category/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/california-catalysts/refs/heads/main/security/california-catalysts-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/california-catalysts-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://calicat.com/
coverage:
  checked: '2026-10-06'
  detail: No public developer program or API documentation was found for California Catalysts.
  evidence:
  - status: 200
    url: https://app.calicat.com/
  reason: no-developer-program
  state: none
created: '2026-10-06'
description: California Catalysts develops advanced materials and stack components for electrolyzers, offering non‑iridium catalysts that lower the levelized cost of hydrogen. Founded to commercialize DOE‑funded research, the company leverages AI‑driven high‑throughput catalyst discovery to accelerate electrolysis technology. It partners with leading manufacturers and provides testing‑as‑a‑service, aiming to make green hydrogen more affordable and scalable.
image: https://calicat.com/wp-content/uploads/2024/08/calicat.jpg
layout: provider
modified: '2026-10-06'
name: California Catalysts
nav: Providers
network: true
overview: California Catalysts is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Electrolyzers, Hydrogen Production, Catalysts, Materials, and Stack Components.
random_paper: 9
score:
  band: minimal
  composite: 5.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: California Catalysts Domain Security
  slug: california-catalysts-domain-security
  summary_line: TLSv1.3
slug: california-catalysts
tags:
- Electrolyzers
- Hydrogen Production
- Catalysts
- Materials
- Stack Components
- Green Hydrogen
website: https://calicat.com/
---
