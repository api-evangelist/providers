---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  - sandbox
  trial: false
  try_now: true
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
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: REST API for Busabase as documented in OpenAPI spec.
  name: Busabase API
  slug: busabase-api
artifact_total: 5
asyncapis:
- description: ''
  name: Busabase Com Webhooks
  slug: busabase-com-webhooks
common:
- group: auth
  href: https://artifacts.apis.io/busabase-com/security/busabase-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/busabase-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://busabase.com/
created: '2026-11-03'
description: 'busabase-com is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-11-03'
name: busabase-com
nav: Providers
network: true
overview: 'busabase-com is listed with 1 API on the [APIs.io](https://apis.io/) network: Busabase API. Tagged areas include AI Agents, Workspace, Open Source, Cloud, and Self-Hosted.


  The busabase-com catalog on APIs.io includes 1 event-driven AsyncAPI specification.'
plans:
- name: Busabase Com Plans Pricing
  plan_count: 4
  slug: busabase-com-plans-pricing
random_paper: 2
score:
  band: emerging
  composite: 20.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 42.0
    catalog_earned_first_party: 12.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 39.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 0.0
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
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Busabase Com Authentication
  slug: busabase-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Busabase Com Domain Security
  slug: busabase-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: busabase-com
tags:
- AI Agents
- Workspace
- Open Source
- Cloud
- Self-Hosted
website: https://busabase.com/
---
