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
    mcp_server: documented
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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for D.O.A.I. providing agent submission and registration.
  name: D.O.A.I. API
  slug: d-o-a-i-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/doaiorbit-com/llms/doaiorbit-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/doaiorbit-com-llms.txt
- group: other
  href: https://artifacts.apis.io/doaiorbit-com/hosts/doaiorbit-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/doaiorbit-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/doaiorbit-com/vendors/doaiorbit-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/doaiorbit-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/doaiorbit-com/security/doaiorbit-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/doaiorbit-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://doaiorbit.com/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://doaiorbit.com/mcp
  - status: 200
    url: https://doaiorbit.com/
  reason: partner-login
  state: gated
created: '2026-11-05'
description: DoAIOrbit provides a narrative series and field guide documenting the transition from passive chatbots to proactive autonomous agents. It offers a plain-language AI Field Guide with definitions and an index of 55 terms, aimed at readers interested in the evolution of artificial intelligence and multi‑agent orchestration.
image: https://doaiorbit.com/og-image-v2.jpg
layout: provider
modified: '2026-11-05'
name: doaiorbit-com
nav: Providers
network: true
overview: doaiorbit-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI Narrative, Field Guide, Autonomous Agents, Multi-Agent Orchestration, and Artificial Intelligence.
random_paper: 1
score:
  band: minimal
  composite: 5.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
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
  name: Doaiorbit Com Domain Security
  slug: doaiorbit-com-domain-security
  summary_line: TLSv1.3
slug: doaiorbit-com
tags:
- AI Narrative
- Field Guide
- Autonomous Agents
- Multi-Agent Orchestration
- Artificial Intelligence
website: https://doaiorbit.com/
---
