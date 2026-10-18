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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/carbonquest/refs/heads/main/hosts/carbonquest-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carbonquest-hosts.yml
- group: other
  title: ''
  type: Leadership
  url: https://carbonquest.com/team
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/carbonquest/refs/heads/main/security/carbonquest-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carbonquest-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://carbonquest.com/
- group: company
  title: ''
  type: Blog
  url: https://carbonquest.com/news
- group: operate
  title: ''
  type: Support
  url: https://carbonquest.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://carbonquest.com/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://carbonquest.com/distributed-carbon-capture
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://carbonquest.com/
  reason: no-developer-program
  state: none
created: '2026-10-07'
description: CarbonQuest provides distributed carbon capture solutions that turn industrial CO₂ emissions into revenue-generating resources. Their modular DCCS™ system captures CO₂ at source across biogas, low‑carbon power, and food & beverage sectors, offering financing with no upfront capital and enabling carbon credit generation, tax credits, and sustainable CO₂ supply.
layout: provider
modified: '2026-10-07'
name: CarbonQuest
nav: Providers
network: true
overview: 'CarbonQuest is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Carbon Capture, Sustainability, Cleantech, and Energy.


  CarbonQuest''s developer surface includes engineering blog, support, getting-started guide, and 5 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 9.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 46.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.2
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Carbonquest Domain Security
  slug: carbonquest-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: carbonquest
tags:
- Company
- Carbon Capture
- Sustainability
- Cleantech
- Energy
website: https://carbonquest.com/
---
