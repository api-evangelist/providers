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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-09-19'
  detail: 'Magician was a personal Mac agent exposed through an ephemeral localhost.run tunnel (a69e75097db0f6.lhr.life) that is now closed: the tunnel host and www.lhr.life both answer localhost.run''s ''no tunnel here :('' 503, the apex lhr.life is a CNAME to dd.localhost.run that does not resolve to a site, and a2aregistry.org''s own health check reports 0% uptime and a failed A2A task-conformance probe, so no agent card, contract, or website exists to profile.'
  evidence:
  - status: 503
    url: https://a69e75097db0f6.lhr.life/.well-known/agent-card.json
  - status: 503
    url: https://a69e75097db0f6.lhr.life/a2a/v1
  - status: 503
    url: https://www.lhr.life/
  - status: 0
    url: https://lhr.life/
  - status: 200
    url: https://a2aregistry.org/api/agents/367b2ef4-a800-4102-b195-2c82bfff3095
  reason: defunct
  state: none
created: '2026-09-19'
description: 'Magician is not a company: it is a single self-described Mac-native personal agent (Feishu chat, deep research, Mac desktop automation, local coding via Goose, A2A task matching) that an individual registered on a2aregistry.org on 2026-09-18 from an ephemeral localhost.run tunnel hostname, a69e75097db0f6.lhr.life. The registrable domain lhr.life belongs to the localhost.run tunnelling service (it is a CNAME to dd.localhost.run), not to Magician; the tunnel is closed and the host now answers localhost.run''s ''no tunnel here'' 503, and the registry itself records the agent at 0% uptime with a failing A2A task-conformance check. There is no website, documentation, contract, or durable endpoint to profile.'
layout: provider
modified: '2026-09-19'
name: Magician
nav: Providers
network: true
overview: Magician is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI Agents, A2A, Personal Agents, and Mac Automation.
random_paper: 19
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 0
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 0.0
    operational_transparency: 0.0
  lifecycle: defunct
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 0.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: lhr-life
tags:
- Company
- AI Agents
- A2A
- Personal Agents
- Mac Automation
- Research Agents
---
