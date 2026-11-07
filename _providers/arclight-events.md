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
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Arclight provides read‑only event search and retrieval tools via its MCP endpoint.
  name: Arclight Events API
  slug: arclight-events-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/arclight-events/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/arclight-events/llms/arclight-events-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/arclight-events-llms.txt
- group: other
  href: https://artifacts.apis.io/arclight-events/hosts/arclight-events-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arclight-events-hosts.yml
- group: other
  href: https://artifacts.apis.io/arclight-events/vendors/arclight-events-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arclight-events-vendors.yml
- group: auth
  href: https://artifacts.apis.io/arclight-events/security/arclight-events-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arclight-events-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arclight.events/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arclight.events/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arclight.events/
created: '2026-11-01'
description: Arclight aggregates AI and tech event calendars across cities, using an AI concierge to present three curated events per day. It offers a free, real-time planner that turns natural language queries into personalized itineraries, pulling from verified listings without inventing events.
image: https://arclight.events/og-card.png
layout: provider
modified: '2026-11-01'
name: Arclight
nav: Providers
network: true
overview: Arclight is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Event, Artificial Intelligence, Tech, Concierge, and Planner.
random_paper: 16
rate_limits:
- limit_count: 0
  name: Arclight Events Rate Limits
  slug: arclight-events-rate-limits
scopes:
- name: Arclight Events Scopes
  scope_count: 0
  slug: arclight-events-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 10.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.6
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.4
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 13.1
  provenance:
    conformance: unknown
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Arclight Events Authentication
  slug: arclight-events-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Arclight Events Domain Security
  slug: arclight-events-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: arclight-events
tags:
- Event
- Artificial Intelligence
- Tech
- Concierge
- Planner
website: https://arclight.events/
---
