---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - '{''url'': ''https://quantive.com/'', ''status'': 302, ''note'': ''declared website redirects to https://www.workboard.com/ — a different registrable domain (quantive.com -> workboard.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 2.5
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: RESTful API v1.0 for the WorkBoard / Quantive strategy-execution platform. Supports OAuth 2.0 (authorization-code) for multi-user apps and an instant-token flow for single-user or testing scenarios. A
  name: WorkBoard REST API (Quantive)
  slug: workboard-rest-api-quantive
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quantive-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://quantive.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.workboard.com/developer
- group: docs
  title: ''
  type: Documentation
  url: https://www.workboard.com/developer
- group: start
  title: ''
  type: Login
  url: https://www.myworkboard.com/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/quantive-well-known.yml
created: '2026-07-17'
description: Quantive is a strategy-execution and OKR (Objectives and Key Results) software company, originally launched as Gtmhub and rebranded to Quantive in 2021. Its flagship product, Quantive Results, helps organizations set, align, track, and report on goals and outcomes with dashboards, insights, and integrations. In 2025 Quantive merged into WorkBoard and the Quantive name became a WorkBoard, Inc. trademark; the quantive.com domain now redirects to workboard.com, and the live developer surface is the WorkBoard REST API v1.0 (OAuth 2.0 plus an instant-token flow) hosted on myworkboard.com. Quantive was surfaced through the Index Ventures and Techstars portfolios and added to the API Evangelist network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/quantive.png
layout: provider
modified: '2026-07-20'
name: Quantive
nav: Providers
network: true
overview: 'Quantive publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Business Applications, OKR, Strategy Execution, and Goal Management.


  Quantive''s developer surface includes documentation and 5 more developer resources.'
random_paper: 16
scopes:
- name: Quantive Scopes
  scope_count: 0
  slug: quantive-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 14.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/quantive/refs/heads/main/screenshots/quantive-2026-09-02T152611.png
security:
- kind: authentication
  name: Quantive Authentication
  slug: quantive-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Quantive Domain Security
  slug: quantive-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: quantive
tags:
- Company
- Business Applications
- OKR
- Strategy Execution
- Goal Management
- Performance Management
- Software-as-a-Service
website: https://quantive.com/
---
