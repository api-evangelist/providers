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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-09-12'
api_count: 3
apis:
- description: Programmatic access to Featureflip — projects, environments, feature flags, variations, targeting, segments, and SDK keys. Bearer-token auth (ffp_ personal / ffs_ service tokens).
  name: Management API
  slug: management-api
- description: High-performance feature flag evaluation service for SDKs, with client and SDK endpoints for evaluation, identify, streaming, flags, and events.
  name: Evaluation API
  slug: evaluation-api
- description: Documentation for the @featureflip/mcp server, a local stdio process run via npx that calls the Management API on your behalf using a bearer token.
  name: MCP Server (local)
  slug: mcp-server-local
artifact_total: 3
created: '2026-09-12'
description: Feature flag platform with automated dead-flag cleanup (via a GitHub Action), flat pricing, and API-first, agent-native surfaces. Exposes a Management REST API and a high-performance Evaluation API, both with public OpenAPI contracts, plus SDKs for many languages.
layout: provider
modified: '2026-09-12'
name: Featureflip
nav: Providers
network: true
overview: 'Featureflip publishes 2 APIs on the [APIs.io](https://apis.io/) network: Management API and Evaluation API. Tagged areas include feature flags, feature management, feature flag cleanup, progressive delivery, and experimentation.'
random_paper: 20
score:
  band: emerging
  composite: 15.8
  coverage:
    artifact_dirs: 0
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 26.7
    developer_ergonomics: 9.5
    discoverability: 72.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  schema_version: 0.22.0
  scored_at: '2026-09-12'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: featureflip
tags:
- feature flags
- feature management
- feature flag cleanup
- progressive delivery
- experimentation
- feature flags as code
- OpenFeature
- MCP
- developer tools
- DevOps/CI-CD
---
