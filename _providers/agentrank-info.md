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
  scored_at: '2026-09-19'
api_count: 0
artifact_total: 0
common:
- group: company
  title: ''
  type: Website
  url: https://agentrank.info/
coverage:
  checked: '2026-09-19'
  detail: AgentRank's entire machine surface (REST, MCP and A2A) lived on api.agentrank.info, which resolves to 167.71.254.98 but refuses TCP connections on 443 and 80, and the company's source repository is archived as "Retired ... The hosted service no longer runs"; agentrank.info still serves the agent card and llms.txt that advertise the dead endpoints while its index pages return HTTP 500 — a product retirement (Crest Deployment Systems LLC is still active on GitHub), not a company closure, and no OpenAPI was ever published.
  evidence:
  - status: 0
    url: https://api.agentrank.info/
  - status: 200
    url: https://api.github.com/repos/andysalvo/agentrank
  - status: 500
    url: https://agentrank.info/agents
  - status: 200
    url: https://agentrank.info/.well-known/agent-card.json
  reason: defunct
  state: none
created: '2026-09-19'
description: 'Crest Deployment Systems LLC is a company surfaced via the API Evangelist harvest backlog (source: a2a-registry) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-09-19'
name: Crest Deployment Systems LLC
nav: Providers
network: true
overview: Crest Deployment Systems LLC is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 20
score:
  band: minimal
  composite: 2.8
  coverage:
    artifact_dirs: 0
    catalog_earned: 15.0
    catalog_earned_first_party: 0.0
    catalog_gap: 100.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 27.8
    operational_transparency: 0.0
  schema_version: 0.22.0
  scored_at: '2026-09-19'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: agentrank-info
tags:
- Company
website: https://agentrank.info/
---
