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
- description: API for BharatPath services as described on the company website.
  name: BharatPath API
  slug: bharatpath-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/webtechinfinity/hosts/webtechinfinity-hosts.yml
  title: ''
  type: Hosts
  url: hosts/webtechinfinity-hosts.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wtiprabhatmishra
- group: auth
  href: https://artifacts.apis.io/webtechinfinity/security/webtechinfinity-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/webtechinfinity-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://webtechinfinity.com/
coverage:
  checked: '2026-10-19'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract files were found on any discovered host.
  evidence:
  - status: 404
    url: https://api.webtechinfinity.com/openapi.json
  - status: 404
    url: https://webtechinfinity.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-19'
description: WebTechInfinity is an AI, software and deep‑tech innovation company based in Kanpur, India. It builds intelligent products, digital infrastructure and technology ventures, offering custom software, AI systems, R&D, and its own technology companies such as BharatPath and Vashitva AI. The firm serves clients worldwide, emphasizing cutting‑edge solutions and venture creation.
layout: provider
modified: '2026-10-19'
name: BharatPath
nav: Providers
network: true
overview: BharatPath is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Software, Deep Tech, and Innovation.
random_paper: 4
score:
  band: minimal
  composite: 4.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.3
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 4.6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/webtechinfinity/webtechinfinity-2026-11-03T150120.png
security:
- kind: domain-security
  name: Webtechinfinity Domain Security
  slug: webtechinfinity-domain-security
  summary_line: TLSv1.3
slug: webtechinfinity
tags:
- Company
- Artificial Intelligence
- Software
- Deep Tech
- Innovation
website: https://webtechinfinity.com/
---
