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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: CoreEL Technologies provides engineering and technology solutions; API details are not publicly documented.
  name: Coreel API
  slug: coreel-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/coreel/hosts/coreel-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coreel-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://coreel.com/news/
- group: other
  title: ''
  type: Leadership
  url: https://coreel.com/leadership/
- group: auth
  href: https://artifacts.apis.io/coreel/security/coreel-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coreel-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://coreel.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://coreel.com
  - status: 403
    url: https://equityzen.com/company/coreel
  reason: no-developer-program
  state: none
created: '2026-10-10'
description: CoreEL Technologies (India) Private Limited, established in 1999, is a world‑class engineering and technology company offering high‑end electronic system‑level products and solutions for aerospace, defence, space and manufacturing sectors. The firm provides RF & microwave, hardware‑mixed‑signal, SoC/FPGA, software and mechanical engineering services, and operates globally from its Indian headquarters. It focuses on high‑end electronic system level products and solutions, serving aerospace and defence customers worldwide.
layout: provider
modified: '2026-10-10'
name: Coreel
nav: Providers
network: true
overview: Coreel is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Engineering, Aerospace, Defence, and Manufacturing.
random_paper: 10
score:
  band: minimal
  composite: 4.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.1
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 55.4
    operational_transparency: 0.0
  previous_composite: 4.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/coreel/coreel-2026-11-03T125326.png
security:
- kind: domain-security
  name: Coreel Domain Security
  slug: coreel-domain-security
  summary_line: TLSv1.2 · DMARC
slug: coreel
tags:
- Company
- Engineering
- Aerospace
- Defence
- Manufacturing
website: https://coreel.com
---
