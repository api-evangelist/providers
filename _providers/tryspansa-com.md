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
  url: https://tryspansa.com/
coverage:
  checked: '2026-09-19'
  detail: The only public API claim is TrySpansa's own a2aregistry.org listing; its agent card at tryspansa.com/.well-known/agent-card.json — like every path on the domain since a 2026-09-16 deployment, including /features, /pricing and /developers — returns HTTP 200 with a 141-byte blank noindex HTML shell, the registry's own 2026-09-14 check recorded NO_TRANSPORTS for that card, and api./docs./mcp.tryspansa.com answer Vercel DEPLOYMENT_NOT_FOUND, so no contract, docs, SDK or portal exists to read.
  evidence:
  - note: blank HTML shell, not JSON
    status: 200
    url: https://tryspansa.com/.well-known/agent-card.json
  - note: blank HTML shell
    status: 200
    url: https://tryspansa.com/features
  - note: blank HTML shell
    status: 200
    url: https://tryspansa.com/developers
  - note: Vercel DEPLOYMENT_NOT_FOUND
    status: 404
    url: https://api.tryspansa.com/
  - note: Vercel DEPLOYMENT_NOT_FOUND
    status: 404
    url: https://docs.tryspansa.com/
  - note: 'registry record (terminal 200 after 2 redirects from the slash-less URL): protocolVersion unknown, task_conformance NO_TRANSPORTS checked 2026-09-14'
    status: 200
    url: https://a2aregistry.org/agents/c235a802-ed05-49e6-8c0d-94db05b8d324/
  reason: no-developer-program
  state: none
created: '2026-09-19'
description: 'TrySpansa is a company surfaced via the API Evangelist harvest backlog (source: a2a-registry) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-09-19'
name: TrySpansa
nav: Providers
network: true
overview: TrySpansa is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 19
score:
  band: minimal
  composite: 2.8
  coverage:
    artifact_dirs: 2
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
slug: tryspansa-com
tags:
- Company
website: https://tryspansa.com/
---
