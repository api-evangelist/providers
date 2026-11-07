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
api_count: 1
apis:
- description: API for Assign-AI task assignment platform.
  name: Assign-AI API
  slug: assign-ai-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/assign-ai/hosts/assign-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/assign-ai-hosts.yml
- group: auth
  href: https://artifacts.apis.io/assign-ai/security/assign-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/assign-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://assign-ai.com/
coverage:
  checked: '2026-10-19'
  detail: Documentation page renders a JavaScript shell with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://www.assign-ai.com/public/chat
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-19'
description: Assign-AI provides AI-driven task assignment solutions, enabling organizations to automate and optimize workload distribution across teams. The platform leverages machine learning to match tasks with appropriate personnel based on skill sets, availability, and project priorities, aiming to improve efficiency and productivity. As a growing company, Assign-AI continues to expand its feature set and integrations to support diverse business needs.
layout: provider
modified: '2026-10-19'
name: Assign-AI
nav: Providers
network: true
overview: Assign-AI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Automation, Task Management, and Software-as-a-Service.
random_paper: 4
score:
  band: minimal
  composite: 3.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 0.0
  previous_composite: 3.9
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
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/assign-ai/assign-ai-2026-11-03T121227.png
security:
- kind: domain-security
  name: Assign Ai Domain Security
  slug: assign-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: assign-ai
tags:
- Company
- Artificial Intelligence
- Automation
- Task Management
- Software-as-a-Service
website: https://assign-ai.com/
---
