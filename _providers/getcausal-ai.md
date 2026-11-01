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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Causal Labs provides APIs for causal inference, simulation, and data-driven insights as described on their website.
  name: Causal API
  slug: causal-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/getcausal-ai/hosts/getcausal-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/getcausal-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/getcausal-ai/vendors/getcausal-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/getcausal-ai-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.causallabs.ai/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://blog.getcausal.ai/
- group: auth
  href: https://artifacts.apis.io/getcausal-ai/security/getcausal-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getcausal-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://getcausal.ai/
coverage:
  checked: '2026-10-26'
  detail: Main site renders via JavaScript and provides no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://www.causallabs.ai/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-25'
description: Causal Labs builds a Large Physics foundation Model (LPM) to learn causality through physics and weather, aiming for general causal intelligence. The company focuses on understanding how actions influence the world, advancing AI by integrating causal reasoning. It offers APIs for causal inference, simulation, and data-driven insights, supporting developers and researchers in building causally-aware applications.
image: https://cdn.prod.website-files.com/6977a9c6055cd296356ce1d0/69786945ff11eafe3793296d_44720ecd47dcbec811e851d0560d3a99_Open%20Graph.png
layout: provider
modified: '2026-10-25'
name: Causal
nav: Providers
network: true
overview: 'Causal is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Causal-Intelligence, Machine-Learning, Physics, and Weather.


  Causal''s developer surface includes engineering blog and 5 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 7.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Getcausal Ai Domain Security
  slug: getcausal-ai-domain-security
  summary_line: TLSv1.3 · HSTS
slug: getcausal-ai
tags:
- AI
- Causal-Intelligence
- Machine-Learning
- Physics
- Weather
website: https://getcausal.ai/
---
