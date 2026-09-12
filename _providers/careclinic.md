---
agent_readiness:
  band: agent-aware
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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.6
  scored_at: '2026-09-12'
api_count: 1
apis:
- description: OAuth-gated MCP endpoint. Unauthenticated initialize answers 401 with a WWW-Authenticate carrying resource_metadata AND granular scopes (careclinic.wellness.read, careclinic.symptoms.write, careclinic
  name: CareClinic MCP
  slug: careclinic-mcp
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://careclinic.io
created: '2026-09-09'
description: 'CareClinic MCP is a private OAuth-connected health-tracking service for supported AI assistants: user-authorized schedule and wellness reads, observational summaries, and explicitly confirmed symptom or mood writes. Medication writes remain disabled. MCP-only surface -- there is no public REST contract, by design.'
layout: provider
mcp_servers:
- description: ''
  name: CareClinic MCP Server
  slug: careclinic-mcp-server
modified: '2026-09-09'
name: CareClinic
nav: Providers
network: true
overview: CareClinic publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Health, Wellness, MCP, Personal Health, and Healthcare.
random_paper: 8
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 1
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    operational_transparency: 0.0
  previous_composite: 5.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 0.0
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: careclinic
tags:
- Health
- Wellness
- MCP
- Personal Health
- Healthcare
website: https://careclinic.io
---
