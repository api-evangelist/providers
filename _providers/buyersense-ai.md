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
- group: other
  href: https://artifacts.apis.io/buyersense-ai/hosts/buyersense-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/buyersense-ai-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://app.buyersense.ai/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BuyerSense
- group: auth
  href: https://artifacts.apis.io/buyersense-ai/security/buyersense-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/buyersense-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://buyersense.ai/
coverage:
  checked: '2026-11-03'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on any discovered host.
  evidence:
  - status: 0
    url: https://api.buyersense.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: BuyerSense provides an Agent Reasoning Optimization platform for B2B SaaS, enabling companies to trace, shape, and improve how AI agents make decisions. The platform offers tools for monitoring agent behavior, optimizing reasoning pathways, and delivering insights to enhance performance and outcomes for enterprise customers.
layout: provider
modified: '2026-11-03'
name: BuyerSense
nav: Providers
network: true
overview: BuyerSense is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, B2B, Software-as-a-Service, Optimization, and AgentReasoning.
random_paper: 20
score:
  band: minimal
  composite: 4.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 2.6
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Buyersense Ai Domain Security
  slug: buyersense-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: buyersense-ai
tags:
- Artificial Intelligence
- B2B
- Software-as-a-Service
- Optimization
- AgentReasoning
website: https://buyersense.ai/
---
