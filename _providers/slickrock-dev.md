---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
api_count: 0
artifact_total: 0
common:
- group: company
  title: ''
  type: Website
  url: https://slickrock.dev/
coverage:
  checked: '2026-09-19'
  detail: slickrock.dev has been on registrar clientHold since 2026-09-17 (its registrar expiration date), so the .dev TLD returns NXDOMAIN for the apex, www and every other host and the A2A agent card a2aregistry.org health-checked as live on 2026-09-14 is unreachable to the public; the origin still answers when its Cloudflare-published IP is pinned, so this reads as a lapsed renewal rather than a confirmed shutdown and should be re-probed.
  evidence:
  - status: 0
    url: https://slickrock.dev/
  - status: 0
    url: https://www.slickrock.dev/.well-known/agent-card.json
  - status: 0
    url: https://www.slickrock.dev/services/agentic-integration
  - status: 200
    url: https://pubapi.registry.google/rdap/domain/slickrock.dev
  - status: 200
    url: https://rdap.squarespace.domains/domain/slickrock.dev
  - status: 200
    url: https://a2aregistry.org/registry.json
  reason: defunct
  state: none
created: '2026-09-19'
description: Slickrock.dev describes itself as an agentic systems integrator that wraps enterprise operational assets (inventory, logistics, compliance, field service) into MCP- and A2A-compliant capability nodes for mid-market enterprises, and it operates one A2A agent listed on a2aregistry.org whose card advertises SaaS TCO calculation, agentic integration assessment and industry migration blueprint skills. That self-description is quoted from the registry listing of its agent card because, as of 2026-09-19, slickrock.dev is on registrar clientHold and does not resolve, so none of its own pages could be fetched.
layout: provider
modified: '2026-09-19'
name: Slickrock.dev
nav: Providers
network: true
overview: Slickrock.dev is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI Agents, A2A, MCP, and Integration.
random_paper: 9
score:
  band: minimal
  composite: 2.2
  coverage:
    artifact_dirs: 2
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 2.2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 0.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: slickrock-dev
tags:
- Company
- AI Agents
- A2A
- MCP
- Integration
- Consulting
- Enterprise
- Systems Integrator
website: https://slickrock.dev/
---
