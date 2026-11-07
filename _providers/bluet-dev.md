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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API documentation for Bluet's Machine‑Centric Protocol.
  name: Bluet API
  slug: bluet-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/bluet-dev/well-known/bluet-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bluet-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/bluet-dev/hosts/bluet-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bluet-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/bluet-dev/vendors/bluet-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bluet-dev-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bluet.dev/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://bluet.dev/docs
- group: auth
  href: https://artifacts.apis.io/bluet-dev/security/bluet-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bluet-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bluet.dev/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://bluet.dev/mcp
  - status: 200
    url: https://bluet.dev/
  reason: partner-login
  state: gated
created: '2026-11-02'
description: Bluet provides an AI‑first product memory platform that captures strategy, decisions, and rules behind software products. It serves this information over an MCP (Machine‑Centric Protocol) allowing teams to read and write product knowledge directly from repositories. The service emphasizes open‑source integration, GitHub‑based read‑only access, and a focus on decision‑making transparency for product managers.
layout: provider
modified: '2026-11-02'
name: Bluet
nav: Providers
network: true
overview: 'Bluet is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Product-Memory, MCP, Open Source, and Decision-Making.


  Bluet''s developer surface includes documentation and 6 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 7.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 62.5
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bluet Dev Domain Security
  slug: bluet-dev-domain-security
  summary_line: TLSv1.3 · HSTS
slug: bluet-dev
tags:
- Artificial Intelligence
- Product-Memory
- MCP
- Open Source
- Decision-Making
website: https://bluet.dev/
---
