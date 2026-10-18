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
- description: Compredict provides AI‑powered virtual sensor data via API (no public machine‑readable spec discovered).
  name: Compredict API
  slug: compredict-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/compredict/refs/heads/main/hosts/compredict-hosts.yml
  title: ''
  type: Hosts
  url: hosts/compredict-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://compredict.ai/datapilot/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://compredict.ai/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://compredict.ai/portfolio_category/news/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/compredict
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/compredict/refs/heads/main/security/compredict-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/compredict-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://compredict.ai
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://compredict.ai
  reason: no-developer-program
  state: none
created: '2026-10-10'
description: Compredict is a German deep‑tech company pioneering AI‑powered virtual sensor technology for the automotive industry. Founded as a spin‑off from TU Darmstadt, it transforms raw vehicle sensor data into trusted physical signals using software‑defined virtual sensors, enabling hardware‑free insights across automotive, manufacturing, defense, robotics, and agriculture sectors.
image: https://compredict.ai/wp-content/uploads/2026/03/Homepage-Thumbnail-1200x630-1-1024x538.png
layout: provider
modified: '2026-10-10'
name: Compredict
nav: Providers
network: true
overview: Compredict is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Automotive, Sensors, and Virtual.
random_paper: 10
score:
  band: minimal
  composite: 10.4
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
    discoverability: 58.9
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Compredict Domain Security
  slug: compredict-domain-security
  summary_line: TLSv1.2 · DMARC
slug: compredict
tags:
- Company
- Artificial Intelligence
- Automotive
- Sensors
- Virtual
website: https://compredict.ai
---
