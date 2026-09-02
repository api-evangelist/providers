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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ubiquitous-energy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ubiquitous.energy/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ubiquitous-energy-llms.txt
coverage:
  checked: '2026-09-01'
  detail: Ubiquitous Energy sells a transparent photovoltaic coating for glass plus R&D and engineering services to window manufacturers, and its entire web presence is a three-page GoDaddy Website Builder site (/, /technology, an empty /ols/products) whose own sitemap lists no developer, docs or API page — while its second domain, ubiquitousenergy.com, now serves a lander that hands off to forsale.godaddy.com.
  evidence:
  - status: 200
    url: https://ubiquitous.energy/
  - status: 200
    url: https://ubiquitous.energy/sitemap.website.xml
  - status: 404
    url: https://ubiquitous.energy/openapi.json
  - status: 404
    url: https://ubiquitous.energy/.well-known/agent-card.json
  - status: 404
    url: https://ubiquitous.energy/docs
  - status: 200
    url: https://www.ubiquitousenergy.com/
  reason: not-a-software-company
  state: none
created: '2026-09-01'
description: Ubiquitous Energy is a Redwood City, California materials-science company and MIT spin-out that develops UE Power (formerly ClearView Power), a transparent photovoltaic coating applied to glass. The coating uses small-molecule organic semiconductor dyes to absorb ultraviolet and infrared light while transmitting visible light, so a window generates electricity without a visible aesthetic change and while retaining low-e thermal performance. The company designs, synthesizes and characterizes novel organic semiconductor molecules, evaluates transparent photovoltaic devices against industry test protocols, and sells technical consultation, R&D, design and engineering services to glass and glass-coating manufacturers. Its product is a physical coating and a licensing/engineering practice, not software; it publishes no developer program, API, SDK or machine-readable contract of any kind.
image: https://img1.wsimg.com/isteam/ip/ca3ad51e-0061-4455-a0dd-122ea9434150/UE_HorizontalLogo.png
layout: provider
modified: '2026-09-01'
name: Ubiquitous Energy
nav: Providers
network: true
overview: Ubiquitous Energy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Solar, Materials Science, and Cleantech.
random_paper: 3
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
security:
- kind: domain-security
  name: Ubiquitous Energy Domain Security
  slug: ubiquitous-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ubiquitous-energy
tags:
- Company
- Energy
- Solar
- Materials Science
- Cleantech
- Manufacturing
- Building Technology
- Research and Development
website: https://ubiquitous.energy/
---
