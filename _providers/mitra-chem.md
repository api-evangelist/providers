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
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mitra-chem-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mitrachem.com/
- group: company
  title: ''
  type: Blog
  url: https://www.mitrachem.com/news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mitrachem.com/privacy-policy-cookie-notice
- group: operate
  title: ''
  type: Contact
  url: mailto:info@mitrachem.com
- group: company
  title: ''
  type: Careers
  url: https://www.mitrachem.com/join-us
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mitrachem/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mitra-chem-llms.txt
coverage:
  checked: '2026-08-25'
  detail: Mitra Chem manufactures physical lithium iron phosphate cathode active material; the "AI Platform" it markets is internal tooling for its own foundry, and www.mitrachem.com serves only seven marketing pages with no developer, docs or login surface at all.
  evidence:
  - status: 404
    url: https://www.mitrachem.com/openapi.json
  - status: 404
    url: https://www.mitrachem.com/.well-known/agent-card.json
  - status: 0
    url: https://api.mitrachem.com/
  - status: 200
    url: https://www.mitrachem.com/platform
  reason: not-a-software-company
  state: none
created: '2026-08-25'
description: Mitra Chem is an AI-enabled innovator and manufacturer of battery and critical materials for energy, AI infrastructure and defense applications, founded in 2021 and headquartered in Mountain View, California. Its first commercial product is iron-based lithium iron phosphate (LFP) and lithium manganese iron phosphate (LMFP) cathode active material produced for Western battery cell makers and energy-storage OEMs as a non-China supply source. The company operates The Foundry, an instrumented shared pilot manufacturing facility spanning wet chemistry, hydrometallurgy, particle sizing, drying and heat treatment, and runs an internal full-stack AI platform of physics-based models, digital twins and engineering co-pilots used to compress materials scale-up cost and timelines. The AI platform is internal tooling for Mitra Chem's own manufacturing operations; it is not sold or exposed as a software product, and the company publishes no public API, developer portal, SDK or machine-readable
  interface.
image: https://www.mitrachem.com/assets/og-image.png
layout: provider
modified: '2026-08-25'
name: Mitra Chem
nav: Providers
network: true
overview: 'Mitra Chem is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Battery Materials, Advanced Manufacturing, Energy Storage, and Chemicals.


  Mitra Chem''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 6.7
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 13.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: domain-security
  name: Mitra Chem Domain Security
  slug: mitra-chem-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mitra-chem
tags:
- Company
- Battery Materials
- Advanced Manufacturing
- Energy Storage
- Chemicals
- Electric Vehicles
- Critical Minerals
- Artificial Intelligence
website: https://www.mitrachem.com/
---
