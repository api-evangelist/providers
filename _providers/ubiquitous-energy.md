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
  scored_at: '2026-09-05'
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
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ubiquitous-energy/refs/heads/main/screenshots/ubiquitous-energy-2026-09-02T164719.png
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
