---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 1
common:
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/USNC
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ultra-safe-nuclear/refs/heads/main/security/ultra-safe-nuclear-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ultra-safe-nuclear-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ultra-safe-nuclear/refs/heads/main/llms/ultra-safe-nuclear-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ultra-safe-nuclear-llms.txt
coverage:
  checked: '2026-09-01'
  detail: Ultra Safe Nuclear Corporation was liquidated in a Chapter 11 Section 363 auction completed in February 2025, and its corporate domain usnc.com now returns NXDOMAIN with no address record while still routing mail on Microsoft 365 US Government cloud, so there is no site, portal, or API host left to probe.
  evidence:
  - status: 0
    url: https://www.usnc.com/
  - status: 200
    url: https://ultrasafenuclear.com/.well-known/api-catalog
  - status: 200
    url: https://ultrasafenuclear.com/.well-known/ultra-safe-nuclear-negative-control-7f3ab91c.json
  - status: 200
    url: https://github.com/USNC
  reason: defunct
  state: none
created: '2026-09-01'
description: 'Ultra Safe Nuclear Corporation (USNC) was a Seattle-based advanced nuclear company, founded in 2011, that vertically integrated fourth-generation nuclear power — the Micro Modular Reactor (MMR), the Pylon space reactor developed through its USNC-Tech subsidiary, and Fully Ceramic Microencapsulated (FCM) TRISO nuclear fuel manufactured at Oak Ridge, Tennessee. It filed for Chapter 11 bankruptcy in the District of Delaware in October 2024 following the death of its principal investor, and its assets were sold in a bifurcated Section 363 auction: NANO Nuclear Energy acquired the MMR and Pylon reactor patents and demonstration partnerships for $8.5 million (court-approved 18 December 2024), and Standard Nuclear acquired the FCM/TRISO fuel business and the Oak Ridge facility for $28 million (closed February 2025). The company no longer operates. Its primary domain, usnc.com, is still registered and still routes mail on the Microsoft 365 US Government cloud but publishes no address
  record, so the corporate web presence is gone. As a reactor and nuclear-fuel manufacturer it never ran a developer program, and no public API, specification, SDK, or agent surface was found under its name.'
image: https://avatars.githubusercontent.com/u/20229671?v=4
layout: provider
modified: '2026-09-01'
name: Ultra Safe Nuclear
nav: Providers
network: true
overview: Ultra Safe Nuclear is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Nuclear, Advanced Reactors, and Small Modular Reactor.
random_paper: 21
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 3
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
    discoverability: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  lifecycle: defunct
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 4.9
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ultra Safe Nuclear Domain Security
  slug: ultra-safe-nuclear-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ultra-safe-nuclear
tags:
- Company
- Energy
- Nuclear
- Advanced Reactors
- Small Modular Reactor
- Nuclear Fuel
- Space
- Manufacturing
- Defunct
---
