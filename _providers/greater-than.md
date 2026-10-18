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
- description: API for predictive intelligence and risk analytics
  name: Greater Than API
  slug: greater-than-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/greater-than/refs/heads/main/hosts/greater-than-hosts.yml
  title: ''
  type: Hosts
  url: hosts/greater-than-hosts.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://greaterthan.eu/features/price-risk/
- group: company
  title: ''
  type: Newsroom
  url: https://greaterthan.eu/resources/category/news/
- group: company
  title: ''
  type: Blog
  url: https://greaterthan.eu/resources/category/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/greater-than/refs/heads/main/security/greater-than-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/greater-than-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://greaterthan.eu/
- group: docs
  title: ''
  type: Documentation
  url: https://greaterthan.eu/technology/api/
- group: docs
  title: ''
  type: APIReference
  url: https://greaterthan.eu/technology/api/
coverage:
  checked: '2026-10-15'
  detail: API documentation is HTML only with no machine‑readable OpenAPI, GraphQL, AsyncAPI or other contract discovered.
  evidence:
  - status: 200
    url: https://greaterthan.eu/technology/api/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: Greater Than provides risk intelligence solutions aimed at improving road safety and reducing climate impact. Their platform leverages AI-driven analytics to assess driver behavior, predict crash probability, and offer actionable insights for insurers, fleet operators, and regulators. Products include Crash Probability Hub, AI Coach, Analytics Reports, and ESG Compliance packages, helping clients meet CSRD requirements while optimizing telematics data and insurance pricing.
image: https://greaterthan.eu/wp-content/uploads/greater-than-driver-analytics-1-1680x813.jpg
layout: provider
modified: '2026-10-15'
name: Greater Than
nav: Providers
network: true
overview: 'Greater Than is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Risk Intelligence, Road Safety, Climate Impact, and Artificial Intelligence.


  Greater Than''s developer surface includes pricing, engineering blog, documentation, API reference, and 4 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Greater Than Domain Security
  slug: greater-than-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: greater-than
tags:
- Company
- Risk Intelligence
- Road Safety
- Climate Impact
- Artificial Intelligence
website: https://greaterthan.eu/
---
