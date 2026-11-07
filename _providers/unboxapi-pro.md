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
- description: UNBOXAPI offers an MCP platform to wrap existing business APIs for AI agents.
  name: UNBOXAPI
  slug: unboxapi
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/unboxapi-pro/hosts/unboxapi-pro-hosts.yml
  title: ''
  type: Hosts
  url: hosts/unboxapi-pro-hosts.yml
- group: other
  href: https://artifacts.apis.io/unboxapi-pro/vendors/unboxapi-pro-vendors.yml
  title: ''
  type: Vendors
  url: vendors/unboxapi-pro-vendors.yml
- group: auth
  href: https://artifacts.apis.io/unboxapi-pro/security/unboxapi-pro-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/unboxapi-pro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://unboxapi.pro/
- group: company
  title: ''
  type: Blog
  url: https://www.unboxapi.pro/blog
coverage:
  checked: '2026-10-31'
  detail: The public website provides marketing information but no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://www.unboxapi.pro/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: UNBOXAPI provides a platform that transforms existing business APIs into agent‑ready action layers, enabling AI assistants such as ChatGPT, Gemini, and Apple Intelligence to interact with services without any code changes or rebuilding. By wrapping legacy APIs with a smart MCP (Machine‑Centric Proxy) server, UNBOXAPI makes businesses instantly discoverable and operable by intelligent agents, supporting e‑commerce, reservation, and service scheduling use cases. Early‑access customers receive founder‑level support and help shape the roadmap.
image: https://www.unboxapi.pro/favicon.svg
layout: provider
modified: '2026-10-31'
name: unboxapi-pro
nav: Providers
network: true
overview: 'unboxapi-pro is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Agents, API Integration, and MCP.


  unboxapi-pro''s developer surface includes engineering blog and 4 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 4.5
  coverage:
    artifact_dirs: 11
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.3
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 4.8
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
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/unboxapi-pro/unboxapi-pro-2026-11-03T145406.png
security:
- kind: domain-security
  name: Unboxapi Pro Domain Security
  slug: unboxapi-pro-domain-security
  summary_line: TLSv1.3
slug: unboxapi-pro
tags:
- Company
- Artificial Intelligence
- Agents
- API Integration
- MCP
- Automation
website: https://unboxapi.pro/
---
