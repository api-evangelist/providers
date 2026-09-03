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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/USNC
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ultra-safe-nuclear-domain-security.yml
- group: agent
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
overview: Ultra Safe Nuclear is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Nuclear, Advanced Reactors, and Small Modular Reactors.
random_paper: 18
score:
  band: minimal
  composite: 4.0
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 4.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
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
- Small Modular Reactors
- Nuclear Fuel
- Space
- Manufacturing
- Defunct
---
