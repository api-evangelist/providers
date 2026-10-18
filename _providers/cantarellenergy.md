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
api_count: 1
apis:
- description: API documentation not publicly available; attempts to locate OpenAPI or other contracts returned none.
  name: Cantarell Energy API
  slug: cantarell-energy-api
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cantarellenergy/refs/heads/main/well-known/cantarellenergy-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cantarellenergy-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cantarellenergy/refs/heads/main/well-known/cantarellenergy-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cantarellenergy-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cantarellenergy/refs/heads/main/hosts/cantarellenergy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cantarellenergy-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cantarell.energy/en/terms
- group: auth
  title: ''
  type: Security
  url: https://cantarell.energy/en/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cantarell.energy/en/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://cantarell.energy/en/news
- group: other
  title: ''
  type: Leadership
  url: https://cantarell.energy/en/leadership
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cantarellenergy/refs/heads/main/security/cantarellenergy-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cantarellenergy-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cantarellenergy/refs/heads/main/security/cantarellenergy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cantarellenergy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cantarell.energy
coverage:
  detail: API documentation pages return JavaScript-rendered HTML with no machine‑readable OpenAPI spec.
  evidence:
  - status: 404
    url: https://cantarell.energy/api-docs
  - status: 404
    url: https://cantarell.energy/en/api-docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-06'
description: Cantarellenergy is a nascent energy technology firm focused on developing advanced renewable power solutions. The company emerged from the API Evangelist harvest backlog and is being profiled to uncover its API offerings, documentation, and ecosystem. While public information is limited, Cantarellenergy aims to innovate in sustainable energy generation, storage, and distribution, targeting both commercial and residential markets. The profiling effort will track the discovery of its web presence, API specifications, and related developer resources as they become available.
image: https://cantarell.energy/opengraph-image
layout: provider
modified: '2026-10-06'
name: Cantarellenergy
nav: Providers
network: true
overview: Cantarellenergy is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Renewables, Technology, Startups, and Cleantech.
random_paper: 16
score:
  band: emerging
  composite: 12.1
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 60.7
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 16.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cantarellenergy Domain Security
  slug: cantarellenergy-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Cantarellenergy Vulnerability Disclosure
  slug: cantarellenergy-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cantarellenergy
tags:
- Energy
- Renewables
- Technology
- Startups
- Cleantech
- Company
website: https://cantarell.energy
---
