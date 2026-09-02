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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sakuu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sakuu.com/
- group: company
  title: ''
  type: Blog
  url: https://www.sakuu.com/news
- group: operate
  title: ''
  type: Support
  url: https://www.sakuu.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sakuu.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sakuu.com/privacy
- group: commercial
  title: ''
  type: Plans
  url: plans/sakuu-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sakuu-rate-limits.yml
coverage:
  checked: '2026-08-26'
  detail: Sakuu sells the Kavian dry-electrode printing machine to battery manufacturers — capital equipment, not software — and its six-page marketing site (Manufacturing, Technology, News, Company, Careers, Contact) has no developer, docs, login or platform section at all; api., developer., docs., app. and portal..sakuu.com do not resolve.
  evidence:
  - status: 404
    url: https://www.sakuu.com/openapi.json
  - status: 404
    url: https://www.sakuu.com/llms.txt
  - status: 404
    url: https://www.sakuu.com/.well-known/agent-card.json
  - status: 404
    url: https://www.sakuu.com/developers
  - status: 404
    url: https://api.github.com/orgs/sakuu
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: Sakuu Corporation is a Silicon Valley advanced-manufacturing company that builds commercial-scale printing equipment for the battery and supercapacitor industries. Founded in 2016 as KeraCel and renamed Sakuu in 2021, it develops the Kavian platform — a dry-process electrode printing system that produces cathodes and anodes without solvents or drying ovens, covering NCA, NCM, LFP, LTO, graphite and silicon-graphite chemistries as well as sodium-ion, aluminum-ion and solid-state formulations. Kavian was named a TIME Best Invention of 2024 and a Fast Company World Changing Idea of 2025, and the Kavian 2000 platform is sold to battery makers serving AI data centers, energy storage, two- and three-wheel mobility, aerospace and industrial electrification. Sakuu sells capital equipment and process technology; it does not operate a software product, a developer program, or any public API.
image: https://www.sakuu.com/media/uploads/home/homepage/Open_Graph_Banner.png
layout: provider
modified: '2026-08-26'
name: Sakuu
nav: Providers
network: true
overview: 'Sakuu is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Manufacturing, Advanced Manufacturing, Batteries, and Energy Storage.


  Sakuu''s developer surface includes engineering blog, support, and 6 more developer resources.'
plans:
- name: Sakuu Plans Pricing
  plan_count: 0
  slug: sakuu-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Sakuu Rate Limits
  slug: sakuu-rate-limits
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Sakuu Domain Security
  slug: sakuu-domain-security
  summary_line: TLSv1.3 · DMARC
slug: sakuu
tags:
- Company
- Manufacturing
- Advanced Manufacturing
- Batteries
- Energy Storage
- Materials Science
- Hardware
- Clean Energy
- Industrial Equipment
website: https://www.sakuu.com/
---
