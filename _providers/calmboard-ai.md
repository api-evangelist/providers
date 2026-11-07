---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for CalmBoard AI-powered project management platform.
  name: CalmBoard API
  slug: calmboard-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/calmboard-ai/well-known/calmboard-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/calmboard-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/calmboard-ai/hosts/calmboard-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/calmboard-ai-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://calmboard.ai/terms
- group: auth
  href: https://artifacts.apis.io/calmboard-ai/security/calmboard-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/calmboard-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://calmboard.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://calmboard.ai/docs
- group: company
  title: ''
  type: Blog
  url: https://calmboard.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://calmboard.ai/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://calmboard.ai/privacy.html
coverage:
  checked: '2026-11-04'
  detail: No machine‑readable API contract (OpenAPI/AsyncAPI/GraphQL) found on calmboard.ai or its API host.
  evidence:
  - status: 200
    url: https://calmboard.ai/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: CalmBoard provides an AI‑powered project management platform for Scrum and Kanban teams, offering a focused five‑state board, explainable AI delivery insights, reports, and integrations. Users can start a 14‑day free trial with no credit card, access APIs and MCP server for automation, and benefit from AI agents that assist sprint planning, retrospectives, and coaching.
layout: provider
modified: '2026-11-04'
name: CalmBoard
nav: Providers
network: true
overview: 'CalmBoard is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Project Management, Scrum, Kanban, and Collaboration.


  CalmBoard''s developer surface includes documentation, engineering blog, pricing, and 6 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Calmboard Ai Domain Security
  slug: calmboard-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: calmboard-ai
tags:
- Artificial Intelligence
- Project Management
- Scrum
- Kanban
- Collaboration
website: https://calmboard.ai/
---
