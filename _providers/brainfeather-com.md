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
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/brainfeather-com/llms/brainfeather-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/brainfeather-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/brainfeather-com/well-known/brainfeather-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/brainfeather-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/brainfeather-com/hosts/brainfeather-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brainfeather-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/brainfeather-com/vendors/brainfeather-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brainfeather-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://brainfeather.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://brainfeather.com/privacy
- group: auth
  href: https://artifacts.apis.io/brainfeather-com/security/brainfeather-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brainfeather-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brainfeather.com/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://brainfeather.com/mcp
  - status: 200
    url: https://brainfeather.com/
  reason: partner-login
  state: gated
created: '2026-11-02'
description: Brainfeather provides a long-term memory layer for AI coding agents, capturing durable facts about projects such as stack, conventions, and decisions, and making them available to Claude Code, Cursor and other agents on subsequent runs. This service helps avoid starting from zero each session, offering background fact capture without added latency, shared across connected clients, and includes a Model Context Protocol (MCP) server. Currently in early development and free while in beta.
image: https://brainfeather.com/opengraph-image
layout: provider
modified: '2026-11-02'
name: Brainfeather
nav: Providers
network: true
overview: Brainfeather is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Memory, Agents, and MCP.
random_paper: 15
score:
  band: minimal
  composite: 6.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brainfeather Com Domain Security
  slug: brainfeather-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: brainfeather-com
tags:
- Company
- Artificial Intelligence
- Memory
- Agents
- MCP
- Beta
website: https://brainfeather.com/
---
